import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("diabetes_model.pkl")

st.title("Diabetes Prediction App")
st.write("Enter patient details:")

# User inputs
age = st.number_input("Age", min_value=0)
chol = st.number_input("Cholesterol", min_value=0)
glu = st.number_input("Stabilized Glucose", min_value=0)
hdl = st.number_input("HDL", min_value=0)
hba1c = st.number_input("HbA1c", min_value=0.0)
bp_sys = st.number_input("Systolic BP", min_value=0)
bp_dia = st.number_input("Diastolic BP", min_value=0)

if st.button("Predict"):
    # IMPORTANT: order must match training
    input_data = pd.DataFrame([[
        age,
        chol,
        glu,
        hdl,
        hba1c,
        bp_sys,
        bp_dia
    ]], columns=[
        "age",
        "chol",
        "stab_glu",
        "hdl",
        "glyhb",
        "bp.1s",
        "bp.1d"
    ])

    result = model.predict(input_data)

    if result[0] == 1:
        st.error("Diabetic")
    else:
        st.success("Non-Diabetic")
