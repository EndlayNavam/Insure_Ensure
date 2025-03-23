import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib  # For saving the trained model

# ✅ Load dataset
df = pd.read_csv("healthcare_insurance_dataset.csv")  # Ensure this file exists

# ✅ Convert Symptoms (Multi-Value) into Separate Binary Columns
symptom_columns = set()  # Collect all unique symptoms

# Extract individual symptoms
for symptoms in df["Symptoms"]:
    for symptom in symptoms.split(", "):  # Split comma-separated values
        symptom_columns.add(symptom)

# Convert symptoms into separate binary columns
for symptom in symptom_columns:
    df[symptom] = df["Symptoms"].apply(lambda x: 1 if symptom in x else 0)

# ✅ Drop original Symptoms column
df.drop(columns=["Symptoms"], inplace=True)

# ✅ Encode categorical features
label_encoders = {}
categorical_columns = ["Smoking", "Disease", "Severity", "Diagnosis Method", "Treatment Type", 
                       "Insurance Type", "Insurance Provider"]

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])  # Convert categorical values to numbers
    label_encoders[col] = le  # Save encoders for later decoding

# ✅ Save the list of symptom column names
label_encoders["Symptom_Columns"] = list(symptom_columns)  # Store symptom columns separately

# ✅ Define input (X) and output (y)
X = df.drop(columns=["ID", "Insurance Type"])  # Features
y = df["Insurance Type"]  # Target variable

# ✅ Split dataset into training & testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ✅ Ensure the 'model/' directory exists before saving
if not os.path.exists("model"):
    os.makedirs("model")

# ✅ Save the trained model & encoders
joblib.dump(model, "model/healthcare_insurance_model.pkl")
joblib.dump(label_encoders, "model/healthcare_label_encoders.pkl")  # Save encoders with symptoms

print("✅ Healthcare insurance model trained and saved successfully!")
