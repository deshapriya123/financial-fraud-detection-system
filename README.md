# financial-fraud-detection-system
This project is an End-to-End Financial Fraud Detection System designed to identify fraudulent credit card transactions in real-time.

In the banking industry, identifying fraud is a critical challenge because fraudulent transactions are extremely rare compared to legitimate ones (the "needle in a haystack" problem). This project bridges the gap between raw data analysis and a deployable AI product.

The Core Lifecycle of the Project
Problem Statement: Addressing extreme Class Imbalance where fraud accounts for less than 0.2% of total transactions.

Data Pipeline:

Exploratory Data Analysis (EDA): Identifying patterns and outliers in transaction amounts and timing.

Advanced Preprocessing: Utilizing SMOTE (Synthetic Minority Over-sampling Technique) to synthetically balance the dataset so the model can effectively learn the characteristics of fraud.

Model Training: Deploying a Random Forest Classifier, which is highly regarded in the industry for its balance between performance and the ability to interpret feature importance.

Evaluation Strategy: Moving beyond basic "Accuracy" and focusing on Precision, Recall, and the F1-Score to ensure we catch as many fraudulent cases as possible without blocking legitimate customers.

Production Readiness:

Model Serialization: Exporting the trained model and data scaler using joblib for external use.

Deployment: Creating an interactive Streamlit dashboard that allows a user to input transaction details and receive a "Fraud/Legitimate" classification in real-time.
