import os
import sys
import re
import json
import requests
from typing import Dict, Any, List, Optional, Tuple
from hardware_knowledge import HARDWARE_EXPLANATIONS
from recommender import (
    format_rupiah, extract_budget, check_unrealistic_request, find_recommendations,
    load_pc_catalog, search_pc_components, build_pc_rig_from_catalog
)

PC_CATALOG = load_pc_catalog()

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# =============================================================================
# METADATA SPESIALIS AI KONSULTAN
# =============================================================================
SPECIALISTS = {
    "laptop": {
        "id": "laptop",
        "name": "Aris",
        "title": "Senior Laptop Consultant",
        "division": "Divisi Laptop & Ultrabook",
        "icon": "💻",
        "color": "cyan",
        "badge": "💻 Spesialis Laptop & Ultrabook",
        "catalog_desc": "500 Unit Laptop Resmi",
        "greeting": "Selamat datang di Sahabat Laptop! Saya Aris, Senior Laptop Consultant. Saya siap membantu Anda memilih laptop yang paling tepat, nyaman, dan seimbang dengan aktivitas harian serta anggaran Anda. Ada yang ingin kita diskusikan hari ini?"
    },
    "pc": {
        "id": "pc",
        "name": "Dimas",
        "title": "Senior PC Master Builder",
        "division": "Divisi Rakit PC & Komponen Desktop",
        "icon": "🛠️",
        "color": "green",
        "badge": "🛠️ Spesialis Rakit PC & Hardware Desktop",
        "catalog_desc": "542 Komponen PC Resmi Gudang",
        "greeting": "Halo! Selamat datang di PC Solution. Saya Dimas, Senior PC Master Builder & Hardware Architect. Saya siap membantu Anda meracik spesifikasi PC desktop dari A sampai Z, memastikan komponen 100% kompatibel tanpa bottleneck, hingga membantu melengkapi part yang sudah Anda miliki. Ada rencana rakit PC seperti apa yang ingin kita wujudkan?"
    }
}

# =============================================================================
# 1. SYSTEM PROMPT UNTUK KONSULTAN LAPTOP (ARIS)
# =============================================================================
LAPTOP_SYSTEM_PROMPT = """
Anda adalah 'Aris', Senior Laptop Consultant & Penasihat Resmi di Toko 'Sahabat Laptop'.
FOKUS KEAHLIAN & SPESIALISASI:
- Anda adalah pakar spesialis dunia LAPTOP (Ultrabook tipis, Laptop Bisnis/Office, Laptop Pelajar & Mahasiswa, Laptop Kreator Layar OLED, dan Laptop Gaming portabel).
- Anda sangat menguasai faktor portabilitas, daya tahan baterai riil, bobot ransel, efisiensi charger Type-C, akurasi layar (sRGB vs DCI-P3), keyboard ergonomis, dan garansi resmi pabrikan (ASUS, Lenovo, Acer, HP, Apple MacBook, MSI, Advan).
- JIKA PELANGGAN BERTANYA SEPUTAR RAKIT PC DESKTOP / KOMPONEN PC:
  Sambut dengan ramah dan jelaskan bahwa toko memiliki divisi khusus Perakitan PC yang dipimpin oleh rekan Anda, 'Mas Dimas' (Senior PC Master Builder). Anda dapat memperkenalkan Mas Dimas dan menyambungkan obrolan dengan beliau.
- STANDAR HARGA REALISTIS PASAR INDONESIA:
  Selalu gunakan harga real resmi pasar Indonesia dalam Rupiah (Rp). Contoh acuan harga pasar resmi Indonesia saat ini:
  * Laptop Entry-Level / Pelajar (Celeron N4020, N100, Athlon): Rp 2.400.000 - Rp 4.900.000
  * Laptop Mainstream Mahasiswa / Kantor (Core i3 Gen 12/13, Ryzen 3/5 7000): Rp 5.800.000 - Rp 8.900.000
  * Laptop Kencang 16GB / Coding / Kreator OLED (Ryzen 5/7 Seri H, Core i5/Ultra 5, 2.8K OLED): Rp 7.000.000 - Rp 15.000.000
  * Laptop Gaming RTX Resmi (RTX 2050 / RTX 3050): Rp 10.000.000 - Rp 12.500.000
  * Laptop Gaming RTX 4050 / RTX 4060: Rp 13.500.000 - Rp 18.000.000
  * MacBook Air M1: Rp 10.500.000 - Rp 11.500.000 (Resmi iBox/Digimap)
  * MacBook Air M2 / M3: Rp 15.000.000 - Rp 21.000.000
  JANGAN PERNAH merekomendasikan laptop fiktif atau kombinasi prosesor yang salah (misal: laptop Dell menggunakan chip Apple Silicon). Selalu rujuk data katalog 500 laptop toko yang dilampirkan.
- BUDAYA KONSULTATIF (Consultative Discovery First):
  Dengarkan dan eksplorasi kebutuhan sebelum menyodorkan unit/harga jika pelanggan belum memintanya secara eksplisit.
- NADA BICARA (Tone): Sopan, santun, hangat, empatik, sabar, dan berbobot (gunakan sapaan 'Kakak', 'Bapak/Ibu', atau 'Anda').
- BASIS REKOMENDASI: Gunakan data resmi katalog 500 unit laptop toko yang dilampirkan.
"""

