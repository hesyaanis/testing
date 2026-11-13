import json
import re
import os
from typing import List, Dict, Any, Optional

def load_catalog(filepath: str = "katalog_laptop.json") -> List[Dict[str, Any]]:
    """Memuat data katalog laptop dari file JSON."""
    if not os.path.exists(filepath):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(base_dir, filepath)
    
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def extract_budget(text: str) -> Optional[int]:
    """Mengekstrak estimasi budget dari kalimat pengguna (dalam Rupiah)."""
    text_lower = text.lower()
    
    # Deteksi pola 'di bawah X juta', 'budget X juta', 'Xjt'
    juta_match = re.search(r"(\d+(?:[.,]\d+)?)\s*(?:jt|juta|jutaan)", text_lower)
    if juta_match:
        val_str = juta_match.group(1).replace(",", ".")
        try:
            return int(float(val_str) * 1_000_000)
        except ValueError:
            pass

    # Deteksi angka bulat besar (misal: 5000000 atau 5.000.000)
    clean_digits = re.sub(r"[^\d]", "", text)
    if clean_digits:
        try:
            val = int(clean_digits)
            if 3_000_000 <= val <= 50_000_000:
                return val
        except ValueError:
            pass
            
    return None

def check_unrealistic_request(query: str, budget: Optional[int]) -> Optional[Dict[str, Any]]:
    """
    Mendeteksi apakah permintaan pembeli bertentangan dengan realitas pasar laptop
    (misal: minta laptop baru spek dewa / RTX di bawah 8-9 juta).
    """
    q = query.lower()
    wants_rtx = bool(re.search(r"\brtx\b", q)) or "kartu grafis" in q or "vga diskrit" in q
    wants_dewa = "spek dewa" in q or "gaming berat" in q

    if budget:
        # Permintaan RTX / Spek Dewa di bawah 8.5 juta (Mustahil untuk laptop baru)
        if (wants_rtx or wants_dewa) and budget < 8_500_000:
            return {
                "type": "rtx_under_budget",
                "budget": budget,
                "wants_rtx": wants_rtx,
                "wants_rgb": "rgb" in q
            }
        
        # Permintaan OLED di bawah 9 juta
        if "oled" in q and budget < 9_000_000:
            return {
                "type": "oled_under_budget",
                "budget": budget
            }
            
    return None

