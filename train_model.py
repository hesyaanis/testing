"""
SKRIP PELATIHAN MACHINE LEARNING (INTENT CLASSIFIER TOKO LAPTOP)
===============================================================
Skrip ini melakukan alur standar Machine Learning (ML Pipeline):
1. Memuat dataset percakapan (Data Preparation)
2. Pra-pemrosesan Teks & Ekstraksi Fitur (TF-IDF Vectorization)
3. Pelatihan Model Klasifikasi (Logistic Regression / Naive Bayes)
4. Evaluasi Akurasi (Classification Report)
5. Menyimpan Model Hasil Pelatihan (.pkl) untuk dipakai aplikasi
"""

import os
import sys
import json
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def main():
    print("=" * 60)
    print("🤖 MEMULAI PELATIHAN MACHINE LEARNING (TRAINING PIPELINE)")
    print("=" * 60)

    # 1. Memuat Dataset
    dataset_file = "dataset_chat_latihan.json"
    if not os.path.exists(dataset_file):
        print(f"Error: File {dataset_file} tidak ditemukan!")
        return

    with open(dataset_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    print(f"✅ Dataset berhasil dimuat: {len(df)} sampel data percakapan.")
    print("\nDistribusi Kategori Intent:")
    print(df["intent"].value_counts().to_string())

    # 2. Split Data: Training Set (80%) & Testing Set (20%)
    X_train, X_test, y_train, y_test = train_test_split(
        df["text"],
        df["intent"],
        test_size=0.2,
        random_state=42,
        stratify=df["intent"]
    )
    print(f"\n📊 Pembagian Data: {len(X_train)} data latih (Train), {len(X_test)} data uji (Test).")

    # 3. Ekstraksi Fitur Teks dengan TF-IDF
    print("\n⚙️ Mengekstrak fitur teks dengan TF-IDF...")
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=1)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # 4. Melatih Model (Model Training - Multinomial Naive Bayes)
    print("🧠 Melatih Model Klasifikasi (Multinomial Naive Bayes)...")
    from sklearn.naive_bayes import MultinomialNB
    model = MultinomialNB(alpha=0.3)
    model.fit(X_train_vec, y_train)

    # 5. Evaluasi Performa Model
    y_pred = model.predict(X_test_vec)
    acc = accuracy_score(y_test, y_pred)
    print(f"\n🎯 Akurasi Model pada Data Uji: {acc * 100:.2f}%")
    print("\nLaporan Klasifikasi Detail:")
    print(classification_report(y_test, y_pred, zero_division=0))

    # 6. Menyimpan Model Hasil Latihan
    model_output = {
        "model": model,
        "vectorizer": vectorizer
    }
    output_filename = "model_intent_laptop.pkl"
    joblib.dump(model_output, output_filename)
    print(f"💾 Model berhasil disimpan ke file: '{output_filename}'!")

    # 7. Uji Coba Langsung dengan Kalimat Baru yang Belum Pernah Dilihat Model
    print("\n" + "=" * 60)
    print("🧪 UJI PREDIKSI MODEL DENGAN KALIMAT BARU")
    print("=" * 60)
    
    kalimat_test = [
        "gw punya duit 7 juta pas, dapet laptop apa ya?",
        "bedanya layar ips sama oled apaan?",
        "masih ada stok advan?",
        "review laptop acer swift oled dong bro",
        "halo selamat sore bang"
    ]

    for k in kalimat_test:
        vec = vectorizer.transform([k])
        pred_intent = model.predict(vec)[0]
        probabilitas = max(model.predict_proba(vec)[0]) * 100
        print(f"Kalimat : \"{k}\"")
        print(f"Hasil Prediksi Intent -> [{pred_intent}] (Keyakinan: {probabilitas:.1f}%)\n")

if __name__ == "__main__":
    main()