# =============================================================================
# 2. SYSTEM PROMPT UNTUK MASTER BUILDER PC (DIMAS)
# =============================================================================
PC_SYSTEM_PROMPT = """
Anda adalah 'Dimas', Senior PC Master Builder & Hardware Architect di Toko 'PC Solution' (Divisi Rakit PC & Komponen Desktop).
FOKUS KEAHLIAN & SPESIALISASI:
- Anda adalah master builder dan arsitek perangkat keras PC Desktop. Sangat menguasai perakitan PC dari A sampai Z, pemilihan 8 komponen utama yang 100% kompatibel dan siap nyala:
  1. Prosesor (CPU AMD AM4/AM5, Intel LGA1200/LGA1700)
  2. Motherboard (A520, B550, B650, H610, B760, Z790 dll.)
  3. RAM Dual-Channel (DDR4 vs DDR5)
  4. Penyimpanan (M.2 NVMe SSD Gen3/Gen4)
  5. Kartu Grafis (GPU / VGA NVIDIA GeForce RTX/GTX, AMD Radeon RX, Intel Arc)
  6. Power Supply (PSU bersertifikasi 80+ Bronze/Gold dengan proteksi OVP/OPP/SCP)
  7. CPU Cooler (Air Cooler tower vs AIO Liquid Cooler 240/360mm)
  8. Casing PC (Airflow mesh vs Panoramic Aquarium tempered glass)
- Menghilangkan Efek Bottleneck & Menghitung Wattage PSU dengan aman.
- STANDAR HARGA REALISTIS PASAR HARDWARE INDONESIA:
  Selalu gunakan harga komponen desktop real pasar Indonesia (standard Enterkomputer, Tokopedia, Mangga Dua) dalam Rupiah (Rp). Contoh acuan:
  * Prosesor: Athlon ~Rp 600rb, Ryzen 5 5600 / i5-12400F ~Rp 1,75jt, Ryzen 5 7500F ~Rp 2,45jt, Ryzen 7 7800X3D ~Rp 6,95jt.
  * GPU: RX 580 8GB ~Rp 1,15jt, GTX 1650 ~Rp 2,1jt, RX 6600 8GB ~Rp 3,1jt, RTX 3050 6GB ~Rp 2,8jt, RTX 4060 8GB ~Rp 4,8jt, RTX 4070 Super ~Rp 10,8jt.
  * Motherboard: A520M ~Rp 850rb, B550M ~Rp 950rb - 1,4jt, H610M ~Rp 950rb, B760M ~Rp 1,6jt - 2,4jt, B650M AM5 ~Rp 1,8jt - 2,5jt.
  * RAM: 16GB DDR4 ~Rp 500rb - 700rb, 32GB DDR4 ~Rp 1,1jt - 1,3jt, 16GB DDR5 ~Rp 800rb - 1jt, 32GB DDR5 6000MHz ~Rp 1,7jt - 2jt.
  * SSD NVMe: 512GB ~Rp 500rb - 650rb, 1TB ~Rp 900rb - 1,3jt.
  * PSU 80+ Bronze: 500W-550W ~Rp 550rb - 750rb, 650W ~Rp 850rb - 1,1jt, 750W Gold ~Rp 1,4jt - 1,8jt.
  * Total racikan PC lengkap 8 part siap nyala:
    - Hemat Office/Kasir (dengan iGPU): Rp 3,5jt - Rp 4,5jt
    - Gaming Hemat Esport (Ryzen 5 5600GT / RX 580): Rp 5,5jt - Rp 6,5jt
    - Sweet Spot Gaming 1080p Ultra (Ryzen 5 5600 + RX 6600 / RTX 3050): Rp 8,5jt - Rp 10jt
    - Modern Next-Gen Gaming (Ryzen 5 7500F / i5-13400F + RTX 4060 DDR5): Rp 13jt - Rp 16jt
- LAYANAN MELENGKAPI PART PARSIAL:
  Jika pelanggan sudah membeli sebagian komponen sendiri, sambut dengan antusias! Cek kompatibilitas soket CPU/Mobo, jenis RAM, watt PSU yang aman, dan sarankan part pelengkap terbaik dari stok toko kami.
- LAYANAN FISIK TOKO:
  Melayani rakit rapi (clean cable management), update BIOS terbaru, instalasi Windows + driver resmi, serta uji beban stress test gratis.
- JIKA PELANGGAN BERTANYA TENTANG LAPTOP PORTABEL:
  Sampaikan dengan ramah bahwa rekan Anda 'Mas Aris' (Senior Laptop Consultant) adalah ahlinya di divisi laptop dan tawarkan untuk menyambungkan obrolan dengan Mas Aris.
- WAJIB MENYERTAKAN CATATAN KEAMANAN PERAKITAN:
  Setiap kali Anda selesai memberikan rekomendasi spesifikasi/racikan PC atau komponen desktop kepada pelanggan, Anda WAJIB menyertakan kalimat penutup persis seperti berikut di bagian paling akhir respon Anda:
  "> ⚠️ **Catatan Penting Keamanan Perakitan:**
  > *Untuk keamanan perakitan yang optimal, mohon konfirmasikan terlebih dahulu rekomendasi ini kepada teknisi atau staf toko kami sebelum proses perakitan dimulai agar saat dirakit tidak mengalami kendala, karena saya hanya dapat memberikan rekomendasi berdasarkan kecocokan data spesifikasi teknis, bukan berdasarkan pengalaman praktik langsung di lapangan.*"
- NADA BICARA (Tone): Ramah, antusias, teknis namun mudah dimengerti orang awam, solutif, dan profesional.
- BASIS REKOMENDASI: Gunakan data resmi 542 komponen PC resmi gudang toko yang dilampirkan.
"""

