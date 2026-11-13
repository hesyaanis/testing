# 💻 AI Toko Laptop - "Bro Aris" (Teman Konsultan Gadget)

Prototipe AI untuk Toko Laptop yang dirancang untuk **menjelaskan spesifikasi**, **memberikan rekomendasi jujur & solutif**, dan **berbicara santai layaknya teman tongkrongan yang paham gadget**.

---

## 📁 Struktur File

```
tetsing aja/
├── katalog_laptop.json       # Database katalog laptop (spek, harga, kelebihan, catatan jujur, stok)
├── hardware_knowledge.py     # Kamus analogi hardware (RAM, SSD, GPU, Layar IPS vs OLED, Prosesor)
├── recommender.py           # Logika penilaian & pencocokan kebutuhan pembeli + filter budget
├── bot_persona.py           # Persona Bro Aris (Mesin Lokal Pintar + Integrasi Cloud LLM Gemini)
├── app.py                   # Aplikasi terminal interaktif dengan UI Rich Console
├── .env.example             # Contoh file konfigurasi API Key (opsional)
└── README.md                # Dokumentasi & panduan penggunaan
```

---

## 🚀 Cara Menjalankan

Buka terminal di folder proyek ini, lalu jalankan:

```bash
python app.py
```

### Fitur yang Bisa Dicoba di Terminal:
1. **Minta Rekomendasi Sesuai Budget & Kebutuhan:**
   - *"Bro, ada laptop 7 jutaan yang enak buat kuliah IT & ngoding?"*
   - *"Cariin laptop gaming 14 jutaan yang layarnya udah bagus dong"*
   - *"Budget 10 juta pengen yang enteng buat dibawa kantor"*
2. **Tanya Penjelasan Hardware (Bahasa Awam):**
   - *"Bedanya RAM 8GB sama 16GB apa ya bro?"*
   - *"Jelasin dong apa bedanya layar IPS sama OLED?"*
   - *"Apa bedanya SSD sama harddisk?"*
3. **Minta Review Spesifik Suatu Laptop:**
   - *"Review jujur Advan Workplus dong, plus minusnya apa?"*
   - *"Gimana spek Lenovo LOQ?"*
4. **Cek Seluruh Stok Toko:**
   - Ketik `katalog` atau `stok`

---

## ⚙️ Dua Mode Mesin (Dual-Mode)

1. **⚡ Smart Local Engine (Bawaan / Default):**
   - Berjalan 100% lokal, cepat, hemat, dan tidak butuh kuota/API key.
   - Menggunakan algoritma scoring kebutuhan + basis data analogi santai.

2. **🌐 Cloud LLM (Google Gemini 2.5 Flash):**
   - Jika ingin respon yang 100% bebas percakapan natural dan lebih fleksibel:
   - Salin file `.env.example` menjadi `.env`.
   - Masukkan API Key gratis dari [Google AI Studio](https://aistudio.google.com/app/apikey).
   - Jalankan ulang `python app.py`. AI akan otomatis beralih ke Mode Gemini.

---

## ➕ Cara Menambah Laptop Baru ke Katalog

Cukup buka file [katalog_laptop.json](file:///c:/Users/kingd/OneDrive/Documents/Belajar/tetsing%20aja/katalog_laptop.json) dan tambahkan objek baru dengan format:

```json
{
  "id": "LP-006",
  "nama": "Nama Laptop Baru",
  "brand": "Merk",
  "harga": 8500000,
  "kategori": "Kategori Laptop",
  "target_user": ["kuliah", "kantor", "editing"],
  "spesifikasi": {
    "prosesor": "...",
    "gpu": "...",
    "ram": "...",
    "storage": "...",
    "layar": "...",
    "baterai": "...",
    "berat": "1.4 kg"
  },
  "kelebihan": [
    "Kelebihan utama 1"
  ],
  "catatan_jujur": [
    "Kekurangan yang perlu pembeli ketahui"
  ],
  "game_support": "Keterangan game",
  "stok": 5
}
```
