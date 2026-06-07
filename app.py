import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("loan_model.pkl", "rb"))

st.title("Loan Approval Prediction System")
st.write("Enter customer details to predict loan approval")

income = st.number_input("Annual Income")
loan_amount = st.number_input("Loan Amount")
loan_term = st.number_input("Loan Term (months)")
cibil_score = st.number_input("CIBIL Score")
dependents = st.number_input("No of Dependents")
assets = st.number_input("Total Assets Value")
self_employed = st.selectbox("Self Employed", [0, 1])
education = st.selectbox("Education (Graduate=1 / Not=0)", [0, 1])

if st.button("Predict Loan Status"):

    input_data = np.array([[dependents, education, self_employed,income, loan_amount, loan_term,cibil_score, assets, 0, 0, 0, 0]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")