# Catatan Disclaimer Keamanan Resmi Perakitan PC
PC_BUILD_SAFETY_DISCLAIMER = (
    "\n\n> ⚠️ **Catatan Penting Keamanan Perakitan:**\n"
    "> *Untuk keamanan perakitan yang optimal, mohon konfirmasikan terlebih dahulu rekomendasi ini kepada teknisi atau staf toko kami sebelum proses perakitan dimulai agar saat dirakit tidak mengalami kendala, karena saya hanya dapat memberikan rekomendasi berdasarkan kecocokan data spesifikasi teknis, bukan berdasarkan pengalaman praktik langsung di lapangan.*"
)

def append_pc_safety_disclaimer_if_needed(text: str, query: str = "") -> str:
    """
    Menambahkan catatan disclaimer keamanan perakitan pada respon AI PC (Dimas)
    jika respon tersebut memuat rekomendasi spesifikasi, part, atau racikan PC.
    """
    if not text:
        return text
    
    # Cek apakah disclaimer sudah ada dalam respon
    if "keamanan perakitan" in text.lower() or "konfirmasi terlebih dahulu pada teknisi" in text.lower():
        return text

    # Indikator rekomendasi hardware/komponen/harga
    indicators = [
        "prosesor", "motherboard", "kartu grafis", "gpu", "vga", "power supply",
        "psu", "casing", "cooler", "ram", "nvme", "ssd", "komponen", "racikan",
        "estimasi biaya", "sisa budget", "sweet spot", "soket", "paket"
    ]
    text_lower = text.lower()
    has_spec = any(w in text_lower for w in indicators) and ("rp" in text_lower or ":" in text or "-" in text or "*" in text)
    
    q_lower = query.lower()
    is_pc_req = any(w in q_lower for w in ["rakit", "pc", "gaming", "budget", "juta", "part", "komponen", "saran", "bagusnya", "pilihan", "rekomendasi"])

    if has_spec or (is_pc_req and any(w in text_lower for w in ["rp", "rekomendasi", "pilihan", "komponen", "prosesor", "vga"])):
        return text.rstrip() + PC_BUILD_SAFETY_DISCLAIMER
    
    return text


import joblib

ML_MODEL_DATA = None
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model_intent_laptop.pkl")
if os.path.exists(MODEL_PATH):
    try:
        ML_MODEL_DATA = joblib.load(MODEL_PATH)
    except Exception:
        ML_MODEL_DATA = None

def predict_intent_ml(text: str):
    """Memprediksi niat percakapan pelanggan menggunakan model Machine Learning yang telah dilatih."""
    if not ML_MODEL_DATA:
        return None, 0.0
    try:
        model = ML_MODEL_DATA["model"]
        vectorizer = ML_MODEL_DATA["vectorizer"]
        vec = vectorizer.transform([text])
        pred = model.predict(vec)[0]
        prob = max(model.predict_proba(vec)[0]) * 100
        return pred, prob
    except Exception:
        return None, 0.0

def detect_specialist_domain(query: str, current_mode: str = "auto", chat_history: Optional[List[Dict[str, str]]] = None) -> str:
    """
    Mendeteksi apakah pertanyaan pelanggan lebih relevan untuk Konsultan Laptop (Aris)
    atau Master Builder PC (Dimas).
    """
    q_low = query.lower().strip()

    # Perintah eksplisit ganti konsultan
    if any(w in q_low for w in ["tanya dimas", "ke dimas", "mode pc", "ganti pc", "pindah pc", "spesialis pc"]):
        return "pc"
    if any(w in q_low for w in ["tanya aris", "ke aris", "mode laptop", "ganti laptop", "pindah laptop", "spesialis laptop"]):
        return "laptop"

    # Jika mode sudah dikunci manual oleh user (bukan auto):
    if current_mode in ["pc", "laptop"]:
        return current_mode

    # Auto-detection berbasis kata kunci
    pc_keywords = [
        "rakit pc", "rakit komputer", "komponen", "desktop", "part pc", "pc gaming",
        "spek pc", "vga", "gpu", "motherboard", "mobo", "ram pc", "casing", "cooler",
        "power supply", "psu", "rakitan", "komputer", "build pc", "bawa part", "sudah beli",
        "am4", "am5", "lga1700", "rtx 4060", "rx 6600", "aio", "heatsink", "fan casing",
        "pc", "cpu rakitan", "nyala", "nyalain pc", "bisa rakit"
    ]
    
    laptop_keywords = [
        "laptop", "notebook", "ultrabook", "macbook", "baterai", "charger", "bawa ke kampus",
        "bobot", "ringan", "enteng", "layar oled", "layar ips", "engsel", "keyboard numpad",
        "sekolah sd", "anak sekolah", "kuliah", "tas ransel"
    ]

    pc_score = sum(1 for kw in pc_keywords if kw in q_low)
    laptop_score = sum(1 for kw in laptop_keywords if kw in q_low)

    ml_intent, _ = predict_intent_ml(query)
    if ml_intent == "tanya_rakit_pc":
        pc_score += 3

    if pc_score > laptop_score:
        return "pc"
    elif laptop_score > pc_score:
        return "laptop"

    # Cek kata kunci rakitan eksplisit
    if any(w in q_low for w in ["rakit", "komponen", "part", "vga", "mobo", "psu", "casing"]):
        return "pc"

    # Default ke laptop jika tidak ada kata kunci PC
    return "laptop"

