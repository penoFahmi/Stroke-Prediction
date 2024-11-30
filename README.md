---

# Stroke Prediction Web App

Aplikasi web prediksi stroke menggunakan machine learning yang dibuat dengan Streamlit. Aplikasi ini memungkinkan pengguna untuk memprediksi kemungkinan terkena stroke berdasarkan input data pribadi dan medis mereka.

## **Fitur Aplikasi**
- Prediksi risiko stroke berdasarkan beberapa parameter seperti usia, tekanan darah, riwayat penyakit jantung, status merokok, dan lainnya.
- Antarmuka pengguna yang ramah dengan Streamlit, memudahkan pengguna untuk memberikan input dan mendapatkan hasil prediksi.

### **Deskripsi File**
- `app.py`: File utama aplikasi Streamlit yang digunakan untuk menjalankan antarmuka pengguna dan prediksi.
- `stroke_model.pkl`: File model yang telah dilatih menggunakan RandomForestClassifier untuk memprediksi risiko stroke.
- `data_preprocessing.ipynb`: Jupyter notebook untuk preprocessing data dan pelatihan model.
- `dataset.csv`: Dataset asli yang digunakan untuk pelatihan model, yang diambil dari Kaggle.
- `requirements.txt`: Daftar dependensi yang diperlukan untuk menjalankan aplikasi.

## **Instalasi dan Persyaratan**
Untuk menjalankan aplikasi ini secara lokal, Anda perlu menginstal beberapa dependensi. Ikuti langkah-langkah berikut:

### 1. **Clone Repository**
Clone repository ini ke mesin lokal Anda:

```bash
git clone https://github.com/username/repository-name.git
cd repository-name
```

### 2. **Buat Virtual Environment**
Buat virtual environment untuk mengisolasi dependensi:

```bash
python3 -m venv venv
```

### 3. **Aktifkan Virtual Environment**
- Di Windows:

```bash
venv\Scripts\activate
```

- Di MacOS/Linux:

```bash
source venv/bin/activate
```

### 4. **Install Dependensi**
Install semua dependensi yang diperlukan:

```bash
pip install -r requirements.txt
```

### 5. **Jalankan Aplikasi**
Jalankan aplikasi Streamlit:

```bash
streamlit run app/app.py
```

Aplikasi akan berjalan di browser pada alamat [http://localhost:8501](http://localhost:8501).

## **Cara Penggunaan**
1. **Input Data:**
   - Pilih nilai untuk setiap parameter seperti `Gender`, `Age`, `Hypertension`, `Heart Disease`, dll.
   - Klik tombol **Predict** untuk melihat prediksi risiko stroke.

2. **Hasil Prediksi:**
   - Jika model memprediksi risiko stroke, aplikasi akan menampilkan pesan peringatan.
   - Jika model memprediksi tidak ada risiko stroke, aplikasi akan menampilkan pesan sukses.

## **Deploy di Streamlit Cloud**
Untuk melakukan deploy aplikasi di Streamlit Cloud:

1. **Buat Repository GitHub** untuk proyek ini.
2. **Push semua file** ke repository GitHub Anda.
3. **Login ke Streamlit Cloud** di [Streamlit.io](https://streamlit.io/cloud).
4. Klik **New App**, pilih repository GitHub Anda, dan tentukan file utama (app.py) dan `requirements.txt`.
5. Klik **Deploy** dan aplikasi akan berjalan di Streamlit Cloud.

## **Model**
Model yang digunakan adalah Random Forest Classifier yang dilatih menggunakan dataset stroke dari Kaggle. Model ini dapat memprediksi apakah seseorang berisiko mengalami stroke berdasarkan data medis dan demografi.

## **Kontribusi**
Jika Anda ingin berkontribusi pada proyek ini, silakan ikuti langkah-langkah berikut:
1. Fork repository ini.
2. Buat cabang baru (`git checkout -b feature-branch`).
3. Lakukan perubahan Anda.
4. Commit perubahan (`git commit -am 'Add new feature'`).
5. Push ke cabang Anda (`git push origin feature-branch`).
6. Buat pull request.

## **Lisensi**
Proyek ini dilisensikan di bawah [MIT License](LICENSE).

---
