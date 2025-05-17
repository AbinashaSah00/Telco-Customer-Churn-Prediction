# Telco Customer Churn Prediction

This project tackles the challenge of predicting customer churn for a telecom company. It simulates a real-world data science workflow—from data cleaning and EDA to model selection, interpretation, and actionable business recommendations.

🔗 **Live Notebook (Kaggle)**: [View on Kaggle](https://www.kaggle.com/code/abinashasahoo/telco-customer-churn-analysis)

## 🧠 Problem Statement
Telecom companies face significant revenue losses from customer churn. This project aims to:
- Predict which customers are likely to churn
- Understand the key drivers behind churn
- Support proactive retention strategies

---

## 📊 Business Context
Retaining a customer is 5x cheaper than acquiring a new one. With data-driven insights, businesses can reduce churn, optimize customer experience, and improve long-term profitability.

---

## 📂 Project Workflow

### 1. Data Preprocessing
- Handled missing values
- Converted categorical variables
- Standardized numeric columns

### 2. Exploratory Data Analysis (EDA)
- Churn vs Tenure, Contract Type, Monthly Charges
- Correlation matrix & distribution plots

### 3. Model Building
- Logistic Regression (baseline)
- Random Forest
- XGBoost (final model based on recall performance)

### 4. Model Evaluation
- Precision, Recall, F1-score
- Confusion Matrix
- ROC-AUC Curve

### 5. Explainability
- SHAP values for feature impact
- Customer-level explanation with waterfall plots

---

## 📌 Key Findings

- **Contract Type** is a major driver of churn (monthly contracts show higher churn rates)
- **High monthly charges** increase churn likelihood
- **Senior Citizens** and **Fiber Optic users** are more likely to churn
- Final model achieved **83% recall**, ensuring fewer high-risk customers are missed

---

## 🔍 Tools & Tech Stack

- Python (Pandas, NumPy, Matplotlib, Seaborn)
- Scikit-learn, XGBoost
- SHAP for explainability
- Kaggle Notebook
- GitHub for versioning

---

## 📁 Repository Structure

