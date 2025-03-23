import pandas as pd
import random

# Generating random but realistic values
num_entries = 1000  # Number of unique entries

data = {
    "ID": range(1, num_entries + 1),
    "Age": [random.randint(18, 80) for _ in range(num_entries)],
    "Income": [random.randint(20000, 200000) for _ in range(num_entries)],
    "Family Size": [random.randint(1, 6) for _ in range(num_entries)],
    "Employment Type": random.choices(["Private Job", "Govt Job", "Self-Employed", "Retired", "Unemployed"], k=num_entries),
    "Health Conditions": random.choices(["None", "Diabetes", "Heart Disease", "Asthma", "Hypertension", "Cancer"], k=num_entries),
    "Existing Policy": random.choices(["Health", "Life", "Motor", "Travel", "Home", "Business", "Senior Citizen", "None"], k=num_entries),
    "Past Claims": [random.randint(0, 5) for _ in range(num_entries)],
    "Claim Amount": [random.randint(5000, 200000) for _ in range(num_entries)],
    "Claim Approved": random.choices(["Yes", "No"], weights=[80, 20], k=num_entries),  # 80% Approval Rate
    "Reimbursement Time (Days)": [random.randint(5, 30) for _ in range(num_entries)],
    "Claim Success Rate (%)": [random.randint(50, 100) for _ in range(num_entries)],
    "Customer Satisfaction": [round(random.uniform(2.5, 5.0), 1) for _ in range(num_entries)],  # Ratings from 2.5 to 5.0
}

# Function to recommend policy based on past data
def recommend_policy(row):
    if row["Health Conditions"] != "None" or row["Past Claims"] > 2:
        return "Health Insurance"
    elif row["Age"] > 50:
        return "Senior Citizen Plan"
    elif row["Income"] > 80000:
        return "Premium Life Insurance"
    elif row["Existing Policy"] == "Motor":
        return "Motor Comprehensive"
    else:
        return "Basic Life Insurance"

# Generate recommended policies
df = pd.DataFrame(data)
df["Recommended Policy"] = df.apply(recommend_policy, axis=1)

# Save dataset
df.to_csv("insurance_wide_dataset.csv", index=False)
print("✅ Dataset Generated Successfully!")