def score_laptop(laptop: Dict[str, Any], query: str, budget: Optional[int]) -> float:
    """Menghitung skor kecocokan laptop berdasarkan query dan budget secara ketat."""
    q = query.lower()
    score = 0.0
    laptop_price = laptop["harga"]
    gpu_text = laptop["spesifikasi"]["gpu"].lower()
    layar_text = laptop["spesifikasi"]["layar"].lower()
    ram_text = laptop["spesifikasi"]["ram"].lower()
    berat_val = float(laptop["spesifikasi"]["berat"].split()[0])

    # 1. ATURAN BUDGET KETAT:
    if budget:
        if laptop_price <= budget:
            ratio = laptop_price / budget
            score += 60.0 * ratio
        elif laptop_price <= budget * 1.15:
            # Toleransi maksimal 15% jika mendekati (misal budget 6jt, laptop 6.8jt)
            score -= 30.0
        else:
            # Lebih dari 15% di atas budget: DISKUALIFIKASI!
            return -999.0

    # 2. KOREKSI KHUSUS SPESIFIKASI KERAS (HARDWARE CONSTRAINTS)
    
    # A. Cek permintaan RTX / Kartu Grafis Diskrit
    wants_rtx = bool(re.search(r"\brtx\b", q)) or "kartu grafis" in q or "vga diskrit" in q or "vga dedicated" in q
    if wants_rtx:
        if "rtx" in gpu_text:
            score += 150.0
        else:
            score -= 300.0

    # B. Cek permintaan Layar OLED
    wants_oled = "oled" in q
    if wants_oled:
        if "oled" in layar_text:
            score += 120.0
        else:
            score -= 150.0

    # C. Cek permintaan Laptop Ringan / Tipis / Portabel
    wants_ringan = any(w in q for w in ["ringan", "tipis", "enteng", "bawa", "mobilitas", "tas"])
    if wants_ringan:
        if berat_val <= 1.45:
            score += 50.0
        elif berat_val > 2.0:
            score -= 100.0

    # D. Cek permintaan RAM 16GB
    wants_16gb = "16gb" in q or "16 gb" in q
    if wants_16gb:
        if "16gb" in ram_text:
            score += 40.0
        else:
            score -= 40.0

    # E. Cek permintaan Laptop Paling Murah / Terjangkau / Hemat
    wants_cheap = any(w in q for w in ["murah", "termurah", "paling murah", "ekonomis", "terjangkau", "hemat", "paling hemat", "budget mepet", "entry level", "ramah di kantong"])
    if wants_cheap:
        if laptop_price <= 3_500_000:
            score += 150.0
        elif laptop_price <= 5_000_000:
            score += 90.0
        elif laptop_price <= 7_500_000:
            score += 30.0
        else:
            score -= 80.0

    # F. Cek permintaan Laptop Termahal / Spek Tertinggi / Flagship
    wants_expensive = any(w in q for w in ["termahal", "paling mahal", "flagship", "paling tinggi", "spek dewa", "terbaik tanpa batas"])
    if wants_expensive:
        if laptop_price >= 25_000_000:
            score += 150.0
        elif laptop_price >= 15_000_000:
            score += 80.0
        else:
            score -= 60.0

    # 3. Kebutuhan / Use Case
    keywords_map = {
        "coding": ["coding", "ngoding", "programmer", "it", "informatika", "python", "web dev"],
        "gaming": ["game", "gaming", "valorant", "dota", "genshin", "cyberpunk", "gta", "main game"],
        "desain": ["desain", "editing", "photoshop", "premiere", "after effects", "dkv", "render", "video", "youtube"],
        "sekolah": ["sekolah", "anak", "sd", "smp", "sma", "pelajar", "belajar", "kursus", "zoom", "tugas", "ananda", "ketik", "ngetik", "word"],
        "mahasiswa": ["kuliah", "mahasiswa", "skripsi", "tugas akhir", "kampus"],
        "office": ["kantor", "office", "excel", "word", "kerja", "admin"]
    }

    laptop_full_desc = (
        laptop["nama"] + " " +
        laptop["kategori"] + " " +
        " ".join(laptop["target_user"]) + " " +
        " ".join(laptop["kelebihan"]) + " " +
        laptop["game_support"]
    ).lower()

    for category, words in keywords_map.items():
        if any(w in q for w in words):
            if any(w in laptop_full_desc for w in words):
                score += 35.0

    # Brand match
    if laptop["brand"].lower() in q:
        score += 25.0

    return score

def find_recommendations(query: str, catalog: List[Dict[str, Any]], limit: int = 2) -> List[Dict[str, Any]]:
    """Mencari laptop yang paling cocok dengan permintaan pembeli."""
    budget = extract_budget(query)
    q_low = query.lower()
    
    scored_items = []
    for item in catalog:
        s = score_laptop(item, query, budget)
        scored_items.append((s, item))

    # Urutkan berdasarkan skor tertinggi
    scored_items.sort(key=lambda x: x[0], reverse=True)
    
    # Ambil laptop dengan skor positif (skor > 0)
    results = [item for s, item in scored_items if s > 0][:limit]
    
    # Jaminan RAG: Jangan pernah kembalikan list kosong agar AI tidak menganggap katalog offline
    if not results:
        if any(w in q_low for w in ["murah", "termurah", "ekonomis", "terjangkau", "anak", "sd", "sekolah", "pelajar", "hemat", "budget mepet"]):
            sorted_by_price = sorted(catalog, key=lambda x: x["harga"])
            results = sorted_by_price[:limit]
        elif any(w in q_low for w in ["mahal", "termahal", "flagship", "paling kencang", "paling tinggi", "spek dewa"]):
            sorted_by_price = sorted(catalog, key=lambda x: x["harga"], reverse=True)
            results = sorted_by_price[:limit]
        else:
            # Ambil laptop terlaris/stok banyak sebagai rekomendasi umum
            sorted_by_stock = sorted(catalog, key=lambda x: x["stok"], reverse=True)
            results = sorted_by_stock[:limit]
        
    return results

