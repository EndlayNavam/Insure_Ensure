import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib  # For saving the trained model

# ✅ Load dataset
df = pd.read_csv("insurance_wide_dataset.csv")  # Ensure this file exists

# ✅ Encode categorical features
label_encoders = {}
categorical_columns = ["Employment Type", "Health Conditions", "Existing Policy", "Claim Approved", "Recommended Policy"]

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])  # Convert categorical values to numbers
    label_encoders[col] = le  # Save encoders for later decoding

# ✅ Define input (X) and output (y)
X = df.drop(columns=["ID", "Recommended Policy"])  # Features
y = df["Recommended Policy"]  # Target variable

# ✅ Split dataset into training & testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ✅ Ensure the 'model/' directory exists before saving
if not os.path.exists("model"):
    os.makedirs("model")

# ✅ Save the trained model & encoders
joblib.dump(model, "model/insurance_model.pkl")
joblib.dump(label_encoders, "model/label_encoders.pkl")  # ✅ Save the encoder for 'Recommended Policy'

print("✅ Model trained and saved successfully!")
