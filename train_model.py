import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load data
df = pd.read_csv("data/transactions.csv")

# Encode categorical columns
le = LabelEncoder()
for col in ["location", "merchant", "txn_type"]:
    df[col] = le.fit_transform(df[col])

X = df.drop("fraud", axis=1)
y = df["fraud"]

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Save model
joblib.dump(model, "model/fraud_model.pkl")

print("Model trained and saved successfully.")