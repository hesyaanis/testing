import json
import random

# Definisi Data Dasar untuk 500 Laptop Realistis
BRANDS_CONFIG = {
    "ASUS": {
        "series": [
            ("Vivobook Go 14 E1404", "Entry-Level / Mahasiswa / Office", 4299000, 6500000, "office"),
            ("Vivobook 14 A1405", "All-Rounder / Produktivitas", 7299000, 10500000, "coding"),
            ("Vivobook 14X K3405", "Creator Pemula / Editing", 10499000, 13990000, "desain"),
            ("Zenbook 14 OLED UX3405", "Ultrabook Premium / Portabel", 16999000, 23999000, "premium"),
            ("TUF Gaming A15 FA506", "Gaming Terjangkau / Heavy Task", 11999000, 16500000, "gaming"),
            ("TUF Gaming F15 FX507", "Gaming & Render 3D Solid", 13499000, 18999000, "gaming"),
            ("ROG Strix G16 G614", "Gaming Esports Pro / Enthusiast", 21999000, 34999000, "gaming_pro"),
            ("ROG Zephyrus G14 GA403", "Ultrabook Gaming Tipis Mewah", 28999000, 42999000, "flagship")
        ]
    },
    "Lenovo": {
        "series": [
            ("IdeaPad Slim 1 14", "Pelajar / Tugas Ringan", 3899000, 5299000, "pelajar"),
            ("IdeaPad Slim 3 14", "Office Harian / Kuliah Santai", 5899000, 8499000, "office"),
            ("IdeaPad Slim 5 14", "Multitasking Cepat / Desain Tipis", 9999000, 13499000, "coding"),
            ("IdeaPad Pro 5 14", "Content Creator Ringan", 14500000, 19999000, "desain"),
            ("LOQ 15IAX9 / 15IRX9", "Budget Gaming Paling Worth It", 12499000, 16999000, "gaming"),
            ("Legion 5 16IRX9", "Gaming & Workstation Tangguh", 18999000, 26999000, "gaming_pro"),
            ("Legion Pro 7 16", "Heavy 3D Render & Esports Rata Kanan", 34999000, 49999000, "flagship"),
            ("ThinkPad E14 Gen 5", "Durabilitas Tinggi / Bisnis / IT", 10999000, 17499000, "bisnis"),
            ("Yoga 7 2-in-1 14", "Convertible Layar Sentuh Stylus", 15499000, 21999000, "creative")
        ]
    },
    "Acer": {
        "series": [
            ("Aspire Lite 14 AL14", "Budget Minimalis / Pelajar", 4499000, 6299000, "pelajar"),
            ("Aspire 5 Slim A514", "All-Rounder Kuliah & Kerja", 6999000, 9999000, "office"),
            ("Swift Go 14 OLED SFG14", "Layar 2.8K OLED / Tipis Mewah", 11999000, 15999000, "desain"),
            ("Swift Edge 16 OLED", "16 Inch Tapi Bobot 1.2 kg", 17999000, 23999000, "premium"),
            ("Nitro V 15 ANV15", "Gaming Ekonomis / Dingin", 10999000, 15499000, "gaming"),
            ("Predator Helios Neo 16", "Gaming Berat / TGP Maksimal", 19999000, 27999000, "gaming_pro"),
            ("Predator Helios 18", "Monster Desktop Replacement", 38999000, 56999000, "flagship")
        ]
    },
    "HP": {
        "series": [
            ("HP 14s-dq / fq", "Laptop Harian Sejuta Umat", 4599000, 7299000, "office"),
            ("HP Pavilion 14-dv", "Elegan / Multitasking Lancar", 8499000, 11999000, "coding"),
            ("HP Pavilion Plus 14", "OLED Tipis / Performa Kencang", 12999000, 16999000, "desain"),
            ("HP Victus 15-fb / fa", "Gaming Pemula / Kalem", 10899000, 14999000, "gaming"),
            ("HP Victus 16-r", "Layar Lebar 16.1 Inch Gaming", 15499000, 20999000, "gaming"),
            ("HP OMEN 16-wf", "Gaming Enthusiast / Audio Bang & Olufsen", 24999000, 36999000, "gaming_pro"),
            ("HP Envy x360 14", "2-in-1 Premium / Gambar & Desain", 16499000, 22999000, "creative")
        ]
    },
    "MSI": {
        "series": [
            ("Modern 14 C12M", "Bodi Aluminium / Ringan / Murah", 5999000, 8999000, "office"),
            ("Prestige 14 AI Evo", "Bisnis / AI Processor / Tipis", 15999000, 21999000, "premium"),
            ("Thin 15 B12U", "Gaming Tipis Paling Terjangkau", 9499000, 12999000, "gaming"),
            ("Cyborg 15 A12V", "Desain Transparan Futuristik", 12499000, 15999000, "gaming"),
            ("Katana 15 B13V", "Performa Murni / Pendingin Kuat", 14999000, 19999000, "gaming"),
            ("Sword 16 HX", "16:10 144Hz / Prosesor HX Kencang", 17999000, 24999000, "gaming_pro"),
            ("Raider GE78 HX", "Monster RGB / Flagship Hardware", 42999000, 68999000, "flagship")
        ]
    },
    "Advan": {
        "series": [
            ("Soulmate 14", "Laptop Termurah Pelajar", 2799000, 3499000, "pelajar"),
            ("Workpro 14", "Layar 16:10 Metal / Best Value 5jt", 4999000, 5999000, "office"),
            ("Workplus 14", "Ryzen Seri H / RAM 16GB / Terlaris", 6999000, 7899000, "coding"),
            ("360 Stylus 14", "2-in-1 Layar Sentuh Murah", 5999000, 6899000, "creative"),
            ("AI Gen 14", "Ryzen 7 8845HS / NPU AI Lokal", 9899000, 10999000, "coding")
        ]
    },
    "Axioo": {
        "series": [
            ("Hype 1 / Hype 3", "Budget Merakyat / Word & Browsing", 2699000, 4299000, "pelajar"),
            ("Hype 5 / Hype 7", "Spek Kencang Harga Mahasiswa", 5499000, 6999000, "coding"),
            ("Pongo 725", "Laptop Gaming RTX 2050 Termurah", 8499000, 9999000, "gaming"),
            ("Pongo 760 V2", "Gaming RTX 4060 Paling Ekonomis", 13999000, 15999000, "gaming")
        ]
    },
    "Apple": {
        "series": [
            ("MacBook Air 13 M1", "Baterai Seharian / Kompak Legendaris", 10999000, 12999000, "premium"),
            ("MacBook Air 13 M2", "Desain Flat Modern / Magsafe", 14999000, 18999000, "premium"),
            ("MacBook Air 15 M2", "Layar Luas Tipis / 18 Jam Baterai", 18999000, 23999000, "premium"),
            ("MacBook Air 13 M3", "Chip M3 Cepat / Support Dual Monitor", 17499000, 22499000, "premium"),
            ("MacBook Pro 14 M3", "Layar Liquid Retina XDR 120Hz", 24999000, 32999000, "creative"),
            ("MacBook Pro 16 M3 Pro/Max", "Standar Industri Studio & Musik", 38999000, 65999000, "flagship")
        ]
    },
    "Dell": {
        "series": [
            ("Inspiron 14 3420", "Durabilitas Harian / Office", 5299000, 7899000, "office"),
            ("Inspiron 15 3520 120Hz", "Layar 120Hz Lancar Buat Kerja", 6899000, 9499000, "office"),
            ("Vostro 3430", "Keamanan Bisnis / Port Komplit", 7999000, 11499000, "bisnis"),
            ("G15 5530 Gaming", "Build Kokoh / Sistem Alienware", 13999000, 18999000, "gaming"),
            ("XPS 13 9340", "Bezel Tertipis / Bodi Machined Aluminium", 25999000, 36999000, "flagship")
        ]
    }
}

