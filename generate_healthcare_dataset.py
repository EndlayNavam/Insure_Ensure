import pandas as pd
import random

# Number of unique records
num_entries = 1000

# Possible values for dataset attributes
diseases = ["Cancer", "Diabetes", "Heart Disease", "Kidney Disease", "Liver Disease", "Alzheimer’s", "Asthma", "Arthritis"]
symptoms = {
    "Cancer": ["Fatigue", "Weight Loss", "Pain", "Lumps", "Bleeding"],
    "Diabetes": ["Frequent Urination", "Increased Thirst", "Fatigue", "Blurred Vision"],
    "Heart Disease": ["Chest Pain", "Breathlessness", "Dizziness", "Fatigue"],
    "Kidney Disease": ["Swelling", "Fatigue", "Nausea", "Shortness of Breath"],
    "Liver Disease": ["Yellow Skin", "Abdominal Pain", "Dark Urine", "Itchy Skin"],
    "Alzheimer’s": ["Memory Loss", "Confusion", "Mood Changes", "Difficulty Speaking"],
    "Asthma": ["Wheezing", "Coughing", "Shortness of Breath", "Chest Tightness"],
    "Arthritis": ["Joint Pain", "Swelling", "Stiffness", "Fatigue"],
}
severity_levels = ["Low", "Medium", "High"]
diagnosis_methods = ["Biopsy", "Blood Test", "ECG", "Ultrasound", "X-ray", "MRI", "CT Scan"]
treatments = {
    "Cancer": ["Chemotherapy", "Radiation Therapy", "Surgery"],
    "Diabetes": ["Insulin Therapy", "Lifestyle Changes", "Medication"],
    "Heart Disease": ["Surgery", "Medication", "Lifestyle Changes"],
    "Kidney Disease": ["Dialysis", "Transplant", "Medication"],
    "Liver Disease": ["Liver Transplant", "Medication", "Dietary Changes"],
    "Alzheimer’s": ["Medication", "Cognitive Therapy"],
    "Asthma": ["Inhalers", "Medication", "Lifestyle Changes"],
    "Arthritis": ["Physical Therapy", "Medication", "Surgery"],
}
insurance_types = ["Health Insurance", "Critical Illness", "Cardiac Plan", "Senior Citizen", "Accident Cover"]
insurance_providers = ["XYZ Insurance", "ABC Health", "HeartCare Inc.", "KidneySafe Ins.", "MediCover", "LifeShield"]

# Generate random values for each entry
data = []
for i in range(1, num_entries + 1):
    age = random.randint(18, 80)
    bmi = round(random.uniform(18.0, 35.0), 1)
    smoking = random.choice(["Yes", "No"])
    disease = random.choice(diseases)
    symptoms_list = random.sample(symptoms[disease], 2)  # Pick 2 random symptoms
    severity = random.choice(severity_levels)
    diagnosis_method = random.choice(diagnosis_methods)
    treatment = random.choice(treatments[disease])
    insurance_type = random.choice(insurance_types)
    claim_amount = random.randint(20000, 200000)  # Claim amount in $
    reimbursement_rate = random.randint(50, 95)  # % of amount covered by insurance
    deductible = random.randint(1000, 20000)  # Fixed amount not covered
    interest_rate = round(random.uniform(2.0, 5.0), 1)  # Loan interest for extra coverage
    approval_time = random.randint(5, 30)  # Days for claim approval
    insurance_provider = random.choice(insurance_providers)

    data.append([
        i, age, bmi, smoking, disease, ", ".join(symptoms_list), severity, diagnosis_method, treatment,
        insurance_type, claim_amount, reimbursement_rate, deductible, interest_rate, approval_time, insurance_provider
    ])

# Create DataFrame
columns = ["ID", "Age", "BMI", "Smoking", "Disease", "Symptoms", "Severity", "Diagnosis Method", 
           "Treatment Type", "Insurance Type", "Claim Amount ($)", "Reimbursement Rate (%)", 
           "Deductible ($)", "Interest Rate (%)", "Approval Time (Days)", "Insurance Provider"]
df = pd.DataFrame(data, columns=columns)

# Save dataset to CSV
df.to_csv("healthcare_insurance_dataset.csv", index=False)
print("✅ Healthcare Insurance Dataset Generated Successfully!")
