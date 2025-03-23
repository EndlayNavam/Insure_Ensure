import joblib
import pandas as pd

# ✅ Load the trained model & encoders
model = joblib.load("model/insurance_model.pkl")
label_encoders = joblib.load("model/label_encoders.pkl")

# ✅ Define test user data
user_data = {
    "Age": 35,
    "Income": 60000,
    "Family Size": 3,
    "Employment Type": "Private Job",
    "Health Conditions": "Diabetes",
    "Existing Policy": "Health",
    "Past Claims": 2,
    "Claim Amount": 45000,
    "Claim Approved": "Yes",
    "Reimbursement Time (Days)": 10,
    "Claim Success Rate (%)": 85,
    "Customer Satisfaction": 4.2,
}

# ✅ Convert categorical values to encoded values
for col in label_encoders:
    if col in user_data:  # ✅ Check if the column exists in input data
        user_data[col] = label_encoders[col].transform([user_data[col]])[0]

# ✅ Convert user data into a DataFrame
user_df = pd.DataFrame([user_data])

# ✅ Make a prediction
predicted_policy_encoded = model.predict(user_df)[0]

# ✅ Decode the predicted policy back to text
predicted_policy = label_encoders["Recommended Policy"].inverse_transform([predicted_policy_encoded])[0]

print(f"✅ Recommended Policy: {predicted_policy}")