CPUS = {
    "budget": ["Intel Celeron N4020", "Intel Processor N100", "AMD Athlon Silver 7120U", "Intel Core i3-1115G4", "Intel Core i3-1215U"],
    "mid": ["AMD Ryzen 5 5500U", "AMD Ryzen 5 7520U", "Intel Core i5-1235U", "AMD Ryzen 5 7530U", "Intel Core i5-1335U", "AMD Ryzen 5 6600H"],
    "upper_mid": ["AMD Ryzen 7 7730U", "Intel Core i7-1355U", "Intel Core i5-13500H", "AMD Ryzen 7 7735HS", "Intel Core Ultra 5 125H"],
    "gaming": ["Intel Core i5-12450H", "Intel Core i5-13450HX", "AMD Ryzen 5 7640HS", "Intel Core i7-13620H", "AMD Ryzen 7 7840HS"],
    "enthusiast": ["Intel Core i7-14700HX", "AMD Ryzen 9 7940HS", "Intel Core i9-13900HX", "Intel Core i9-14900HX", "Apple M3 Pro", "Apple M3 Max"]
}

GPUS = {
    "integrated": ["Intel UHD Graphics", "Intel Iris Xe Graphics", "AMD Radeon 610M", "AMD Radeon Vega 7", "AMD Radeon 660M", "Intel Arc Graphics (8 Xe-cores)"],
    "rtx_budget": ["NVIDIA GeForce RTX 2050 (4GB GDDR6)", "NVIDIA GeForce RTX 3050 (4GB GDDR6, 60W)", "NVIDIA GeForce RTX 3050 (6GB GDDR6)"],
    "rtx_mid": ["NVIDIA GeForce RTX 4050 (6GB GDDR6, 95W)", "NVIDIA GeForce RTX 4050 (6GB GDDR6, 105W)", "NVIDIA GeForce RTX 4060 (8GB GDDR6, 115W)", "NVIDIA GeForce RTX 4060 (8GB GDDR6, 140W)"],
    "rtx_high": ["NVIDIA GeForce RTX 4070 (8GB GDDR6, 140W)", "NVIDIA GeForce RTX 4080 (12GB GDDR6X)", "NVIDIA GeForce RTX 4090 (16GB GDDR6X, 175W)"]
}

