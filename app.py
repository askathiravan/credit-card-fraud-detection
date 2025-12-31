import streamlit as st
import pandas as pd
import joblib
import mysql.connector
from db_config import get_connection

# Load ML model
model = joblib.load("model/fraud_model.pkl")

st.set_page_config(page_title="Fraud Detection System", layout="wide")
st.title("💳 Credit Card Fraud Detection & Risk Scoring System")

# ---------- INPUT FORM ----------
st.subheader("Enter Transaction Details")

amount = st.number_input("Transaction Amount", min_value=0.0)
hour = st.slider("Transaction Hour (0–23)", 0, 23)
location = st.selectbox("Transaction Location", ["Domestic", "International"])
merchant = st.selectbox("Merchant Category", ["Retail", "E-commerce", "Fuel", "ATM"])
txn_type = st.selectbox("Transaction Type", ["Online", "Offline"])

# Encode inputs
location_map = {"Domestic": 0, "International": 1}
merchant_map = {"Retail": 0, "E-commerce": 1, "Fuel": 2, "ATM": 3}
txn_map = {"Online": 1, "Offline": 0}

# ---------- RISK SCORE LOGIC ----------
def calculate_risk(amount, hour, location, txn_type):
    risk = 0
    if amount > 5000:
        risk += 30
    if hour >= 22 or hour <= 5:
        risk += 20
    if location == "International":
        risk += 25
    if txn_type == "Online":
        risk += 15
    return min(risk, 100)

if st.button("Check Transaction"):
    input_data = [[
        amount,
        hour,
        location_map[location],
        merchant_map[merchant],
        txn_map[txn_type]
    ]]

    prediction = model.predict(input_data)[0]
    risk_score = calculate_risk(amount, hour, location, txn_type)

    status = "Fraud" if prediction == 1 else "Safe"

    # Save to DB
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO transactions 
        (amount, hour, location, merchant, txn_type, prediction, risk_score)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, (
        amount, hour, location, merchant,
        txn_type, status, risk_score
    ))
    conn.commit()
    conn.close()

    # Output
    st.subheader("Result")
    st.write(f"**Prediction:** {status}")
    st.write(f"**Risk Score:** {risk_score}%")

    if risk_score >= 70:
        st.error("🚨 High Risk Transaction")
    elif risk_score >= 40:
        st.warning("⚠️ Medium Risk Transaction")
    else:
        st.success("✅ Low Risk Transaction")

# ---------- DASHBOARD ----------
st.subheader("📊 Fraud Monitoring Dashboard")

conn = get_connection()
df = pd.read_sql("SELECT * FROM transactions", conn)
conn.close()

st.metric("Total Transactions", len(df))
st.metric("Fraud Transactions", len(df[df["prediction"] == "Fraud"]))

st.dataframe(df)
