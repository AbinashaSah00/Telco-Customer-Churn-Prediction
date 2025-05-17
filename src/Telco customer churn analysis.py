import pandas as pd

# Step 1: Load original dataset
df = pd.read_csv(r"D:\Data Science\Freelance projects\Telco Customer Churn Analysis\telco_churn_dashboard.csv")

# Step 2: Replace Yes/No in Churn with 1/0 (for modeling if needed)
df['Churn'] = df['Churn'].replace({'Yes': 1, 'No': 0})

# Step 3: Label encode Male/Female and other binary columns for modeling
df['gender'] = df['gender'].replace({'Male': 1, 'Female': 0})
df['Partner'] = df['Partner'].replace({'Yes': 1, 'No': 0})
df['Dependents'] = df['Dependents'].replace({'Yes': 1, 'No': 0})
df['PhoneService'] = df['PhoneService'].replace({'Yes': 1, 'No': 0})
df['PaperlessBilling'] = df['PaperlessBilling'].replace({'Yes': 1, 'No': 0})

# ✅ Save intermediate cleaned file if needed (optional)
# df.to_csv(r"D:\Data Science\Freelance projects\Telco Customer Churn Analysis\telco_churn_dashboard_cleaned.csv", index=False)

# Step 4: Map encoded values back to readable labels for dashboard
binary_mappings = {
    'gender': {1: 'Male', 0: 'Female'},
    'Partner': {1: 'Yes', 0: 'No'},
    'Dependents': {1: 'Yes', 0: 'No'},
    'PhoneService': {1: 'Yes', 0: 'No'},
    'PaperlessBilling': {1: 'Yes', 0: 'No'},
    'Churn': {1: 'Yes', 0: 'No'}
}
df.replace(binary_mappings, inplace=True)

# Step 5: Add tenure groups
def tenure_group(tenure):
    if tenure <= 12:
        return '0-1 Year'
    elif tenure <= 24:
        return '1-2 Years'
    elif tenure <= 48:
        return '2-4 Years'
    elif tenure <= 60:
        return '4-5 Years'
    else:
        return '5+ Years'
df['TenureGroup'] = df['tenure'].apply(tenure_group)

# Step 6: Monthly charge bucket
def charge_category(charge):
    if charge < 35:
        return 'Low'
    elif charge < 70:
        return 'Medium'
    else:
        return 'High'
df['MonthlyChargeCategory'] = df['MonthlyCharges'].apply(charge_category)

def get_contract_type(row):
    if row['Contract_One year']:
        return 'One year'
    elif row['Contract_Two year']:
        return 'Two year'
    else:
        return 'Month-to-month'

df['Contract'] = df.apply(get_contract_type, axis=1)


# Step 7: High-risk customer flag
df['HighRiskCustomer'] = df.apply(
    lambda x: 'Yes' if x['Contract'] == 'Month-to-month' and x['tenure'] < 12 and x['Churn'] == 'Yes' else 'No',
    axis=1
)


# Step 8: Final save for Tableau
df.to_csv(r"D:\Data Science\Freelance projects\Telco Customer Churn Analysis\telco_churn_dashboard_final.csv", index=False)

print("✅ Final dataset saved successfully to:")
print(r"D:\Data Science\Freelance projects\Telco Customer Churn Analysis\telco_churn_dashboard_final.csv")