SCREENS = [
    "14 inch HD (1366x768) Anti-glare",
    "14 inch FHD (1920x1080) IPS 250 nits",
    "14 inch FHD (1920x1080) IPS 300 nits 100% sRGB",
    "14 inch WUXGA (1920x1200) IPS 16:10",
    "14 inch 2.8K (2880x1800) OLED 90Hz 100% DCI-P3",
    "15.6 inch FHD (1920x1080) IPS 144Hz",
    "15.6 inch FHD (1920x1080) IPS 144Hz 100% sRGB",
    "16 inch WQXGA (2560x1600) IPS 165Hz 100% sRGB 500 nits",
    "16 inch 3.2K (3200x2000) Mini-LED 240Hz HDR1000"
]

def generate_laptops(total=500):
    laptops = []
    id_counter = 1

    # Ambil 5 laptop utama kita dulu agar kompatibilitas tetap 100% terjaga
    first_five = [
        {
            "id": f"LP-{id_counter:03d}",
            "nama": "Advan Workplus 14 R5",
            "brand": "Advan",
            "harga": 6999000,
            "kategori": "Best Value / Mahasiswa / Coding",
            "target_user": ["mahasiswa", "kantoran", "coding", "multitasking"],
            "spesifikasi": {
                "prosesor": "AMD Ryzen 5 6600H (6 Core / 12 Thread)",
                "gpu": "AMD Radeon 660M (Integrated)",
                "ram": "16GB LPDDR5 Dual Channel",
                "storage": "512GB SSD NVMe PCIe 3.0",
                "layar": "14 inch WUXGA (1920x1200) IPS 16:10",
                "baterai": "58Wh",
                "berat": "1.4 kg"
            },
            "kelebihan": ["Prosesor Ryzen Seri H kencang di harga 6 jutaan", "RAM bawaan 16GB lega buat ngoding", "Layar 16:10 luas"],
            "catatan_jujur": ["RAM disolder (onboard)", "Webcam standar"],
            "game_support": "Esports ringan lancar (Valorant, CS2, Dota 2, Genshin low)",
            "stok": 8
        },
        {
            "id": f"LP-{id_counter+1:03d}",
            "nama": "Lenovo IdeaPad Slim 3 14IAU7",
            "brand": "Lenovo",
            "harga": 5899000,
            "kategori": "Entry-Level / Office / Pelajar",
            "target_user": ["pelajar", "mahasiswa", "administrasi", "browsing", "zoom"],
            "spesifikasi": {
                "prosesor": "Intel Core i3-1215U (6 Core, up to 4.4 GHz)",
                "gpu": "Intel UHD Graphics",
                "ram": "8GB DDR4 (Upgradable)",
                "storage": "512GB SSD NVMe PCIe 4.0",
                "layar": "14 inch FHD (1920x1080) IPS 300 nits",
                "baterai": "38Wh",
                "berat": "1.43 kg"
            },
            "kelebihan": ["Keyboard khas Lenovo empuk", "Layar sudah IPS nyaman di mata", "RAM bisa di-upgrade"],
            "catatan_jujur": ["Baterai 38Wh standar", "Bukan untuk gaming berat"],
            "game_support": "Game kasual (Roblox, Minecraft, PB)",
            "stok": 12
        },
        {
            "id": f"LP-{id_counter+2:03d}",
            "nama": "ASUS Vivobook 14X K3405VC RTX 3050",
            "brand": "ASUS",
            "harga": 10499000,
            "kategori": "Creator Pemula / Editing / Desain",
            "target_user": ["desain grafis", "video editing", "arsitektur", "mahasiswa dkv"],
            "spesifikasi": {
                "prosesor": "Intel Core i5-13500H (12 Core / 16 Thread)",
                "gpu": "NVIDIA GeForce RTX 3050 (4GB GDDR6)",
                "ram": "16GB DDR4 Dual Channel",
                "storage": "512GB SSD NVMe PCIe 4.0",
                "layar": "14 inch WUXGA IPS-level 144Hz",
                "baterai": "50Wh",
                "berat": "1.4 kg"
            },
            "kelebihan": ["Punya kartu grafis RTX 3050 tapi tetap tipis ringan 1.4kg", "Prosesor i5 Seri H kencang buat Premiere & Photoshop"],
            "catatan_jujur": ["Fan cukup berisik saat rendering maksimal"],
            "game_support": "Game AAA modern setting medium lancar (GTA V, Cyberpunk low-med)",
            "stok": 5
        },
        {
            "id": f"LP-{id_counter+3:03d}",
            "nama": "Lenovo LOQ 15IRX9 RTX 4050",
            "brand": "Lenovo",
            "harga": 14299000,
            "kategori": "Gaming Murni / 3D Render Berat / Arsitektur",
            "target_user": ["gamer", "3d artist", "blender", "arsitektur", "engineering"],
            "spesifikasi": {
                "prosesor": "Intel Core i5-13450HX (10 Core / 16 Thread)",
                "gpu": "NVIDIA GeForce RTX 4050 (6GB GDDR6, TGP 95W)",
                "ram": "16GB DDR5 4800MHz (Dual slot)",
                "storage": "512GB SSD NVMe PCIe 4.0",
                "layar": "15.6 inch FHD IPS 144Hz 100% sRGB",
                "baterai": "60Wh",
                "berat": "2.38 kg"
            },
            "kelebihan": ["RTX 4050 support DLSS 3 Frame Gen", "Layar sudah 100% sRGB akurat", "Keyboard ada 4-Zone RGB"],
            "catatan_jujur": ["Bobot laptop + charger berat sekitar 3kg", "Baterai boros tanpa colokan listrik"],
            "game_support": "Semua game modern rata kanan (Wukong, Cyberpunk, Valorant 250+ FPS)",
            "stok": 4
        },
        {
            "id": f"LP-{id_counter+4:03d}",
            "nama": "Acer Swift Go 14 OLED SFG14-72",
            "brand": "Acer",
            "harga": 13499000,
            "kategori": "Ultrabook Premium / Profesional / Portabilitas",
            "target_user": ["profesional", "eksekutif", "programmer", "content creator mobile"],
            "spesifikasi": {
                "prosesor": "Intel Core Ultra 5 125H (14 Core with NPU AI)",
                "gpu": "Intel Arc Graphics (8 Xe-cores)",
                "ram": "16GB LPDDR5X onboard",
                "storage": "512GB SSD PCIe Gen4",
                "layar": "14 inch 2.8K (2880x1800) OLED 90Hz 100% DCI-P3",
                "baterai": "65Wh (Tahan 8-10 jam)",
                "berat": "1.32 kg"
            },
            "kelebihan": ["Layar OLED 2.8K luar biasa tajam dan warna akurat", "Ada NPU AI Boost", "Bodi aluminium tipis ringan"],
            "catatan_jujur": ["RAM disolder", "Bukan untuk game berat AAA"],
            "game_support": "Game eSports dan kasual lancar",
            "stok": 6
        }
    ]

    laptops.extend(first_five)
    id_counter += 5

    # Buat sisa hingga genap 500
    all_brands = list(BRANDS_CONFIG.keys())

    while id_counter <= total:
        brand = random.choice(all_brands)
        brand_data = BRANDS_CONFIG[brand]
        series_info = random.choice(brand_data["series"])
        
        series_name, kategori, min_price, max_price, tier = series_info
        
        # Bulatkan harga ke kelipatan 50.000 atau 99.000
        raw_price = random.randint(min_price // 100000, max_price // 100000) * 100000
        harga = raw_price + (99000 if raw_price % 2 == 0 else 0)

        # Tentukan CPU & GPU sesuai tier
        if "Apple" in brand:
            cpu = random.choice(["Apple M1 (8 Core CPU / 7 Core GPU)", "Apple M2 (8 Core CPU / 8 Core GPU)", "Apple M2 (8 Core CPU / 10 Core GPU)", "Apple M3 (8 Core CPU / 10 Core GPU)", "Apple M3 Pro (11 Core CPU / 14 Core GPU)"])
            gpu = "Apple Integrated GPU Metal"
            ram = random.choice(["8GB Unified Memory", "16GB Unified Memory", "24GB Unified Memory", "36GB Unified Memory"])
            storage = random.choice(["256GB SSD", "512GB SSD", "1TB SSD"])
            layar = random.choice(["13.6 inch Liquid Retina IPS 500 nits", "15.3 inch Liquid Retina IPS", "14.2 inch Liquid Retina XDR Mini-LED 120Hz"])
            berat = f"{random.uniform(1.24, 1.6):.2f} kg"
            baterai = "Up to 18 jam"
            game_support = "Game native Mac & Apple Arcade lancar (Resident Evil 4, Baldur's Gate 3 medium)"
            kelebihan = ["Efisiensi baterai terbaik di industri (bisa 15-18 jam kerja)", "Trackpad dan bodi aluminium terhalus", "Layar Liquid Retina sangat jernih"]
            catatan_jujur = ["Tidak support banyak game Windows lawas", "Storage & RAM tidak bisa di-upgrade sama sekali"]
            target_user = ["desain grafis", "video editing", "musik", "eksekutif", "programmer"]
        else:
            if tier in ["pelajar", "office"]:
                cpu = random.choice(CPUS["budget"] + CPUS["mid"][:2])
                gpu = random.choice(GPUS["integrated"][:4])
                ram = random.choice(["8GB DDR4 (Upgradable)", "8GB LPDDR4x", "16GB DDR4"])
                storage = random.choice(["256GB SSD NVMe", "512GB SSD NVMe PCIe 3.0", "512GB SSD NVMe PCIe 4.0"])
                layar = random.choice(SCREENS[:3])
                berat = f"{random.uniform(1.38, 1.55):.2f} kg"
                baterai = random.choice(["38Wh (4-5 jam)", "42Wh (5-6 jam)", "47Wh (6 jam)"])
                game_support = "Game kasual (Roblox, Minecraft, Point Blank, Zuma)"
                kelebihan = ["Harga sangat terjangkau di kantong", "Hemat daya dan adem untuk ketik dokumen harian", "Desain simpel dan mudah dibawa"]
                catatan_jujur = ["Layar akurasi warna standar 45% NTSC", "Bukan untuk rendering 3D atau game berat"]
                target_user = ["pelajar", "mahasiswa", "kantoran", "administrasi", "zoom"]
            elif tier in ["coding", "creative"]:
                cpu = random.choice(CPUS["mid"] + CPUS["upper_mid"])
                gpu = random.choice(GPUS["integrated"])
                ram = random.choice(["16GB DDR4 Dual Channel", "16GB LPDDR5", "16GB DDR5 4800MHz"])
                storage = random.choice(["512GB SSD NVMe PCIe 4.0", "1TB SSD NVMe PCIe 4.0"])
                layar = random.choice(SCREENS[1:5])
                berat = f"{random.uniform(1.35, 1.50):.2f} kg"
                baterai = random.choice(["50Wh (6-8 jam)", "56Wh (7-9 jam)", "60Wh (8 jam)"])
                game_support = "eSports ringan lancar (Valorant, CS2, Dota 2, Genshin low)"
                kelebihan = ["RAM bawaan 16GB sangat lega buat multitasking banyak tab", "Prosesor responsif buat kompilasi coding & Photoshop", "Bodi cukup tipis dan baterai awet"]
                catatan_jujur = ["GPU bawaan belum ada RTX untuk game berat", "Sebagian model RAM disolder"]
                target_user = ["coding", "programmer", "mahasiswa it", "desain grafis", "multitasking"]
            elif tier in ["desain", "premium"]:
                cpu = random.choice(CPUS["upper_mid"] + CPUS["gaming"][:2])
                gpu = random.choice(GPUS["integrated"][-2:] + GPUS["rtx_budget"][:1])
                ram = random.choice(["16GB LPDDR5X", "16GB DDR5", "32GB LPDDR5X"])
                storage = random.choice(["512GB SSD PCIe 4.0", "1TB SSD PCIe 4.0"])
                layar = random.choice(SCREENS[3:6])
                berat = f"{random.uniform(1.20, 1.45):.2f} kg"
                baterai = random.choice(["65Wh (8-10 jam)", "70Wh (9-11 jam)", "75Wh (10 jam)"])
                game_support = "Game eSports lancar dan game AAA setting low"
                kelebihan = ["Layar luar biasa tajam dengan akurasi warna 100% sRGB / DCI-P3", "Bodi premium tipis enteng di bawah 1.4 kg", "Kapasitas baterai besar seharian"]
                catatan_jujur = ["Harga lumayan premium", "RAM tidak bisa ditambah lagi"]
                target_user = ["desain grafis", "content creator", "eksekutif", "programmer", "video editing"]
            elif tier in ["gaming", "gaming_pro"]:
                cpu = random.choice(CPUS["gaming"] + CPUS["enthusiast"][:2])
                gpu = random.choice(GPUS["rtx_budget"][1:] + GPUS["rtx_mid"])
                ram = random.choice(["16GB DDR5 Dual Channel", "16GB DDR5 5600MHz", "32GB DDR5 Dual Slot"])
                storage = random.choice(["512GB SSD NVMe Gen4", "1TB SSD NVMe Gen4 (Dual M.2 Slot)"])
                layar = random.choice(SCREENS[5:8])
                berat = f"{random.uniform(2.1, 2.45):.2f} kg"
                baterai = random.choice(["54Wh (2-3 jam)", "60Wh (2.5 jam)", "80Wh (3.5 jam)"])
                game_support = "Semua game modern AAA lancar high-ultra (Cyberpunk, Black Myth Wukong, Forza)"
                kelebihan = ["Dilengkapi kartu grafis NVIDIA RTX kencang support Ray Tracing & DLSS 3", "Sistem pendingin dual-fan dengan heatpipe tebal", "Keyboard empuk dengan backlight RGB"]
                catatan_jujur = ["Bobot berat di tas sekitar 2.3 - 2.5 kg", "Adaptor charger besar dan baterai cepat habis tanpa colokan"]
                target_user = ["gamer", "3d artist", "blender", "arsitektur", "engineering", "video editing"]
            else: # flagship
                cpu = random.choice(CPUS["enthusiast"])
                gpu = random.choice(GPUS["rtx_high"])
                ram = random.choice(["32GB DDR5 5600MHz", "64GB DDR5"])
                storage = random.choice(["1TB SSD NVMe Gen4", "2TB SSD NVMe Gen4 RAID"])
                layar = random.choice(SCREENS[7:])
                berat = f"{random.uniform(2.5, 3.1):.2f} kg"
                baterai = "99.9Wh (Maksimal legal penerbangan pesawat)"
                game_support = "Rata kanan semua game 4K / QHD 165Hz+ tanpa kompromi"
                kelebihan = ["Performa tertinggi setara PC Desktop", "Layar 240Hz Mini-LED / QHD sangat responsif", "Komponen terbaik tanpa bottleneck"]
                catatan_jujur = ["Harga sangat mahal", "Sangat berat dan tebal"]
                target_user = ["pro gamer", "studio animasi", "ai researcher", "hardcore enthusiast"]

        variant_code = f"{random.choice(['A', 'B', 'X', 'Pro', 'Plus', 'Ultra', 'G', 'Max'])}-{random.randint(10, 99)}"
        nama_lengkap = f"{brand} {series_name} ({variant_code})"

        item = {
            "id": f"LP-{id_counter:03d}",
            "nama": nama_lengkap,
            "brand": brand,
            "harga": harga,
            "kategori": kategori,
            "target_user": target_user,
            "spesifikasi": {
                "prosesor": cpu,
                "gpu": gpu,
                "ram": ram,
                "storage": storage,
                "layar": layar,
                "baterai": baterai,
                "berat": berat
            },
            "kelebihan": kelebihan,
            "catatan_jujur": catatan_jujur,
            "game_support": game_support,
            "stok": random.randint(2, 20)
        }
        laptops.append(item)
        id_counter += 1

    return laptops

if __name__ == "__main__":
    data = generate_laptops(500)
    with open("katalog_laptop.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Berhasil membuat katalog dengan {len(data)} laptop!")