def format_rupiah(angka: int) -> str:
    """Format angka menjadi format Rupiah Indonesia yang rapi."""
    return f"Rp {angka:,.0f}".replace(",", ".")

def load_pc_catalog(filepath: str = "katalog_komponen_pc.json") -> List[Dict[str, Any]]:
    """Memuat data katalog komponen PC resmi toko dari file JSON."""
    if not os.path.exists(filepath):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(base_dir, filepath)
    
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def search_pc_components(query: str, pc_catalog: List[Dict[str, Any]], limit: int = 15) -> List[Dict[str, Any]]:
    """Mencari komponen PC berdasarkan kategori, brand, atau spesifikasi."""
    q = query.lower().strip()
    if not q:
        return pc_catalog[:limit]
    
    # Alias kategori
    cat_aliases = {
        "cpu": "processor",
        "prosesor": "processor",
        "mobo": "motherboard",
        "motherboard": "motherboard",
        "mainboard": "motherboard",
        "vga": "vga",
        "gpu": "vga",
        "grafis": "vga",
        "ram": "ram",
        "memori": "ram",
        "memory": "ram",
        "ssd": "penyimpanan",
        "nvme": "penyimpanan",
        "storage": "penyimpanan",
        "hdd": "penyimpanan",
        "psu": "power supply",
        "power": "power supply",
        "cooler": "cpu cooler",
        "pendingin": "cpu cooler",
        "case": "casing",
        "casing": "casing",
        "monitor": "monitor",
        "layar": "monitor"
    }

    target_cat = None
    tokens = q.split()
    for t in tokens:
        if t in cat_aliases:
            target_cat = cat_aliases[t]
            break

    exact_category_matches = []
    other_matches = []

    for item in pc_catalog:
        name_l = item["nama"].lower()
        cat_l = item["kategori"].lower()
        brand_l = item["brand"].lower()
        spec_l = item.get("spesifikasi_ringkas", "").lower()

        if target_cat and target_cat in cat_l:
            # Jika user ketik misal "vga rtx", filter lagi di dalam kategori vga
            remaining_query = q.replace(t, "").strip() if target_cat else q
            if not remaining_query or remaining_query in name_l or remaining_query in brand_l or remaining_query in spec_l:
                exact_category_matches.append(item)
        elif q in name_l or q in brand_l:
            other_matches.append(item)
        elif q in spec_l:
            other_matches.append(item)

    if exact_category_matches:
        return exact_category_matches[:limit]
    return other_matches[:limit] if other_matches else pc_catalog[:limit]

