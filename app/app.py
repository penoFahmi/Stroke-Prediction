import streamlit as st
import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "../models/stroke_model.pkl")
model = joblib.load(model_path)


# # Load model
# model = joblib.load('../models/stroke_model.pkl')

# Set up title and page layout
st.set_page_config(page_title="Aplikasi Prediksi Stroke", layout="wide")
st.title("Aplikasi Prediksi Stroke")

# Deskripsi aplikasi
st.markdown("""
Aplikasi ini memprediksi apakah seseorang berisiko mengalami stroke berdasarkan data usia, BMI, level glukosa, jenis kelamin, dan status merokok.
Silakan masukkan data Anda untuk melihat prediksi.
""")

# Input dari pengguna
age = st.number_input("Usia", min_value=0, max_value=120, step=1, value=25)
bmi = st.number_input("Indeks Massa Tubuh (BMI)", min_value=10.0, max_value=50.0, step=0.1, value=20.0)
glucose = st.number_input("Rata-rata Level Glukosa", min_value=50.0, max_value=300.0, step=1.0, value=100.0)

gender = st.selectbox("Jenis Kelamin", options=["Laki-laki", "Perempuan"])
smoking_status = st.selectbox("Status Merokok", options=["Tidak pernah merokok", "Pernah merokok", "Merokok"])

# Encode inputs
gender_encoded = 1 if gender == "Laki-laki" else 0
smoking_encoded = {"Tidak pernah merokok": 0, "Pernah merokok": 1, "Merokok": 2}[smoking_status]

# Predict
if st.button("Prediksi"):
    input_data = np.array([[age, bmi, glucose, gender_encoded, smoking_encoded]])
    prediction = model.predict(input_data)
    result = "Stroke" if prediction[0] == 1 else "Tidak Stroke"
    st.write(f"Prediksi hasilnya adalah: **{result}**")

# Add additional styling or image
st.markdown("""
    <style>
        .stButton>button {
            background-color: #FF6F61;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px 20px;
        }
        .stTitle {
            font-size: 36px;
            color: #2E3A59;
        }
    </style>
""", unsafe_allow_html=True)

# You can also add an image if you'd like:
# st.image("stroke_image.png", width=700)
