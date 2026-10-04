# Loan Approval Prediction API

A machine learning based Loan Approval Prediction API built with Python, Scikit-learn, and FastAPI.

The project predicts whether a loan application will be **Approved** or **Rejected** and also provides the probability of approval.

## Features

- Loan approval prediction using a trained Machine Learning model
- Approval probability
- Single loan application prediction
- Batch prediction through CSV upload
- CSV output with predictions and probabilities
- Health check endpoint
- Interactive Swagger API documentation
- Input validation using Pydantic

## 🌐 Live API

The API is deployed and publicly accessible.

## 🌐 Live API

The API is deployed and publicly accessible.

- **Live API:** [Open API](https://loan-approval-ml-kon7.onrender.com/)
- **Swagger Docs:** [Open Swagger UI](https://loan-approval-ml-kon7.onrender.com/docs)
- **Health Check:** [Check API Health](https://loan-approval-ml-kon7.onrender.com/health)

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Uvicorn
- Pydantic
- Joblib
- PyArrow

## Project Structure

```text
loan_approval_ml/
│
├── app/
│   ├── main.py
│   ├── schemas.py
│   └── predict.py
│
├── model/
│   ├── loan_approval.pkl
│   └── accuracy.pkl
│
├── data/
│
├── notebooks/
│
├── README.md
├── requirements.txt
├── .gitignore
└── loanenv/
```

## API Endpoints

### `GET /`

Returns a welcome message.

### `GET /health`

Returns the current API status, model name, and model accuracy.

Example response:

```json
{
  "status": "running",
  "model": "RandomForestClassifier",
  "accuracy": 85.42
}
```

### `POST /predict`

Accepts a single loan application and returns the prediction and approval probability.

Example response:

```json
{
  "prediction": "Approved",
  "approval_probability": 82.34
}
```

### `POST /predict-file`

Accepts a CSV file containing multiple loan applications.

The API processes all rows and returns a CSV file containing:

- Original input data
- `Loan_prediction`
- `Loan_probability`

## Input Features

The model uses the following features:

| Feature | Description |
|---|---|
| Age | Age of the applicant |
| Income | Applicant's income |
| Loan_Amount | Requested loan amount |
| Loan_Term | Loan repayment term |
| Credit_Score | Applicant's credit score |
| Employment_Years | Years of employment |
| Dependents | Number of dependents |
| Education | Education level |
| Self_employed | Self-employment status |
| Property_Area | Property area type |
| Marital_Status | Marital status |
| PreviousDefault | Previous loan default status |

## Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd loan_approval_ml
```

### 2. Create a virtual environment

```bash
python -m venv loanenv
```

### 3. Activate the virtual environment

For Windows:

```bash
.\loanenv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the API

Start the FastAPI server from the project root:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides interactive API documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## Machine Learning Workflow

The machine learning workflow includes:

1. Data loading
2. Data preprocessing
3. Handling missing values
4. Encoding categorical features
5. Feature scaling
6. Train-test split
7. Model training using Random Forest
8. Model evaluation
9. Saving the trained model using Joblib
10. Serving predictions through FastAPI

## Prediction Flow

```text
Loan Application
       ↓
Pydantic Validation
       ↓
Pandas DataFrame
       ↓
Trained ML Pipeline
       ↓
Prediction + Probability
       ↓
FastAPI Response
```

For CSV prediction:

```text
CSV Upload
    ↓
Pandas DataFrame
    ↓
ML Model
    ↓
Predictions + Probabilities
    ↓
Output CSV
```

## Model

The project uses a trained `RandomForestClassifier`.

The complete trained model is stored using Joblib and loaded by the FastAPI application for inference.

## Future Improvements

- Add authentication
- Add better error handling
- Add automated tests
- Add Docker support
- Add model versioning
- Deploy the API to a cloud platform
- Add a frontend for easier interaction

## Disclaimer

This project is created for educational and demonstration purposes. Predictions from the model should not be used as the sole basis for real-world financial decisions.