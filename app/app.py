"""Streamlit application for customer churn prediction."""

import streamlit as st


st.set_page_config(page_title="Customer Churn Predictor", page_icon="📉")
st.title("Customer Churn Predictor")
st.write("This app will display churn probability, RFM segment, and SHAP explanations.")

customer_id = st.text_input("Customer ID", value="")
if st.button("Predict"):
    if customer_id:
        st.info(f"Scoring Customer ID: {customer_id}")
    else:
        st.warning("Please enter a customer ID.")

