import streamlit as st
import joblib
import pandas as pd

# Load the model and scaler
model = joblib.load('fraud_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("🛡️ Fraud Detection System")

# Create inputs for the user
amount = st.number_input("Transaction Amount", min_value=0.0)

if st.button("Check for Fraud"):
    # Preprocess input
    input_data = pd.DataFrame([[0, amount]], columns=['Time', 'Amount']) # Dummy Time
    input_data['Amount'] = scaler.transform(input_data[['Amount']])
    
    # Predict
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("🚨 Fraudulent Transaction Detected!")
    else:
        st.success("✅ Transaction is Legitimate.")
