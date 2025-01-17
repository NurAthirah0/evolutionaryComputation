import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Title of the app
st.title("Loan Eligibility Prediction")

# File uploader
uploaded_file = st.file_uploader("Upload Loan Dataset (CSV)", type="csv")

if uploaded_file is not None:
    # Load the dataset
    df = pd.read_csv(uploaded_file)
    st.write("Dataset Preview:")
    st.dataframe(df.head())
    
    # Preprocess the data
    df = df.drop(['Loan_ID'], axis=1)
    df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
    df['Married'].fillna(df['Married'].mode()[0], inplace=True)
    df['Dependents'].fillna(df['Dependents'].mode()[0], inplace=True)
    df['Self_Employed'].fillna(df['Self_Employed'].mode()[0], inplace=True)
    df['Credit_History'].fillna(df['Credit_History'].mode()[0], inplace=True)
    df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0], inplace=True)
    df['LoanAmount'].fillna(df['LoanAmount'].mean(), inplace=True)
    
    # Encoding categorical variables
    df = pd.get_dummies(df, drop_first=True)
    
    # Feature-target split
    X = df.drop("Loan_Status_Y", axis=1)
    y = df["Loan_Status_Y"]
    
    # Scaling
    X = MinMaxScaler().fit_transform(X)
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    
    # Logistic Regression
    model = LogisticRegression(solver='saga', max_iter=500, random_state=1)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    # Accuracy
    acc = accuracy_score(y_test, y_pred)
    st.write(f"Model Accuracy: {acc * 100:.2f}%")
    st.text("Classification Report:")
    st.text(classification_report(y_test, y_pred))
    
    # Prediction
    st.subheader("Make a Prediction")
    inputs = {}
    for column in df.columns[:-1]:
        inputs[column] = st.number_input(column, value=0.0)
    inputs_df = pd.DataFrame([inputs])
    
    if st.button("Predict"):
        prediction = model.predict(inputs_df)
        result = "Approved" if prediction[0] == 1 else "Rejected"
        st.write(f"Loan Status: {result}")
