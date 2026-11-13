"""
Modul Pengetahuan Hardware Laptop (Standar Konsultan Profesional)
Menyajikan penjelasan edukatif dan analogi terstruktur mengenai komponen hardware laptop
untuk membantu pelanggan memahami spesifikasi teknis dengan mudah dan objektif.
"""

HARDWARE_EXPLANATIONS = {
    "ram": {
        "istilah": "RAM (Random Access Memory)",
        "analogi": "Diibaratkan sebagai luas meja kerja tempat Anda meletakkan dokumen dan peralatan saat bekerja.",
        "penjelasan": (
            "Semakin besar kapasitas RAM (misalnya 16GB), semakin leluasa Anda membuka banyak aplikasi, dokumen, "
            "dan puluhan tab browser secara bersamaan tanpa mengalami penurunan performa (lag). "
            "Untuk standar saat ini, 8GB adalah kapasitas minimum untuk komputasi harian. "
            "Bagi pengguna yang membutuhkan multitasking lancar, pemrograman (coding), atau editing konten, kami sangat menyarankan minimal 16GB."
        ),
        "rekomendasi_kapasitas": {
            "8gb": "Optimal untuk kebutuhan administrasi kantor, pengolah kata (Word/Excel), browsing, dan meeting online.",
            "16gb": "Standar ideal untuk produktivitas tinggi, coding, editing grafis/video Full HD, dan multitasking intensif.",
            "32gb": "Dikhususkan untuk beban kerja profesional seperti rendering 3D, animasi, editing video 4K, atau simulasi teknik."
        }
    },
    "ssd": {
        "istilah": "SSD (Solid State Drive) vs Harddisk (HDD)",
        "analogi": "Diibaratkan sebagai sistem arsip digital berkecepatan tinggi tanpa komponen mekanik yang bergerak.",
        "penjelasan": (
            "Laptop modern saat ini telah beralih ke penyimpanan SSD NVMe PCIe. "
            "Kecepatannya mencapai 5 hingga 10 kali lipat lebih cepat dibandingkan harddisk konvensional. "
            "Hasilnya, proses booting laptop hanya memakan waktu beberapa detik dan proses pembukaan aplikasi berlangsung seketika."
        )
    },
    "prosesor": {
        "istilah": "Prosesor (CPU) - Pusat Komputasi Laptop",
        "analogi": "Merupakan 'otak utama' yang mengatur dan memproses seluruh instruksi komputasi pada laptop.",
        "penjelasan": (
            "Terdapat dua kategori prosesor yang umum di pasaran:\n"
            "1. **Seri Hemat Daya (Kode 'U', misal Core i5-1335U / Ryzen 5 7530U):** Dirancang untuk efisiensi daya maksimal, suhu tetap sejuk, dan daya tahan baterai yang panjang (cocok untuk mobilitas kerja harian).\n"
            "2. **Seri Performa Tinggi (Kode 'H' / 'HX', misal Core i5-13500H / Ryzen 7 7840HS):** Menghasilkan daya komputasi besar untuk pemrosesan berat seperti rendering video, 3D modeling, dan gaming."
        )
    },
    "gpu": {
        "istilah": "GPU / Kartu Grafis (Graphics Processing Unit)",
        "analogi": "Unit pemroses visual yang bertugas merender seluruh tampilan grafis pada layar.",
        "penjelasan": (
            "GPU terbagi menjadi dua jenis:\n"
            "1. **Integrated GPU (Terintegrasi):** Menyatu dengan prosesor, sangat hemat daya, dan optimal untuk kebutuhan komputasi harian, multimedia, serta game kasual.\n"
            "2. **Discrete GPU (Kartu Grafis Terpisah, seperti NVIDIA GeForce RTX):** Memiliki chip dan VRAM mandiri, esensial bagi pengguna yang memerlukan akselerasi 3D, render video resolusi tinggi, atau gaming modern."
        )
    },
    "layar": {
        "istilah": "Teknologi Panel Layar: TN vs IPS vs OLED",
        "analogi": "Media visual utama yang berinteraksi langsung dengan mata Anda sepanjang hari.",
        "penjelasan": (
            "1. **Panel TN:** Memiliki sudut pandang dan akurasi warna yang terbatas, umumnya ditemukan pada unit generasi lama.\n"
            "2. **Panel IPS:** Menjadi standar kenyamanan saat ini dengan sudut pandang lebar (178 derajat) dan reproduksi warna yang stabil, sangat nyaman untuk penggunaan durasi panjang.\n"
            "3. **Panel OLED:** Menghadirkan rasio kontras tak terbatas, warna hitam sempurna, serta cakupan warna profesional (100% DCI-P3), ideal untuk desainer grafis, fotografer, dan penikmat multimedia."
        )
    },
    "psu": {
        "istilah": "PSU (Power Supply Unit) - Jantung Daya PC",
        "analogi": "Diibaratkan seperti jantung yang memompa pasokan darah bersih dan stabil ke seluruh organ tubuh PC.",
        "penjelasan": (
            "PSU adalah komponen paling krusial untuk keselamatan PC rakitan:\n"
            "1. **Sertifikasi Efisiensi 80+ (Bronze / Gold):** Menjamin efisiensi konversi listrik di atas 80%, menghemat tagihan listrik dan meminimalkan panas terbuang.\n"
            "2. **Fitur Proteksi (OVP, OPP, SCP):** Melindungi komponen mahal (GPU dan Motherboard) dari lonjakan voltase atau korsleting.\n"
            "3. **Kapasitas Watt yang Tepat:** Contohnya 550W untuk rig i5/Ryzen 5 + RTX 3050/4060, dan 650W–750W+ untuk kartu grafis kelas atas seperti RTX 4070 series."
        )
    },
    "motherboard": {
        "istilah": "Motherboard / Mainboard - Papan Sirkuit Penghubung",
        "analogi": "Diibaratkan sebagai pondasi rangka kota dan jalan raya utama yang menghubungkan semua komponen komputer.",
        "penjelasan": (
            "Hal yang wajib diperhatikan pada motherboard:\n"
            "1. **Socket & Kompatibilitas:** Socket LGA1700 (Intel Gen 12-14) atau Socket AM5 (AMD Ryzen 7000/9000).\n"
            "2. **Kelas Chipset:** Kelas H/A (Entry level/Budget), Kelas B (Mid-range paling populer dengan fitur seimbang), dan Kelas Z/X (Flagship dengan dukungan overclocking penuh).\n"
            "3. **Slot Ekspansi & VRM:** Kualitas heatsink daya (VRM) untuk kestabilan pasokan arus ke prosesor dan slot M.2 NVMe tambahan untuk SSD masa depan."
        )
    },
    "cooler": {
        "istilah": "CPU Cooler (Pendingin Prosesor): Air Cooler vs AIO Liquid Cooler",
        "analogi": "Sistem pendingin mesin mobil yang menjaga suhu prosesor tetap adem di batas kerja optimal.",
        "penjelasan": (
            "1. **Air Cooler (Kipas & Heatpipe Tembaga):** Sangat andal, bebas resiko kebocoran cairan, biaya ramah kantong, dan sangat awet untuk pemakaian harian jangka panjang (bahkan 5-10 tahun).\n"
            "2. **AIO Liquid Cooler (Radiator & Pompa Cairan):** Tampilan visual sangat estetik dan bersih di dalam casing kaca, serta sangat efektif meredam lonjakan suhu prosesor berdaya tinggi saat rendering 3D atau render video berjam-jam."
        )
    },
    "bottleneck": {
        "istilah": "Bottleneck (Ketidakseimbangan Komponen PC)",
        "analogi": "Diibaratkan mesin mobil balap Ferrari yang dipasangi ban sepeda mini; salah satu komponen menghambat performa keseluruhan.",
        "penjelasan": (
            "Bottleneck terjadi jika salah satu part tertinggal jauh dibanding part lainnya. "
            "Contohnya: Menggabungkan GPU kencang (seperti RTX 4070) dengan prosesor lama 4-core, sehingga GPU tidak bisa mengeluarkan performa maksimal 100%. "
            "Di toko kami, tim teknisi selalu memastikan sinergi dan perbandingan performa antara CPU, GPU, dan RAM seimbang dan efisien."
        )
    }
}

