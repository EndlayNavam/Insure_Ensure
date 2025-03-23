import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import joblib  # For saving the trained model

# Load dataset
df = pd.read_csv("insurance_dataset.csv")  # Ensure this dataset is in the same folder

# Encode categorical features
encoder = LabelEncoder()
df["Health Conditions"] = encoder.fit_transform(df["Health Conditions"])
df["Recommended Policy"] = encoder.fit_transform(df["Recommended Policy"])

# Split dataset into features (X) and labels (y)
X = df.drop(columns=["Recommended Policy"])
y = df["Recommended Policy"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Save the trained model and encoder
joblib.dump(model, "CAD/insurance_model.pkl")
joblib.dump(encoder, "CAD/label_encoder.pkl")

print("✅ Model trained and saved successfully!")
