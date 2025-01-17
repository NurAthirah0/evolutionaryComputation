import streamlit as st
import pickle
import numpy as np

# Load the logistic regression model
with open("logistic_regression_model.pkl", "rb") as file:
    model = pickle.load(file)

# Title of the app
st.title("Loan Eligibility Prediction")

# Input fields
st.header("Enter Applicant Details")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self-Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_amount_term = st.number_input("Loan Amount Term (months)", min_value=0)
credit_history = st.selectbox("Credit History", ["Good (1)", "Bad (0)"])
property_area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])

# Data preprocessing for prediction
def preprocess_input():
    gender_val = 1 if gender == "Male" else 0
    married_val = 1 if married == "Yes" else 0
    education_val = 1 if education == "Graduate" else 0
    self_employed_val = 1 if self_employed == "Yes" else 0
    credit_history_val = 1 if credit_history == "Good (1)" else 0
    property_area_urban = 1 if property_area == "Urban" else 0
    property_area_rural = 1 if property_area == "Rural" else 0
    property_area_semiurban = 1 if property_area == "Semiurban" else 0

    # Return processed input as a single array
    return np.array([[
        gender_val, married_val, education_val, self_employed_val,
        np.sqrt(applicant_income), np.sqrt(coapplicant_income),
        np.sqrt(loan_amount), loan_amount_term,
        credit_history_val, property_area_rural, property_area_semiurban
    ]])

# Predict button
if st.button("Predict Loan Eligibility"):
    input_data = preprocess_input()
    prediction = model.predict(input_data)
    result = "Eligible" if prediction[0] == 1 else "Not Eligible"
    st.success(f"The applicant is {result}.")

