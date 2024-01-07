import streamlit as st
import pickle
import pandas as pd

# Load the model
model = pickle.load(open("rf_model.sav", "rb"))

# Define input features with appropriate data types and options
st.title("Drug Prediction App")

age = st.number_input("Enter patient's age:", min_value=1, max_value=120)
na_to_k = st.number_input("Enter Na_to_K ratio:", min_value=0.0)
sex_m = st.radio("Select patient's sex:", options=["M", "F"])
bp = st.selectbox("Select patient's blood pressure:", options=["LOW", "NORMAL", "HIGH"])
cholesterol_normal = st.selectbox("Is cholesterol normal?:", options=["Yes", "No"])

# Create a DataFrame with appropriate dummy encoding
df = pd.DataFrame({
    "Age": [age],
    "Na_to_K": [na_to_k],
    "Sex_M": [1 if sex_m == "M" else 0],  # Apply dummy encoding for sex
    "BP_LOW": [1 if bp == "LOW" else 0],  # Apply dummy encoding for blood pressure
    "BP_NORMAL": [1 if bp == "NORMAL" else 0],  # (assuming "HIGH" is the reference category)
    "Cholesterol_NORMAL": [1 if cholesterol_normal == "Yes" else 0]
})

# Make predictions and display results in a user-friendly format
if st.button("Predict Drug"):
    prediction = model.predict(df)[0]  # Predict for a single sample
    drug_name = {0: "Drug X", 1: "Drug Y", 2: "Drug C", 3: "Drug A", 4: "Drug B"}[prediction]
    st.subheader("Recommended Drug:")
    st.success(drug_name)