# =============================================================================
# 3. MESIN RESPON LOKAL: SPESIALIS LAPTOP (ARIS)
# =============================================================================
def generate_local_laptop_response(
    query: str,
    recommendations: List[Dict[str, Any]],
    catalog: List[Dict[str, Any]],
    chat_history: Optional[List[Dict[str, str]]] = None
) -> str:
    """Respon lokal khusus divisi Laptop oleh Aris (Senior Laptop Consultant)."""
    q_lower = query.lower()
    budget = extract_budget(query)

    # Handover ke Dimas jika pelanggan tiba-tiba bertanya rakit PC
    if any(w in q_lower for w in ["rakit pc", "rakit komputer", "komponen pc", "part pc", "bisa rakit"]):
        return (
            "Halo Kak! Untuk perakitan PC desktop kustom dan pengecekan part hardware secara detail, "
            "toko kami memiliki divisi spesialis yang dipimpin oleh rekan saya, **Mas Dimas (Senior PC Master Builder)**.\n\n"
            "Mas Dimas sangat menguasai perakitan 8 part PC, kompatibilitas soket, pencegahan bottleneck, hingga melengkapi part yang sudah Kakak miliki.\n\n"
            "💡 *Tips:* Ketik **'mode pc'** atau **'tanya dimas'** untuk langsung berkonsultasi mendalam dengan Mas Dimas!"
        )

    # 1. Istilah 'Laptop Ghaib'
    if "ghaib" in q_lower or "gaib" in q_lower:
        return (
            "Pertanyaan yang sangat menarik dan sering ditanyakan!\n\n"
            "Istilah **'Laptop Ghaib'** adalah ungkapan populer untuk menggambarkan laptop dengan spesifikasi impian yang sangat tinggi "
            "(seperti GPU NVIDIA RTX, layar OLED 100% sRGB, bodi tipis) namun diharapkan berada pada harga yang secara realitas industri tidak ada (misalnya di bawah 5 juta baru).\n\n"
            "Kunci utama dalam memilih laptop adalah menyelaraskan prioritas kebutuhan dengan anggaran yang realistis. Apakah ada rencana penggunaan laptop tertentu yang sedang Kakak pertimbangkan saat ini?"
        )

    # 2. Mac vs Windows
    if ("mac" in q_lower and "windows" in q_lower) or "mending mac" in q_lower or "mending windows" in q_lower or "bagusan mac" in q_lower:
        return (
            "Dilema antara **Windows** atau **MacBook (Apple)** adalah hal yang sangat wajar dialami calon pengguna.\n\n"
            "⚖️ **Tinjauan Objektif:**\n"
            "1. **Pilih Windows jika:** Anda menginginkan fleksibilitas software yang luas (banyak aplikasi teknik, akuntansi, game yang hanya ada di Windows) dan kemudahan opsi upgrade.\n"
            "2. **Pilih MacBook jika:** Prioritas utama Anda adalah efisiensi baterai (baterai Apple Silicon tahan 15-18 jam riil tanpa charger) dan akurasi warna layar untuk desain/video kreatif.\n\n"
            "Bolehkah kami mengetahui software atau aktivitas utama yang paling sering Anda gunakan sehari-hari?"
        )

    # 3. Kebutuhan Anak Sekolah SD / Pelajar
    if any(w in q_lower for w in ["anak sekolah", "sekolah sd", "anak sd", "sd", "pelajar", "sekolah"]):
        return (
            "Untuk kebutuhan ananda sekolah SD atau pelajar, prioritas utama bukanlah spesifikasi gaming yang mahal, "
            "melainkan **ketahanan fisik (durability), layar yang aman di mata, keyboard yang nyaman mengetik tugas, dan bobot yang tidak memberatkan ransel**.\n\n"
            "📝 **Kriteria Laptop Ideal untuk Pelajar SD/SMP:**\n"
            "1. **Prosesor Cukup & Hemat Daya:** Intel Core i3 / Celeron generasi baru atau AMD Ryzen 3 / Athlon sudah sangat lancar untuk mengetik di Microsoft Word, browsing tugas, dan Google Classroom / Zoom.\n"
            "2. **RAM & Penyimpanan:** Minimal RAM 8GB agar tidak lag saat membuka banyak tab materi belajar, dan wajib SSD (minimal 256GB/512GB) agar booting cepat.\n"
            "3. **Layar:** Ukuran 14 inci berpanel IPS dengan fitur anti-glare agar mata anak tidak cepat lelah saat belajar daring.\n"
            "4. **Rentang Harga Ekonomis:** Umumnya berada di kisaran **3 jutaan hingga 5 jutaan rupiah** sudah sangat memadai dan awet bertahun-tahun.\n\n"
            "Apakah ananda sudah memiliki preferensi tertentu, atau ingin kami tampilkan daftar pilihan paling terjangkau yang saat ini ready stok di toko?"
        )

    # 4. Tips Memilih Laptop / Pemula Bingung
    if any(w in q_lower for w in ["bingung", "pemula", "awam", "tips memilih", "cara memilih", "pertama kali"]):
        return (
            "Sangat wajar jika Anda merasa bingung saat pertama kali memilih laptop. Dunia spesifikasi komputer memang dipenuhi banyak istilah teknis.\n\n"
            "🎯 **3 Pertanyaan Kunci untuk Menemukan Kebutuhan Anda yang Sebenarnya:**\n"
            "1. **Seberapa Sering Anda Bepergian?** Jika sering dibawa bepergian, prioritaskan bobot ringan (di bawah 1.4 kg) dan baterai awet.\n"
            "2. **Aktivitas Terberat yang Dijalankan?** Mengetik/office cukup RAM 8-16GB prosesor hemat daya; desain/programming butuh layar akurat; 3D/gaming butuh GPU RTX.\n"
            "3. **Berapa Pagu Anggaran Nyaman Anda?** Menetapkan pagu anggaran membantu menyaring opsi terbaik.\n\n"
            "Dari gambaran di atas, kira-kira aktivitas harian Anda nantinya akan lebih banyak seperti apa? Jangan sungkan untuk berbagi cerita dulu."
        )

    # 5. Permintaan di Luar Realitas Pasar
    unrealistic = check_unrealistic_request(query, budget)
    if unrealistic:
        if unrealistic["type"] == "rtx_under_budget":
            b_str = format_rupiah(unrealistic["budget"])
            return (
                f"Perlu kami sampaikan secara transparan bahwa laptop baru dengan kartu grafis **NVIDIA RTX**, "
                f"saat ini belum tersedia di pasar resmi pada kisaran harga di bawah {b_str}.\n"
                f"Laptop berbasis NVIDIA RTX resmi umumnya dimulai pada kisaran **Rp 9.500.000 – Rp 10.500.000** (misal ASUS Vivobook 14X RTX 3050). "
                f"Untuk budget Kakak, kami siap carikan laptop komputasi harian terbaik."
            )

    # 6. Rekomendasi konkret jika diminta
    is_asking_for_product = any(w in q_lower for w in [
        "rekomendasi", "saran laptop", "pilihin", "dapet apa", "budget", "ada laptop",
        "opsi laptop", "tipe apa", "katalog", "harga", "beli laptop", "rekomendasikan", "cari laptop",
        "paling murah", "termurah", "murah", "list", "minta list", "pilihan laptop", "unit apa"
    ]) or (budget is not None)

    if is_asking_for_product and recommendations:
        reply = [f"Berdasarkan kebutuhan dan kriteria yang Kakak sampaikan, berikut adalah rekomendasi laptop resmi pilihan di toko kami:\n"]
        for idx, lap in enumerate(recommendations, 1):
            specs = lap["spesifikasi"]
            reply.append(f"**Opsi #{idx}: {lap['nama']}** ({format_rupiah(lap['harga'])})")
            reply.append(f"- **Kategori:** {lap['kategori']}")
            reply.append(f"- **Dapur Pacu:** {specs['prosesor']} | GPU: {specs['gpu']} | RAM {specs['ram']}")
            reply.append(f"- **Display & Bobot:** {specs['layar']} ({specs['berat']})")
            reply.append(f"- **Keunggulan Utama:** {lap['kelebihan'][0]}")
            reply.append(f"- **Stok Gudang:** Tersedia {lap['stok']} unit\n")
        reply.append("Apakah ada seri tertentu yang ingin Kakak diskusikan lebih mendalam?")
        return "\n".join(reply)

    # Default Konsultatif
    return (
        "Selamat datang di Sahabat Laptop! Saya Aris, Senior Laptop Consultant.\n\n"
        "Kami sangat senang membantu Anda membedah kebutuhan terlebih dahulu sebelum Anda memutuskan memilih tipe tertentu. "
        "Bolehkah kami mengetahui jenis aktivitas atau pekerjaan utama apa saja yang rencananya akan Anda jalankan dengan laptop ini? "
        "Silakan bercerita santai, kami siap mendengarkan."
    )