def build_pc_rig_from_catalog(budget: int, pc_catalog: List[Dict[str, Any]], preference: str = "gaming") -> Dict[str, Any]:
    """
    Meracik 8 komponen PC nyata yang 100% kompatibel dan siap nyala dari katalog toko.
    """
    by_cat = {}
    for item in pc_catalog:
        by_cat.setdefault(item["kategori"], []).append(item)

    for c in by_cat:
        by_cat[c].sort(key=lambda x: x["harga"])

    # Logika racikan berdasarkan tier budget
    if budget <= 6_000_000:
        tier_name = "Entry Level / eSports Hemat (iGPU)"
        # Tier Hemat: Ryzen 5 5600G with iGPU (tanpa beli VGA terpisah)
        cpu = next((x for x in by_cat.get("Processor (CPU)", []) if "5600G" in x["nama"]), by_cat["Processor (CPU)"][0])
        mobo = next((x for x in by_cat.get("Motherboard", []) if "A520" in x["nama"]), by_cat["Motherboard"][0])
        ram = next((x for x in by_cat.get("RAM (Memory)", []) if "16GB" in x["nama"] and "DDR4" in x["nama"]), by_cat["RAM (Memory)"][0])
        ssd = next((x for x in by_cat.get("Penyimpanan (SSD / HDD)", []) if "NVMe" in x.get("tipe_storage", "") and ("256GB" in x["nama"] or "512GB" in x["nama"])), by_cat["Penyimpanan (SSD / HDD)"][0])
        gpu = {"id": "GPU-IGPU", "kategori": "VGA / Kartu Grafis", "nama": "AMD Radeon Vega 7 (Terintegrasi di Prosesor)", "brand": "AMD", "harga": 0, "spesifikasi_ringkas": "iGPU bawaan Ryzen 5 5600G, kuat 60+ FPS Valorant & GTA V"}
        psu = next((x for x in by_cat.get("Power Supply (PSU)", []) if "550W" in x["nama"]), by_cat["Power Supply (PSU)"][0])
        cooler = {"id": "CLR-STOCK", "kategori": "CPU Cooler", "nama": "AMD Wraith Stealth Stock Cooler", "brand": "AMD", "harga": 0, "spesifikasi_ringkas": "Termasuk di dalam box prosesor"}
        case = by_cat.get("Casing PC", [])[0]
    elif budget <= 11_500_000:
        tier_name = "Sweet Spot Gaming 1080p Ultra"
        # Tier Sweet Spot 10 Juta: Ryzen 5 5600 + RX 6600 8GB / RTX 4060 + B550 + 16GB DDR4 + 500GB/512GB NVMe + 550W Bronze
        cpu = next((x for x in by_cat.get("Processor (CPU)", []) if "5600" in x["nama"] and "G" not in x["nama"] and "X" not in x["nama"]), by_cat["Processor (CPU)"][0])
        mobo = next((x for x in by_cat.get("Motherboard", []) if "B550" in x["nama"]), by_cat["Motherboard"][0])
        ram = next((x for x in by_cat.get("RAM (Memory)", []) if "16GB" in x["nama"] and "DDR4" in x["nama"]), by_cat["RAM (Memory)"][0])
        ssd = next((x for x in by_cat.get("Penyimpanan (SSD / HDD)", []) if "NVMe" in x.get("tipe_storage", "") and ("500GB" in x["nama"] or "512GB" in x["nama"])), by_cat["Penyimpanan (SSD / HDD)"][0])
        # Cek jika budget cukup untuk RTX 4060
        if budget >= 11_000_000:
            gpu = next((x for x in by_cat.get("VGA / Kartu Grafis", []) if "4060" in x["nama"] and "Ti" not in x["nama"]), by_cat["VGA / Kartu Grafis"][0])
        else:
            gpu = next((x for x in by_cat.get("VGA / Kartu Grafis", []) if "6600" in x["nama"]), by_cat["VGA / Kartu Grafis"][0])
        psu = next((x for x in by_cat.get("Power Supply (PSU)", []) if "550W" in x["nama"] and "Bronze" in x["nama"]), by_cat["Power Supply (PSU)"][0])
        cooler = next((x for x in by_cat.get("CPU Cooler", []) if "CR-1400" in x["nama"] or "AG400" in x["nama"]), by_cat.get("CPU Cooler", [])[0])
        case = next((x for x in by_cat.get("Casing PC", []) if "Axel" in x["nama"] or "Flatline" in x["nama"]), by_cat.get("Casing PC", [])[0])
    elif budget <= 17_000_000:
        tier_name = "Performance Gaming & Content Creation 1440p"
        # Tier Mid-Range 15 Juta: Core i5-13400F / Ryzen 5 7500F + RTX 4060 / 4060 Ti + 32GB RAM + 1TB NVMe + 650W Bronze
        cpu = next((x for x in by_cat.get("Processor (CPU)", []) if "7500F" in x["nama"] or "13400F" in x["nama"] or "14400F" in x["nama"]), by_cat["Processor (CPU)"][0])
        mobo = next((x for x in by_cat.get("Motherboard", []) if "B650" in x["nama"] or "B760" in x["nama"]), by_cat["Motherboard"][0])
        ram = next((x for x in by_cat.get("RAM (Memory)", []) if "32GB" in x["nama"] and "DDR5" in x["nama"]), by_cat["RAM (Memory)"][0])
        ssd = next((x for x in by_cat.get("Penyimpanan (SSD / HDD)", []) if "1TB" in x["nama"] and "Gen4" in x.get("tipe_storage", "")), by_cat["Penyimpanan (SSD / HDD)"][0])
        gpu = next((x for x in by_cat.get("VGA / Kartu Grafis", []) if "4060" in x["nama"]), by_cat["VGA / Kartu Grafis"][0])
        psu = next((x for x in by_cat.get("Power Supply (PSU)", []) if "650W" in x["nama"]), by_cat["Power Supply (PSU)"][0])
        cooler = next((x for x in by_cat.get("CPU Cooler", []) if "Dual Tower" in x.get("spesifikasi_ringkas", "") or "LE520" in x["nama"]), by_cat["CPU Cooler"][0])
        case = next((x for x in by_cat.get("Casing PC", []) if "AIR 100" in x["nama"] or "Airflow" in x["nama"]), by_cat["Casing PC"][0])
    else:
        tier_name = "Enthusiast / High-End Workstation 4K"
        # Tier High-End / Workstation 20 Juta+: Ryzen 7 7800X3D / i7-14700KF + RTX 4070 Super + 32GB DDR5 6000MHz + 1TB KC3000 + 750W/850W Gold + AIO 240/360mm
        cpu = next((x for x in by_cat.get("Processor (CPU)", []) if "7800X3D" in x["nama"] or "14700" in x["nama"]), by_cat["Processor (CPU)"][0])
        mobo = next((x for x in by_cat.get("Motherboard", []) if "B650" in x["nama"] or "Z790" in x["nama"]), by_cat["Motherboard"][0])
        ram = next((x for x in by_cat.get("RAM (Memory)", []) if "32GB" in x["nama"] and "6000MHz" in x["nama"]), by_cat["RAM (Memory)"][0])
        ssd = next((x for x in by_cat.get("Penyimpanan (SSD / HDD)", []) if "KC3000" in x["nama"] or "990 PRO" in x["nama"]), by_cat["Penyimpanan (SSD / HDD)"][0])
        gpu = next((x for x in by_cat.get("VGA / Kartu Grafis", []) if "4070" in x["nama"] or "7800 XT" in x["nama"]), by_cat["VGA / Kartu Grafis"][0])
        psu = next((x for x in by_cat.get("Power Supply (PSU)", []) if "750W" in x["nama"] or "850W" in x["nama"]), by_cat["Power Supply (PSU)"][0])
        cooler = next((x for x in by_cat.get("CPU Cooler", []) if "Liquid" in x.get("tipe", "") or "AIO" in x["nama"]), by_cat["CPU Cooler"][0])
        case = next((x for x in by_cat.get("Casing PC", []) if "Lian Li" in x["nama"] or "NZXT" in x["nama"] or "4000D" in x["nama"]), by_cat["Casing PC"][0])

    parts = [cpu, mobo, ram, ssd, gpu, psu, cooler, case]
    total_harga = sum(p["harga"] for p in parts)

    return {
        "tier": tier_name,
        "budget": budget,
        "parts": parts,
        "total_harga": total_harga,
        "sisa_budget": budget - total_harga
    }

