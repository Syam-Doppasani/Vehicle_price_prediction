# app.py

import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("vehicle_price_model.pkl")

st.title("🚗 Vehicle Price Predictor")

# User input
make = st.selectbox("Make", [
    "Jeep", "GMC", "Dodge", "RAM", "Nissan", "Ford", "Hyundai", "Chevrolet",
    "Volkswagen", "Chrysler", "Kia", "Acura", "Mazda", "Subaru", "Audi", "BMW",
    "Toyota", "Buick", "Mercedes-Benz", "Lincoln", "Cadillac", "INFINITI",
    "Lexus", "Honda", "Land Rover", "Volvo", "Jaguar"
])

model_input = st.text_input("Model (e.g., Camry, F-150)")
year = st.number_input("Year", min_value=1990, max_value=2025, value=2015)
mileage = st.number_input("Mileage", min_value=0, max_value=500000, value=60000)
fuel = st.selectbox("Fuel Type", ["Gasoline", "Diesel", "Electric", "Hybrid"])
transmission = st.selectbox("Transmission", ["Automatic", "Manual"])
body = st.selectbox("Body Style", ["Sedan", "SUV", "Truck", "Coupe", "Hatchback"])
drivetrain = st.selectbox("Drivetrain", ["Front-wheel Drive", "Rear-wheel Drive", "All-wheel Drive"])
engine = st.text_input("Engine (e.g., 2.0L I4 Turbo)")

if st.button("Predict Price"):
    input_df = pd.DataFrame([{
        "make": make,
        "model": model_input,
        "year": year,
        "mileage": mileage,
        "fuel": fuel,
        "transmission": transmission,
        "body": body,
        "drivetrain": drivetrain,
        "engine": engine
    }])

    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Price: ${prediction:,.2f}")
