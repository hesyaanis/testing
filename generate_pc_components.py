import json
import random
import sys

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def generate_full_pc_catalog():
    components = []
    current_id = 1

    # 1. PROCESSORS (CPU) - 45 Items
    cpu_templates = [
        # AMD AM4
        ("AMD Athlon 3000G with Radeon Vega 3", "AMD", 650000, "Socket AM4", "2 Core / 4 Thread, 3.5 GHz, Vega 3 iGPU, 35W", ["Hemat daya ekstrem 35W", "Sudah ada display tanpa VGA"], ["Kasir / POS", "PC Ketik Sederhana"]),
        ("AMD Ryzen 3 3200G with Radeon Vega 8", "AMD", 1050000, "Socket AM4", "4 Core / 4 Thread, 4.0 GHz, Vega 8 iGPU, 65W", ["iGPU Vega 8 handal", "Bisa main game kasual tanpa VGA"], ["Office", "Pelajar"]),
        ("AMD Ryzen 3 4100", "AMD", 890000, "Socket AM4", "4 Core / 8 Thread, 4.0 GHz, 65W (Wajib VGA)", ["4 Core 8 Thread termurah", "Suhu dingin"], ["Budget Esports"]),
        ("AMD Ryzen 5 3600", "AMD", 1150000, "Socket AM4", "6 Core / 12 Thread, 4.2 GHz, 35MB Cache, PCIe 4.0", ["Legenda 6 core sejuta umat", "Mendukung PCIe 4.0"], ["Budget Gaming"]),
        ("AMD Ryzen 5 4500", "AMD", 1120000, "Socket AM4", "6 Core / 12 Thread, 4.1 GHz, 65W", ["6 Core harga sejutaan", "Multitasking lancar"], ["All-Rounder Hemat"]),
        ("AMD Ryzen 5 5500", "AMD", 1380000, "Socket AM4", "6 Core / 12 Thread, 4.2 GHz, 19MB Cache, 65W", ["Arsitektur Zen 3 kencang", "Suhu sangat dingin"], ["Gaming 1080p Value"]),
        ("AMD Ryzen 5 5600G with Radeon Graphics", "AMD", 1950000, "Socket AM4", "6 Core / 12 Thread, 4.4 GHz, Vega 7 iGPU 1.9GHz", ["Bisa rakit tanpa beli VGA terpisah", "Kuat GTA V & Valorant 60+ FPS"], ["Rakit Tanpa VGA", "Desain Grafis"]),
        ("AMD Ryzen 5 5600GT with Radeon Graphics", "AMD", 2150000, "Socket AM4", "6 Core / 12 Thread, 4.6 GHz, Vega 7 iGPU Boost", ["Versi refresh 5600G clock lebih tinggi", "Gaming esport mulus"], ["Esports Tanpa VGA"]),
        ("AMD Ryzen 5 5600", "AMD", 1750000, "Socket AM4", "6 Core / 12 Thread, 4.4 GHz, 35MB Cache, PCIe 4.0", ["Sweet spot gaming 1080p", "Tidak bottleneck dipadu RTX 4060"], ["Sweet Spot Gaming", "Editing Video"]),
        ("AMD Ryzen 5 5600X", "AMD", 2150000, "Socket AM4", "6 Core / 12 Thread, 4.6 GHz, 35MB Cache", ["Clock speed tinggi", "Single-core kencang untuk game kompetitif"], ["Gaming Kompetitif"]),
        ("AMD Ryzen 7 5700", "AMD", 2250000, "Socket AM4", "8 Core / 16 Thread, 4.6 GHz, 20MB Cache, 65W", ["8 Core terjangkau", "Multithread kuat"], ["Workstation Budget"]),
        ("AMD Ryzen 7 5700G with Radeon Graphics", "AMD", 2650000, "Socket AM4", "8 Core / 16 Thread, 4.6 GHz, Vega 8 iGPU 2.0GHz", ["8 Core lengkap dengan iGPU", "Kuat rendering & komputasi"], ["Workstation Tanpa VGA"]),
        ("AMD Ryzen 7 5700X", "AMD", 2550000, "Socket AM4", "8 Core / 16 Thread, 4.6 GHz, 36MB Cache, TDP 65W", ["8 Core sangat dingin", "Pilihan terbaik upgrade soket AM4"], ["Workstation 3D", "Video Rendering"]),
        ("AMD Ryzen 7 5700X3D", "AMD", 3350000, "Socket AM4", "8 Core / 16 Thread, 3D V-Cache 100MB, 4.1 GHz", ["Monster gaming soket AM4", "3D V-Cache mendongkrak 1% low FPS"], ["Hardcore Gaming AM4"]),
        ("AMD Ryzen 7 5800X3D", "AMD", 4450000, "Socket AM4", "8 Core / 16 Thread, 3D V-Cache 100MB, 4.5 GHz", ["Raja legendaris AM4", "FPS stabil di game simulasi"], ["Enthusiast Gaming AM4"]),
        ("AMD Ryzen 9 5900X", "AMD", 4650000, "Socket AM4", "12 Core / 24 Thread, 4.8 GHz, 70MB Cache", ["12 Core raksasa untuk rendering studio", "Performa multithread masif"], ["Studio Produksi Video"]),
        ("AMD Ryzen 9 5950X", "AMD", 5950000, "Socket AM4", "16 Core / 32 Thread, 4.9 GHz, 72MB Cache", ["Puncak AM4 16 Core", "Workstation kompilasi software besar"], ["Heavy Workstation"]),

        # AMD AM5 & 8000/9000
        ("AMD Ryzen 5 8500G with Radeon 740M", "AMD", 2450000, "Socket AM5", "6 Core / 12 Thread, 5.0 GHz, RDNA 3 iGPU, Zen 4/4c", ["Arsitektur baru dengan iGPU RDNA 3", "DDR5 support"], ["Modern Entry AM5"]),
        ("AMD Ryzen 5 8600G with Radeon 760M & NPU", "AMD", 3350000, "Socket AM5", "6 Core / 12 Thread, 5.0 GHz, Radeon 760M, Ryzen AI NPU", ["iGPU terkuat setara GTX 1650", "Punya AI NPU terdedikasi"], ["Gaming Tanpa VGA AM5"]),
        ("AMD Ryzen 7 8700G with Radeon 780M & NPU", "AMD", 4850000, "Socket AM5", "8 Core / 16 Thread, 5.1 GHz, Radeon 780M RDNA 3, Ryzen AI", ["8 Core dengan iGPU paling kencang di dunia", "Ryzen AI"], ["Compact SFF Workstation"]),
        ("AMD Ryzen 5 7500F", "AMD", 2450000, "Socket AM5", "6 Core / 12 Thread, up to 5.0 GHz, Zen 4 5nm (Wajib VGA)", ["Best value AM5 saat ini", "Performa gaming setara i5-13400F"], ["Modern Gaming DDR5"]),
        ("AMD Ryzen 5 7600", "AMD", 3100000, "Socket AM5", "6 Core / 12 Thread, 5.1 GHz, Radeon iGPU, 65W", ["Ada iGPU bawaan", "Efisiensi daya luar biasa 65W", "Include cooler"], ["Sweet Spot AM5"]),
        ("AMD Ryzen 5 7600X", "AMD", 3450000, "Socket AM5", "6 Core / 12 Thread, 5.3 GHz, 38MB Cache, TDP 105W", ["Clock speed 5.3 GHz kencang", "Unlocked multiplier"], ["Competitive Gaming AM5"]),
        ("AMD Ryzen 7 7700", "AMD", 4650000, "Socket AM5", "8 Core / 16 Thread, 5.3 GHz, 40MB Cache, TDP 65W", ["8 Core hemat daya", "Suhu dingin dengan performa tinggi"], ["Creator & Gaming"]),
        ("AMD Ryzen 7 7700X", "AMD", 5150000, "Socket AM5", "8 Core / 16 Thread, 5.4 GHz, 40MB Cache, TDP 105W", ["Performa komputasi tinggi", "Sangat kencang untuk render berat"], ["Heavy Workstation"]),
        ("AMD Ryzen 7 7800X3D", "AMD", 6950000, "Socket AM5", "8 Core / 16 Thread, 3D V-Cache 104MB, 5.0 GHz", ["Prosesor gaming nomor 1 di dunia", "FPS tertinggi di game esport & simulasi"], ["Ultra High-End Gaming"]),
        ("AMD Ryzen 9 7900X", "AMD", 6850000, "Socket AM5", "12 Core / 24 Thread, 5.6 GHz, 76MB Cache", ["12 Core monster multitasking", "Ideal untuk 3D Blender & VFX"], ["Studio Workstation"]),
        ("AMD Ryzen 9 7950X", "AMD", 8650000, "Socket AM5", "16 Core / 32 Thread, 5.7 GHz, 80MB Cache", ["16 Core 32 Thread kelas atas", "Daya komputasi tak tertandingi"], ["Enterprise Creator"]),
        ("AMD Ryzen 9 7950X3D", "AMD", 9850000, "Socket AM5", "16 Core / 32 Thread, 144MB V-Cache, 5.7 GHz", ["Kombinasi 16 Core dan 3D V-Cache", "Terbaik untuk gaming dan render sekaligus"], ["Ultimate Flagship"]),
        ("AMD Ryzen 7 9700X", "AMD", 5850000, "Socket AM5", "8 Core / 16 Thread, Zen 5 4nm, 5.5 GHz, 65W", ["Arsitektur terbaru Zen 5", "IPC naik signifikan", "Suhu sangat dingin"], ["Next-Gen Workstation"]),

        # Intel LGA1700
        ("Intel Core i3-12100F", "Intel", 1250000, "Socket LGA1700", "4 Core / 8 Thread, 4.3 GHz, 12MB Cache (Wajib VGA)", ["Single-core kencang di harga 1 jutaan", "Suhu adem"], ["Entry Gaming 1080p"]),
        ("Intel Core i3-12100 with UHD 730", "Intel", 1650000, "Socket LGA1700", "4 Core / 8 Thread, 4.3 GHz, Intel UHD Graphics 730", ["Ada display tanpa VGA", "QuickSync video"], ["Office Cepat"]),
        ("Intel Core i3-14100F", "Intel", 1550000, "Socket LGA1700", "4 Core / 8 Thread, 4.7 GHz, Gen 14 Raptor Lake", ["Generasi 14 terbaru", "Clock speed 4.7 GHz kencang"], ["Budget Esports 1080p"]),
        ("Intel Core i5-12400F", "Intel", 1750000, "Socket LGA1700", "6 Core / 12 Thread, 4.4 GHz, 18MB Cache (Wajib VGA)", ["Prosesor sejuta umat terpopuler", "Tidak bottleneck dipadu RTX 4060"], ["Sweet Spot Gaming 1080p"]),
        ("Intel Core i5-12400 with UHD 730", "Intel", 2150000, "Socket LGA1700", "6 Core / 12 Thread, 4.4 GHz, Intel UHD 730", ["Lengkap dengan iGPU", "Stabilitas tinggi"], ["Office Bisnis", "Editing Ringan"]),
        ("Intel Core i5-12600KF", "Intel", 2650000, "Socket LGA1700", "10 Core (6P + 4E) / 16 Thread, 4.9 GHz, Unlocked", ["10 Core murah", "Bisa overclock", "Kencang untuk gaming & rendering"], ["Performance Gaming"]),
        ("Intel Core i5-13400F", "Intel", 2950000, "Socket LGA1700", "10 Core (6P + 4E) / 16 Thread, 4.6 GHz", ["Arsitektur Hybrid 10 Core", "Multitasking berat lancar"], ["Mid-Range Creator"]),
        ("Intel Core i5-13500", "Intel", 3650000, "Socket LGA1700", "14 Core (6P + 8E) / 20 Thread, 4.8 GHz, Intel UHD 770", ["14 Core harga bersahabat", "iGPU UHD 770 QuickSync"], ["Editing Video Studio"]),
        ("Intel Core i5-14400F", "Intel", 3250000, "Socket LGA1700", "10 Core (6P + 4E) / 16 Thread, 4.7 GHz, Gen 14", ["Clock speed lebih tinggi", "Dukungan memori DDR4 & DDR5"], ["Modern Gaming Gen 14"]),
        ("Intel Core i5-13600KF", "Intel", 4250000, "Socket LGA1700", "14 Core (6P + 8E) / 20 Thread, 5.1 GHz, Unlocked", ["Monster 14 Core", "Mampu melibas editing 4K dan game berat"], ["High-End Gaming Intel"]),
        ("Intel Core i5-14600KF", "Intel", 4550000, "Socket LGA1700", "14 Core (6P + 8E) / 20 Thread, 5.3 GHz, Gen 14", ["Clock speed 5.3 GHz", "Performa tinggi di game kompetitif"], ["Enthusiast Gaming"]),
        ("Intel Core i7-13700F", "Intel", 5450000, "Socket LGA1700", "16 Core (8P + 8E) / 24 Thread, 5.2 GHz", ["16 Core bertenaga dahsyat", "Stabil untuk pekerjaan nonstop"], ["Workstation 3D"]),
        ("Intel Core i7-14700KF", "Intel", 6350000, "Socket LGA1700", "20 Core (12E + 8P) / 28 Thread, 5.6 GHz", ["20 Core monster terbaru", "Lompatan performa dari gen 13"], ["Heavy Render Studio"]),
        ("Intel Core i9-13900KF", "Intel", 7850000, "Socket LGA1700", "24 Core (8P + 16E) / 32 Thread, 5.8 GHz", ["24 Core monster", "Daya komputasi studio render animasi"], ["Studio Workstation"]),
        ("Intel Core i9-14900KF", "Intel", 8950000, "Socket LGA1700", "24 Core (8P + 16E) / 32 Thread, 6.0 GHz", ["Tembus 6.0 GHz out of the box", "Puncak komputasi Intel"], ["Flagship Extreme PC"])
    ]

    for name, brand, price, socket, spec, pros, target in cpu_templates:
        components.append({
            "id": f"CPU-{current_id:03d}",
            "kategori": "Processor (CPU)",
            "nama": name,
            "brand": brand,
            "harga": price,
            "stok": random.randint(4, 18),
            "socket": socket,
            "spesifikasi_ringkas": spec,
            "kelebihan": pros,
            "target_build": target,
            "garansi": "3 Tahun Resmi Distributor"
        })
        current_id += 1

    # 2. MOTHERBOARDS - 50 Items
    mobo_brands = ["ASUS", "MSI", "Gigabyte", "ASRock", "Colorful"]
    mobo_templates = [
        # AM4
        ("A520M-HDV", "ASRock", 820000, "AM4", "Micro-ATX, 2x DDR4, 1x M.2 NVMe, DVI/HDMI", ["Ekonomis AM4", "PCIe NVMe support"]),
        ("A520M-A PRO", "MSI", 860000, "AM4", "Micro-ATX, 2x DDR4, Audio Boost, Core Boost", ["Komponen militer tahan lama", "BIOS user-friendly"]),
        ("Prime A520M-K", "ASUS", 910000, "AM4", "Micro-ATX, 2x DDR4, 1x M.2 NVMe, 5X Protection III", ["Proteksi kelistrikan ASUS", "Stabil"]),
        ("B450M-HDV R4.0", "ASRock", 840000, "AM4", "Micro-ATX, 2x DDR4, 1x Ultra M.2, AMD B450", ["B450 harga murah", "Bisa tuning CPU"]),
        ("B450M PRO-VDH MAX", "MSI", 1050000, "AM4", "Micro-ATX, 4x DDR4, Turbo M.2, Heatsink VRM", ["4 Slot RAM", "VRM ada heatsink"]),
        ("B550M-HDV", "ASRock", 950000, "AM4", "Micro-ATX, PCIe 4.0 Support, 1x Hyper M.2", ["B550 termurah", "PCIe 4.0 kencang"]),
        ("B550M PRO-VDH WiFi", "MSI", 1450000, "AM4", "Micro-ATX, 4x DDR4, 2x M.2, WiFi & Bluetooth", ["WiFi bawaan", "VRM heatsink tebal"]),
        ("B550M Pro4", "ASRock", 1420000, "AM4", "Micro-ATX, 4x DDR4, Dual M.2, Desain Putih Silver", ["VRM 8 phase Dr.MOS", "Desain silver estetik"]),
        ("B550M DS3H AC", "Gigabyte", 1380000, "AM4", "Micro-ATX, 4x DDR4, Built-in AC WiFi, Dual M.2", ["WiFi AC bawaan", "Q-Flash Plus"]),
        ("TUF GAMING B550M-PLUS WiFi II", "ASUS", 2150000, "AM4", "Micro-ATX, 4x DDR4, WiFi 6, 2.5Gb LAN, Aura Sync", ["Komponen militer TUF", "Audio Realtek premium"]),
        ("ROG STRIX B550-F GAMING WiFi II", "ASUS", 3150000, "AM4", "ATX, 14 Power Stages, WiFi 6E, SupremeFX Audio", ["Papan ATX gagah", "Audio kelas audiophile"]),

        # AM5
        ("A620M-HDV/M.2+", "ASRock", 1320000, "AM5", "Micro-ATX, 2x DDR5 Slot, Hyper M.2 PCIe 4.0", ["Ekonomis AM5 DDR5", "Kuat Ryzen 5 7500F"]),
        ("Prime A620M-K", "ASUS", 1420000, "AM5", "Micro-ATX, 2x DDR5, 1x M.2 PCIe 4.0, 5X Protection", ["Kualitas ASUS", "DDR5 support"]),
        ("B650M-HDV/M.2", "ASRock", 1850000, "AM5", "Micro-ATX, VRM 8+2+1 Dr.MOS, 1x Blazing M.2 Gen5", ["Best value B650", "Support M.2 PCIe Gen 5"]),
        ("B650M GAMING PLUS WIFI", "Gigabyte", 2350000, "AM5", "Micro-ATX, 4x DDR5, WiFi 6, 2.5Gb LAN, PCIe 4.0", ["WiFi 6", "VRM dingin", "4 Slot RAM"]),
        ("PRO B650M-A WiFi", "MSI", 2450000, "AM5", "Micro-ATX, 4x DDR5 Slot, WiFi 6E, 2x M.2", ["Fitur lengkap", "WiFi 6E kencang"]),
        ("B650M Pro RS WiFi White", "ASRock", 2490000, "AM5", "Micro-ATX, 4x DDR5, Desain Putih Silver, WiFi 6E", ["Tema putih salju estetik", "VRM Dr.MOS"]),
        ("TUF GAMING B650M-PLUS WiFi", "ASUS", 3250000, "AM5", "Micro-ATX, 12+2 Power Stages, PCIe 5.0, WiFi 6", ["VRM kuat untuk Ryzen 7 & 9", "Desain TUF"]),
        ("B650 AORUS ELITE AX", "Gigabyte", 3850000, "AM5", "ATX, 14+2+1 Phase, WiFi 6E, PCIe 5.0 M.2", ["Ukuran ATX gagah", "Thermal armor luas"]),
        ("MAG B650 TOMAHAWK WIFI", "MSI", 3950000, "AM5", "ATX, 14+2+1 Duet Rail, WiFi 6E, Audio ALC4080", ["Papan hitam legendaris", "Audio premium"]),
        ("ROG STRIX B650-A GAMING WIFI", "ASUS", 4750000, "AM5", "ATX, Desain Putih Silver Mewah, WiFi 6E, USB 3.2 Gen 2x2", ["Estetika putih flagship", "SupremeFX"]),
        ("X670E GAMING PLUS WIFI", "MSI", 4650000, "AM5", "ATX, Chipset X670E, PCIe 5.0 x16, 4x M.2", ["Chipset X670E jalur PCIe melimpah", "Overclocking"]),
        ("ROG CROSSHAIR X670E HERO", "ASUS", 9850000, "AM5", "ATX Flagship, 18+2 Power Stages, USB4, Polymo Lighting", ["Puncak motherboard AM5", "Fitur ekstrim"]),

        # LGA1700
        ("PRO H610M-E DDR4", "MSI", 950000, "LGA1700", "Micro-ATX, 2x DDR4 Slot, 1x M.2 NVMe, Core Boost", ["Paling ekonomis untuk i3 & i5", "BIOS stabil"]),
        ("Prime H610M-K D4", "ASUS", 1020000, "LGA1700", "Micro-ATX, 2x DDR4, 1x M.2 NVMe, Fan Xpert", ["Kualitas komponen ASUS", "Proteksi 5X III"]),
        ("H610M H V2 DDR4", "Gigabyte", 980000, "LGA1700", "Micro-ATX, 2x DDR4, NVMe PCIe 3.0, Smart Fan 6", ["Suhu stabil", "Harga bersahabat"]),
        ("B760M-HDV/M.2 D4", "ASRock", 1350000, "LGA1700", "Micro-ATX, 2x DDR4, 2x Hyper M.2, Gen 14 Ready", ["B760 termurah", "2 Slot NVMe"]),
        ("B760M DS3H AX DDR4", "Gigabyte", 1850000, "LGA1700", "Micro-ATX, 4x DDR4, WiFi 6E, 2.5G LAN, 2x M.2", ["WiFi 6E terintegrasi", "4 Slot RAM"]),
        ("B760M Pro RS/D4 White", "ASRock", 1750000, "LGA1700", "Micro-ATX, 4x DDR4, Dual M.2 Heatsink, Putih", ["Estetika putih bersih", "VRM 7+1+1 Dr.MOS"]),
        ("B760M GAMING PLUS WIFI DDR4", "MSI", 2150000, "LGA1700", "Micro-ATX, 4x DDR4, WiFi 6E, Heatsink VRM", ["Konektivitas WiFi 6E", "VRM adem"]),
        ("TUF GAMING B760M-PLUS WIFI D4", "ASUS", 2650000, "LGA1700", "Micro-ATX, 4x DDR4, 12+1 Dr.MOS, WiFi 6", ["Kelas militer", "Audio DTS"]),
        ("B760 GAMING PLUS WIFI DDR5", "MSI", 2650000, "LGA1700", "ATX, 4x DDR5 Slot (Up to 6800MHz), WiFi 6E", ["DDR5 & ATX besar", "Ideal untuk i5/i7"]),
        ("TUF GAMING B760M-PLUS WIFI DDR5", "ASUS", 3150000, "LGA1700", "Micro-ATX, 12+1 Dr.MOS, DDR5, PCIe 5.0", ["Siap angkat Core i7", "DDR5 kencang"]),
        ("B760 AORUS ELITE AX DDR5", "Gigabyte", 3450000, "LGA1700", "ATX, 12+1+1 Twin Hybrid, WiFi 6E, 3x M.2", ["Ukuran ATX gagah", "3 Slot M.2 heatsink"]),
        ("ROG STRIX B760-A GAMING WIFI D4 White", "ASUS", 3750000, "LGA1700", "ATX, Desain Putih Perak Mewah, WiFi 6E", ["Desain putih ikonik ROG", "SupremeFX"]),
        ("PRO Z790-P WIFI DDR5", "MSI", 3650000, "LGA1700", "ATX, Chipset Z790, 4x DDR5, WiFi 6E, PCIe 5.0", ["Z790 entry level", "Bisa overclock CPU K-series"]),
        ("Prime Z790-A WiFi DDR5", "ASUS", 4650000, "LGA1700", "ATX, 16+1 Dr.MOS, 4x M.2, WiFi 6E, Putih Perak", ["Estetika silver elegan", "Fitur AI Overclocking"]),
        ("MAG Z790 TOMAHAWK WIFI", "MSI", 4450000, "LGA1700", "ATX, 16+1+1 Mirrored Power, DDR5, 4x M.2", ["Papan hitam legendaris", "VRM tebal siap i9"]),
        ("ROG MAXIMUS Z790 DARK HERO", "ASUS", 10850000, "LGA1700", "ATX Flagship, 20+1+2 Stages, PCIe 5.0, WiFi 7", ["Puncak overclocking Intel", "Fitur sultan"])
    ]

    for name, brand, price, socket, spec, pros in mobo_templates:
        components.append({
            "id": f"MB-{current_id:03d}",
            "kategori": "Motherboard",
            "nama": f"{brand} {name}",
            "brand": brand,
            "harga": price,
            "stok": random.randint(3, 14),
            "socket": socket,
            "spesifikasi_ringkas": spec,
            "kelebihan": pros,
            "target_build": ["PC Rakitan", f"Soket {socket}"],
            "garansi": "3 Tahun Resmi Distributor"
        })
        current_id += 1

    # 3. RAM (MEMORY) - 45 Items
    ram_templates = [
        # DDR4
        ("Team Elite Plus 8GB DDR4 3200MHz", "TeamGroup", 265000, "DDR4", "Single Channel 8GB 3200MHz CL22 Black"),
        ("Kingston FURY Beast 8GB DDR4 3200MHz", "Kingston", 310000, "DDR4", "Single Channel 8GB 3200MHz CL16 Black"),
        ("Corsair Vengeance LPX 8GB DDR4 3200MHz", "Corsair", 335000, "DDR4", "Single Channel 8GB 3200MHz CL16 Black"),
        ("Team Elite Plus 16GB (2x8GB) DDR4 3200MHz", "TeamGroup", 520000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz CL22"),
        ("Kingston FURY Beast 16GB (2x8GB) DDR4 3200MHz", "Kingston", 585000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz CL16"),
        ("Kingston FURY Beast RGB 16GB (2x8GB) DDR4 3200MHz", "Kingston", 685000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz CL16 RGB"),
        ("Corsair Vengeance LPX 16GB (2x8GB) DDR4 3200MHz", "Corsair", 625000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz CL16"),
        ("Corsair Vengeance RGB PRO 16GB (2x8GB) DDR4 3200MHz Black", "Corsair", 785000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz RGB"),
        ("Corsair Vengeance RGB PRO 16GB (2x8GB) DDR4 3200MHz White", "Corsair", 815000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz RGB White"),
        ("Team T-Force Delta RGB 16GB (2x8GB) DDR4 3200MHz Black", "TeamGroup", 695000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz RGB"),
        ("Team T-Force Delta RGB 16GB (2x8GB) DDR4 3200MHz White", "TeamGroup", 715000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz RGB White"),
        ("Team T-Force Delta RGB 16GB (2x8GB) DDR4 3600MHz White", "TeamGroup", 765000, "DDR4", "Dual Channel 16GB (2x8GB) 3600MHz CL18 RGB"),
        ("G.Skill Ripjaws V 16GB (2x8GB) DDR4 3600MHz", "G.Skill", 695000, "DDR4", "Dual Channel 16GB (2x8GB) 3600MHz CL18 Classic"),
        ("G.Skill Trident Z RGB 16GB (2x8GB) DDR4 3600MHz", "G.Skill", 925000, "DDR4", "Dual Channel 16GB (2x8GB) 3600MHz CL18 RGB Mewah"),
        ("ADATA XPG SPECTRIX D50 16GB (2x8GB) DDR4 3200MHz Tungsten Grey", "ADATA", 665000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz RGB"),
        ("Kingston FURY Beast 32GB (2x16GB) DDR4 3200MHz", "Kingston", 1120000, "DDR4", "Dual Channel 32GB (2x16GB) 3200MHz CL16"),
        ("Corsair Vengeance LPX 32GB (2x16GB) DDR4 3200MHz", "Corsair", 1180000, "DDR4", "Dual Channel 32GB (2x16GB) 3200MHz CL16"),
        ("Corsair Vengeance LPX 32GB (2x16GB) DDR4 3600MHz", "Corsair", 1260000, "DDR4", "Dual Channel 32GB (2x16GB) 3600MHz CL18"),
        ("Team T-Force Delta RGB 32GB (2x16GB) DDR4 3600MHz White", "TeamGroup", 1380000, "DDR4", "Dual Channel 32GB (2x16GB) 3600MHz RGB White"),
        ("Kingston FURY Beast 64GB (2x32GB) DDR4 3200MHz", "Kingston", 2150000, "DDR4", "Dual Channel 64GB (2x32GB) 3200MHz CL16"),

        # DDR5
        ("Crucial 16GB (2x8GB) DDR5 4800MHz", "Crucial", 780000, "DDR5", "Dual Channel 16GB (2x8GB) 4800MHz JEDEC Standard"),
        ("Kingston FURY Beast 16GB (2x8GB) DDR5 5200MHz", "Kingston", 950000, "DDR5", "Dual Channel 16GB (2x8GB) 5200MHz CL40 XMP/EXPO"),
        ("Team T-Force Vulcan 16GB (2x8GB) DDR5 5600MHz Black", "TeamGroup", 920000, "DDR5", "Dual Channel 16GB (2x8GB) 5600MHz CL36"),
        ("Kingston FURY Beast 32GB (2x16GB) DDR5 5600MHz", "Kingston", 1580000, "DDR5", "Dual Channel 32GB (2x16GB) 5600MHz CL40"),
        ("Corsair Vengeance 32GB (2x16GB) DDR5 6000MHz Black", "Corsair", 1750000, "DDR5", "Dual Channel 32GB (2x16GB) 6000MHz CL36 AMD EXPO"),
        ("Corsair Vengeance RGB 32GB (2x16GB) DDR5 6000MHz White", "Corsair", 1950000, "DDR5", "Dual Channel 32GB (2x16GB) 6000MHz CL36 RGB White"),
        ("Team T-Force Delta RGB 32GB (2x16GB) DDR5 6000MHz White", "TeamGroup", 1850000, "DDR5", "Dual Channel 32GB (2x16GB) 6000MHz CL38 RGB White"),
        ("Team T-Force Delta RGB 32GB (2x16GB) DDR5 6000MHz Black", "TeamGroup", 1820000, "DDR5", "Dual Channel 32GB (2x16GB) 6000MHz CL38 RGB Black"),
        ("G.Skill Ripjaws S5 32GB (2x16GB) DDR5 6000MHz CL32", "G.Skill", 1880000, "DDR5", "Dual Channel 32GB (2x16GB) 6000MHz CL32 Low Profile"),
        ("G.Skill Trident Z5 Neo RGB 32GB (2x16GB) DDR5 6000MHz CL30", "G.Skill", 2150000, "DDR5", "Dual Channel 32GB (2x16GB) 6000MHz CL30 AMD EXPO"),
        ("ADATA XPG Lancer Blade RGB 32GB (2x16GB) DDR5 6000MHz", "ADATA", 1780000, "DDR5", "Dual Channel 32GB (2x16GB) 6000MHz CL30 RGB"),
        ("Kingston FURY Renegade RGB 32GB (2x16GB) DDR5 6400MHz", "Kingston", 2450000, "DDR5", "Dual Channel 32GB (2x16GB) 6400MHz CL32 Silver RGB"),
        ("Corsair Dominator Titanium 32GB (2x16GB) DDR5 6000MHz White", "Corsair", 2850000, "DDR5", "Dual Channel 32GB (2x16GB) 6000MHz CL30 Flagship"),
        ("Corsair Vengeance 64GB (2x32GB) DDR5 5600MHz", "Corsair", 3250000, "DDR5", "Dual Channel 64GB (2x32GB) 5600MHz CL40"),
        ("G.Skill Trident Z5 RGB 64GB (2x32GB) DDR5 6000MHz CL30", "G.Skill", 3850000, "DDR5", "Dual Channel 64GB (2x32GB) 6000MHz CL30 Extreme Workstation")
    ]

    for name, brand, price, socket, spec in ram_templates:
        components.append({
            "id": f"RAM-{current_id:03d}",
            "kategori": "RAM (Memory)",
            "nama": name,
            "brand": brand,
            "harga": price,
            "stok": random.randint(5, 20),
            "tipe_memori": socket,
            "spesifikasi_ringkas": spec,
            "kelebihan": ["Garansi seumur hidup resmi distributor", "Suhu stabil", "Kompatibel 100%"],
            "target_build": ["PC Gaming", "Workstation", "Office"],
            "garansi": "Lifetime Warranty (Seumur Hidup)"
        })
        current_id += 1

    # 4. VGA / GPU - 55 Items
    gpu_templates = [
        # NVIDIA GTX / RTX Entry
        ("MSI GeForce GTX 1650 VENTUS XS 4GB GDDR6", "MSI", 2150000, "NVIDIA", "4GB GDDR6, Dual Fan, TDP 75W"),
        ("ASUS Phoenix GeForce GTX 1650 4GB GDDR6", "ASUS", 2190000, "NVIDIA", "4GB GDDR6, Single Axial-tech Fan, Ringkas"),
        ("ZOTAC Gaming GeForce GTX 1660 SUPER 6GB GDDR6", "ZOTAC", 2750000, "NVIDIA", "6GB GDDR6 192-bit, Dual Fan IceStorm 2.0"),
        ("ASUS TUF Gaming GeForce GTX 1660 SUPER 6GB", "ASUS", 2950000, "NVIDIA", "6GB GDDR6, Dual Fan, Komponen Militer"),
        ("ZOTAC Gaming GeForce RTX 3050 Twin Edge 8GB", "ZOTAC", 3350000, "NVIDIA", "8GB GDDR6, Ray Tracing, DLSS 2, Dual Fan"),
        ("ASUS Dual GeForce RTX 3050 OC 8GB GDDR6", "ASUS", 3450000, "NVIDIA", "8GB GDDR6, Axial-tech Fan, 0dB Technology"),
        ("MSI GeForce RTX 3050 VENTUS 2X 8GB OC", "MSI", 3390000, "NVIDIA", "8GB GDDR6, TORX Fan 3.0, Dual Fan"),
        ("Colorful GeForce RTX 3050 NB DUO 8GB-V", "Colorful", 3250000, "NVIDIA", "8GB GDDR6, Desain Merah Hitam BattleAx"),
        ("ZOTAC Gaming GeForce RTX 3060 Twin Edge 12GB", "ZOTAC", 4450000, "NVIDIA", "12GB GDDR6 192-bit, VRAM Besar untuk 3D"),
        ("MSI GeForce RTX 3060 VENTUS 2X 12GB OC", "MSI", 4550000, "NVIDIA", "12GB GDDR6 192-bit, Desain Dual Fan Minimalis"),

        # NVIDIA RTX 4000 Series
        ("ASUS Dual GeForce RTX 4060 V2 OC 8GB", "ASUS", 4950000, "NVIDIA", "8GB GDDR6, DLSS 3 Frame Gen, Dual Fan"),
        ("MSI GeForce RTX 4060 VENTUS 2X Black 8GB OC", "MSI", 4850000, "NVIDIA", "8GB GDDR6, TORX Fan 4.0, Zero Frozr"),
        ("Gigabyte GeForce RTX 4060 WINDFORCE OC 8GB", "Gigabyte", 4880000, "NVIDIA", "8GB GDDR6, Dual Windforce Fan, Screen Cooling"),
        ("Gigabyte GeForce RTX 4060 EAGLE OC 8GB (Triple Fan)", "Gigabyte", 5250000, "NVIDIA", "8GB GDDR6, 3x Kipas Ekstra Dingin, RGB Fusion"),
        ("ZOTAC Gaming GeForce RTX 4060 Twin Edge 8GB", "ZOTAC", 4750000, "NVIDIA", "8GB GDDR6, Desain Kompak, IceStorm 2.0"),
        ("Colorful iGame GeForce RTX 4060 Ultra W OC 8GB White", "Colorful", 5350000, "NVIDIA", "8GB GDDR6, Desain Hologram Pop-Art Putih Mewah"),
        ("ASUS TUF Gaming GeForce RTX 4060 OC 8GB", "ASUS", 5650000, "NVIDIA", "8GB GDDR6, Bodi Aluminium TUF, Triple Fan"),
        ("ASUS Dual GeForce RTX 4060 Ti OC 8GB", "ASUS", 6750000, "NVIDIA", "8GB GDDR6, DLSS 3, 4352 CUDA Cores"),
        ("MSI GeForce RTX 4060 Ti VENTUS 2X Black 8GB OC", "MSI", 6650000, "NVIDIA", "8GB GDDR6, Desain Ramping Kompak"),
        ("Gigabyte GeForce RTX 4060 Ti GAMING OC 8GB", "Gigabyte", 7150000, "NVIDIA", "8GB GDDR6, Triple Fan Windforce, Dual BIOS"),
        ("Colorful iGame GeForce RTX 4060 Ti Ultra W DUO 16GB", "Colorful", 8350000, "NVIDIA", "16GB GDDR6 Raksasa, Desain Putih Hologram"),
        ("MSI GeForce RTX 4060 Ti GAMING X SLIM 16GB", "MSI", 8450000, "NVIDIA", "16GB GDDR6, Desain Slim Mewah, Twin Frozr 9"),
        ("ASUS Dual GeForce RTX 4070 SUPER EVO OC 12GB", "ASUS", 10750000, "NVIDIA", "12GB GDDR6X, DLSS 3, Dual Fan Axial-tech"),
        ("MSI GeForce RTX 4070 SUPER 12G VENTUS 2X OC", "MSI", 10650000, "NVIDIA", "12GB GDDR6X, Desain Kompak Dual Fan"),
        ("Gigabyte GeForce RTX 4070 SUPER WINDFORCE OC 12GB", "Gigabyte", 10950000, "NVIDIA", "12GB GDDR6X, Triple Fan, Plat Tembaga Langsung"),
        ("ASUS TUF Gaming GeForce RTX 4070 SUPER 12GB", "ASUS", 11650000, "NVIDIA", "12GB GDDR6X, Komponen Militer, Dual BIOS"),
        ("ZOTAC Gaming GeForce RTX 4070 Ti SUPER Trinity Black 16GB", "ZOTAC", 14450000, "NVIDIA", "16GB GDDR6X 256-bit, IceStorm 2.0 Triple Fan"),
        ("MSI GeForce RTX 4070 Ti SUPER 16G GAMING X SLIM", "MSI", 15450000, "NVIDIA", "16GB GDDR6X, Tri Frozr 3, RGB Mystic Light"),
        ("ASUS TUF Gaming GeForce RTX 4070 Ti SUPER 16GB", "ASUS", 15950000, "NVIDIA", "16GB GDDR6X, Bodi Metal Solid TUF"),
        ("MSI GeForce RTX 4080 SUPER 16G VENTUS 3X OC", "MSI", 18850000, "NVIDIA", "16GB GDDR6X 256-bit, Triple Fan, Monster 4K"),
        ("ASUS ROG Strix GeForce RTX 4080 SUPER OC 16GB", "ASUS", 21500000, "NVIDIA", "16GB GDDR6X, Desain ROG Cyberpunk Flagship"),
        ("ASUS ROG Strix GeForce RTX 4090 OC 24GB", "ASUS", 35500000, "NVIDIA", "24GB GDDR6X 384-bit, Vapor Chamber, Raja VGA"),

        # AMD Radeon
        ("ASRock AMD Radeon RX 6500 XT Phantom Gaming 4GB", "ASRock", 2150000, "AMD", "4GB GDDR6, Dual Fan, TDP 107W"),
        ("ASRock AMD Radeon RX 6600 Challenger D 8GB", "ASRock", 3150000, "AMD", "8GB GDDR6 128-bit, PCIe 4.0, TDP 132W"),
        ("Sapphire PULSE AMD Radeon RX 6600 8GB", "Sapphire", 3250000, "AMD", "8GB GDDR6, Kualitas Komponen Sapphire"),
        ("PowerColor Fighter AMD Radeon RX 6600 8GB", "PowerColor", 3090000, "AMD", "8GB GDDR6, Dual Fan Hening"),
        ("Sapphire PULSE AMD Radeon RX 7600 8GB", "Sapphire", 4450000, "AMD", "8GB GDDR6, RDNA 3, FSR 3 Support"),
        ("ASRock AMD Radeon RX 7600 Steel Legend 8GB White", "ASRock", 4750000, "AMD", "8GB GDDR6, Triple Fan Putih Salju, ARGB"),
        ("Sapphire PULSE AMD Radeon RX 7700 XT 12GB", "Sapphire", 7650000, "AMD", "12GB GDDR6 192-bit, RDNA 3, Dual-X"),
        ("ASRock AMD Radeon RX 7800 XT Challenger 16GB", "ASRock", 9450000, "AMD", "16GB GDDR6 256-bit, Ring Fan Dual"),
        ("Sapphire NITRO+ AMD Radeon RX 7800 XT 16GB", "Sapphire", 9950000, "AMD", "16GB GDDR6, Tri-X Cooling, ARGB Bar"),
        ("PowerColor Hellhound AMD Radeon RX 7800 XT 16GB", "PowerColor", 9750000, "AMD", "16GB GDDR6, LED Biru/Ice Blue, Hening"),
        ("Sapphire PULSE AMD Radeon RX 7900 GRE 16GB", "Sapphire", 10850000, "AMD", "16GB GDDR6 256-bit, Performa setara RTX 4070 Ti"),
        ("PowerColor Red Devil AMD Radeon RX 7900 XTX 24GB", "PowerColor", 18500000, "AMD", "24GB GDDR6 384-bit, Monster 4K AMD Flagship"),

        # Intel Arc
        ("ASRock Intel Arc A380 Low Profile 6GB GDDR6", "Intel", 1750000, "Intel", "6GB GDDR6 96-bit, Low Profile, AV1 Encode"),
        ("ASRock Intel Arc A580 Challenger 8GB GDDR6", "Intel", 2950000, "Intel", "8GB GDDR6 256-bit, Dual Fan, AV1"),
        ("Acer Predator BiFrost Intel Arc A770 16GB OC", "Intel", 5450000, "Intel", "16GB GDDR6 256-bit, Dual Fan Hybrid")
    ]

    for name, brand, price, socket, spec in gpu_templates:
        components.append({
            "id": f"GPU-{current_id:03d}",
            "kategori": "VGA / Kartu Grafis",
            "nama": name,
            "brand": brand,
            "harga": price,
            "stok": random.randint(2, 12),
            "chipset": socket,
            "spesifikasi_ringkas": spec,
            "kelebihan": ["Garansi resmi distributor 3 tahun", "Performa gaming & render solid", "Suhu dingin"],
            "target_build": ["PC Gaming", "Editing Video", "Workstation 3D"],
            "garansi": "3 Tahun Resmi Distributor"
        })
        current_id += 1

    # 5. PENYIMPANAN (SSD / HDD) - 35 Items
    ssd_templates = [
        ("Team MP33 PRO 256GB M.2 NVMe", "TeamGroup", 325000, "NVMe Gen3", "Read 2100 MB/s, Write 1100 MB/s"),
        ("Team MP33 PRO 512GB M.2 NVMe", "TeamGroup", 485000, "NVMe Gen3", "Read 2100 MB/s, Write 1700 MB/s"),
        ("ADATA Legend 710 512GB M.2 NVMe", "ADATA", 520000, "NVMe Gen3", "Read 2400 MB/s, Write 1800 MB/s, Heatsink Biru"),
        ("Kingston NV2 500GB M.2 NVMe PCIe 4.0", "Kingston", 565000, "NVMe Gen4", "Read 3500 MB/s, Write 2100 MB/s"),
        ("Team MP44L 500GB M.2 NVMe PCIe 4.0", "TeamGroup", 625000, "NVMe Gen4", "Read 5000 MB/s, Write 2500 MB/s"),
        ("WD Blue SN580 500GB M.2 NVMe PCIe 4.0", "Western Digital", 695000, "NVMe Gen4", "Read 4000 MB/s, Write 3600 MB/s"),
        ("Team MP33 1TB M.2 NVMe PCIe 3.0", "TeamGroup", 875000, "NVMe Gen3", "Read 1800 MB/s, Write 1500 MB/s, 1000GB"),
        ("ADATA Legend 710 1TB M.2 NVMe PCIe 3.0", "ADATA", 920000, "NVMe Gen3", "Read 2400 MB/s, Write 1800 MB/s, Heatsink"),
        ("Kingston NV2 1TB M.2 NVMe PCIe 4.0", "Kingston", 985000, "NVMe Gen4", "Read 3500 MB/s, Write 2100 MB/s, Best Seller"),
        ("Team MP44L 1TB M.2 NVMe PCIe 4.0", "TeamGroup", 1080000, "NVMe Gen4", "Read 5000 MB/s, Write 4500 MB/s"),
        ("WD Blue SN580 1TB M.2 NVMe PCIe 4.0", "Western Digital", 1150000, "NVMe Gen4", "Read 4150 MB/s, Write 4150 MB/s"),
        ("ADATA Legend 850 1TB M.2 NVMe PCIe 4.0", "ADATA", 1250000, "NVMe Gen4", "Read 5000 MB/s, Write 4500 MB/s"),
        ("Crucial P3 Plus 1TB M.2 NVMe PCIe 4.0", "Crucial", 1190000, "NVMe Gen4", "Read 5000 MB/s, Write 4200 MB/s"),
        ("Kingston KC3000 1TB M.2 NVMe PCIe 4.0", "Kingston", 1550000, "NVMe Gen4", "Read 7000 MB/s, Write 6000 MB/s, DRAM Cache"),
        ("Samsung 980 PRO 1TB M.2 NVMe PCIe 4.0", "Samsung", 1750000, "NVMe Gen4", "Read 7000 MB/s, Write 5000 MB/s, DRAM LPDDR4"),
        ("Samsung 990 PRO 1TB M.2 NVMe PCIe 4.0", "Samsung", 1950000, "NVMe Gen4", "Read 7450 MB/s, Write 6900 MB/s, Raja SSD Gen 4"),
        ("WD Black SN850X 1TB M.2 NVMe PCIe 4.0", "Western Digital", 1850000, "NVMe Gen4", "Read 7300 MB/s, Write 6300 MB/s, Game Mode 2.0"),
        ("Kingston NV2 2TB M.2 NVMe PCIe 4.0", "Kingston", 1850000, "NVMe Gen4", "Read 3500 MB/s, Write 2800 MB/s, 2000GB"),
        ("WD Blue SN580 2TB M.2 NVMe PCIe 4.0", "Western Digital", 2150000, "NVMe Gen4", "Read 4150 MB/s, Write 4150 MB/s, 2048GB"),
        ("Kingston KC3000 2TB M.2 NVMe PCIe 4.0", "Kingston", 2850000, "NVMe Gen4", "Read 7000 MB/s, Write 7000 MB/s, DRAM Cache"),
        ("Samsung 990 PRO 2TB M.2 NVMe PCIe 4.0", "Samsung", 3450000, "NVMe Gen4", "Read 7450 MB/s, Write 6900 MB/s, 2048GB Flagship"),
        ("Seagate BarraCuda 1TB HDD 7200RPM 3.5 Inch", "Seagate", 650000, "HDD 3.5 Inch", "SATA III, 7200 RPM, 64MB Cache"),
        ("Western Digital Blue 1TB HDD 7200RPM", "Western Digital", 660000, "HDD 3.5 Inch", "SATA III, 7200 RPM, 64MB Cache"),
        ("Western Digital Blue 2TB HDD 7200RPM", "Western Digital", 950000, "HDD 3.5 Inch", "SATA III, 7200 RPM, 256MB Cache"),
        ("Seagate BarraCuda 2TB HDD 7200RPM", "Seagate", 940000, "HDD 3.5 Inch", "SATA III, 7200 RPM, 256MB Cache"),
        ("Western Digital Blue 4TB HDD 5400RPM", "Western Digital", 1550000, "HDD 3.5 Inch", "SATA III, 256MB Cache, Arsip Jumbo")
    ]

    for name, brand, price, socket, spec in ssd_templates:
        components.append({
            "id": f"SSD-{current_id:03d}",
            "kategori": "Penyimpanan (SSD / HDD)",
            "nama": name,
            "brand": brand,
            "harga": price,
            "stok": random.randint(5, 25),
            "tipe_storage": socket,
            "spesifikasi_ringkas": spec,
            "kelebihan": ["Kecepatan baca-tulis stabil", "Garansi resmi 3-5 tahun", "Loading instan"],
            "target_build": ["PC Rakitan", "Storage Cepat"],
            "garansi": "3 s/d 5 Tahun Resmi Distributor"
        })
        current_id += 1

    # 6. POWER SUPPLY (PSU) - 30 Items
    psu_templates = [
        ("FSP HV PRO 550W 80+ White", "FSP", 580000, "550W", "80+ White, Flat Cable Black, Single Rail"),
        ("Deepcool PK550D 550W 80+ Bronze", "Deepcool", 640000, "550W", "80+ Bronze Certified, OVP/OPP/SCP, Flat Cable"),
        ("MSI MAG A550BN 550W 80+ Bronze", "MSI", 690000, "550W", "80+ Bronze, DC-DC Structure, 120mm Low Noise Fan"),
        ("Corsair CV550 550W 80+ Bronze", "Corsair", 750000, "550W", "80+ Bronze, Compact 125mm Casing"),
        ("be quiet! System Power 10 550W 80+ Bronze", "be quiet!", 785000, "550W", "80+ Bronze, Kipas Super Hening be quiet!"),
        ("Deepcool PK650D 650W 80+ Bronze", "Deepcool", 760000, "650W", "650W 80+ Bronze, Dual PCIe 8-pin"),
        ("MSI MAG A650BN 650W 80+ Bronze", "MSI", 790000, "650W", "650W 80+ Bronze, DC-DC, Kipas Hening"),
        ("Corsair CX650 650W 80+ Bronze", "Corsair", 895000, "650W", "650W 80+ Bronze, Black Sleeved Cable"),
        ("Seasonic B12 BC-650 650W 80+ Bronze", "Seasonic", 950000, "650W", "650W 80+ Bronze, Smart & Silent Fan S2FC, Garansi 5 Thn"),
        ("FSP HV PRO 650W 80+ Bronze", "FSP", 780000, "650W", "650W 80+ Bronze, Efisiensi 85%"),
        ("Deepcool PN750M 750W 80+ Gold ATX 3.1", "Deepcool", 1450000, "750W", "750W 80+ Gold, Full Modular, Native PCIe 5.1"),
        ("FSP Hydro G PRO 750W 80+ Gold Full Modular", "FSP", 1650000, "750W", "750W 80+ Gold, 100% Japanese E-Cap, Garansi 10 Thn"),
        ("MSI MAG A750GL PCIE5 750W 80+ Gold ATX 3.0", "MSI", 1680000, "750W", "750W 80+ Gold, Native 12V-2x6 Cable RTX 4000"),
        ("Corsair RM750e 750W 80+ Gold Full Modular ATX 3.0", "Corsair", 1850000, "750W", "750W 80+ Gold, ATX 3.0, 105C Capacitors"),
        ("Seasonic FOCUS GX-750 750W 80+ Gold Modular", "Seasonic", 1950000, "750W", "750W 80+ Gold, Fluid Dynamic Fan, Garansi 10 Thn"),
        ("MSI MAG A850GL PCIE5 850W 80+ Gold ATX 3.0", "MSI", 1980000, "850W", "850W 80+ Gold, Native PCIe 5.0, Full Modular"),
        ("Corsair RM850e 850W 80+ Gold Full Modular ATX 3.0", "Corsair", 2150000, "850W", "850W 80+ Gold, Ultra Low Noise"),
        ("Seasonic FOCUS GX-850 850W 80+ Gold Full Modular", "Seasonic", 2350000, "850W", "850W 80+ Gold, Tier A PSU, Garansi 10 Thn"),
        ("be quiet! Pure Power 12 M 850W 80+ Gold ATX 3.0", "be quiet!", 2250000, "850W", "850W 80+ Gold, Super Senyap, Dual Rail 12V"),
        ("Corsair RM1000x 1000W 80+ Gold Full Modular", "Corsair", 2950000, "1000W", "1000W 80+ Gold, Japanese Cap 105C, Siap RTX 4090"),
        ("Seasonic VERTEX GX-1000 1000W 80+ Gold ATX 3.0", "Seasonic", 3450000, "1000W", "1000W 80+ Gold, ATX 3.0 & PCIe 5.0 Native")
    ]

    for name, brand, price, socket, spec in psu_templates:
        components.append({
            "id": f"PSU-{current_id:03d}",
            "kategori": "Power Supply (PSU)",
            "nama": name,
            "brand": brand,
            "harga": price,
            "stok": random.randint(4, 15),
            "daya": socket,
            "spesifikasi_ringkas": spec,
            "kelebihan": ["Sertifikasi efisiensi 80+ resmi", "Proteksi listrik lengkap OVP/OPP/SCP", "Kabel rapi"],
            "target_build": ["PC Gaming", "Workstation", "Office"],
            "garansi": "3 s/d 10 Tahun Resmi Distributor"
        })
        current_id += 1

    # 7. CPU COOLER - 25 Items
    cooler_templates = [
        ("Jonsbo CR-1400 EVO ARGB Black", "Jonsbo", 195000, "Air Cooler", "Tower 4 Heatpipe Tembaga, 92mm PWM ARGB"),
        ("Jonsbo CR-1400 EVO ARGB White", "Jonsbo", 215000, "Air Cooler", "Tower 4 Heatpipe Tembaga, Putih Salju ARGB"),
        ("Thermalright Assassin X 120 Refined SE ARGB", "Thermalright", 245000, "Air Cooler", "Tower 4 Heatpipe AGHP, Fan 120mm PWM S-FDB"),
        ("Thermalright Assassin X 120 Refined SE White ARGB", "Thermalright", 265000, "Air Cooler", "Tower Putih Bersih, Fan 120mm ARGB"),
        ("Deepcool AG400 ARGB Single Tower", "Deepcool", 285000, "Air Cooler", "Tower 4 Heatpipe Direct Contact, Fan 120mm Hydro"),
        ("Deepcool AG400 White ARGB", "Deepcool", 310000, "Air Cooler", "Full White Theme, Fan 120mm ARGB"),
        ("Deepcool AK400 Digital Black (Display Suhu)", "Deepcool", 465000, "Air Cooler", "Layar Digital Real-time Suhu CPU di Heatsink"),
        ("Deepcool AK400 Digital White (Display Suhu)", "Deepcool", 495000, "Air Cooler", "Full White dengan Layar Digital Suhu CPU"),
        ("Thermalright Peerless Assassin 120 SE ARGB", "Thermalright", 485000, "Air Cooler", "Dual Tower 6 Heatpipes, 2x Fan 120mm PWM"),
        ("Thermalright Peerless Assassin 120 SE White ARGB", "Thermalright", 515000, "Air Cooler", "Dual Tower Putih, 6 Heatpipes, Dingin Setara AIO 240"),
        ("Deepcool AK620 High Performance Dual Tower", "Deepcool", 825000, "Air Cooler", "Dual Tower 6 Heatpipes, Disipasi Panas 260W"),
        ("Noctua NH-U12S chromax.black", "Noctua", 1350000, "Air Cooler", "Single Tower Hitam Pekat, Kipas NF-F12 Legendaris"),
        ("Noctua NH-D15 chromax.black", "Noctua", 1850000, "Air Cooler", "Raja Air Cooler Dunia, Dual Tower Dual NF-A15"),
        ("Deepcool LE520 240mm ARGB AIO Liquid Cooler", "Deepcool", 785000, "AIO Liquid 240mm", "Radiator 240mm, Anti-Leak Tech, 2x Fan ARGB"),
        ("Deepcool LE520 White 240mm ARGB AIO", "Deepcool", 825000, "AIO Liquid 240mm", "Full White Radiator 240mm, Anti-Leak Tech"),
        ("Deepcool LT520 240mm Infinity Mirror Liquid", "Deepcool", 1250000, "AIO Liquid 240mm", "Pompa Cermin Infinity Kubus 3D, Kipas FK120"),
        ("Arctic Liquid Freezer III 240 ARGB Black", "Arctic", 1380000, "AIO Liquid 240mm", "Radiator Tebal 38mm, VRM Fan Terintegrasi"),
        ("Arctic Liquid Freezer III 240 A-RGB White", "Arctic", 1450000, "AIO Liquid 240mm", "Radiator 38mm Putih, VRM Fan Terintegrasi"),
        ("MSI MAG CoreLiquid M240 ARGB", "MSI", 1150000, "AIO Liquid 240mm", "Radiator 240mm, Desain Curve Blok Pompa Mewah"),
        ("Deepcool LE720 360mm ARGB AIO Liquid Cooler", "Deepcool", 1050000, "AIO Liquid 360mm", "Radiator 360mm 3 Kipas, Anti-Leak Tech"),
        ("Arctic Liquid Freezer III 360 ARGB Black", "Arctic", 1680000, "AIO Liquid 360mm", "Radiator 360mm Raksasa, VRM Fan, Dingin Maksimal"),
        ("Arctic Liquid Freezer III 360 A-RGB White", "Arctic", 1750000, "AIO Liquid 360mm", "Radiator 360mm Putih Salju, VRM Fan"),
        ("NZXT Kraken 240 RGB Black (Layar LCD)", "NZXT", 2450000, "AIO Liquid 240mm", "Layar LCD 1.54 inch di Pompa untuk GIF/Suhu, 2x Kipas RGB"),
        ("NZXT Kraken Elite 360 RGB White (Layar LCD 2.36)", "NZXT", 4850000, "AIO Liquid 360mm", "Layar LCD 2.36 inch 60 FPS Resolusi Tinggi di Pompa")
    ]

    for name, brand, price, socket, spec in cooler_templates:
        components.append({
            "id": f"CLR-{current_id:03d}",
            "kategori": "CPU Cooler",
            "nama": name,
            "brand": brand,
            "harga": price,
            "stok": random.randint(4, 15),
            "tipe": socket,
            "spesifikasi_ringkas": spec,
            "kelebihan": ["Disipasi panas optimal", "Kipas PWM hening", "Pemasangan mudah"],
            "target_build": ["PC Gaming", "Workstation Render"],
            "garansi": "2 s/d 6 Tahun Resmi Distributor"
        })
        current_id += 1

    # 8. CASING PC - 30 Items
    case_templates = [
        ("Cube Gaming Axel Black (M-ATX)", "Cube Gaming", 345000, "Micro-ATX", "Mesh Front, Tempered Glass, Free 3x 120mm Fans"),
        ("Cube Gaming Axel White (M-ATX)", "Cube Gaming", 365000, "Micro-ATX", "Full White Mesh Front, Tempered Glass, Free 3x Fans"),
        ("VenomRX Praetorian Black M-ATX", "VenomRX", 380000, "Micro-ATX", "Door Tempered Glass Magnet, Free 3x RGB Fans"),
        ("VenomRX Praetorian White M-ATX", "VenomRX", 395000, "Micro-ATX", "Door Tempered Glass Magnet Putih, Free 3x RGB Fans"),
        ("Paradox Gaming Ghost M-ATX Aquarium", "Paradox Gaming", 425000, "Micro-ATX Aquarium", "Dual Tempered Glass View, Free 3x ARGB Fans"),
        ("Cube Gaming Byron Black Aquarium M-ATX", "Cube Gaming", 465000, "Micro-ATX Aquarium", "Panoramic Tempered Glass, Free 3x ARGB Fans"),
        ("Montech AIR 100 ARGB Black (M-ATX)", "Montech", 645000, "Micro-ATX", "Ultra-fine Mesh Front, Include 4x ARGB Fans + Hub"),
        ("Montech AIR 100 ARGB White (M-ATX)", "Montech", 675000, "Micro-ATX", "Full White Theme, Include 4x ARGB White Fans + Hub"),
        ("DarkFlash DLM21 Mesh Black (M-ATX)", "DarkFlash", 545000, "Micro-ATX", "Low Poly Mesh Front, Door Tempered Glass"),
        ("DarkFlash DLM21 Mesh White (M-ATX)", "DarkFlash", 565000, "Micro-ATX", "Low Poly Mesh Putih, Door Tempered Glass"),
        ("Montech AIR 903 BASE Black (ATX)", "Montech", 820000, "Mid-Tower ATX", "3x Kipas 140mm High Airflow PWM, USB Type-C"),
        ("Montech AIR 903 MAX White (ATX)", "Montech", 965000, "Mid-Tower ATX", "4x Kipas 140mm ARGB PWM Putih, USB Type-C"),
        ("NZXT H5 Flow Black (ATX)", "NZXT", 1250000, "Mid-Tower ATX", "Perforated Mesh, Dedicated Bottom GPU Fan"),
        ("NZXT H5 Flow White (ATX)", "NZXT", 1280000, "Mid-Tower ATX", "All-White Perforated Mesh, Bottom GPU Fan"),
        ("Corsair 4000D Airflow Black (ATX)", "Corsair", 1350000, "Mid-Tower ATX", "High-Airflow Steel Front, RapidRoute Cable System"),
        ("Corsair 4000D Airflow White (ATX)", "Corsair", 1380000, "Mid-Tower ATX", "White Steel Front, RapidRoute Cable System"),
        ("Lian Li LANCOOL 216 RGB Black (ATX)", "Lian Li", 1450000, "Mid-Tower ATX", "2x Kipas Raksasa 160mm ARGB Depan, Airflow Monster"),
        ("Lian Li LANCOOL 216 RGB White (ATX)", "Lian Li", 1520000, "Mid-Tower ATX", "2x Kipas Raksasa 160mm ARGB Putih, Airflow Monster"),
        ("Fractal Design Pop Air Black Solid/TG", "Fractal Design", 1350000, "Mid-Tower ATX", "Desain Skandinavia Elegan, Kualitas Cat Premium"),
        ("Lian Li O11 Dynamic Mini Black", "Lian Li", 1650000, "Dual Chamber M-ATX/ITX", "Aquarium Kompak, Support SFX/SFX-L PSU"),
        ("Lian Li O11 Dynamic EVO Black (ATX)", "Lian Li", 2450000, "Dual Chamber ATX", "Dual Tempered Glass Aquarium, Reversible Chassis"),
        ("Lian Li O11 Dynamic EVO White (ATX)", "Lian Li", 2550000, "Dual Chamber ATX", "All-White Aquarium Showcase Flagship"),
        ("NZXT H9 Flow Black Dual Chamber ATX", "NZXT", 2650000, "Dual Chamber ATX", "Panoramic Glass, Support 10 Fans, Airflow Atas Mesh"),
        ("Hyte Y60 Modern Aesthetic Red/Black", "Hyte", 3250000, "Panoramic Corner 3-Piece Glass", "Kaca Sudut 3 Bagian Unik, Include Riser PCIe 4.0")
    ]

    for name, brand, price, socket, spec in case_templates:
        components.append({
            "id": f"CASE-{current_id:03d}",
            "kategori": "Casing PC",
            "nama": name,
            "brand": brand,
            "harga": price,
            "stok": random.randint(3, 12),
            "form_factor": socket,
            "spesifikasi_ringkas": spec,
            "kelebihan": ["Bahan baja SPCC tebal", "Sirkulasi udara dingin", "Kabel tertata rapi"],
            "target_build": ["PC Gaming", "Showcase PC"],
            "garansi": "1 Tahun Resmi"
        })
        current_id += 1

    # 9. MONITOR - 20 Items
    monitor_templates = [
        ("Xiaomi Monitor G24i 23.8 Inch IPS 180Hz", "Xiaomi", 1450000, "23.8 Inch FHD", "Fast IPS, 180Hz, 1ms, 99% sRGB, FreeSync, HDR10"),
        ("ViewSonic OMNI VX2428 24 Inch IPS 165Hz", "ViewSonic", 1650000, "23.8 Inch FHD", "Fast IPS, 165Hz, 0.5ms, Speaker Internal Stereo"),
        ("LG UltraGear 24GN60R-B 24 Inch IPS 144Hz", "LG", 1850000, "23.8 Inch FHD", "IPS Panel LG, 144Hz, 1ms MBR, sRGB 99%"),
        ("AOC 24G2SP 23.8 Inch IPS 165Hz Stand Ergonomis", "AOC", 2050000, "23.8 Inch FHD", "IPS, 165Hz, 1ms, 125% sRGB, Stand Naik-Turun & Pivot"),
        ("ASUS TUF Gaming VG249Q3A 23.8 Inch IPS 180Hz", "ASUS", 2150000, "23.8 Inch FHD", "Fast IPS, 180Hz, 1ms, ELMB Sync, Speaker"),
        ("Xiaomi Monitor G27i 27 Inch IPS 165Hz", "Xiaomi", 1950000, "27 Inch FHD", "Fast IPS 27 Inch, 165Hz, 1ms, Layar Lebar Bezel Tipis"),
        ("ViewSonic OMNI VX2728 27 Inch IPS 165Hz", "ViewSonic", 2150000, "27 Inch FHD", "Fast IPS 27 Inch, 165Hz, 0.5ms, FreeSync Premium"),
        ("LG UltraGear 27GN65R-B 27 Inch IPS 144Hz Ergonomis", "LG", 2650000, "27 Inch FHD", "IPS, 144Hz, 1ms, Stand Ergonomis Naik-Turun Pivot"),
        ("AOC 27G2SP 27 Inch IPS 165Hz Ergonomis", "AOC", 2550000, "27 Inch FHD", "IPS, 165Hz, 1ms, 122% sRGB, Stand Ergonomis"),
        ("Xiaomi Curved Gaming Monitor G34WQi 34 Inch Ultrawide 180Hz", "Xiaomi", 3650000, "34 Inch WQHD Ultrawide (3440x1440)", "Curved 1500R, 180Hz, 1ms, 95% DCI-P3, 21:9 Ultrawide"),
        ("ViewSonic OMNI VX2780-2K-SHDJ 27 Inch QHD 2K 170Hz", "ViewSonic", 3350000, "27 Inch QHD (2560x1440)", "SuperClear IPS, 170Hz, 1ms, Stand Ergonomis"),
        ("AOC Q27G2S/EU 27 Inch QHD 2K 165Hz", "AOC", 3550000, "27 Inch QHD (2560x1440)", "IPS, 165Hz, 1ms, 10-bit Color, Stand Ergonomis"),
        ("LG UltraGear 27GP850-B 27 Inch Nano IPS QHD 2K 165Hz", "LG", 4650000, "27 Inch QHD (2560x1440)", "Nano IPS, 165Hz (OC 180Hz), 1ms GtG, 98% DCI-P3, G-Sync"),
        ("ASUS ROG Strix XG27ACS 27 Inch Fast IPS 180Hz QHD 2K", "ASUS", 4950000, "27 Inch QHD (2560x1440)", "Fast IPS, 180Hz, 1ms, Type-C DP Alt Mode, Stand Handphone"),
        ("Samsung Odyssey G5 G55C 27 Inch QHD 165Hz Curved 1000R", "Samsung", 3150000, "27 Inch QHD (2560x1440)", "VA 1000R Lengkung Ekstrem, 165Hz, 1ms, HDR10")
    ]

    for name, brand, price, socket, spec in monitor_templates:
        components.append({
            "id": f"MON-{current_id:03d}",
            "kategori": "Monitor",
            "nama": name,
            "brand": brand,
            "harga": price,
            "stok": random.randint(3, 10),
            "panel": socket,
            "spesifikasi_ringkas": spec,
            "kelebihan": ["Panel Fast IPS warna akurat", "Refresh rate tinggi bebas ghosting", "Garansi resmi"],
            "target_build": ["Pelengkap PC Gaming", "Color Grading"],
            "garansi": "3 Tahun Resmi Distributor"
        })
        current_id += 1

    return components

if __name__ == "__main__":
    catalog = generate_full_pc_catalog()
    output_path = "katalog_komponen_pc.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)
    print(f"Sukses menghasilkan {len(catalog)} data komponen PC resmi ke '{output_path}'!")