# =============================================================================
# 4. MESIN RESPON LOKAL: MASTER BUILDER PC (DIMAS)
# =============================================================================
def generate_local_pc_response(
    query: str,
    pc_catalog: List[Dict[str, Any]],
    chat_history: Optional[List[Dict[str, str]]] = None
) -> str:
    """Respon lokal khusus divisi Rakit PC & Komponen oleh Dimas (Senior PC Master Builder)."""
    q_lower = query.lower()
    budget = extract_budget(query)

    # Handover ke Aris jika pelanggan bertanya laptop
    if any(w in q_lower for w in ["laptop", "ultrabook", "macbook", "notebook", "baterai awet", "laptop kuliah"]):
        return (
            "Halo Kak! Kalau kebutuhan Kakak adalah komputer portabel yang ringan, praktis dibawa bepergian, dan hemat baterai, "
            "toko kami memiliki divisi khusus Laptop bersama rekan saya, **Mas Aris (Senior Laptop Consultant)**.\n\n"
            "Mas Aris sangat paham seluk-beluk 500 unit laptop resmi toko kami untuk kuliah, kantor, hingga kreator.\n\n"
            "💡 *Tips:* Ketik **'mode laptop'** atau **'tanya aris'** untuk langsung terhubung dengan Mas Aris!"
        )

    # 1. Melengkapi Part Parsial yang Sudah Dibeli Sendiri
    if any(w in q_lower for w in ["sudah beli", "sudah punya", "beberapa komponen", "punya beberapa", "part sendiri", "bawa part", "melengkapi", "bagusnya yang mana", "cocoknya apa"]):
        res = (
            "Kabar baik untuk Kakak, **tentu saja SANGAT BISA dan amat kami anjurkan!** 👍\n\n"
            "Bahkan, berkonsultasi sebelum membeli part pelengkap adalah langkah paling tepat untuk menghindari risiko salah beli, ketidaktercocokan soket, atau ketimpangan performa (*bottleneck*).\n\n"
            "🔍 **5 Poin Pemeriksaan Teknis yang Akan Saya Bantu Analisis:**\n"
            "1. **Kesesuaian Soket & Chipset Motherboard:** Memastikan motherboard cocok 100% dengan prosesor yang sudah Kakak beli (misal: AMD AM4 vs AM5, atau Intel LGA1200 vs LGA1700).\n"
            "2. **Kesesuaian Generasi RAM:** Menyesuaikan standar memori (DDR4 vs DDR5) agar pas dengan slot motherboard.\n"
            "3. **Kalkulasi Daya & Keamanan PSU:** Menghitung total konsumsi daya (TDP CPU + GPU yang sudah ada) agar kapasitas watt PSU (550W / 650W / 750W 80+ Bronze/Gold) aman dan stabil.\n"
            "4. **Dimensi Fisik (*Clearance Check*):** Memastikan panjang VGA muat di casing dan tinggi pendingin CPU tidak mentok kaca samping.\n"
            "5. **Layanan Rakit & Finishing Toko:** Kakak boleh membawa part yang sudah dibeli ke toko. Saya dan tim teknisi siap melengkapi part sisanya langsung dari 542 stok gudang toko kami, merakit dengan *clean cable management*, install Windows, update BIOS, dan uji *stress test* sampai PC siap pakai.\n\n"
            "Agar bisa langsung saya carikan pasangan part terbaik dari stok toko kami:\n"
            "👉 **Komponen apa saja yang saat ini sudah Kakak beli (sebutkan merk & tipenya)?**\n"
            "👉 **Dan kira-kira berapa sisa budget yang Kakak siapkan untuk part pelengkapnya?**"
        )
        return append_pc_safety_disclaimer_if_needed(res, query)

    # 2. Simulasi Rakit PC berdasarkan Budget atau Permintaan Rekomendasi
    is_asking_rig = budget or any(w in q_lower for w in ["rakit", "pc", "gaming", "budget", "juta", "jt", "part", "komponen", "spek", "build", "saran", "bagusnya"])
    if is_asking_rig:
        target_budget = budget if budget else 10_000_000
        rig = build_pc_rig_from_catalog(target_budget, pc_catalog)
        
        reply = [
            f"Pilihan yang sangat tepat, Kak! Untuk budget **{format_rupiah(target_budget)}**, racikan **'{rig['tier']}'** adalah racikan paling seimbang, bertenaga, dan 100% siap nyala.\n",
            f"🖥️ **Rincian Lengkap 8 Komponen Utama dari Stok Resmi Toko Kami:**\n"
        ]
        
        for idx, p in enumerate(rig["parts"], 1):
            cat_short = p["kategori"].replace("Processor (CPU)", "CPU").replace("Penyimpanan (SSD / HDD)", "SSD").replace("VGA / Kartu Grafis", "VGA")
            reply.append(f"{idx}. **{cat_short}:** {p['nama']} ~ **{format_rupiah(p['harga'])}**")
            reply.append(f"   • *{p.get('spesifikasi_ringkas', 'Komponen resmi bergaransi')}*")
            
        reply.append(f"\n💰 **Total Estimasi Biaya Komponen:** **{format_rupiah(rig['total_harga'])}**")
        if rig['sisa_budget'] > 0:
            reply.append(f"💵 **Sisa Anggaran:** **{format_rupiah(rig['sisa_budget'])}** *(Bisa dialokasikan untuk monitor gaming, upgrade RAM/SSD, atau periferal pendukung!)*")
        
        reply.append("\n🎁 **Fasilitas Gratis di Toko:** Clean Cable Management, Update BIOS terbaru, Instalasi Windows 11 & Driver resmi, serta Stress Test pengujian beban penuh sebelum diserahkan.")
        reply.append("\nBagaimana Kak, apakah racikan spesifikasi ini sudah sesuai dengan kebutuhan Kakak?")
        
        full_res = "\n".join(reply)
        return append_pc_safety_disclaimer_if_needed(full_res, query)

    # 3. Layanan Rakit PC Umum
    res_default = (
        "Halo! Selamat datang di PC Solution. Saya Dimas, Senior PC Master Builder & Hardware Architect.\n\n"
        "Toko kami melayani perakitan custom PC desktop dari nol maupun melengkapi part yang sudah Kakak bawa sendiri. "
        "Seluruh perakitan dikerjakan oleh teknisi ahli dengan standar:\n"
        "1. **Clean Cable Management** (kabel rapi di belakang untuk sirkulasi udara dingin).\n"
        "2. **Update BIOS & Instalasi OS Resmi** (Windows 11 aktif + driver terbaru).\n"
        "3. **Thermal Paste Premium & Stress Test** (uji beban Cinebench & FurMark sebelum diserahkan).\n"
        "4. **Garansi Resmi Distributor Penuh** (1 hingga 3 tahun per part).\n\n"
        "Boleh ceritakan, rencana penggunaan PC ini untuk apa (Gaming, Editing/3D, atau Office)? Dan berapa anggaran yang ingin disiapkan?"
    )
    return res_default

