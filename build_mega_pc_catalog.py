import json
import random
import sys

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def generate_mega_pc_catalog():
    components = []
    
    # -------------------------------------------------------------------------
    # 1. PROCESSOR (CPU) - 75 Items
    # -------------------------------------------------------------------------
    cpu_list = [
        # AMD AM4
        ("AMD Athlon 3000G with Radeon Vega 3", "AMD", 650000, "Socket AM4", "2 Core / 4 Thread, 3.5 GHz, Vega 3 iGPU, 35W", ["Hemat daya 35W", "Ada display tanpa VGA terpisah"], ["Kasir / POS", "PC Office Sederhana"]),
        ("AMD Athlon 200GE with Radeon Vega 3", "AMD", 550000, "Socket AM4", "2 Core / 4 Thread, 3.2 GHz, Vega 3 iGPU, 35W", ["Harga super ekonomis", "Suhu dingin"], ["Office Pelajar"]),
        ("AMD Ryzen 3 3200G with Radeon Vega 8", "AMD", 1050000, "Socket AM4", "4 Core / 4 Thread, 4.0 GHz, Vega 8 iGPU, 65W", ["Vega 8 handal untuk esport", "Tanpa butuh VGA eksternal"], ["Office", "Pelajar"]),
        ("AMD Ryzen 3 4100", "AMD", 890000, "Socket AM4", "4 Core / 8 Thread, 4.0 GHz, 65W (Wajib VGA)", ["4 Core 8 Thread termurah", "Suhu dingin"], ["Budget Esports"]),
        ("AMD Ryzen 3 4300G with Radeon Graphics", "AMD", 1250000, "Socket AM4", "4 Core / 8 Thread, 4.0 GHz, Radeon Graphics 6 Core", ["Zen 2 dengan 8 thread + iGPU", "Kuat Valorant 60+ FPS"], ["All-in-One Office"]),
        ("AMD Ryzen 5 3500X", "AMD", 1080000, "Socket AM4", "6 Core / 6 Thread, 4.1 GHz, 32MB L3 Cache (Wajib VGA)", ["Cache besar 32MB", "Gaming 1080p budget"], ["Budget Gaming"]),
        ("AMD Ryzen 5 3600", "AMD", 1150000, "Socket AM4", "6 Core / 12 Thread, 4.2 GHz, 35MB Cache, PCIe 4.0", ["Legenda 6 core sejuta umat", "Mendukung PCIe 4.0"], ["Budget Gaming", "Multitasking"]),
        ("AMD Ryzen 5 4500", "AMD", 1120000, "Socket AM4", "6 Core / 12 Thread, 4.1 GHz, 65W", ["6 Core harga sejutaan", "Multitasking lancar"], ["All-Rounder Hemat"]),
        ("AMD Ryzen 5 4600G with Radeon Graphics", "AMD", 1450000, "Socket AM4", "6 Core / 12 Thread, 4.2 GHz, Vega 7 iGPU", ["6 Core 12 Thread ada iGPU", "Rendering ringan lancar tanpa VGA"], ["Office Desain", "Esports"]),
        ("AMD Ryzen 5 5500", "AMD", 1380000, "Socket AM4", "6 Core / 12 Thread, 4.2 GHz, 19MB Cache, Zen 3, 65W", ["Arsitektur Zen 3 kencang", "Suhu dingin TDP 65W"], ["Gaming 1080p Value"]),
        ("AMD Ryzen 5 5500GT with Radeon Graphics", "AMD", 1750000, "Socket AM4", "6 Core / 12 Thread, 4.4 GHz, Radeon Vega 7 Boost", ["Peningkatan clock dari 4600G", "Tanpa VGA terpisah"], ["PC Kantor Produktif"]),
        ("AMD Ryzen 5 5600G with Radeon Graphics", "AMD", 1950000, "Socket AM4", "6 Core / 12 Thread, 4.4 GHz, Vega 7 iGPU 1.9GHz", ["Bisa rakit tanpa beli VGA terpisah", "Kuat GTA V & Valorant 60+ FPS"], ["Rakit Tanpa VGA", "Desain Grafis"]),
        ("AMD Ryzen 5 5600GT with Radeon Graphics", "AMD", 2150000, "Socket AM4", "6 Core / 12 Thread, 4.6 GHz, Vega 7 iGPU Boost", ["Versi refresh 5600G clock lebih tinggi", "Gaming esport mulus"], ["Esports Tanpa VGA"]),
        ("AMD Ryzen 5 5600", "AMD", 1750000, "Socket AM4", "6 Core / 12 Thread, 4.4 GHz, 35MB Cache, PCIe 4.0", ["Sweet spot gaming 1080p", "Tidak bottleneck dipadu RTX 4060"], ["Sweet Spot Gaming", "Editing Video"]),
        ("AMD Ryzen 5 5600X", "AMD", 2150000, "Socket AM4", "6 Core / 12 Thread, 4.6 GHz, 35MB Cache", ["Clock speed tinggi", "Single-core kencang untuk game kompetitif"], ["Gaming Kompetitif"]),
        ("AMD Ryzen 5 5600XT", "AMD", 2350000, "Socket AM4", "6 Core / 12 Thread, 4.7 GHz, 35MB Cache, Zen 3", ["Varian clock maksimal Zen 3", "Performa kompetitif tinggi"], ["Enthusiast AM4"]),
        ("AMD Ryzen 7 3700X", "AMD", 1750000, "Socket AM4", "8 Core / 16 Thread, 4.4 GHz, 36MB Cache, TDP 65W", ["8 Core terjangkau", "Cocok untuk live streaming"], ["Budget Streamer"]),
        ("AMD Ryzen 7 5700", "AMD", 2250000, "Socket AM4", "8 Core / 16 Thread, 4.6 GHz, 20MB Cache, 65W", ["8 Core harga bersahabat", "Multithread kuat"], ["Workstation Budget"]),
        ("AMD Ryzen 7 5700G with Radeon Graphics", "AMD", 2650000, "Socket AM4", "8 Core / 16 Thread, 4.6 GHz, Vega 8 iGPU 2.0GHz", ["8 Core lengkap dengan iGPU", "Kuat rendering & komputasi"], ["Workstation Tanpa VGA"]),
        ("AMD Ryzen 7 5700X", "AMD", 2550000, "Socket AM4", "8 Core / 16 Thread, 4.6 GHz, 36MB Cache, TDP 65W", ["8 Core sangat dingin", "Pilihan terbaik upgrade soket AM4"], ["Workstation 3D", "Video Rendering"]),
        ("AMD Ryzen 7 5700X3D", "AMD", 3350000, "Socket AM4", "8 Core / 16 Thread, 3D V-Cache 100MB, 4.1 GHz", ["Monster gaming soket AM4", "3D V-Cache mendongkrak 1% low FPS"], ["Hardcore Gaming AM4"]),
        ("AMD Ryzen 7 5800X", "AMD", 2950000, "Socket AM4", "8 Core / 16 Thread, 4.7 GHz, 36MB Cache, TDP 105W", ["Clock single-core tinggi", "Mantap untuk simulasi & gaming"], ["Gaming & Editing"]),
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
        ("AMD Ryzen 9 7900", "AMD", 5850000, "Socket AM5", "12 Core / 24 Thread, 5.4 GHz, 76MB Cache, TDP 65W", ["12 Core super efisien", "Cocok untuk rendering hening"], ["Silent Workstation"]),
        ("AMD Ryzen 9 7900X", "AMD", 6850000, "Socket AM5", "12 Core / 24 Thread, 5.6 GHz, 76MB Cache", ["12 Core monster multitasking", "Ideal untuk 3D Blender & VFX"], ["Studio Workstation"]),
        ("AMD Ryzen 9 7900X3D", "AMD", 7950000, "Socket AM5", "12 Core / 24 Thread, 140MB Cache, 5.6 GHz", ["12 Core dengan 3D V-Cache", "Dual use gaming & render"], ["High-End Hybrid"]),
        ("AMD Ryzen 9 7950X", "AMD", 8650000, "Socket AM5", "16 Core / 32 Thread, 5.7 GHz, 80MB Cache", ["16 Core 32 Thread kelas atas", "Daya komputasi tak tertandingi"], ["Enterprise Creator"]),
        ("AMD Ryzen 9 7950X3D", "AMD", 9850000, "Socket AM5", "16 Core / 32 Thread, 144MB V-Cache, 5.7 GHz", ["Kombinasi 16 Core dan 3D V-Cache", "Terbaik untuk gaming dan render sekaligus"], ["Ultimate Flagship"]),
        ("AMD Ryzen 5 9600X", "AMD", 4350000, "Socket AM5", "6 Core / 12 Thread, Zen 5 4nm, 5.4 GHz, 38MB Cache", ["Arsitektur Zen 5 terbaru", "Single core sangat kencang"], ["Next-Gen Gaming"]),
        ("AMD Ryzen 7 9700X", "AMD", 5850000, "Socket AM5", "8 Core / 16 Thread, Zen 5 4nm, 5.5 GHz, 65W", ["Arsitektur terbaru Zen 5", "IPC naik signifikan", "Suhu sangat dingin"], ["Next-Gen Workstation"]),
        ("AMD Ryzen 9 9900X", "AMD", 7950000, "Socket AM5", "12 Core / 24 Thread, Zen 5 4nm, 5.6 GHz, 76MB Cache", ["12 Core Zen 5 performa tinggi", "Efisien dan dingin"], ["Next-Gen Studio"]),
        ("AMD Ryzen 9 9950X", "AMD", 10250000, "Socket AM5", "16 Core / 32 Thread, Zen 5 4nm, 5.7 GHz, 80MB Cache", ["Raja prosesor consumer Zen 5", "Multithread brutal"], ["Ultimate Creator PC"]),

        # Intel LGA1200
        ("Intel Core i3-10100F", "Intel", 890000, "Socket LGA1200", "4 Core / 8 Thread, 4.3 GHz, 6MB Cache (Wajib VGA)", ["4 Core 8 Thread termurah Intel", "Stabil untuk office & gaming entry"], ["Ultra Budget Gaming"]),
        ("Intel Core i3-10105 with UHD 630", "Intel", 1150000, "Socket LGA1200", "4 Core / 8 Thread, 4.4 GHz, Intel UHD Graphics 630", ["Lengkap dengan iGPU", "Tanpa VGA eksternal"], ["Office Bisnis"]),
        ("Intel Core i5-10400F", "Intel", 1350000, "Socket LGA1200", "6 Core / 12 Thread, 4.3 GHz, 12MB Cache (Wajib VGA)", ["6 Core ekonomis", "Sejuta umat LGA1200"], ["Budget Gaming 1080p"]),
        ("Intel Core i5-10400 with UHD 630", "Intel", 1650000, "Socket LGA1200", "6 Core / 12 Thread, 4.3 GHz, Intel UHD 630", ["6 Core serbaguna", "QuickSync video"], ["Office Produktif"]),
        ("Intel Core i5-11400F", "Intel", 1550000, "Socket LGA1200", "6 Core / 12 Thread, 4.4 GHz, PCIe 4.0 Support", ["Mendukung PCIe 4.0 M.2 SSD", "Single-core kencang"], ["All-Rounder Gaming"]),
        ("Intel Core i5-11400 with UHD 730", "Intel", 1850000, "Socket LGA1200", "6 Core / 12 Thread, 4.4 GHz, Intel UHD 730", ["iGPU UHD 730 lebih kencang", "Stabil"], ["Office Desain"]),
        ("Intel Core i7-10700F", "Intel", 2450000, "Socket LGA1200", "8 Core / 16 Thread, 4.8 GHz, 16MB Cache", ["8 Core terjangkau", "Multitasking lancar"], ["Workstation LGA1200"]),
        ("Intel Core i7-11700F", "Intel", 2850000, "Socket LGA1200", "8 Core / 16 Thread, 4.9 GHz, 16MB Cache", ["Arsitektur Rocket Lake", "Mendukung PCIe 4.0 x16"], ["Content Creator LGA1200"]),

        # Intel LGA1700
        ("Intel Core i3-12100F", "Intel", 1250000, "Socket LGA1700", "4 Core / 8 Thread, 4.3 GHz, 12MB Cache (Wajib VGA)", ["Single-core kencang di harga 1 jutaan", "Suhu adem"], ["Entry Gaming 1080p"]),
        ("Intel Core i3-12100 with UHD 730", "Intel", 1650000, "Socket LGA1700", "4 Core / 8 Thread, 4.3 GHz, Intel UHD Graphics 730", ["Ada display tanpa VGA", "QuickSync video"], ["Office Cepat"]),
        ("Intel Core i3-13100F", "Intel", 1450000, "Socket LGA1700", "4 Core / 8 Thread, 4.5 GHz, Raptor Lake Architecture", ["Clock lebih tinggi dari 12100F", "Efisien"], ["Modern Esports 1080p"]),
        ("Intel Core i3-14100F", "Intel", 1550000, "Socket LGA1700", "4 Core / 8 Thread, 4.7 GHz, Gen 14 Raptor Lake", ["Generasi 14 terbaru", "Clock speed 4.7 GHz kencang"], ["Budget Esports 1080p"]),
        ("Intel Core i3-14100 with UHD 730", "Intel", 1850000, "Socket LGA1700", "4 Core / 8 Thread, 4.7 GHz, Gen 14 UHD 730", ["Gen 14 lengkap dengan grafis bawaan", "QuickSync"], ["Office Modern Gen 14"]),
        ("Intel Core i5-12400F", "Intel", 1750000, "Socket LGA1700", "6 Core / 12 Thread, 4.4 GHz, 18MB Cache (Wajib VGA)", ["Prosesor sejuta umat terpopuler", "Tidak bottleneck dipadu RTX 4060"], ["Sweet Spot Gaming 1080p"]),
        ("Intel Core i5-12400 with UHD 730", "Intel", 2150000, "Socket LGA1700", "6 Core / 12 Thread, 4.4 GHz, Intel UHD 730", ["Lengkap dengan iGPU", "Stabilitas tinggi"], ["Office Bisnis", "Editing Ringan"]),
        ("Intel Core i5-12600KF", "Intel", 2650000, "Socket LGA1700", "10 Core (6P + 4E) / 16 Thread, 4.9 GHz, Unlocked", ["10 Core murah", "Bisa overclock", "Kencang untuk gaming & rendering"], ["Performance Gaming"]),
        ("Intel Core i5-13400F", "Intel", 2950000, "Socket LGA1700", "10 Core (6P + 4E) / 16 Thread, 4.6 GHz", ["Arsitektur Hybrid 10 Core", "Multitasking berat lancar"], ["Mid-Range Creator"]),
        ("Intel Core i5-13400 with UHD 730", "Intel", 3250000, "Socket LGA1700", "10 Core (6P + 4E) / 16 Thread, 4.6 GHz, UHD 730", ["10 Core dengan iGPU bawaan", "Pilihan tepat editor video"], ["Editor Video Pemula"]),
        ("Intel Core i5-13500", "Intel", 3650000, "Socket LGA1700", "14 Core (6P + 8E) / 20 Thread, 4.8 GHz, Intel UHD 770", ["14 Core harga bersahabat", "iGPU UHD 770 QuickSync"], ["Editing Video Studio"]),
        ("Intel Core i5-14400F", "Intel", 3250000, "Socket LGA1700", "10 Core (6P + 4E) / 16 Thread, 4.7 GHz, Gen 14", ["Clock speed lebih tinggi", "Dukungan memori DDR4 & DDR5"], ["Modern Gaming Gen 14"]),
        ("Intel Core i5-14400 with UHD 730", "Intel", 3550000, "Socket LGA1700", "10 Core (6P + 4E) / 16 Thread, 4.7 GHz, Gen 14 UHD", ["10 Core Gen 14 dengan iGPU", "Multitasking mulus"], ["Creator Gen 14"]),
        ("Intel Core i5-14500", "Intel", 3850000, "Socket LGA1700", "14 Core (6P + 8E) / 20 Thread, 5.0 GHz, Intel UHD 770", ["14 Core kencang tembus 5.0 GHz", "iGPU UHD 770"], ["Studio Editing Gen 14"]),
        ("Intel Core i5-13600KF", "Intel", 4250000, "Socket LGA1700", "14 Core (6P + 8E) / 20 Thread, 5.1 GHz, Unlocked", ["Monster 14 Core", "Mampu melibas editing 4K dan game berat"], ["High-End Gaming Intel"]),
        ("Intel Core i5-14600KF", "Intel", 4550000, "Socket LGA1700", "14 Core (6P + 8E) / 20 Thread, 5.3 GHz, Gen 14", ["Clock speed 5.3 GHz", "Performa tinggi di game kompetitif"], ["Enthusiast Gaming"]),
        ("Intel Core i7-12700F", "Intel", 3850000, "Socket LGA1700", "12 Core (8P + 4E) / 20 Thread, 4.9 GHz, 25MB Cache", ["12 Core harga hemat", "8 Performance core murni"], ["Value Workstation"]),
        ("Intel Core i7-13700F", "Intel", 5450000, "Socket LGA1700", "16 Core (8P + 8E) / 24 Thread, 5.2 GHz", ["16 Core bertenaga dahsyat", "Stabil untuk pekerjaan nonstop"], ["Workstation 3D"]),
        ("Intel Core i7-13700KF", "Intel", 5850000, "Socket LGA1700", "16 Core (8P + 8E) / 24 Thread, 5.4 GHz, Unlocked", ["16 Core unlocked", "Performa single & multi-core monster"], ["Heavy Workstation"]),
        ("Intel Core i7-14700F", "Intel", 5950000, "Socket LGA1700", "20 Core (8P + 12E) / 28 Thread, 5.4 GHz", ["20 Core masif", "Lompatan 4 E-Core tambahan dibanding gen 13"], ["Pro Content Creator"]),
        ("Intel Core i7-14700KF", "Intel", 6350000, "Socket LGA1700", "20 Core (8P + 12E) / 28 Thread, 5.6 GHz, Gen 14", ["20 Core monster terbaru", "Clock speed 5.6 GHz"], ["Heavy Render Studio"]),
        ("Intel Core i9-13900KF", "Intel", 7850000, "Socket LGA1700", "24 Core (8P + 16E) / 32 Thread, 5.8 GHz", ["24 Core monster", "Daya komputasi studio render animasi"], ["Studio Workstation"]),
        ("Intel Core i9-14900KF", "Intel", 8950000, "Socket LGA1700", "24 Core (8P + 16E) / 32 Thread, 6.0 GHz", ["Tembus 6.0 GHz out of the box", "Puncak komputasi Intel"], ["Flagship Extreme PC"]),
        ("Intel Core i9-14900KS Special Edition", "Intel", 10850000, "Socket LGA1700", "24 Core / 32 Thread, up to 6.2 GHz, Binned Chip", ["Edisi spesial silikon terbaik dunia", "Tembus 6.2 GHz"], ["Ultimate Overclocking"])
    ]

    for name, brand, price, socket, spec, pros, target in cpu_list:
        components.append({
            "id": f"CPU-{len(components)+1:03d}",
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

    # -------------------------------------------------------------------------
    # 2. MOTHERBOARD - 80 Items
    # -------------------------------------------------------------------------
    mobo_list = [
        # AM4
        ("A320M-HDV R4.0", "ASRock", 720000, "AM4", "Micro-ATX, 2x DDR4, 1x Ultra M.2, DVI/HDMI", ["Paling murah AM4", "Support Ryzen 3000/4000/5000"]),
        ("A520M-HDV", "ASRock", 820000, "AM4", "Micro-ATX, 2x DDR4, 1x M.2 NVMe, DVI/HDMI", ["Ekonomis AM4", "PCIe NVMe support"]),
        ("A520M-A PRO", "MSI", 860000, "AM4", "Micro-ATX, 2x DDR4, Audio Boost, Core Boost", ["Komponen militer tahan lama", "BIOS user-friendly"]),
        ("Prime A520M-K", "ASUS", 910000, "AM4", "Micro-ATX, 2x DDR4, 1x M.2 NVMe, 5X Protection III", ["Proteksi kelistrikan ASUS", "Stabil"]),
        ("A520M DS3H V2", "Gigabyte", 980000, "AM4", "Micro-ATX, 4x DDR4, 1x NVMe M.2, Q-Flash Plus", ["4 Slot RAM harga murah", "Q-Flash Plus update BIOS"]),
        ("B450M-HDV R4.0", "ASRock", 840000, "AM4", "Micro-ATX, 2x DDR4, 1x Ultra M.2, AMD B450", ["B450 harga murah", "Bisa tuning CPU"]),
        ("B450M PRO-VDH MAX", "MSI", 1050000, "AM4", "Micro-ATX, 4x DDR4, Turbo M.2, Heatsink VRM", ["4 Slot RAM", "VRM ada heatsink"]),
        ("B450M DS3H V2", "Gigabyte", 1020000, "AM4", "Micro-ATX, 4x DDR4, Realtek GbE, Audio Noise Guard", ["Populer sejuta umat", "4 Slot RAM"]),
        ("Prime B450M-A II", "ASUS", 1080000, "AM4", "Micro-ATX, 4x DDR4, BIOS FlashBack, Aura Sync", ["BIOS FlashBack mudah", "Komponen handal"]),
        ("B550M-HDV", "ASRock", 950000, "AM4", "Micro-ATX, PCIe 4.0 Support, 1x Hyper M.2", ["B550 termurah", "PCIe 4.0 kencang"]),
        ("B550M-A PRO", "MSI", 1150000, "AM4", "Micro-ATX, 2x DDR4, PCIe 4.0, Heatsink Chipset", ["Stabil untuk Ryzen 5 5600", "PCIe Gen 4"]),
        ("B550M PRO-VDH WiFi", "MSI", 1450000, "AM4", "Micro-ATX, 4x DDR4, 2x M.2, WiFi & Bluetooth", ["WiFi bawaan", "VRM heatsink tebal"]),
        ("B550M Pro4", "ASRock", 1420000, "AM4", "Micro-ATX, 4x DDR4, Dual M.2, Desain Putih Silver", ["VRM 8 phase Dr.MOS", "Desain silver estetik"]),
        ("B550M DS3H AC", "Gigabyte", 1380000, "AM4", "Micro-ATX, 4x DDR4, Built-in AC WiFi, Dual M.2", ["WiFi AC bawaan", "Q-Flash Plus"]),
        ("Prime B550M-A WiFi II", "ASUS", 1680000, "AM4", "Micro-ATX, 4x DDR4, WiFi 6, 2x M.2, Aura Sync", ["WiFi 6 kencang", "Aura Sync RGB"]),
        ("CVN B550M GAMING FROZEN V14", "Colorful", 1550000, "AM4", "Micro-ATX, Desain Full White Putih, 4x DDR4, PCIe 4.0", ["Full putih salju estetik", "VRM dingin"]),
        ("B550 Phantom Gaming 4", "ASRock", 1580000, "AM4", "ATX Penuh, 4x DDR4, Dual PCIe 4.0, Nahimic Audio", ["Form factor ATX gagah", "Jalur ekspansi lega"]),
        ("TUF GAMING B550M-PLUS WiFi II", "ASUS", 2150000, "AM4", "Micro-ATX, 4x DDR4, WiFi 6, 2.5Gb LAN, Aura Sync", ["Komponen militer TUF", "Audio Realtek premium"]),
        ("B550 AORUS ELITE V2", "Gigabyte", 2350000, "AM4", "ATX, 12+2 Phase Digital VRM, Dual M.2 Shield", ["VRM dingin untuk Ryzen 7 & 9", "ATX gagah"]),
        ("MPG B550 GAMING PLUS", "MSI", 2450000, "AM4", "ATX, Heatsink Tebal Extended, Flash BIOS Button", ["Desain hitam elegan", "Performa gaming stabil"]),
        ("ROG STRIX B550-F GAMING WiFi II", "ASUS", 3150000, "AM4", "ATX, 14 Power Stages, WiFi 6E, SupremeFX Audio", ["Papan ATX gagah", "Audio kelas audiophile"]),

        # AM5
        ("A620M-HDV/M.2+", "ASRock", 1320000, "AM5", "Micro-ATX, 2x DDR5 Slot, Hyper M.2 PCIe 4.0", ["Ekonomis AM5 DDR5", "Kuat Ryzen 5 7500F"]),
        ("Prime A620M-K", "ASUS", 1420000, "AM5", "Micro-ATX, 2x DDR5, 1x M.2 PCIe 4.0, 5X Protection", ["Kualitas ASUS", "DDR5 support"]),
        ("PRO A620M-E", "MSI", 1390000, "AM5", "Micro-ATX, 2x DDR5, Core Boost, Audio Boost", ["MSI hemat AM5", "BIOS stabil"]),
        ("A620M GAMING X", "Gigabyte", 1650000, "AM5", "Micro-ATX, 4x DDR5 Slot, VRM Heatsink, Q-Flash Plus", ["4 Slot RAM DDR5", "Heatsink VRM"]),
        ("B650M-HDV/M.2", "ASRock", 1850000, "AM5", "Micro-ATX, VRM 8+2+1 Dr.MOS, 1x Blazing M.2 Gen5", ["Best value B650", "Support M.2 PCIe Gen 5"]),
        ("B650M GAMING PLUS WIFI", "Gigabyte", 2350000, "AM5", "Micro-ATX, 4x DDR5, WiFi 6, 2.5Gb LAN, PCIe 4.0", ["WiFi 6", "VRM dingin", "4 Slot RAM"]),
        ("PRO B650M-A WiFi", "MSI", 2450000, "AM5", "Micro-ATX, 4x DDR5 Slot, WiFi 6E, 2x M.2", ["Fitur lengkap", "WiFi 6E kencang"]),
        ("B650M Pro RS WiFi White", "ASRock", 2490000, "AM5", "Micro-ATX, 4x DDR5, Desain Putih Silver, WiFi 6E", ["Tema putih salju estetik", "VRM Dr.MOS"]),
        ("B650M DS3H", "Gigabyte", 2050000, "AM5", "Micro-ATX, 4x DDR5, Dual M.2 PCIe 4.0, 2.5GbE", ["VRM 6+2+1 phase", "Koneksi LAN 2.5G"]),
        ("CVN B650M GAMING FROZEN V14 White", "Colorful", 2350000, "AM5", "Micro-ATX, Full White PCB, WiFi 6, Dual Gen 5 M.2", ["Desain putih salju murni", "Support Gen 5"]),
        ("TUF GAMING B650M-PLUS WiFi", "ASUS", 3250000, "AM5", "Micro-ATX, 12+2 Power Stages, PCIe 5.0, WiFi 6", ["VRM kuat untuk Ryzen 7 & 9", "Desain TUF"]),
        ("B650 EAGLE AX", "Gigabyte", 2850000, "AM5", "ATX, 12+2+2 Phases, WiFi 6E, 3x M.2 Slots", ["Papan ATX harga bersahabat", "3 Slot M.2"]),
        ("B650 GAMING PLUS WIFI", "MSI", 2950000, "AM5", "ATX Penuh, 4x DDR5, WiFi 6E, Audio 7.1 HD", ["Form factor ATX", "Konektivitas melimpah"]),
        ("B650 AORUS ELITE AX", "Gigabyte", 3850000, "AM5", "ATX, 14+2+1 Phase, WiFi 6E, PCIe 5.0 M.2", ["Ukuran ATX gagah", "Thermal armor luas"]),
        ("B650 AORUS ELITE AX ICE (Full White)", "Gigabyte", 4150000, "AM5", "ATX Full White PCB, 14+2+1 Phase, WiFi 6E", ["Full White PCB estetik tinggi", "PCIe 5.0"]),
        ("MAG B650 TOMAHAWK WIFI", "MSI", 3950000, "AM5", "ATX, 14+2+1 Duet Rail, WiFi 6E, Audio ALC4080", ["Papan hitam legendaris", "Audio premium"]),
        ("ROG STRIX B650-A GAMING WIFI White", "ASUS", 4750000, "AM5", "ATX, Desain Putih Silver Mewah, WiFi 6E, USB 3.2 Gen 2x2", ["Estetika putih flagship", "SupremeFX"]),
        ("ROG STRIX B650E-F GAMING WIFI", "ASUS", 5350000, "AM5", "ATX, Chipset B650E (PCIe 5.0 x16 + M.2), WiFi 6E", ["PCIe Gen 5 GPU & SSD", "VRM 12+2"]),
        ("X670E GAMING PLUS WIFI", "MSI", 4650000, "AM5", "ATX, Chipset X670E, PCIe 5.0 x16, 4x M.2", ["Chipset X670E jalur PCIe melimpah", "Overclocking"]),
        ("X670 AORUS ELITE AX", "Gigabyte", 5250000, "AM5", "ATX, 16+2+2 Twin Digital VRM, 4x M.2, WiFi 6E", ["16 Phase VRM siap Ryzen 9", "Konektivitas luas"]),
        ("ROG CROSSHAIR X670E HERO", "ASUS", 9850000, "AM5", "ATX Flagship, 18+2 Power Stages, USB4, Polymo Lighting", ["Puncak motherboard AM5", "Fitur ekstrim"]),
        ("ROG CROSSHAIR X870E HERO", "ASUS", 11500000, "AM5", "ATX Next-Gen, WiFi 7, Dual USB4 40Gbps, SlimSAS", ["Flagship generasi terbaru X870E", "WiFi 7"]),

        # LGA1200
        ("H410M-H V2", "Gigabyte", 790000, "LGA1200", "Micro-ATX, 2x DDR4, 1x NVMe M.2, HDMI/VGA", ["Budget termurah Gen 10", "Stabil"]),
        ("H510M-HDV/M.2", "ASRock", 880000, "LGA1200", "Micro-ATX, 2x DDR4, 1x Ultra M.2, DVI/HDMI", ["Ekonomis Gen 10 & 11", "M.2 PCIe 3.0"]),
        ("Prime H510M-K", "ASUS", 930000, "LGA1200", "Micro-ATX, 2x DDR4, 1x M.2, 5X Protection III", ["Proteksi ASUS", "Pilihan kantor"]),
        ("H510M-A PRO", "MSI", 910000, "LGA1200", "Micro-ATX, 2x DDR4, Turbo M.2, Core Boost", ["MSI H510 stabil", "Audio Boost"]),
        ("B560M PRO-E", "MSI", 1150000, "LGA1200", "Micro-ATX, 2x DDR4, PCIe 4.0 Support Gen 11, Core Boost", ["Mendukung PCIe Gen 4", "B560 ekonomis"]),
        ("B560M DS3H V2", "Gigabyte", 1350000, "LGA1200", "Micro-ATX, 4x DDR4, Dual M.2, RGB Fusion", ["4 Slot RAM", "Bisa RAM XMP tinggi"]),
        ("TUF GAMING B560M-PLUS", "ASUS", 1750000, "LGA1200", "Micro-ATX, 4x DDR4, 8+1 Dr.MOS, 2.5Gb LAN", ["Komponen militer", "VRM tebal"]),

        # LGA1700
        ("PRO H610M-E DDR4", "MSI", 950000, "LGA1700", "Micro-ATX, 2x DDR4 Slot, 1x M.2 NVMe, Core Boost", ["Paling ekonomis untuk i3 & i5", "BIOS stabil"]),
        ("Prime H610M-K D4", "ASUS", 1020000, "LGA1700", "Micro-ATX, 2x DDR4, 1x M.2 NVMe, Fan Xpert", ["Kualitas komponen ASUS", "Proteksi 5X III"]),
        ("H610M H V2 DDR4", "Gigabyte", 980000, "LGA1700", "Micro-ATX, 2x DDR4, NVMe PCIe 3.0, Smart Fan 6", ["Suhu stabil", "Harga bersahabat"]),
        ("H610M-HDV/M.2 D4", "ASRock", 940000, "LGA1700", "Micro-ATX, 2x DDR4, 1x Hyper M.2 PCIe 3.0, HDMI", ["Pilihan budget gaming", "PCIe Gen3 NVMe"]),
        ("B760M-HDV/M.2 D4", "ASRock", 1350000, "LGA1700", "Micro-ATX, 2x DDR4, 2x Hyper M.2, Gen 14 Ready", ["B760 termurah", "2 Slot NVMe"]),
        ("B760M DS3H AX DDR4", "Gigabyte", 1850000, "LGA1700", "Micro-ATX, 4x DDR4, WiFi 6E, 2.5G LAN, 2x M.2", ["WiFi 6E terintegrasi", "4 Slot RAM"]),
        ("B760M Pro RS/D4 White", "ASRock", 1750000, "LGA1700", "Micro-ATX, 4x DDR4, Dual M.2 Heatsink, Putih", ["Estetika putih bersih", "VRM 7+1+1 Dr.MOS"]),
        ("B760M GAMING PLUS WIFI DDR4", "MSI", 2150000, "LGA1700", "Micro-ATX, 4x DDR4, WiFi 6E, Heatsink VRM", ["Konektivitas WiFi 6E", "VRM adem"]),
        ("Prime B760M-A WiFi D4", "ASUS", 2250000, "LGA1700", "Micro-ATX, 4x DDR4, WiFi 6, 2x M.2 PCIe 4.0", ["Kualitas ASUS Prime", "WiFi 6 bawaan"]),
        ("TUF GAMING B760M-PLUS WIFI D4", "ASUS", 2650000, "LGA1700", "Micro-ATX, 4x DDR4, 12+1 Dr.MOS, WiFi 6", ["Kelas militer", "Audio DTS"]),
        ("CVN B760M FROZEN WIFI D4 White", "Colorful", 2150000, "LGA1700", "Micro-ATX, Full White PCB & Armor, WiFi 6, 3x M.2", ["Full putih salju", "3 Slot M.2"]),
        ("B760M GAMING PLUS WIFI DDR5", "MSI", 2350000, "LGA1700", "Micro-ATX, 4x DDR5 Slot, WiFi 6E, Extended Heatsink", ["DDR5 bersahabat", "VRM dingin"]),
        ("B760 GAMING PLUS WIFI DDR5", "MSI", 2650000, "LGA1700", "ATX, 4x DDR5 Slot (Up to 6800MHz), WiFi 6E", ["DDR5 & ATX besar", "Ideal untuk i5/i7"]),
        ("TUF GAMING B760M-PLUS WIFI DDR5", "ASUS", 3150000, "LGA1700", "Micro-ATX, 12+1 Dr.MOS, DDR5, PCIe 5.0", ["Siap angkat Core i7", "DDR5 kencang"]),
        ("B760 AORUS ELITE AX DDR5", "Gigabyte", 3450000, "LGA1700", "ATX, 12+1+1 Twin Hybrid, WiFi 6E, 3x M.2", ["Ukuran ATX gagah", "3 Slot M.2 heatsink"]),
        ("B760 AORUS ELITE AX ICE DDR5 White", "Gigabyte", 3650000, "LGA1700", "ATX Full White PCB, WiFi 6E, PCIe 4.0 x16", ["Seri ICE Full White", "Komponen elit"]),
        ("ROG STRIX B760-A GAMING WIFI D4 White", "ASUS", 3750000, "LGA1700", "ATX, Desain Putih Perak Mewah, WiFi 6E", ["Desain putih ikonik ROG", "SupremeFX"]),
        ("ROG STRIX B760-F GAMING WIFI DDR5", "ASUS", 4450000, "LGA1700", "ATX, 16+1 Power Stages, DDR5 7800+ OC, PCIe 5.0", ["Papan gaming kelas atas", "Audio ROG SupremeFX"]),
        ("PRO Z790-P WIFI DDR5", "MSI", 3650000, "LGA1700", "ATX, Chipset Z790, 4x DDR5, WiFi 6E, PCIe 5.0", ["Z790 entry level", "Bisa overclock CPU K-series"]),
        ("Prime Z790-P WiFi DDR5", "ASUS", 3950000, "LGA1700", "ATX, 14+1 Dr.MOS, 3x M.2, WiFi 6, PCIe 5.0", ["Z790 kualitas ASUS", "Aura Sync"]),
        ("Z790 GAMING PLUS WIFI DDR5", "MSI", 3950000, "LGA1700", "ATX, 14+1+1 Duet Rail, 4x M.2 PCIe 4.0, WiFi 6E", ["VRM tebal siap i7 K-series", "4 Slot M.2"]),
        ("Z790 AORUS ELITE AX DDR5", "Gigabyte", 4550000, "LGA1700", "ATX, 16+2+1 Twin Digital, PCIe 5.0, WiFi 6E", ["VRM monster 16 Phase", "Thermal Guard"]),
        ("Prime Z790-A WiFi DDR5 White/Silver", "ASUS", 4650000, "LGA1700", "ATX, 16+1 Dr.MOS, 4x M.2, WiFi 6E, Putih Perak", ["Estetika silver elegan", "Fitur AI Overclocking"]),
        ("MAG Z790 TOMAHAWK WIFI DDR5", "MSI", 4450000, "LGA1700", "ATX, 16+1+1 Mirrored Power, DDR5, 4x M.2", ["Papan hitam legendaris", "VRM tebal siap i9"]),
        ("ROG STRIX Z790-A GAMING WIFI II DDR5 White", "ASUS", 6250000, "LGA1700", "ATX, 16+1 Power Stages, WiFi 7, Desain Putih Perak", ["WiFi 7 terbaru", "Tema putih mewah"]),
        ("ROG MAXIMUS Z790 DARK HERO", "ASUS", 10850000, "LGA1700", "ATX Flagship, 20+1+2 Stages, PCIe 5.0, WiFi 7", ["Puncak overclocking Intel", "Fitur sultan"])
    ]

    for name, brand, price, socket, spec, pros in mobo_list:
        components.append({
            "id": f"MB-{len(components)+1:03d}",
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

    # -------------------------------------------------------------------------
    # 3. RAM (MEMORY) - 65 Items
    # -------------------------------------------------------------------------
    ram_list = [
        # DDR4 Single & Kits
        ("Team Elite Plus 8GB DDR4 3200MHz Black", "TeamGroup", 265000, "DDR4", "Single Channel 8GB 3200MHz CL22"),
        ("Kingston FURY Beast 8GB DDR4 3200MHz Black", "Kingston", 310000, "DDR4", "Single Channel 8GB 3200MHz CL16"),
        ("Corsair Vengeance LPX 8GB DDR4 3200MHz Black", "Corsair", 335000, "DDR4", "Single Channel 8GB 3200MHz CL16"),
        ("ADATA XPG GAMMIX D30 8GB DDR4 3200MHz", "ADATA", 295000, "DDR4", "Single Channel 8GB 3200MHz CL16 Heatsink Merah"),
        ("Klevv Bolt X 8GB DDR4 3200MHz", "Klevv", 290000, "DDR4", "Single Channel 8GB 3200MHz CL16 Low Profile"),
        ("Team Elite Plus 16GB (2x8GB) DDR4 3200MHz", "TeamGroup", 520000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz CL22"),
        ("Kingston FURY Beast 16GB (2x8GB) DDR4 3200MHz", "Kingston", 585000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz CL16"),
        ("Kingston FURY Beast White 16GB (2x8GB) DDR4 3200MHz", "Kingston", 610000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz Putih"),
        ("Kingston FURY Beast RGB 16GB (2x8GB) DDR4 3200MHz", "Kingston", 685000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz CL16 RGB"),
        ("Kingston FURY Beast RGB White 16GB (2x8GB) DDR4 3200MHz", "Kingston", 710000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz CL16 RGB White"),
        ("Corsair Vengeance LPX 16GB (2x8GB) DDR4 3200MHz", "Corsair", 625000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz CL16 Black"),
        ("Corsair Vengeance LPX White 16GB (2x8GB) DDR4 3200MHz", "Corsair", 645000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz Putih"),
        ("Corsair Vengeance RGB PRO 16GB (2x8GB) DDR4 3200MHz Black", "Corsair", 785000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz RGB"),
        ("Corsair Vengeance RGB PRO 16GB (2x8GB) DDR4 3200MHz White", "Corsair", 815000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz RGB White"),
        ("Corsair Vengeance RGB RS 16GB (2x8GB) DDR4 3200MHz", "Corsair", 745000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz Compact RGB"),
        ("Team T-Force Delta RGB 16GB (2x8GB) DDR4 3200MHz Black", "TeamGroup", 695000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz RGB"),
        ("Team T-Force Delta RGB 16GB (2x8GB) DDR4 3200MHz White", "TeamGroup", 715000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz RGB White"),
        ("Team T-Force Delta RGB 16GB (2x8GB) DDR4 3600MHz Black", "TeamGroup", 745000, "DDR4", "Dual Channel 16GB (2x8GB) 3600MHz CL18 RGB"),
        ("Team T-Force Delta RGB 16GB (2x8GB) DDR4 3600MHz White", "TeamGroup", 765000, "DDR4", "Dual Channel 16GB (2x8GB) 3600MHz CL18 RGB White"),
        ("Team T-Create Expert 16GB (2x8GB) DDR4 3200MHz", "TeamGroup", 620000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz CL16 Silver"),
        ("Team T-Create Expert 32GB (2x16GB) DDR4 3200MHz", "TeamGroup", 1150000, "DDR4", "Dual Channel 32GB (2x16GB) 3200MHz CL16 Silver"),
        ("G.Skill Ripjaws V 16GB (2x8GB) DDR4 3200MHz", "G.Skill", 645000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz CL16"),
        ("G.Skill Ripjaws V 16GB (2x8GB) DDR4 3600MHz", "G.Skill", 695000, "DDR4", "Dual Channel 16GB (2x8GB) 3600MHz CL18 Classic"),
        ("G.Skill Trident Z RGB 16GB (2x8GB) DDR4 3200MHz", "G.Skill", 875000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz CL16 RGB"),
        ("G.Skill Trident Z RGB 16GB (2x8GB) DDR4 3600MHz", "G.Skill", 925000, "DDR4", "Dual Channel 16GB (2x8GB) 3600MHz CL18 RGB Mewah"),
        ("G.Skill Trident Z Neo 16GB (2x8GB) DDR4 3600MHz (AMD)", "G.Skill", 985000, "DDR4", "Dual Channel 16GB (2x8GB) 3600MHz CL16 Dioptimasi Ryzen"),
        ("ADATA XPG SPECTRIX D50 16GB (2x8GB) DDR4 3200MHz Grey", "ADATA", 665000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz RGB"),
        ("ADATA XPG SPECTRIX D50 White 16GB (2x8GB) DDR4 3200MHz", "ADATA", 685000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz RGB White"),
        ("Klevv Cras X RGB 16GB (2x8GB) DDR4 3200MHz", "Klevv", 710000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz Kristal Gem RGB"),
        ("PNY XLR8 Gaming EPIC-X RGB 16GB (2x8GB) DDR4 3200MHz", "PNY", 675000, "DDR4", "Dual Channel 16GB (2x8GB) 3200MHz RGB"),
        ("Kingston FURY Beast 32GB (2x16GB) DDR4 3200MHz", "Kingston", 1120000, "DDR4", "Dual Channel 32GB (2x16GB) 3200MHz CL16"),
        ("Kingston FURY Beast RGB 32GB (2x16GB) DDR4 3200MHz", "Kingston", 1290000, "DDR4", "Dual Channel 32GB (2x16GB) 3200MHz RGB"),
        ("Corsair Vengeance LPX 32GB (2x16GB) DDR4 3200MHz", "Corsair", 1180000, "DDR4", "Dual Channel 32GB (2x16GB) 3200MHz CL16"),
        ("Corsair Vengeance LPX 32GB (2x16GB) DDR4 3600MHz", "Corsair", 1260000, "DDR4", "Dual Channel 32GB (2x16GB) 3600MHz CL18"),
        ("Corsair Vengeance RGB PRO 32GB (2x16GB) DDR4 3600MHz White", "Corsair", 1490000, "DDR4", "Dual Channel 32GB (2x16GB) 3600MHz RGB White"),
        ("Team T-Force Delta RGB 32GB (2x16GB) DDR4 3600MHz White", "TeamGroup", 1380000, "DDR4", "Dual Channel 32GB (2x16GB) 3600MHz RGB White"),
        ("Kingston FURY Beast 64GB (2x32GB) DDR4 3200MHz", "Kingston", 2150000, "DDR4", "Dual Channel 64GB (2x32GB) 3200MHz CL16"),
        ("Corsair Vengeance LPX 64GB (2x32GB) DDR4 3200MHz", "Corsair", 2280000, "DDR4", "Dual Channel 64GB (2x32GB) 3200MHz CL16"),

        # DDR5 Single & Kits
        ("Crucial 16GB (2x8GB) DDR5 4800MHz JEDEC", "Crucial", 780000, "DDR5", "Dual Channel 16GB (2x8GB) 4800MHz Standard"),
        ("Kingston FURY Beast 16GB (2x8GB) DDR5 5200MHz", "Kingston", 950000, "DDR5", "Dual Channel 16GB (2x8GB) 5200MHz CL40 XMP/EXPO"),
        ("Kingston FURY Beast 16GB (2x8GB) DDR5 5600MHz", "Kingston", 1050000, "DDR5", "Dual Channel 16GB (2x8GB) 5600MHz CL40"),
        ("Team T-Force Vulcan 16GB (2x8GB) DDR5 5600MHz Black", "TeamGroup", 920000, "DDR5", "Dual Channel 16GB (2x8GB) 5600MHz CL36"),
        ("Team T-Force Vulcan 16GB (2x8GB) DDR5 6000MHz Black", "TeamGroup", 1080000, "DDR5", "Dual Channel 16GB (2x8GB) 6000MHz CL38"),
        ("Corsair Vengeance 16GB (2x8GB) DDR5 5200MHz Black", "Corsair", 980000, "DDR5", "Dual Channel 16GB (2x8GB) 5200MHz CL40"),
        ("Kingston FURY Beast 32GB (2x16GB) DDR5 5600MHz", "Kingston", 1580000, "DDR5", "Dual Channel 32GB (2x16GB) 5600MHz CL40"),
        ("Kingston FURY Beast RGB 32GB (2x16GB) DDR5 5600MHz White", "Kingston", 1790000, "DDR5", "Dual Channel 32GB (2x16GB) 5600MHz RGB White"),
        ("Kingston FURY Beast 32GB (2x16GB) DDR5 6000MHz AMD EXPO", "Kingston", 1750000, "DDR5", "Dual Channel 32GB (2x16GB) 6000MHz CL36 EXPO"),
        ("Kingston FURY Renegade RGB 32GB (2x16GB) DDR5 6400MHz Silver", "Kingston", 2450000, "DDR5", "Dual Channel 32GB (2x16GB) 6400MHz CL32 Silver RGB"),
        ("Corsair Vengeance 32GB (2x16GB) DDR5 6000MHz Black", "Corsair", 1750000, "DDR5", "Dual Channel 32GB (2x16GB) 6000MHz CL36 AMD EXPO"),
        ("Corsair Vengeance White 32GB (2x16GB) DDR5 6000MHz", "Corsair", 1790000, "DDR5", "Dual Channel 32GB (2x16GB) 6000MHz CL36 Putih"),
        ("Corsair Vengeance RGB 32GB (2x16GB) DDR5 6000MHz Black", "Corsair", 1920000, "DDR5", "Dual Channel 32GB (2x16GB) 6000MHz CL36 RGB"),
        ("Corsair Vengeance RGB 32GB (2x16GB) DDR5 6000MHz White", "Corsair", 1950000, "DDR5", "Dual Channel 32GB (2x16GB) 6000MHz CL36 RGB White"),
        ("Corsair Dominator Titanium 32GB (2x16GB) DDR5 6000MHz White", "Corsair", 2850000, "DDR5", "Dual Channel 32GB (2x16GB) 6000MHz CL30 Flagship"),
        ("Team T-Force Delta RGB 32GB (2x16GB) DDR5 6000MHz Black", "TeamGroup", 1820000, "DDR5", "Dual Channel 32GB (2x16GB) 6000MHz CL38 RGB Black"),
        ("Team T-Force Delta RGB 32GB (2x16GB) DDR5 6000MHz White", "TeamGroup", 1850000, "DDR5", "Dual Channel 32GB (2x16GB) 6000MHz CL38 RGB White"),
        ("Team T-Create Expert 32GB (2x16GB) DDR5 6000MHz White", "TeamGroup", 1720000, "DDR5", "Dual Channel 32GB (2x16GB) 6000MHz CL30 Low Profile"),
        ("G.Skill Ripjaws S5 32GB (2x16GB) DDR5 6000MHz CL32", "G.Skill", 1880000, "DDR5", "Dual Channel 32GB (2x16GB) 6000MHz CL32 Low Profile"),
        ("G.Skill Flare X5 32GB (2x16GB) DDR5 6000MHz CL30 (AMD EXPO)", "G.Skill", 1950000, "DDR5", "Dual Channel 32GB (2x16GB) 6000MHz CL30 Sweet Spot AM5"),
        ("G.Skill Trident Z5 Neo RGB 32GB (2x16GB) DDR5 6000MHz CL30", "G.Skill", 2150000, "DDR5", "Dual Channel 32GB (2x16GB) 6000MHz CL30 AMD EXPO"),
        ("G.Skill Trident Z5 RGB 32GB (2x16GB) DDR5 6400MHz CL32 Silver", "G.Skill", 2350000, "DDR5", "Dual Channel 32GB (2x16GB) 6400MHz CL32 Intel XMP"),
        ("ADATA XPG Lancer Blade RGB 32GB (2x16GB) DDR5 6000MHz", "ADATA", 1780000, "DDR5", "Dual Channel 32GB (2x16GB) 6000MHz CL30 RGB"),
        ("Klevv Cras V RGB 32GB (2x16GB) DDR5 6000MHz Obsidian Black", "Klevv", 1890000, "DDR5", "Dual Channel 32GB (2x16GB) 6000MHz CL30 Desain Futuristik"),
        ("Corsair Vengeance 64GB (2x32GB) DDR5 5600MHz", "Corsair", 3250000, "DDR5", "Dual Channel 64GB (2x32GB) 5600MHz CL40"),
        ("Corsair Vengeance RGB 64GB (2x32GB) DDR5 6000MHz White", "Corsair", 3750000, "DDR5", "Dual Channel 64GB (2x32GB) 6000MHz CL30 RGB White"),
        ("G.Skill Trident Z5 RGB 64GB (2x32GB) DDR5 6000MHz CL30", "G.Skill", 3850000, "DDR5", "Dual Channel 64GB (2x32GB) 6000MHz CL30 Extreme Workstation")
    ]

    for name, brand, price, socket, spec in ram_list:
        components.append({
            "id": f"RAM-{len(components)+1:03d}",
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

    # -------------------------------------------------------------------------
    # 4. VGA / GPU - 85 Items
    # -------------------------------------------------------------------------
    gpu_list = [
        # NVIDIA GTX Entry
        ("MSI GeForce GTX 1650 VENTUS XS 4GB GDDR6", "MSI", 2150000, "NVIDIA", "4GB GDDR6, Dual Fan, TDP 75W, Tanpa Butuh Power Pin"),
        ("ASUS Phoenix GeForce GTX 1650 4GB GDDR6", "ASUS", 2190000, "NVIDIA", "4GB GDDR6, Single Axial-tech Fan, Ringkas"),
        ("Colorful GeForce GTX 1650 NB 4GD6-V", "Colorful", 2050000, "NVIDIA", "4GB GDDR6, Dual 90mm Fan Battle-Ax"),
        ("Galax GeForce GTX 1650 EX PLUS 4GB GDDR6", "Galax", 2120000, "NVIDIA", "4GB GDDR6, Dual Fan 80mm, 1-Click OC"),
        ("ZOTAC Gaming GeForce GTX 1660 SUPER 6GB GDDR6", "ZOTAC", 2750000, "NVIDIA", "6GB GDDR6 192-bit, Dual Fan IceStorm 2.0"),
        ("ASUS TUF Gaming GeForce GTX 1660 SUPER 6GB", "ASUS", 2950000, "NVIDIA", "6GB GDDR6, Dual Fan, Komponen Militer"),
        ("MSI GeForce GTX 1660 SUPER VENTUS XS 6GB OC", "MSI", 2890000, "NVIDIA", "6GB GDDR6, TORX Fan 2.0, Heatsink Tembaga"),
        ("Galax GeForce GTX 1660 SUPER 6GB 1-Click OC", "Galax", 2690000, "NVIDIA", "6GB GDDR6 192-bit, Dual 90mm Fan"),

        # NVIDIA RTX 30 Series
        ("Palit GeForce RTX 3050 StormX 6GB GDDR6", "Palit", 2750000, "NVIDIA", "6GB GDDR6 96-bit, TDP 70W Hemat Daya Ekstrem"),
        ("MSI GeForce RTX 3050 VENTUS 2X 6G OC", "MSI", 2890000, "NVIDIA", "6GB GDDR6, Dual Fan, Tanpa Butuh Kabel Power 8-Pin"),
        ("ZOTAC Gaming GeForce RTX 3050 Twin Edge 8GB", "ZOTAC", 3350000, "NVIDIA", "8GB GDDR6, Ray Tracing, DLSS 2, Dual Fan"),
        ("ASUS Dual GeForce RTX 3050 OC 8GB GDDR6", "ASUS", 3450000, "NVIDIA", "8GB GDDR6, Axial-tech Fan, 0dB Technology"),
        ("MSI GeForce RTX 3050 VENTUS 2X 8GB OC", "MSI", 3390000, "NVIDIA", "8GB GDDR6, TORX Fan 3.0, Dual Fan"),
        ("Colorful GeForce RTX 3050 NB DUO 8GB-V", "Colorful", 3250000, "NVIDIA", "8GB GDDR6, Desain Merah Hitam BattleAx"),
        ("Galax GeForce RTX 3050 EX 8GB GDDR6", "Galax", 3350000, "NVIDIA", "8GB GDDR6, Dual 92mm Fan, RGB Wings"),
        ("ZOTAC Gaming GeForce RTX 3060 Twin Edge 12GB", "ZOTAC", 4450000, "NVIDIA", "12GB GDDR6 192-bit, VRAM Besar untuk 3D"),
        ("MSI GeForce RTX 3060 VENTUS 2X 12GB OC", "MSI", 4550000, "NVIDIA", "12GB GDDR6 192-bit, Desain Dual Fan Minimalis"),
        ("ASUS Dual GeForce RTX 3060 OC Edition 12GB", "ASUS", 4650000, "NVIDIA", "12GB GDDR6, Axial-tech Fan, Backplate Metal"),
        ("Gigabyte GeForce RTX 3060 WINDFORCE OC 12GB", "Gigabyte", 4590000, "NVIDIA", "12GB GDDR6, Windforce 2X, Alternate Spinning"),
        ("Colorful iGame GeForce RTX 3060 Ultra W OC 12GB White", "Colorful", 4850000, "NVIDIA", "12GB GDDR6, Tema Putih Hologram Pop-Art"),
        ("Galax GeForce RTX 3060 1-Click OC 12GB", "Galax", 4390000, "NVIDIA", "12GB GDDR6 192-bit, 1-Click Overclocking"),
        ("Inno3D GeForce RTX 3060 Twin X2 12GB", "Inno3D", 4350000, "NVIDIA", "12GB GDDR6, Dual Slot Kompak"),
        ("Colorful iGame GeForce RTX 3060 Ti Ultra W OC GDDR6X 8GB", "Colorful", 5450000, "NVIDIA", "8GB GDDR6X Kencang, Triple Fan Putih"),
        ("Galax GeForce RTX 3060 Ti Plus 8GB GDDR6X", "Galax", 5350000, "NVIDIA", "8GB GDDR6X Kencang, Dual Fan 102mm"),

        # NVIDIA RTX 40 Series
        ("Inno3D GeForce RTX 4060 Twin X2 8GB", "Inno3D", 4650000, "NVIDIA", "8GB GDDR6, DLSS 3 Frame Gen, Kompak Dual Slot"),
        ("Palit GeForce RTX 4060 Dual 8GB", "Palit", 4690000, "NVIDIA", "8GB GDDR6, Dual 95mm Fan, 0dB Tech"),
        ("ZOTAC Gaming GeForce RTX 4060 Twin Edge 8GB", "ZOTAC", 4750000, "NVIDIA", "8GB GDDR6, Desain Kompak, IceStorm 2.0"),
        ("MSI GeForce RTX 4060 VENTUS 2X Black 8GB OC", "MSI", 4850000, "NVIDIA", "8GB GDDR6, TORX Fan 4.0, Zero Frozr"),
        ("MSI GeForce RTX 4060 VENTUS 2X White 8GB OC", "MSI", 4950000, "NVIDIA", "8GB GDDR6, Desain Full Putih Elegan"),
        ("Gigabyte GeForce RTX 4060 WINDFORCE OC 8GB", "Gigabyte", 4880000, "NVIDIA", "8GB GDDR6, Dual Windforce Fan, Screen Cooling"),
        ("ASUS Dual GeForce RTX 4060 V2 OC 8GB", "ASUS", 4950000, "NVIDIA", "8GB GDDR6, DLSS 3 Frame Gen, Dual Fan Axial"),
        ("ASUS Dual GeForce RTX 4060 White OC 8GB", "ASUS", 5150000, "NVIDIA", "8GB GDDR6, Full White Fan & Shroud"),
        ("Galax GeForce RTX 4060 1-Click OC 2X 8GB", "Galax", 4750000, "NVIDIA", "8GB GDDR6, Dual Fan, Backplate Metal"),
        ("Gigabyte GeForce RTX 4060 EAGLE OC 8GB (Triple Fan)", "Gigabyte", 5250000, "NVIDIA", "8GB GDDR6, 3x Kipas Ekstra Dingin, RGB Fusion"),
        ("Colorful iGame GeForce RTX 4060 Ultra W OC 8GB White", "Colorful", 5350000, "NVIDIA", "8GB GDDR6, Desain Hologram Pop-Art Putih Mewah"),
        ("ASUS TUF Gaming GeForce RTX 4060 OC 8GB", "ASUS", 5650000, "NVIDIA", "8GB GDDR6, Bodi Aluminium TUF, Triple Fan"),
        ("ROG Strix GeForce RTX 4060 OC 8GB", "ASUS", 6150000, "NVIDIA", "8GB GDDR6, Pendingin Triple Fan Monster ROG"),
        ("Palit GeForce RTX 4060 Ti Dual 8GB", "Palit", 6450000, "NVIDIA", "8GB GDDR6, DLSS 3, Dual Fan"),
        ("MSI GeForce RTX 4060 Ti VENTUS 2X Black 8GB OC", "MSI", 6650000, "NVIDIA", "8GB GDDR6, Desain Ramping Kompak"),
        ("MSI GeForce RTX 4060 Ti VENTUS 2X White 8GB OC", "MSI", 6750000, "NVIDIA", "8GB GDDR6, Varian Putih Bersih"),
        ("ASUS Dual GeForce RTX 4060 Ti OC 8GB", "ASUS", 6750000, "NVIDIA", "8GB GDDR6, DLSS 3, 4352 CUDA Cores"),
        ("Gigabyte GeForce RTX 4060 Ti GAMING OC 8GB", "Gigabyte", 7150000, "NVIDIA", "8GB GDDR6, Triple Fan Windforce, Dual BIOS"),
        ("ZOTAC Gaming GeForce RTX 4060 Ti Twin Edge 8GB", "ZOTAC", 6550000, "NVIDIA", "8GB GDDR6, IceStorm 2.0"),
        ("Colorful iGame GeForce RTX 4060 Ti Ultra W DUO 16GB", "Colorful", 8350000, "NVIDIA", "16GB GDDR6 Raksasa, Desain Putih Hologram"),
        ("MSI GeForce RTX 4060 Ti GAMING X SLIM 16GB", "MSI", 8450000, "NVIDIA", "16GB GDDR6, Desain Slim Mewah, Twin Frozr 9"),
        ("Gigabyte GeForce RTX 4060 Ti GAMING OC 16GB", "Gigabyte", 8550000, "NVIDIA", "16GB GDDR6, Triple Fan Windforce"),
        ("ASUS TUF Gaming GeForce RTX 4060 Ti OC 8GB", "ASUS", 7450000, "NVIDIA", "8GB GDDR6, Komponen Militer TUF"),
        ("Inno3D GeForce RTX 4070 Twin X2 12GB", "Inno3D", 9850000, "NVIDIA", "12GB GDDR6X, DLSS 3, Dual Fan Kompak"),
        ("MSI GeForce RTX 4070 SUPER 12G VENTUS 2X OC", "MSI", 10650000, "NVIDIA", "12GB GDDR6X, Desain Kompak Dual Fan"),
        ("MSI GeForce RTX 4070 SUPER 12G VENTUS 2X White OC", "MSI", 10850000, "NVIDIA", "12GB GDDR6X, Full White Theme"),
        ("ASUS Dual GeForce RTX 4070 SUPER EVO OC 12GB", "ASUS", 10750000, "NVIDIA", "12GB GDDR6X, DLSS 3, Dual Fan Axial-tech"),
        ("ASUS Dual GeForce RTX 4070 SUPER White OC 12GB", "ASUS", 10950000, "NVIDIA", "12GB GDDR6X, Full White Edition"),
        ("Gigabyte GeForce RTX 4070 SUPER WINDFORCE OC 12GB", "Gigabyte", 10950000, "NVIDIA", "12GB GDDR6X, Triple Fan, Plat Tembaga Langsung"),
        ("Colorful iGame GeForce RTX 4070 SUPER Ultra W OC 12GB", "Colorful", 11450000, "NVIDIA", "12GB GDDR6X, Triple Fan Putih Hologram"),
        ("ASUS TUF Gaming GeForce RTX 4070 SUPER 12GB", "ASUS", 11650000, "NVIDIA", "12GB GDDR6X, Komponen Militer, Dual BIOS"),
        ("ZOTAC Gaming GeForce RTX 4070 Ti SUPER Trinity Black 16GB", "ZOTAC", 14450000, "NVIDIA", "16GB GDDR6X 256-bit, IceStorm 2.0 Triple Fan"),
        ("ZOTAC Gaming GeForce RTX 4070 Ti SUPER Trinity White 16GB", "ZOTAC", 14750000, "NVIDIA", "16GB GDDR6X, Varian Full White Melengkung"),
        ("MSI GeForce RTX 4070 Ti SUPER 16G GAMING X SLIM", "MSI", 15450000, "NVIDIA", "16GB GDDR6X, Tri Frozr 3, RGB Mystic Light"),
        ("Gigabyte GeForce RTX 4070 Ti SUPER AERO OC 16GB White", "Gigabyte", 15750000, "NVIDIA", "16GB GDDR6X, Seri AERO Silver Putih Kreator"),
        ("ASUS TUF Gaming GeForce RTX 4070 Ti SUPER 16GB", "ASUS", 15950000, "NVIDIA", "16GB GDDR6X, Bodi Metal Solid TUF"),
        ("MSI GeForce RTX 4080 SUPER 16G VENTUS 3X OC", "MSI", 18850000, "NVIDIA", "16GB GDDR6X 256-bit, Triple Fan, Monster 4K"),
        ("Gigabyte GeForce RTX 4080 SUPER GAMING OC 16GB", "Gigabyte", 19500000, "NVIDIA", "16GB GDDR6X, Windforce 3X, Halo RGB Fans"),
        ("ASUS TUF Gaming GeForce RTX 4080 SUPER 16GB", "ASUS", 19950000, "NVIDIA", "16GB GDDR6X, Pendingin Logam Tebal 3.65 Slot"),
        ("ASUS ROG Strix GeForce RTX 4080 SUPER OC 16GB", "ASUS", 21500000, "NVIDIA", "16GB GDDR6X, Desain ROG Cyberpunk Flagship"),
        ("MSI GeForce RTX 4090 GAMING X SLIM 24GB", "MSI", 33500000, "NVIDIA", "24GB GDDR6X 384-bit, Tri Frozr 3, Monster AI"),
        ("ASUS TUF Gaming GeForce RTX 4090 OC 24GB", "ASUS", 34500000, "NVIDIA", "24GB GDDR6X, Bodi Logam TUF, Vapor Chamber"),
        ("ASUS ROG Strix GeForce RTX 4090 OC 24GB", "ASUS", 35500000, "NVIDIA", "24GB GDDR6X 384-bit, Vapor Chamber, Raja VGA Dunia"),

        # AMD Radeon
        ("Peladn AMD Radeon RX 580 8GB GDDR5 (2048SP)", "Peladn", 1150000, "AMD", "8GB GDDR5 256-bit, Dual Fan, Paling Murah 8GB"),
        ("AISURIX AMD Radeon RX 580 8GB GDDR5", "AISURIX", 1180000, "AMD", "8GB GDDR5 256-bit, Dual Fan Ice, Gaming 1080p Hemat"),
        ("ASRock AMD Radeon RX 6500 XT Phantom Gaming 4GB", "ASRock", 2150000, "AMD", "4GB GDDR6, Dual Fan, TDP 107W"),
        ("PowerColor Fighter AMD Radeon RX 6600 8GB", "PowerColor", 3090000, "AMD", "8GB GDDR6, Dual Fan Hening, 1080p Value"),
        ("ASRock AMD Radeon RX 6600 Challenger D 8GB", "ASRock", 3150000, "AMD", "8GB GDDR6 128-bit, PCIe 4.0, TDP 132W"),
        ("Sapphire PULSE AMD Radeon RX 6600 8GB", "Sapphire", 3250000, "AMD", "8GB GDDR6, Kualitas Komponen Sapphire"),
        ("XFX Speedster SWFT 210 AMD Radeon RX 6600 8GB", "XFX", 3190000, "AMD", "8GB GDDR6, Dual Fan Khas XFX Bersih"),
        ("XFX Speedster QICK 308 AMD Radeon RX 6650 XT 8GB", "XFX", 3850000, "AMD", "8GB GDDR6, Triple Fan Panjang Ekstra Dingin"),
        ("Sapphire PULSE AMD Radeon RX 7600 8GB", "Sapphire", 4450000, "AMD", "8GB GDDR6, RDNA 3 Arsitektur, FSR 3 Support"),
        ("ASRock AMD Radeon RX 7600 Challenger 8GB", "ASRock", 4350000, "AMD", "8GB GDDR6, Dual Fan Ring Fan"),
        ("ASRock AMD Radeon RX 7600 Steel Legend 8GB White", "ASRock", 4750000, "AMD", "8GB GDDR6, Triple Fan Putih Salju, ARGB"),
        ("Sapphire PULSE AMD Radeon RX 7600 XT 16GB", "Sapphire", 5850000, "AMD", "16GB GDDR6 VRAM Besar, Kuat Texturing Tinggi"),
        ("PowerColor Hellhound AMD Radeon RX 7600 XT 16GB", "PowerColor", 5950000, "AMD", "16GB GDDR6, Dual Fan LED Biru/Ungu"),
        ("PowerColor Fighter AMD Radeon RX 7700 XT 12GB", "PowerColor", 7450000, "AMD", "12GB GDDR6 192-bit, Triple Fan"),
        ("Sapphire PULSE AMD Radeon RX 7700 XT 12GB", "Sapphire", 7650000, "AMD", "12GB GDDR6 192-bit, RDNA 3, Dual-X"),
        ("ASRock AMD Radeon RX 7800 XT Challenger 16GB", "ASRock", 9450000, "AMD", "16GB GDDR6 256-bit, Ring Fan Dual"),
        ("PowerColor Hellhound AMD Radeon RX 7800 XT 16GB", "PowerColor", 9750000, "AMD", "16GB GDDR6, LED Biru/Ice Blue, Hening"),
        ("Sapphire NITRO+ AMD Radeon RX 7800 XT 16GB", "Sapphire", 9950000, "AMD", "16GB GDDR6, Tri-X Cooling, ARGB Bar"),
        ("Sapphire PULSE AMD Radeon RX 7900 GRE 16GB", "Sapphire", 10850000, "AMD", "16GB GDDR6 256-bit, Performa setara RTX 4070 Ti"),
        ("PowerColor Hellhound AMD Radeon RX 7900 GRE 16GB", "PowerColor", 11200000, "AMD", "16GB GDDR6, Dual BIOS, Kipas LED"),
        ("Sapphire NITRO+ AMD Radeon RX 7900 XTX Vapor-X 24GB", "Sapphire", 18950000, "AMD", "24GB GDDR6 384-bit, Vapor-X Chamber Raksasa"),
        ("PowerColor Red Devil AMD Radeon RX 7900 XTX 24GB", "PowerColor", 18500000, "AMD", "24GB GDDR6 384-bit, Monster 4K AMD Flagship"),

        # Intel Arc
        ("Sparkle Intel Arc A310 ECO 4GB GDDR6", "Sparkle", 1350000, "Intel", "4GB GDDR6 64-bit, Single Slot, AV1 Encoder Murah"),
        ("ASRock Intel Arc A380 Low Profile 6GB GDDR6", "Intel", 1750000, "Intel", "6GB GDDR6 96-bit, Low Profile, AV1 Encode"),
        ("ASRock Intel Arc A580 Challenger 8GB GDDR6", "Intel", 2950000, "Intel", "8GB GDDR6 256-bit, Dual Fan, AV1"),
        ("Sparkle Intel Arc A750 ORC OC 8GB GDDR6", "Sparkle", 3550000, "Intel", "8GB GDDR6 256-bit, Dual Fan Biru Metalik"),
        ("ASRock Intel Arc A750 Challenger D 8GB GDDR6", "Intel", 3650000, "Intel", "8GB GDDR6 256-bit, 3584 Xe Cores"),
        ("Acer Predator BiFrost Intel Arc A770 16GB OC", "Intel", 5450000, "Intel", "16GB GDDR6 256-bit, Dual Fan Hybrid")
    ]

    for name, brand, price, socket, spec in gpu_list:
        components.append({
            "id": f"GPU-{len(components)+1:03d}",
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

    # -------------------------------------------------------------------------
    # 5. PENYIMPANAN (SSD / HDD) - 60 Items
    # -------------------------------------------------------------------------
    storage_list = [
        # SATA SSD 2.5"
        ("Team GX2 128GB SATA III 2.5 Inch", "TeamGroup", 165000, "SATA 2.5 Inch", "Read 500 MB/s, Write 400 MB/s, 7mm"),
        ("Kingston A400 240GB SATA III 2.5 Inch", "Kingston", 295000, "SATA 2.5 Inch", "Read 500 MB/s, Write 350 MB/s"),
        ("Team GX2 256GB SATA III 2.5 Inch", "TeamGroup", 285000, "SATA 2.5 Inch", "Read 500 MB/s, Write 400 MB/s"),
        ("V-GeN Platinum 256GB SATA III 2.5 Inch", "V-GeN", 290000, "SATA 2.5 Inch", "Read 550 MB/s, Write 450 MB/s, Garansi 3 Thn"),
        ("Western Digital Green 240GB SATA III 2.5 Inch", "Western Digital", 325000, "SATA 2.5 Inch", "Read 545 MB/s, Efisien Daya"),
        ("Kingston A400 480GB SATA III 2.5 Inch", "Kingston", 465000, "SATA 2.5 Inch", "Read 500 MB/s, Write 450 MB/s"),
        ("Team GX2 512GB SATA III 2.5 Inch", "TeamGroup", 450000, "SATA 2.5 Inch", "Read 530 MB/s, Write 430 MB/s"),
        ("Crucial BX500 500GB SATA III 2.5 Inch", "Crucial", 495000, "SATA 2.5 Inch", "Read 540 MB/s, Micron 3D NAND"),
        ("Western Digital Green 480GB SATA III 2.5 Inch", "Western Digital", 515000, "SATA 2.5 Inch", "Read 545 MB/s, Garansi 3 Tahun"),
        ("Kingston A400 960GB SATA III 2.5 Inch", "Kingston", 845000, "SATA 2.5 Inch", "Read 500 MB/s, Write 450 MB/s"),
        ("Team GX2 1TB SATA III 2.5 Inch", "TeamGroup", 820000, "SATA 2.5 Inch", "Read 530 MB/s, Write 480 MB/s"),
        ("Crucial BX500 1TB SATA III 2.5 Inch", "Crucial", 895000, "SATA 2.5 Inch", "Read 540 MB/s, 1000GB"),
        ("Samsung 870 EVO 500GB SATA III 2.5 Inch", "Samsung", 850000, "SATA 2.5 Inch", "Read 560 MB/s, Write 530 MB/s, V-NAND DRAM"),
        ("Samsung 870 EVO 1TB SATA III 2.5 Inch", "Samsung", 1450000, "SATA 2.5 Inch", "Read 560 MB/s, Write 530 MB/s, Raja SATA"),

        # NVMe Gen 3
        ("Team MP33 PRO 256GB M.2 NVMe PCIe 3.0", "TeamGroup", 325000, "NVMe Gen3", "Read 2100 MB/s, Write 1100 MB/s"),
        ("ADATA Legend 710 256GB M.2 NVMe PCIe 3.0", "ADATA", 335000, "NVMe Gen3", "Read 2400 MB/s, Write 1000 MB/s, Heatsink"),
        ("Klevv Cras C710 256GB M.2 NVMe PCIe 3.0", "Klevv", 345000, "NVMe Gen3", "Read 1950 MB/s, Write 1250 MB/s"),
        ("Team MP33 PRO 512GB M.2 NVMe PCIe 3.0", "TeamGroup", 485000, "NVMe Gen3", "Read 2100 MB/s, Write 1700 MB/s"),
        ("ADATA Legend 710 512GB M.2 NVMe PCIe 3.0", "ADATA", 520000, "NVMe Gen3", "Read 2400 MB/s, Write 1800 MB/s, Heatsink Biru"),
        ("Western Digital Blue SN570 500GB NVMe PCIe 3.0", "Western Digital", 565000, "NVMe Gen3", "Read 3500 MB/s, Write 2300 MB/s"),
        ("Klevv Cras C710 512GB M.2 NVMe PCIe 3.0", "Klevv", 510000, "NVMe Gen3", "Read 2050 MB/s, Write 1650 MB/s"),
        ("Team MP33 1TB M.2 NVMe PCIe 3.0", "TeamGroup", 875000, "NVMe Gen3", "Read 1800 MB/s, Write 1500 MB/s, 1000GB"),
        ("ADATA Legend 710 1TB M.2 NVMe PCIe 3.0", "ADATA", 920000, "NVMe Gen3", "Read 2400 MB/s, Write 1800 MB/s, Heatsink"),
        ("Western Digital Blue SN570 1TB NVMe PCIe 3.0", "Western Digital", 995000, "NVMe Gen3", "Read 3500 MB/s, Write 3000 MB/s"),
        ("ADATA SX8200 Pro 1TB M.2 NVMe PCIe 3.0 (DRAM)", "ADATA", 1095000, "NVMe Gen3", "Read 3500 MB/s, Write 3000 MB/s, Ada DRAM Cache"),
        ("Team MP33 PRO 2TB M.2 NVMe PCIe 3.0", "TeamGroup", 1650000, "NVMe Gen3", "Read 2400 MB/s, Write 2000 MB/s, 2048GB"),

        # NVMe Gen 4
        ("Kingston NV2 500GB M.2 NVMe PCIe 4.0", "Kingston", 565000, "NVMe Gen4", "Read 3500 MB/s, Write 2100 MB/s"),
        ("Team MP44L 500GB M.2 NVMe PCIe 4.0", "TeamGroup", 625000, "NVMe Gen4", "Read 5000 MB/s, Write 2500 MB/s"),
        ("Western Digital Blue SN580 500GB NVMe PCIe 4.0", "Western Digital", 695000, "NVMe Gen4", "Read 4000 MB/s, Write 3600 MB/s"),
        ("Crucial P3 Plus 500GB M.2 NVMe PCIe 4.0", "Crucial", 650000, "NVMe Gen4", "Read 4700 MB/s, Write 1900 MB/s"),
        ("ADATA Legend 850 LITE 500GB NVMe PCIe 4.0", "ADATA", 635000, "NVMe Gen4", "Read 4700 MB/s, Write 1700 MB/s"),
        ("Kingston NV2 1TB M.2 NVMe PCIe 4.0", "Kingston", 985000, "NVMe Gen4", "Read 3500 MB/s, Write 2100 MB/s, Best Seller"),
        ("Team MP44L 1TB M.2 NVMe PCIe 4.0", "TeamGroup", 1080000, "NVMe Gen4", "Read 5000 MB/s, Write 4500 MB/s"),
        ("Western Digital Blue SN580 1TB NVMe PCIe 4.0", "Western Digital", 1150000, "NVMe Gen4", "Read 4150 MB/s, Write 4150 MB/s"),
        ("Crucial P3 Plus 1TB M.2 NVMe PCIe 4.0", "Crucial", 1190000, "NVMe Gen4", "Read 5000 MB/s, Write 4200 MB/s"),
        ("ADATA Legend 850 1TB M.2 NVMe PCIe 4.0", "ADATA", 1250000, "NVMe Gen4", "Read 5000 MB/s, Write 4500 MB/s"),
        ("Klevv CRAS C910 1TB M.2 NVMe PCIe 4.0", "Klevv", 1120000, "NVMe Gen4", "Read 5000 MB/s, Write 4800 MB/s"),
        ("Western Digital Black SN770 1TB NVMe PCIe 4.0", "Western Digital", 1390000, "NVMe Gen4", "Read 5150 MB/s, Write 4900 MB/s, Gaming Drive"),
        ("Kingston KC3000 1TB M.2 NVMe PCIe 4.0", "Kingston", 1550000, "NVMe Gen4", "Read 7000 MB/s, Write 6000 MB/s, DRAM Cache"),
        ("Western Digital Black SN850X 1TB NVMe PCIe 4.0", "Western Digital", 1850000, "NVMe Gen4", "Read 7300 MB/s, Write 6300 MB/s, Game Mode 2.0"),
        ("Samsung 980 PRO 1TB M.2 NVMe PCIe 4.0", "Samsung", 1750000, "NVMe Gen4", "Read 7000 MB/s, Write 5000 MB/s, DRAM LPDDR4"),
        ("Samsung 990 PRO 1TB M.2 NVMe PCIe 4.0", "Samsung", 1950000, "NVMe Gen4", "Read 7450 MB/s, Write 6900 MB/s, Raja SSD Gen 4"),
        ("Crucial T500 1TB M.2 NVMe PCIe 4.0 (DRAM)", "Crucial", 1680000, "NVMe Gen4", "Read 7300 MB/s, Write 6800 MB/s, LPDDR4 DRAM"),
        ("Kingston NV2 2TB M.2 NVMe PCIe 4.0", "Kingston", 1850000, "NVMe Gen4", "Read 3500 MB/s, Write 2800 MB/s, 2000GB"),
        ("Team MP44L 2TB M.2 NVMe PCIe 4.0", "TeamGroup", 1980000, "NVMe Gen4", "Read 4800 MB/s, Write 4400 MB/s, 2048GB"),
        ("Western Digital Blue SN580 2TB NVMe PCIe 4.0", "Western Digital", 2150000, "NVMe Gen4", "Read 4150 MB/s, Write 4150 MB/s, 2048GB"),
        ("Crucial P3 Plus 2TB M.2 NVMe PCIe 4.0", "Crucial", 2190000, "NVMe Gen4", "Read 5000 MB/s, Write 4200 MB/s"),
        ("Kingston KC3000 2TB M.2 NVMe PCIe 4.0", "Kingston", 2850000, "NVMe Gen4", "Read 7000 MB/s, Write 7000 MB/s, DRAM Cache"),
        ("Western Digital Black SN850X 2TB NVMe PCIe 4.0", "Western Digital", 3250000, "NVMe Gen4", "Read 7300 MB/s, Write 6600 MB/s"),
        ("Samsung 990 PRO 2TB M.2 NVMe PCIe 4.0", "Samsung", 3450000, "NVMe Gen4", "Read 7450 MB/s, Write 6900 MB/s, 2048GB Flagship"),
        ("Samsung 990 PRO with Heatsink 2TB PCIe 4.0", "Samsung", 3750000, "NVMe Gen4", "Read 7450 MB/s, Heatsink Pabrikan, Support PS5 & PC"),
        ("Kingston KC3000 4TB M.2 NVMe PCIe 4.0", "Kingston", 5850000, "NVMe Gen4", "Read 7000 MB/s, Write 7000 MB/s, Kapasitas Raksasa 4TB"),
        ("Samsung 990 PRO 4TB M.2 NVMe PCIe 4.0", "Samsung", 6850000, "NVMe Gen4", "Read 7450 MB/s, Write 6900 MB/s, Kapasitas Sultan 4096GB"),

        # HDD 3.5" Internal
        ("Seagate BarraCuda 1TB HDD 7200RPM 3.5 Inch", "Seagate", 650000, "HDD 3.5 Inch", "SATA III, 7200 RPM, 64MB Cache"),
        ("Western Digital Blue 1TB HDD 7200RPM", "Western Digital", 660000, "HDD 3.5 Inch", "SATA III, 7200 RPM, 64MB Cache"),
        ("Seagate BarraCuda 2TB HDD 7200RPM", "Seagate", 940000, "HDD 3.5 Inch", "SATA III, 7200 RPM, 256MB Cache"),
        ("Western Digital Blue 2TB HDD 7200RPM", "Western Digital", 950000, "HDD 3.5 Inch", "SATA III, 7200 RPM, 256MB Cache"),
        ("Western Digital Purple 2TB HDD CCTV / Storage", "Western Digital", 995000, "HDD 3.5 Inch", "AllFrame 4K, 24/7 Reliability"),
        ("Western Digital Blue 4TB HDD 5400RPM", "Western Digital", 1550000, "HDD 3.5 Inch", "SATA III, 256MB Cache, Arsip Jumbo"),
        ("Seagate BarraCuda 4TB HDD 5400RPM", "Seagate", 1540000, "HDD 3.5 Inch", "SATA III, 256MB Cache, Arsip Jumbo")
    ]

    for name, brand, price, socket, spec in storage_list:
        components.append({
            "id": f"SSD-{len(components)+1:03d}",
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

    # -------------------------------------------------------------------------
    # 6. POWER SUPPLY (PSU) - 50 Items
    # -------------------------------------------------------------------------
    psu_list = [
        # 450W - 550W
        ("Aerocool United Power 500W 80+ White", "Aerocool", 475000, "500W", "80+ White, 120mm Silent Fan, Flat Cable"),
        ("FSP HV PRO 550W 80+ White", "FSP", 580000, "550W", "80+ White, Flat Cable Black, Single Rail"),
        ("Deepcool PK550D 550W 80+ Bronze", "Deepcool", 640000, "550W", "80+ Bronze Certified, OVP/OPP/SCP, Flat Cable"),
        ("MSI MAG A550BN 550W 80+ Bronze", "MSI", 690000, "550W", "80+ Bronze, DC-DC Structure, 120mm Low Noise Fan"),
        ("Corsair CV550 550W 80+ Bronze", "Corsair", 750000, "550W", "80+ Bronze, Compact 125mm Casing"),
        ("Cooler Master MWE 550 Bronze V2", "Cooler Master", 745000, "550W", "80+ Bronze, DC-to-DC, Flat Cables, HDB Fan"),
        ("be quiet! System Power 10 550W 80+ Bronze", "be quiet!", 785000, "550W", "80+ Bronze, Kipas Super Hening be quiet!"),
        ("Super Flower Silver Green 500W 80+ Silver", "Super Flower", 695000, "500W", "80+ Silver Efisiensi Tinggi, Kapasitor Taiwan"),

        # 600W - 650W
        ("Deepcool PK650D 650W 80+ Bronze", "Deepcool", 760000, "650W", "650W 80+ Bronze, Dual PCIe 8-pin, Flat Cable"),
        ("MSI MAG A650BN 650W 80+ Bronze", "MSI", 790000, "650W", "650W 80+ Bronze, DC-DC, Kipas Hening 120mm"),
        ("FSP HV PRO 650W 80+ Bronze", "FSP", 780000, "650W", "650W 80+ Bronze, Efisiensi 85%, Proteksi Komplit"),
        ("Corsair CV650 650W 80+ Bronze", "Corsair", 845000, "650W", "650W 80+ Bronze, Garansi 3 Thn"),
        ("Corsair CX650 650W 80+ Bronze", "Corsair", 895000, "650W", "650W 80+ Bronze, Black Sleeved Cable, Garansi 5 Thn"),
        ("Cooler Master MWE 650 Bronze V2", "Cooler Master", 885000, "650W", "650W 80+ Bronze, DC-DC, HDB Fan 120mm"),
        ("Seasonic B12 BC-650 650W 80+ Bronze", "Seasonic", 950000, "650W", "650W 80+ Bronze, Smart & Silent Fan S2FC, Garansi 5 Thn"),
        ("be quiet! System Power 10 650W 80+ Bronze", "be quiet!", 925000, "650W", "650W 80+ Bronze, 2x PCIe 8-pin, Super Hening"),
        ("Thermaltake Smart BX1 650W 80+ Bronze", "Thermaltake", 795000, "650W", "650W 80+ Bronze, Kapasitor Utama Jepang"),
        ("Super Flower Legion GX Pro 650W 80+ Gold Semi-Modular", "Super Flower", 1150000, "650W", "650W 80+ Gold, Semi-Modular, Efisiensi 90%"),

        # 750W
        ("Deepcool PL750D 750W 80+ Bronze Native PCIe 5.0", "Deepcool", 985000, "750W", "750W 80+ Bronze, Native 12VHPWR Cable"),
        ("MSI MAG A750BN 750W 80+ Bronze PCIE5", "MSI", 1050000, "750W", "750W 80+ Bronze, Native PCIe 5.0 16-pin"),
        ("Cooler Master MWE 750 Bronze V2", "Cooler Master", 1025000, "750W", "750W 80+ Bronze, Dual EPS 8-pin"),
        ("Deepcool PN750M 750W 80+ Gold ATX 3.1", "Deepcool", 1450000, "750W", "750W 80+ Gold, Full Modular, Native PCIe 5.1"),
        ("FSP Hydro G PRO 750W 80+ Gold Full Modular", "FSP", 1650000, "750W", "750W 80+ Gold, 100% Japanese E-Cap, Garansi 10 Thn"),
        ("MSI MAG A750GL PCIE5 750W 80+ Gold ATX 3.0", "MSI", 1680000, "750W", "750W 80+ Gold, Native 12V-2x6 Cable RTX 4000"),
        ("Corsair RM750e 750W 80+ Gold Full Modular ATX 3.0", "Corsair", 1850000, "750W", "750W 80+ Gold, ATX 3.0, 105C Capacitors"),
        ("Corsair RM750x 750W 80+ Gold Full Modular White", "Corsair", 2150000, "750W", "750W 80+ Gold, Full White Kabel & Bodi, Kipas ML135"),
        ("Seasonic FOCUS GX-750 750W 80+ Gold Modular", "Seasonic", 1950000, "750W", "750W 80+ Gold, Fluid Dynamic Fan, Garansi 10 Thn"),
        ("Seasonic FOCUS GX-750 ATX 3.0 (PCIe 5.0)", "Seasonic", 2150000, "750W", "750W 80+ Gold, Native 12VHPWR, Garansi 10 Thn"),
        ("be quiet! Pure Power 12 M 750W 80+ Gold ATX 3.0", "be quiet!", 1950000, "750W", "750W 80+ Gold, ATX 3.0, Kipas Silent Wings"),
        ("Cooler Master GX III 750W 80+ Gold ATX 3.0", "Cooler Master", 1890000, "750W", "750W 80+ Gold, 90-degree 12VHPWR Cable"),
        ("Super Flower Leadex III Gold 750W Full Modular", "Super Flower", 1750000, "750W", "750W 80+ Gold, Tiga Mode Fan ECO, Full Modular"),

        # 850W
        ("Deepcool PN850M 850W 80+ Gold ATX 3.1", "Deepcool", 1680000, "850W", "850W 80+ Gold, Full Modular, Native PCIe 5.1"),
        ("MSI MAG A850GL PCIE5 850W 80+ Gold ATX 3.0", "MSI", 1980000, "850W", "850W 80+ Gold, Native PCIe 5.0, Full Modular"),
        ("MSI MAG A850GL PCIE5 White 850W 80+ Gold", "MSI", 2080000, "850W", "850W 80+ Gold, Full White Bodi & Kabel ATX 3.0"),
        ("FSP Hydro G PRO 850W 80+ Gold ATX 3.0", "FSP", 2050000, "850W", "850W 80+ Gold, Native PCIe 5.0, Kapasitor Jepang"),
        ("Corsair RM850e 850W 80+ Gold Full Modular ATX 3.0", "Corsair", 2150000, "850W", "850W 80+ Gold, Ultra Low Noise"),
        ("Corsair RM850x 850W 80+ Gold Full Modular White", "Corsair", 2390000, "850W", "850W 80+ Gold, All White Theme, Garansi 10 Thn"),
        ("Seasonic FOCUS GX-850 850W 80+ Gold Full Modular", "Seasonic", 2350000, "850W", "850W 80+ Gold, Tier A PSU, Garansi 10 Thn"),
        ("Seasonic FOCUS GX-850 ATX 3.0 White (PCIe 5.0)", "Seasonic", 2550000, "850W", "850W 80+ Gold, Full White ATX 3.0, Garansi 10 Thn"),
        ("be quiet! Pure Power 12 M 850W 80+ Gold ATX 3.0", "be quiet!", 2250000, "850W", "850W 80+ Gold, Super Senyap, Dual Rail 12V"),
        ("Super Flower Leadex VII Gold 850W ATX 3.0", "Super Flower", 2250000, "850W", "850W 80+ Gold, ATX 3.0, Ribbon Cable"),

        # 1000W - 1200W
        ("Deepcool PX1000G 1000W 80+ Gold ATX 3.0", "Deepcool", 2450000, "1000W", "1000W 80+ Gold, Native 12VHPWR 600W"),
        ("MSI MAG A1000GL PCIE5 1000W 80+ Gold ATX 3.0", "MSI", 2650000, "1000W", "1000W 80+ Gold, Dual-Color 16-Pin Connector"),
        ("FSP Hydro G PRO 1000W 80+ Gold ATX 3.0", "FSP", 2690000, "1000W", "1000W 80+ Gold, 100% Japanese E-Cap, Garansi 10 Thn"),
        ("Corsair RM1000e 1000W 80+ Gold Full Modular ATX 3.0", "Corsair", 2650000, "1000W", "1000W 80+ Gold, Siap RTX 4080 & 4090"),
        ("Corsair RM1000x 1000W 80+ Gold Full Modular", "Corsair", 2950000, "1000W", "1000W 80+ Gold, Japanese Cap 105C, Siap RTX 4090"),
        ("Corsair RM1000x Shift ATX 3.0 (Side Cable Interface)", "Corsair", 3250000, "1000W", "1000W 80+ Gold, Colokan Modular di Samping Revolusioner"),
        ("Seasonic VERTEX GX-1000 1000W 80+ Gold ATX 3.0", "Seasonic", 3450000, "1000W", "1000W 80+ Gold, ATX 3.0 & PCIe 5.0 Native"),
        ("MSI MEG Ai1000P PCIE5 1000W 80+ Platinum ATX 3.0", "MSI", 4450000, "1000W", "1000W 80+ Platinum, Software Monitoring, Gaming Intelligence"),
        ("Corsair RM1200x Shift ATX 3.0 1200W 80+ Gold", "Corsair", 3850000, "1200W", "1200W 80+ Gold, Side Interface, Siap Dual GPU/RTX 4090 OC"),
        ("Seasonic PRIME TX-1000 1000W 80+ Titanium Flagship", "Seasonic", 5650000, "1000W", "1000W 80+ Titanium Puncak Efisiensi 94%, Garansi 12 Thn")
    ]

    for name, brand, price, socket, spec in psu_list:
        components.append({
            "id": f"PSU-{len(components)+1:03d}",
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

    # -------------------------------------------------------------------------
    # 7. CPU COOLER - 40 Items
    # -------------------------------------------------------------------------
    cooler_list = [
        # Air Cooler Budget
        ("Jonsbo CR-1400 EVO ARGB Black", "Jonsbo", 195000, "Air Cooler", "Tower 4 Heatpipe Tembaga, 92mm PWM ARGB"),
        ("Jonsbo CR-1400 EVO ARGB White", "Jonsbo", 215000, "Air Cooler", "Tower 4 Heatpipe Tembaga, Putih Salju ARGB"),
        ("ID-Cooling SE-214-XT ARGB Black", "ID-Cooling", 235000, "Air Cooler", "Tower 4 Heatpipes direct touch, Fan 120mm PWM ARGB"),
        ("ID-Cooling SE-214-XT White ARGB", "ID-Cooling", 245000, "Air Cooler", "Full White 4 Heatpipes, Fan 120mm PWM ARGB"),
        ("Thermalright Assassin X 120 Refined SE ARGB", "Thermalright", 245000, "Air Cooler", "Tower 4 Heatpipe AGHP, Fan 120mm PWM S-FDB"),
        ("Thermalright Assassin X 120 Refined SE White ARGB", "Thermalright", 265000, "Air Cooler", "Tower Putih Bersih, Fan 120mm ARGB"),
        ("Deepcool AG400 ARGB Single Tower", "Deepcool", 285000, "Air Cooler", "Tower 4 Heatpipe Direct Contact, Fan 120mm Hydro"),
        ("Deepcool AG400 White ARGB", "Deepcool", 310000, "Air Cooler", "Full White Theme, Fan 120mm ARGB"),
        ("Deepcool AG400 PLUS Dual Fan", "Deepcool", 345000, "Air Cooler", "Push-Pull Dual Fan 120mm, Sirkulasi Cepat"),
        ("Cooler Master Hyper 212 Spectrum V3", "Cooler Master", 315000, "Air Cooler", "Legenda Hyper 212 dengan Kipas ARGB Spectrum"),
        ("Cooler Master Hyper 212 Halo White", "Cooler Master", 495000, "Air Cooler", "Dual Ring Halo ARGB Putih, Fin Aluminium Rapi"),
        ("Deepcool AK400 Black", "Deepcool", 365000, "Air Cooler", "Matrix Fin Design, Kipas FDB FDB Hening"),
        ("Deepcool AK400 White", "Deepcool", 395000, "Air Cooler", "Full White Matrix Fin Design"),
        ("Deepcool AK400 Digital Black (Display Suhu)", "Deepcool", 465000, "Air Cooler", "Layar Digital Real-time Suhu CPU di Heatsink"),
        ("Deepcool AK400 Digital White (Display Suhu)", "Deepcool", 495000, "Air Cooler", "Full White dengan Layar Digital Suhu CPU"),

        # Air Cooler Dual Tower
        ("Thermalright Peerless Assassin 120 SE ARGB", "Thermalright", 485000, "Air Cooler", "Dual Tower 6 Heatpipes, 2x Fan 120mm PWM"),
        ("Thermalright Peerless Assassin 120 SE White ARGB", "Thermalright", 515000, "Air Cooler", "Dual Tower Putih, 6 Heatpipes, Dingin Setara AIO 240"),
        ("Thermalright Phantom Spirit 120 SE ARGB", "Thermalright", 565000, "Air Cooler", "Dual Tower 7 Heatpipes AGHP Gen 4, Performa Tertinggi"),
        ("Deepcool AG620 ARGB Dual Tower", "Deepcool", 645000, "Air Cooler", "Dual Tower 6 Heatpipe, Disipasi Daya 260W"),
        ("Deepcool AK620 High Performance Dual Tower", "Deepcool", 825000, "Air Cooler", "Dual Tower 6 Heatpipes, Kipas FDB Presisi"),
        ("Deepcool AK620 Digital Black (Display Suhu Dual)", "Deepcool", 985000, "Air Cooler", "Dual Tower Layar Digital Suhu & Utilisasi CPU"),
        ("be quiet! Dark Rock Pro 5 Dual Tower", "be quiet!", 1450000, "Air Cooler", "7 Heatpipes, Silent Wings PWM, Suara Nyaris Tak Terdengar"),
        ("Noctua NH-U12S chromax.black", "Noctua", 1350000, "Air Cooler", "Single Tower Hitam Pekat, Kipas NF-F12 Legendaris"),
        ("Noctua NH-D15 chromax.black", "Noctua", 1850000, "Air Cooler", "Raja Air Cooler Dunia, Dual Tower Dual NF-A15"),

        # AIO Liquid Coolers 240mm
        ("Thermalright Frozen Notte 240 Black ARGB", "Thermalright", 745000, "AIO Liquid 240mm", "Radiator 240mm, Pompa 5300 RPM Kencang, ARGB"),
        ("Thermalright Frozen Notte 240 White ARGB", "Thermalright", 775000, "AIO Liquid 240mm", "Full White Radiator 240mm, Pompa Kencang"),
        ("Deepcool LE520 240mm ARGB AIO Liquid Cooler", "Deepcool", 785000, "AIO Liquid 240mm", "Radiator 240mm, Anti-Leak Tech, 2x Fan ARGB"),
        ("Deepcool LE520 White 240mm ARGB AIO", "Deepcool", 825000, "AIO Liquid 240mm", "Full White Radiator 240mm, Anti-Leak Tech"),
        ("MSI MAG CoreLiquid M240 ARGB", "MSI", 1150000, "AIO Liquid 240mm", "Radiator 240mm, Desain Curve Blok Pompa Mewah"),
        ("Deepcool LT520 240mm Infinity Mirror Liquid", "Deepcool", 1250000, "AIO Liquid 240mm", "Pompa Cermin Infinity Kubus 3D, Kipas FK120"),
        ("Deepcool LT520 White 240mm Infinity Mirror", "Deepcool", 1320000, "AIO Liquid 240mm", "Full White Infinity Mirror 3D Cube"),
        ("Arctic Liquid Freezer III 240 ARGB Black", "Arctic", 1380000, "AIO Liquid 240mm", "Radiator Tebal 38mm, VRM Fan Terintegrasi"),
        ("Arctic Liquid Freezer III 240 A-RGB White", "Arctic", 1450000, "AIO Liquid 240mm", "Radiator 38mm Putih, VRM Fan Terintegrasi"),
        ("NZXT Kraken 240 RGB Black (Layar LCD)", "NZXT", 2450000, "AIO Liquid 240mm", "Layar LCD 1.54 inch di Pompa untuk GIF/Suhu, 2x Kipas RGB"),

        # AIO Liquid Coolers 360mm
        ("Thermalright Frozen Warframe 360 Black (Layar LCD)", "Thermalright", 1350000, "AIO Liquid 360mm", "Layar IPS LCD 2.4 inch di Pompa, 3x Fan ARGB"),
        ("Thermalright Frozen Warframe 360 White (Layar LCD)", "Thermalright", 1420000, "AIO Liquid 360mm", "Full White dengan Layar IPS LCD 2.4 inch"),
        ("Deepcool LE720 360mm ARGB AIO Liquid Cooler", "Deepcool", 1050000, "AIO Liquid 360mm", "Radiator 360mm 3 Kipas, Anti-Leak Tech"),
        ("Deepcool LT720 360mm Infinity Mirror Black", "Deepcool", 1550000, "AIO Liquid 360mm", "Radiator 360mm, Infinity Mirror Kubus Mewah"),
        ("Deepcool LT720 White 360mm Infinity Mirror", "Deepcool", 1620000, "AIO Liquid 360mm", "Full White Infinity Mirror 360mm"),
        ("Arctic Liquid Freezer III 360 ARGB Black", "Arctic", 1680000, "AIO Liquid 360mm", "Radiator 360mm Raksasa, VRM Fan, Dingin Maksimal"),
        ("Arctic Liquid Freezer III 360 A-RGB White", "Arctic", 1750000, "AIO Liquid 360mm", "Radiator 360mm Putih Salju, VRM Fan"),
        ("Lian Li Galahad II Trinity SL-INF 360 White", "Lian Li", 2850000, "AIO Liquid 360mm", "Kipas Uni Fan SL-Infinity Cantik, 3 Pilihan Tutup Pompa"),
        ("NZXT Kraken Elite 360 RGB White (Layar LCD 2.36)", "NZXT", 4850000, "AIO Liquid 360mm", "Layar LCD 2.36 inch 60 FPS Resolusi Tinggi di Pompa")
    ]

    for name, brand, price, socket, spec in cooler_list:
        components.append({
            "id": f"CLR-{len(components)+1:03d}",
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

    # -------------------------------------------------------------------------
    # 8. CASING PC - 45 Items
    # -------------------------------------------------------------------------
    case_list = [
        # M-ATX Compact & Mesh
        ("Cube Gaming Axel Black (M-ATX)", "Cube Gaming", 345000, "Micro-ATX", "Mesh Front, Tempered Glass, Free 3x 120mm Fans"),
        ("Cube Gaming Axel White (M-ATX)", "Cube Gaming", 365000, "Micro-ATX", "Full White Mesh Front, Tempered Glass, Free 3x Fans"),
        ("VenomRX Praetorian Black M-ATX", "VenomRX", 380000, "Micro-ATX", "Door Tempered Glass Magnet, Free 3x RGB Fans"),
        ("VenomRX Praetorian White M-ATX", "VenomRX", 395000, "Micro-ATX", "Door Tempered Glass Magnet Putih, Free 3x RGB Fans"),
        ("Tecware Flatline Black (M-ATX)", "Tecware", 445000, "Micro-ATX", "High Airflow Mesh Depan, Free 4x Kipas 120mm"),
        ("Tecware Flatline White (M-ATX)", "Tecware", 465000, "Micro-ATX", "Full White Mesh Depan, Free 4x Kipas Putih"),
        ("DarkFlash DLM21 Mesh Black (M-ATX)", "DarkFlash", 545000, "Micro-ATX", "Low Poly Mesh Front, Door Tempered Glass"),
        ("DarkFlash DLM21 Mesh White (M-ATX)", "DarkFlash", 565000, "Micro-ATX", "Low Poly Mesh Putih, Door Tempered Glass"),
        ("DarkFlash DLM21 Mesh Neo Mint Green", "DarkFlash", 585000, "Micro-ATX", "Warna Unik Hijau Mint Pastel, Door Glass"),
        ("DarkFlash DLM21 Mesh Pink Sakura", "DarkFlash", 585000, "Micro-ATX", "Warna Pink Pastel Cantik untuk Setup Cewek"),
        ("Cooler Master MasterBox Q300L V2", "Cooler Master", 595000, "Micro-ATX", "Pola Magnetik Filter Debu, USB Type-C Depan"),
        ("Deepcool CC360 ARGB Black (M-ATX)", "Deepcool", 585000, "Micro-ATX", "Mesh Panel, Free 3x Pre-installed ARGB Fans"),
        ("Deepcool CC360 ARGB White (M-ATX)", "Deepcool", 615000, "Micro-ATX", "Full White Mesh Panel, Free 3x ARGB Fans"),
        ("Montech AIR 100 ARGB Black (M-ATX)", "Montech", 645000, "Micro-ATX", "Ultra-fine Mesh Front, Include 4x ARGB Fans + Hub"),
        ("Montech AIR 100 ARGB White (M-ATX)", "Montech", 675000, "Micro-ATX", "Full White Theme, Include 4x ARGB White Fans + Hub"),

        # M-ATX Panoramic Aquarium
        ("Paradox Gaming Ghost M-ATX Aquarium Black", "Paradox Gaming", 425000, "Micro-ATX Aquarium", "Dual Tempered Glass View, Free 3x ARGB Fans"),
        ("Paradox Gaming Ghost M-ATX Aquarium White", "Paradox Gaming", 445000, "Micro-ATX Aquarium", "Dual Tempered Glass View Putih, Free 3x ARGB"),
        ("Cube Gaming Byron Black Aquarium M-ATX", "Cube Gaming", 465000, "Micro-ATX Aquarium", "Panoramic Tempered Glass, Free 3x ARGB Fans"),
        ("Cube Gaming Byron White Aquarium M-ATX", "Cube Gaming", 485000, "Micro-ATX Aquarium", "Full White Panoramic Glass, Free 3x ARGB Fans"),
        ("VenomRX Daemon Aquarium Black", "VenomRX", 465000, "Micro-ATX Aquarium", "Dual Tempered Glass Showcase, Free 3x Kipas"),
        ("VenomRX Daemon Aquarium White", "VenomRX", 485000, "Micro-ATX Aquarium", "Dual Tempered Glass Putih, Free 3x Kipas"),
        ("DarkFlash DS900 Air Aquarium White", "DarkFlash", 695000, "Micro-ATX Aquarium", "270 Derajat Panoramic View, Support 240/360 AIO"),

        # Mid-Tower ATX High Airflow
        ("Deepcool CC560 V2 Black (ATX)", "Deepcool", 650000, "Mid-Tower ATX", "High Airflow Front, Include 4x LED Fans"),
        ("Deepcool CC560 V2 White (ATX)", "Deepcool", 685000, "Mid-Tower ATX", "Full White High Airflow, Include 4x LED Fans"),
        ("Montech AIR 903 BASE Black (ATX)", "Montech", 820000, "Mid-Tower ATX", "3x Kipas 140mm High Airflow PWM, USB Type-C"),
        ("Montech AIR 903 BASE White (ATX)", "Montech", 850000, "Mid-Tower ATX", "Full White 3x Kipas 140mm PWM, USB Type-C"),
        ("Montech AIR 903 MAX Black (ATX)", "Montech", 935000, "Mid-Tower ATX", "4x Kipas 140mm ARGB PWM Depan, Airflow Monster"),
        ("Montech AIR 903 MAX White (ATX)", "Montech", 965000, "Mid-Tower ATX", "4x Kipas 140mm ARGB PWM Putih, USB Type-C"),
        ("Phanteks Eclipse G300A Black", "Phanteks", 895000, "Mid-Tower ATX", "Ultra-fine Performance Mesh, Free 3x DRGB Fans"),
        ("Deepcool CH560 Digital Black (Display Suhu)", "Deepcool", 1250000, "Mid-Tower ATX", "Layar Digital Real-time Suhu CPU & GPU di Casing"),
        ("Deepcool CH560 Digital White (Display Suhu)", "Deepcool", 1320000, "Mid-Tower ATX", "Full White dengan Layar Digital Suhu CPU/GPU"),
        ("NZXT H5 Flow Black (ATX)", "NZXT", 1250000, "Mid-Tower ATX", "Perforated Mesh, Dedicated Bottom GPU Fan"),
        ("NZXT H5 Flow White (ATX)", "NZXT", 1280000, "Mid-Tower ATX", "All-White Perforated Mesh, Bottom GPU Fan"),
        ("Corsair 4000D Airflow Black (ATX)", "Corsair", 1350000, "Mid-Tower ATX", "High-Airflow Steel Front, RapidRoute Cable System"),
        ("Corsair 4000D Airflow White (ATX)", "Corsair", 1380000, "Mid-Tower ATX", "White Steel Front, RapidRoute Cable System"),
        ("Lian Li LANCOOL 216 RGB Black (ATX)", "Lian Li", 1450000, "Mid-Tower ATX", "2x Kipas Raksasa 160mm ARGB Depan, Airflow Monster"),
        ("Lian Li LANCOOL 216 RGB White (ATX)", "Lian Li", 1520000, "Mid-Tower ATX", "2x Kipas Raksasa 160mm ARGB Putih, Airflow Monster"),
        ("Fractal Design Pop Air Black Solid/TG", "Fractal Design", 1350000, "Mid-Tower ATX", "Desain Skandinavia Elegan, Kualitas Cat Premium"),
        ("Fractal Design Pop Air White TG Clear", "Fractal Design", 1390000, "Mid-Tower ATX", "Skandinavia Putih Bersih, Kaca Bening"),

        # ATX Showcase & Dual Chamber Flagship
        ("Fractal Design North Charcoal Black (Real Walnut Wood)", "Fractal Design", 2250000, "Mid-Tower ATX Kayu Asli", "Panel Depan Kayu Walnut Asli Elegan Mewah"),
        ("Fractal Design North Chalk White (Real Oak Wood)", "Fractal Design", 2290000, "Mid-Tower ATX Kayu Asli", "Panel Depan Kayu Oak Asli Elegan Mewah"),
        ("Lian Li O11 Dynamic Mini Black", "Lian Li", 1650000, "Dual Chamber M-ATX/ITX", "Aquarium Kompak, Support SFX/SFX-L PSU"),
        ("Lian Li O11 Dynamic EVO Black (ATX)", "Lian Li", 2450000, "Dual Chamber ATX", "Dual Tempered Glass Aquarium, Reversible Chassis"),
        ("Lian Li O11 Dynamic EVO White (ATX)", "Lian Li", 2550000, "Dual Chamber ATX", "All-White Aquarium Showcase Flagship"),
        ("NZXT H9 Flow Black Dual Chamber ATX", "NZXT", 2650000, "Dual Chamber ATX", "Panoramic Glass, Support 10 Fans, Airflow Atas Mesh"),
        ("NZXT H9 Flow White Dual Chamber ATX", "NZXT", 2750000, "Dual Chamber ATX", "Full White Panoramic Glass Showcase Raksasa"),
        ("Hyte Y60 Modern Aesthetic Red/Black", "Hyte", 3250000, "Panoramic Corner 3-Piece Glass", "Kaca Sudut 3 Bagian Unik, Include Riser PCIe 4.0")
    ]

    for name, brand, price, socket, spec in case_list:
        components.append({
            "id": f"CASE-{len(components)+1:03d}",
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

    # -------------------------------------------------------------------------
    # 9. MONITOR - 30 Items
    # -------------------------------------------------------------------------
    monitor_list = [
        # 24 Inch FHD (1080p)
        ("Xiaomi Monitor G24i 23.8 Inch IPS 180Hz", "Xiaomi", 1450000, "23.8 Inch FHD", "Fast IPS, 180Hz, 1ms, 99% sRGB, FreeSync, HDR10"),
        ("ViewSonic OMNI VX2428 24 Inch IPS 165Hz", "ViewSonic", 1650000, "23.8 Inch FHD", "Fast IPS, 165Hz, 0.5ms, Speaker Internal Stereo"),
        ("MSI G244F E2 23.8 Inch Rapid IPS 180Hz", "MSI", 1750000, "23.8 Inch FHD", "Rapid IPS, 180Hz, 1ms GtG, Wide Color Gamut"),
        ("Acer Nitro VG240Y M3 23.8 Inch IPS 180Hz", "Acer", 1690000, "23.8 Inch FHD", "IPS, 180Hz, 0.5ms, sRGB 99%, AMD FreeSync Premium"),
        ("Philips 24M1N3200Z 24 Inch IPS 165Hz", "Philips", 1790000, "23.8 Inch FHD", "IPS, 165Hz, 1ms MPRT, Ultra Wide-Color, Bezel Tipis"),
        ("LG UltraGear 24GN60R-B 24 Inch IPS 144Hz", "LG", 1850000, "23.8 Inch FHD", "IPS Panel LG, 144Hz, 1ms MBR, sRGB 99%"),
        ("AOC 24G2SP 23.8 Inch IPS 165Hz Stand Ergonomis", "AOC", 2050000, "23.8 Inch FHD", "IPS, 165Hz, 1ms, 125% sRGB, Stand Naik-Turun & Pivot"),
        ("ASUS TUF Gaming VG249Q3A 23.8 Inch IPS 180Hz", "ASUS", 2150000, "23.8 Inch FHD", "Fast IPS, 180Hz, 1ms, ELMB Sync, Speaker"),
        ("AOC 24G4 23.8 Inch Fast IPS 180Hz HDR10", "AOC", 1950000, "23.8 Inch FHD", "Fast IPS Generasi Baru, 180Hz, 0.5ms, HDR10"),

        # 27 Inch FHD (1080p)
        ("Xiaomi Monitor G27i 27 Inch IPS 165Hz", "Xiaomi", 1950000, "27 Inch FHD", "Fast IPS 27 Inch, 165Hz, 1ms, Layar Lebar Bezel Tipis"),
        ("ViewSonic OMNI VX2728 27 Inch IPS 165Hz", "ViewSonic", 2150000, "27 Inch FHD", "Fast IPS 27 Inch, 165Hz, 0.5ms, FreeSync Premium"),
        ("MSI G274F 27 Inch Rapid IPS 180Hz", "MSI", 2350000, "27 Inch FHD", "Rapid IPS 27 Inch, 180Hz, 1ms GtG, Night Vision"),
        ("AOC 27G2SP 27 Inch IPS 165Hz Ergonomis", "AOC", 2550000, "27 Inch FHD", "IPS, 165Hz, 1ms, 122% sRGB, Stand Ergonomis"),
        ("LG UltraGear 27GN65R-B 27 Inch IPS 144Hz Ergonomis", "LG", 2650000, "27 Inch FHD", "IPS, 144Hz, 1ms, Stand Ergonomis Naik-Turun Pivot"),
        ("ASUS TUF Gaming VG279Q3A 27 Inch IPS 180Hz", "ASUS", 2750000, "27 Inch FHD", "Fast IPS 27 Inch, 180Hz, 1ms, ELMB Sync"),

        # 27 Inch QHD 2K (1440p)
        ("ViewSonic OMNI VX2780-2K-SHDJ 27 Inch QHD 2K 170Hz", "ViewSonic", 3350000, "27 Inch QHD (2560x1440)", "SuperClear IPS, 170Hz, 1ms, Stand Ergonomis Naik-Turun"),
        ("AOC Q27G2S/EU 27 Inch QHD 2K 165Hz", "AOC", 3550000, "27 Inch QHD (2560x1440)", "IPS, 165Hz, 1ms, 10-bit Color, Stand Ergonomis"),
        ("AOC Q27G4 27 Inch Fast IPS 180Hz QHD 2K HDR400", "AOC", 3650000, "27 Inch QHD (2560x1440)", "Fast IPS 180Hz, VESA DisplayHDR 400, 1ms"),
        ("Gigabyte M27Q 27 Inch IPS 170Hz QHD 2K KVM Switch", "Gigabyte", 4250000, "27 Inch QHD (2560x1440)", "SS IPS, 170Hz, 0.5ms, Fitur KVM Switch Bawaan"),
        ("MSI MAG 274QRF QD E2 27 Inch Rapid IPS 180Hz Quantum Dot", "MSI", 4450000, "27 Inch QHD (2560x1440)", "Quantum Dot IPS, 180Hz, 1ms GtG, 98% DCI-P3"),
        ("LG UltraGear 27GP850-B 27 Inch Nano IPS QHD 2K 165Hz", "LG", 4650000, "27 Inch QHD (2560x1440)", "Nano IPS, 165Hz (OC 180Hz), 1ms GtG, 98% DCI-P3, G-Sync"),
        ("ASUS ROG Strix XG27ACS 27 Inch Fast IPS 180Hz QHD 2K", "ASUS", 4950000, "27 Inch QHD (2560x1440)", "Fast IPS, 180Hz, 1ms, Type-C DP Alt Mode, Stand Handphone"),

        # Ultrawide & Curved Gaming
        ("Samsung Odyssey G5 G55C 27 Inch QHD 165Hz Curved 1000R", "Samsung", 3150000, "27 Inch QHD Curved (2560x1440)", "VA 1000R Lengkung Ekstrem, 165Hz, 1ms, HDR10"),
        ("Samsung Odyssey G5 G55C 32 Inch QHD 165Hz Curved 1000R", "Samsung", 3850000, "32 Inch QHD Curved (2560x1440)", "32 Inch 1000R Curve Imersif, 165Hz, 1ms"),
        ("Xiaomi Curved Gaming Monitor G34WQi 34 Inch Ultrawide 180Hz", "Xiaomi", 3650000, "34 Inch WQHD Ultrawide (3440x1440)", "Curved 1500R, 180Hz, 1ms, 95% DCI-P3, 21:9 Ultrawide"),
        ("ViewSonic VX3418-2KPC 34 Inch Ultrawide 144Hz Curved", "ViewSonic", 4550000, "34 Inch WQHD Ultrawide (3440x1440)", "Curved 1500R, 144Hz, 1ms, Speaker Stereo"),
        ("AOC CU34G2XP 34 Inch Ultrawide 180Hz Curved", "AOC", 4850000, "34 Inch WQHD Ultrawide (3440x1440)", "1500R Curve, 180Hz, HDR400, Stand Ergonomis"),

        # 4K & OLED Extreme Gaming
        ("ASUS TUF Gaming VG28UQL1A 28 Inch 4K UHD 144Hz HDMI 2.1", "ASUS", 8950000, "28 Inch 4K UHD (3840x2160)", "Fast IPS, 144Hz, Dual HDMI 2.1 Siap PS5/PC 4K, 90% DCI-P3"),
        ("LG UltraGear 27GR95QE-B 27 Inch OLED QHD 240Hz", "LG", 12850000, "27 Inch OLED QHD (2560x1440)", "OLED Panel, 240Hz, 0.03ms GtG Respon Instan, Kontras 1.500.000:1"),
        ("ASUS ROG Swift OLED PG27AQDM 27 Inch 240Hz OLED", "ASUS", 14500000, "27 Inch OLED QHD (2560x1440)", "OLED 240Hz, Custom Heatsink Anti Burn-in, 0.03ms")
    ]

    for name, brand, price, socket, spec in monitor_list:
        components.append({
            "id": f"MON-{len(components)+1:03d}",
            "kategori": "Monitor",
            "nama": name,
            "brand": brand,
            "harga": price,
            "stok": random.randint(3, 10),
            "panel": socket,
            "spesifikasi_ringkas": spec,
            "kelebihan": ["Panel Fast IPS / OLED warna akurat", "Refresh rate tinggi bebas ghosting", "Garansi resmi"],
            "target_build": ["Pelengkap PC Gaming", "Color Grading", "Esports"],
            "garansi": "3 Tahun Resmi Distributor"
        })

    return components

if __name__ == "__main__":
    catalog = generate_mega_pc_catalog()
    output_path = "katalog_komponen_pc.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)
    print(f"Sukses menghasilkan {len(catalog)} data komponen PC resmi ke '{output_path}'!")
