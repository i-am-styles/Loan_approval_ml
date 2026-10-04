import pandas as pd
import numpy as np

np.random.seed(42)
n = 8000

df = pd.DataFrame({
    'Age': np.random.randint(18, 71, size=n),
    'Income': np.random.randint(20000, 150000, size=n),
    'Loan_Amount': np.random.randint(1000, 50000, size=n),
    'Loan_Term': np.random.randint(12, 61, size=n),
    'Credit_Score': np.random.randint(300, 850, size=n),
    'Employment_Years': np.random.randint(0, 40, size=n),
    'Dependents': np.random.randint(0, 5, size=n),
    "Education": np.random.choice(['high school', 'bachelor', 'master', 'phd'], size=n,p=[0.4, 0.3, 0.2, 0.1]),
    'Self_employed': np.random.choice(["Yes", "No"], size=n,p=[0.2, 0.8]),
    'Property_Area': np.random.choice(['urban', 'semiurban', 'rural'], size=n,p=[0.3, 0.5, 0.2]),
    'Marital_Status': np.random.choice(['single', 'married'], size=n,p=[0.35, 0.65]),
    'PreviousDefault': np.random.choice(['yes', 'no'], size=n,p=[0.1, 0.9]),
})

df["Loan_Status"] = np.where(
    (df['Credit_Score'] > 600) &
    (df['Income'] > 50000) &
    (df['PreviousDefault'] == 'no') &
    (df["Employment_Years"] >= 3),
    'Approved', 'Rejected'
)

df.to_csv('loan_data.csv', index=False)