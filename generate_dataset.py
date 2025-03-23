import pandas as pd
import random

# Sample data
ages = [random.randint(18, 70) for _ in range(1000)]
incomes = [random.randint(20000, 200000) for _ in range(1000)]
health_conditions = random.choices(["None", "Diabetes", "Heart Disease", "Asthma"], k=1000)
family_sizes = [random.randint(1, 6) for _ in range(1000)]
past_claims = [random.randint(0, 5) for _ in range(1000)]

# Assigning a policy based on logic
def assign_policy(age, income, health, claims):
    if health != "None" or claims > 1:
        return "Health Insurance"
    elif age > 50:
        return "Senior Citizen Plan"
    elif income > 80000:
        return "Premium Life Insurance"
    else:
        return "Basic Life Insurance"

policies = [assign_policy(a, i, h, c) for a, i, h, c in zip(ages, incomes, health_conditions, past_claims)]

# Create DataFrame
df = pd.DataFrame({
    "Age": ages,
    "Income": incomes,
    "Health Conditions": health_conditions,
    "Family Size": family_sizes,
    "Past Claims": past_claims,
    "Recommended Policy": policies
})

# Save dataset
df.to_csv("insurance_dataset.csv", index=False)
print("Dataset Generated Successfully! ✅")
