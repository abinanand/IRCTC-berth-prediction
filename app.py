import streamlit as st
import pandas as pd
import joblib

# Load model + encoders
model = joblib.load("model.pkl")
encoders = joblib.load("encoders.pkl")

st.set_page_config(page_title="IRCTC Berth Predictor", layout="centered")

st.title("🚆 IRCTC Berth Prediction System")

st.write("Enter passenger details to predict berth allocation")

# ---------------- INPUTS ---------------- #
age = st.slider("Age", 18, 70)

gender = st.selectbox("Gender", ["M", "F"])
booking_status = st.selectbox("Booking Status", ["CNF", "RAC", "WL"])
quota = st.selectbox("Quota", ["GN", "TQ", "LD"])
coach = st.selectbox("Coach Type", ["SL", "3AC", "2AC"])

booking_time = st.slider("Booking Hour", 0, 23)
distance = st.number_input("Travel Distance (km)", 100, 2000)

wl = st.number_input("Waiting List Number", 0, 20)

pref = st.selectbox("Seat Preference", ["LB", "UB", "SL", "Unknown"])

# ---------------- FEATURE ENGINEERING ---------------- #
seat_pref_missing = 1 if pref == "Unknown" else 0

# ---------------- PREDICT BUTTON ---------------- #
if st.button("Predict Berth"):

    input_df = pd.DataFrame([[age, gender, booking_status, quota, coach,
                              booking_time, distance, wl, pref, seat_pref_missing]],
                            columns=[
                                "age", "gender", "booking_status", "quota",
                                "coach_type", "booking_time",
                                "travel_distance", "waiting_list_number",
                                "seat_preference", "seat_pref_missing"
                            ])

    # Encode categorical columns
    for col in input_df.columns:
        if col in encoders:
            input_df[col] = encoders[col].transform(input_df[col])

    # Prediction
    prediction = model.predict(input_df)

    # Decode output
    result = encoders["berth_type"].inverse_transform(prediction)

    st.success(f"🎯 Predicted Berth: {result[0]}")