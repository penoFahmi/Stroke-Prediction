import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('../models/stroke_model.pkl')

st.title("Stroke Prediction App")

# Input user
age = st.number_input("Age", min_value=0, max_value=120, step=1, value=25)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, step=0.1, value=20.0)
glucose = st.number_input("Average Glucose Level", min_value=50.0, max_value=300.0, step=1.0, value=100.0)

gender = st.selectbox("Gender", options=["Male", "Female"])
smoking_status = st.selectbox("Smoking Status", options=["never smoked", "formerly smoked", "smokes"])

# Encode inputs
gender_encoded = 1 if gender == "Male" else 0
smoking_encoded = {"never smoked": 0, "formerly smoked": 1, "smokes": 2}[smoking_status]

# Predict
if st.button("Predict"):
    input_data = np.array([[age, bmi, glucose, gender_encoded, smoking_encoded]])
    prediction = model.predict(input_data)
    result = "Stroke" if prediction[0] == 1 else "No Stroke"
    st.write(f"The prediction is: **{result}**")
