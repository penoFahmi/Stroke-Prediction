import streamlit as st
import joblib
import numpy as np
import os

# Load model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "../models/stroke_best_model.pkl")
model = joblib.load(model_path)

# Set up title and page layout
st.set_page_config(page_title="Aplikasi Prediksi Stroke", layout="wide")
st.title("Aplikasi Prediksi Stroke")

# Deskripsi aplikasi
st.markdown("""
Aplikasi ini memprediksi apakah seseorang berisiko mengalami stroke berdasarkan data usia, BMI, level glukosa, jenis kelamin, status merokok, status pernikahan, dan jenis tempat tinggal.
Silakan masukkan data Anda untuk melihat prediksi.
""")

# Input dari pengguna
age = st.number_input("Usia", min_value=0, max_value=120, step=1, value=25)
bmi = st.number_input("Indeks Massa Tubuh (BMI)", min_value=10.0, max_value=50.0, step=0.1, value=20.0)
glucose = st.number_input("Rata-rata Level Glukosa", min_value=50.0, max_value=300.0, step=1.0, value=100.0)

gender = st.selectbox("Jenis Kelamin", options=["Laki-laki", "Perempuan"])
smoking_status = st.selectbox("Status Merokok", options=["Tidak pernah merokok", "Pernah merokok", "Merokok"])
married = st.selectbox("Apakah Anda sudah menikah?", options=["Ya", "Tidak"])
residence = st.selectbox("Jenis Tempat Tinggal", options=["Urban", "Rural"])

# Encode inputs
gender_encoded = 1 if gender == "Laki-laki" else 0
smoking_encoded = {"Tidak pernah merokok": 0, "Pernah merokok": 1, "Merokok": 2}[smoking_status]
married_encoded = 1 if married == "Ya" else 0
residence_encoded = 1 if residence == "Urban" else 0

# Gabungkan semua fitur
input_data = np.array([[age, bmi, glucose, gender_encoded, smoking_encoded, married_encoded, residence_encoded]])

# Predict
if st.button("Prediksi"):
    prediction = model.predict(input_data)
    result = "Stroke" if prediction[0] == 1 else "Tidak Stroke"
    st.write(f"Prediksi hasilnya adalah: **{result}**")
