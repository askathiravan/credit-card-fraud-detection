# 💳 Credit Card Fraud Detection & Risk Scoring System

This project is a machine learning–based system designed to identify suspicious credit card transactions and assign a fraud risk score.  
It simulates how real-world banking systems monitor transactions to reduce financial fraud.

---

## 🚀 Features

- Predicts whether a transaction is fraudulent using a Random Forest classifier
- Calculates a transaction risk score based on amount, time, location, and type
- Stores transaction data and predictions in a MySQL database
- Interactive Streamlit dashboard for monitoring fraud patterns
- Simple and explainable ML pipeline for interview discussions

---

## 🛠 Tech Stack

- **Python**
- **Machine Learning (Random Forest)**
- **Streamlit**
- **MySQL**
- **pandas, scikit-learn**

---

## ⚙️ How It Works

1. User enters transaction details through a Streamlit interface  
2. Data is preprocessed and passed to a trained ML model  
3. The system predicts fraud status and calculates a risk score  
4. Transaction details and results are stored in MySQL  
5. Dashboard displays fraud statistics and trends  


## ▶️ Running the Project

1. Install dependencies:
   ```
   pip install -r requirements.txt
Train the model:
```python train_model.py```

## Run the application:
```streamlit run app.py```


📌 Use Case
This project demonstrates how machine learning and system design can be combined to solve real-world financial fraud problems.
It focuses on explainability and end-to-end workflow, rather than only model accuracy.