# =============================================================================
# 5. INTEGRASI DENGAN GOOGLE GEMINI API (DUAL SPECIALIST RAG)
# =============================================================================
def ask_gemini_api(
    query_or_history,
    catalog: List[Dict[str, Any]],
    api_key: str,
    specialist: str = "auto"
) -> Tuple[Optional[str], str]:
    """
    Mengirimkan riwayat percakapan ke Google Gemini API dengan memilih persona spesialis yang tepat:
    - Aris (Senior Laptop Consultant) untuk pertanyaan seputar laptop.
    - Dimas (Senior PC Master Builder) untuk pertanyaan seputar rakit PC & komponen.
    
    Mengembalikan Tuple: (teks_respon, active_specialist)
    """
    try:
        if isinstance(query_or_history, list):
            user_messages = [turn["content"] for turn in query_or_history if turn["role"] == "user"]
            user_query = " ".join(user_messages[-3:]) if user_messages else ""
        else:
            user_query = str(query_or_history)

        # Tentukan spesialis aktif
        active_specialist = detect_specialist_domain(user_query, current_mode=specialist)
        user_lower = user_query.lower()
        budget = extract_budget(user_query)

        if active_specialist == "pc":
            spec_info = SPECIALISTS["pc"]
            system_prompt_base = PC_SYSTEM_PROMPT
            pc_context = {}
            if budget:
                pc_context["simulasi_rig_pc_lengkap_sesuai_budget"] = build_pc_rig_from_catalog(budget, PC_CATALOG)
            
            limit_items = 25 if any(w in user_lower for w in ["sebanyak", "banyak", "list", "daftar", "semua", "stok"]) else 12
            pc_context["kandidat_stok_komponen_toko"] = search_pc_components(user_query, PC_CATALOG, limit=limit_items)
            
            cat_counts = {}
            for item in PC_CATALOG:
                cat_counts[item["kategori"]] = cat_counts.get(item["kategori"], 0) + 1
            pc_context["ringkasan_stok_gudang"] = {
                "total_stok_komponen": len(PC_CATALOG),
                "kategori_tersedia": cat_counts
            }
            
            catalog_summary = json.dumps(pc_context, indent=2, ensure_ascii=False)
            catalog_header = "--- DATA RESMI STOK KOMPONEN PC & SIMULASI GUDANG TOKO (542 PART RESMI) ---"
            catalog_footer = "--- AKHIR DATA KOMPONEN PC ---"
            instructions_extra = (
                "PANDUAN INTERAKSI MASTER BUILDER PC (DIMAS):\n"
                "1. Fokuskan jawaban sebagai Dimas, Master Builder PC desktop.\n"
                "2. Jika diminta meracik PC, sajikan 8 komponen lengkap sampai nyala dengan harga resmi toko.\n"
                "3. Jika pelanggan sudah beli sebagian part, bantu cek kompatibilitas soket, RAM, watt PSU, dan sarankan part pelengkap dari stok toko.\n"
                "4. Jika pelanggan bertanya laptop, arahkan dengan ramah ke rekan Anda, Mas Aris (Laptop Consultant).\n"
                "5. WAJIB: Setiap kali memberikan rekomendasi racikan/spesifikasi PC atau komponen desktop, selalu akhiri respon dengan catatan penutup:\n"
                "   '> ⚠️ **Catatan Penting Keamanan Perakitan:**\n"
                "   > *Untuk keamanan perakitan yang optimal, mohon konfirmasikan terlebih dahulu rekomendasi ini kepada teknisi atau staf toko kami sebelum proses perakitan dimulai agar saat dirakit tidak mengalami kendala, karena saya hanya dapat memberikan rekomendasi berdasarkan kecocokan data spesifikasi teknis, bukan berdasarkan pengalaman praktik langsung di lapangan.*'"
            )
        else:
            spec_info = SPECIALISTS["laptop"]
            system_prompt_base = LAPTOP_SYSTEM_PROMPT
            candidates = find_recommendations(user_query, catalog, limit=8)
            if not candidates:
                candidates = sorted(catalog, key=lambda x: x["harga"])[:8]
            catalog_summary = json.dumps(candidates, indent=2, ensure_ascii=False)
            catalog_header = "--- DATA KANDIDAT UNIT LAPTOP RESMI DARI KATALOG 500 STOK TOKO ---"
            catalog_footer = "--- AKHIR KATALOG LAPTOP ---"
            instructions_extra = (
                "PANDUAN INTERAKSI KONSULTAN LAPTOP (ARIS):\n"
                "1. Fokuskan jawaban sebagai Aris, Senior Laptop Consultant.\n"
                "2. Dahulukan diskusi kebutuhan mobilitas, baterai, layar, dan kenyamanan sebelum menodongkan produk.\n"
                "3. Jika pelanggan bertanya rakit PC, jelaskan layanan toko dan perkenalkan rekan Anda, Mas Dimas (Senior PC Master Builder).\n"
                "4. Gunakan data kandidat laptop toko yang dilampirkan jika pelanggan meminta rekomendasi."
            )

        system_instruction_text = (
            f"{system_prompt_base}\n\n"
            f"{catalog_header}\n"
            f"{catalog_summary}\n"
            f"{catalog_footer}\n\n"
            f"{instructions_extra}\n"
            f"SELALU RAMAH & EMPATIK: Bimbing orang awam dengan analogi yang mudah dipahami, gunakan sapaan 'Kakak', 'Bapak/Ibu', atau 'Anda'."
        )

        if isinstance(query_or_history, list):
            contents = []
            for turn in query_or_history:
                role = "user" if turn["role"] == "user" else "model"
                contents.append({
                    "role": role,
                    "parts": [{"text": turn["content"]}]
                })
        else:
            contents = [
                {
                    "role": "user",
                    "parts": [{"text": str(query_or_history)}]
                }
            ]

        payload = {
            "system_instruction": {
                "parts": [{"text": system_instruction_text}]
            },
            "contents": contents,
            "generationConfig": {
                "temperature": 0.6,
                "maxOutputTokens": 1200
            }
        }

        # Model urutan prioritas: Utamakan model lite yang aktif dan cepat
        models_to_try = [
            "gemini-3.5-flash-lite",
            "gemini-flash-lite-latest",
            "gemini-2.5-flash-lite",
            "gemini-2.5-flash",
            "gemini-3.5-flash"
        ]

        for model_name in models_to_try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
            headers = {"Content-Type": "application/json"}
            
            try:
                response = requests.post(url, headers=headers, json=payload, timeout=12)
                if response.status_code == 200:
                    data = response.json()
                    candidates_res = data.get("candidates", [])
                    if candidates_res:
                        content_part = candidates_res[0].get("content", {}).get("parts", [])
                        if content_part:
                            raw_reply = content_part[0].get("text", "").strip()
                            if active_specialist == "pc":
                                raw_reply = append_pc_safety_disclaimer_if_needed(raw_reply, user_query)
                            return raw_reply, active_specialist
                elif response.status_code == 429:
                    continue
            except Exception:
                continue

        return None, active_specialist
    except Exception:
        return None, "laptop"

# =============================================================================
# 6. ROUTER RESPON LOKAL TERPADU
# =============================================================================
def generate_local_response(
    query: str,
    recommendations: List[Dict[str, Any]],
    catalog: List[Dict[str, Any]],
    pc_catalog: Optional[List[Dict[str, Any]]] = None,
    chat_history: Optional[List[Dict[str, str]]] = None,
    specialist: str = "auto"
) -> Tuple[str, str]:
    """
    Router lokal yang memilih spesialis Aris (Laptop) atau Dimas (PC).
    Mengembalikan Tuple: (response_text, active_specialist)
    """
    if pc_catalog is None:
        pc_catalog = PC_CATALOG

    active_specialist = detect_specialist_domain(query, current_mode=specialist, chat_history=chat_history)
    
    if active_specialist == "pc":
        response_text = generate_local_pc_response(query, pc_catalog, chat_history)
        response_text = append_pc_safety_disclaimer_if_needed(response_text, query)
    else:
        response_text = generate_local_laptop_response(query, recommendations, catalog, chat_history)

    return response_text, active_specialist

