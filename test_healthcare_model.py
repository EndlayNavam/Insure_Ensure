import joblib
import pandas as pd

# ✅ Load the trained model & encoders
model = joblib.load("model/healthcare_insurance_model.pkl")
label_encoders = joblib.load("model/healthcare_label_encoders.pkl")

# ✅ Define test user data
user_data = {
    "Age": 40,
    "BMI": 28.5,
    "Smoking": "Yes",
    "Disease": "Heart Disease",
    "Symptoms": ["Chest Pain", "Breathlessness"],  # Multiple symptoms
    "Severity": "High",
    "Diagnosis Method": "ECG",
    "Treatment Type": "Surgery",
    "Claim Amount ($)": 120000,
    "Reimbursement Rate (%)": 85,
    "Deductible ($)": 10000,
    "Interest Rate (%)": 3.5,
    "Approval Time (Days)": 20,
    "Insurance Provider": "HeartCare Inc."
}

# ✅ Convert categorical values to encoded values
for col in label_encoders:
    if col in user_data and col != "Symptom_Columns":  # Exclude Symptoms (handled separately)
        user_data[col] = label_encoders[col].transform([user_data[col]])[0]

# ✅ Convert Symptoms to binary features using saved column names
for symptom in label_encoders["Symptom_Columns"]:
    user_data[symptom] = 1 if symptom in user_data["Symptoms"] else 0

# ✅ Remove original Symptoms column
del user_data["Symptoms"]

# ✅ Convert user data into a DataFrame
user_df = pd.DataFrame([user_data])

# ✅ Make a prediction
predicted_policy_encoded = model.predict(user_df)[0]

# ✅ Decode the predicted policy back to text
predicted_policy = label_encoders["Insurance Type"].inverse_transform([predicted_policy_encoded])[0]

print(f"✅ Recommended Insurance Policy: {predicted_policy}")
