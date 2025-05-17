# 📉 Telco Customer Churn Prediction

An end-to-end machine learning project to predict customer churn using real-world telecom data. It applies advanced modeling (XGBoost, Logistic Regression, Random Forest), interpretability techniques (SHAP), and EDA to uncover churn patterns.

---

## 🚀 Project Highlights

- **Goal**: Predict customers likely to churn and understand key drivers behind churn.
- **Tech Stack**: Python, Pandas, scikit-learn, XGBoost, SHAP, Matplotlib, Seaborn
- **Dataset**: Telco Customer Churn dataset (Kaggle)
- **Modeling Focus**: Maximizing recall to capture churners
- **Model Interpretability**: SHAP value analysis for transparency
- **Key Deliverables**:
  - Model training & comparison
  - Visual EDA & feature analysis
  - SHAP-based interpretability
  - Confusion matrices, ROC curves, feature importance plots

---

## 📁 Folder Structure

Telco-Customer-Churn-Prediction/
│
├── images/ # All project visualizations (see below)
├── data/ # Cleaned dataset
├── notebooks/ # Jupyter notebooks for each phase
├── models/ # Saved model files
├── README.md # This file
└── requirements.txt # Dependencies


📸 *Project visuals folder preview:*

## 📊 Exploratory Data Analysis (EDA)

### 1. Churn Distribution
![Churn Distribution](images/churn_distribution.png)

### 2. Churn Rate by Contract Type
![Contract Type vs Churn](images/churnrate_by_contracttype.png)

### 3. Monthly Charges vs Churn
![Monthly Charges](images/monthlycharges_vs_churn.png)

### 4. Tenure vs Churn
![Tenure Distribution](images/tenure_vs_churn.png)

---

## 📈 Model Evaluation

### 1. Confusion Matrix - Tuned XGBoost
![Confusion Matrix](images/confusion_matrix.png)

### 2. ROC Curve - Logistic Regression
![ROC - Logistic Regression](images/lr_roc_curve.png)

### 3. ROC Curve - Random Forest
![ROC - Random Forest](images/rf_roc_curve.png)

### 4. ROC Curve - Tuned XGBoost
![ROC - XGBoost](images/roc_curve_tunedxgb.png)

### 5. ROC Curve - XGBoost Final
![ROC - Final XGBoost](images/xgb_roc_curve.png)

---

## 🧠 Feature Importance & SHAP

### 1. XGBoost Top 15 Feature Importances
![Top 15 Features](images/top15_features_xgboost.png)

### 2. TreeExplainer Global Importance
![Tree Explainer](images/tree-explainer.png)

### 3. SHAP Summary Plot
![SHAP Summary](images/shap_value.png)

### 4. SHAP Force Plot
![Force Plot](images/force_plot.png)

---

## ✅ Key Learnings

- Importance of **recall** in churn problems
- Clear impact of **contract type** and **tenure**
- How **SHAP** values can build trust and transparency in predictions

---

## 📌 Next Steps

- 📉 Integrate cost-sensitive learning
- 📊 Deploy dashboard using **Streamlit**
- 🔁 Hyperparameter tuning via **Optuna**

---

## 📬 Let's Connect

- 🔗 [LinkedIn](https://www.linkedin.com/in/abinashsahoo/)
- 🔗 [Portfolio](https://www.notion.so/Hey-there-I-am-Abinash-Sahoo-1dfe544fcbea80ef973eec9fd705f513)
- 📫 Reach me for collaboration, feedback, or project walkthroughs!

---

