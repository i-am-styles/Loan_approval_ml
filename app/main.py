from fastapi import FastAPI,HTTPException,File,UploadFile
from fastapi.responses import StreamingResponse
from app.schemas import LoanApplication
import joblib
import pandas as pd
import io

app = FastAPI()
model = joblib.load("model/loan_approval.pkl")
accuracy = joblib.load("model/accuracy.pkl")

@app.get("/")
def intro():
    return {
        "message": "Welcome to the loan predictor api"
    }

@app.get("/health")
def health():
    return {
        "status": "running",
        "model": "RandomForestClassifier",
        "accuracy": round(float(accuracy * 100), 2)
    }

@app.post("/predict")
def predict(loan: LoanApplication):
    try:
        input_data = pd.DataFrame([loan.model_dump()])

        prediction = model.predict(input_data)
        predict_proba = model.predict_proba(input_data)

        approval_probability = predict_proba[0][0]

        return {
            "prediction": prediction[0],
            "approval_probability": round(
                float(approval_probability) * 100, 2
            )
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@app.post("/predict-file")
def predict_file(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        df = pd.read_csv(io.StringIO(contents.decode('utf-8')))
        predictions = model.predict(df)
        probabilities = model.predict_proba(df)[:,0]

        df['Loan_prediction'] = predictions
        df['Loan_probability'] = (
            probabilities * 100
        ).round(2)

        output = io.StringIO()
        df.to_csv(output,index=False)
        output.seek(0)

        return StreamingResponse(output,media_type="text/csv",
            headers={"Content-Disposition":
                    f"attachment: filename=predictions.csv"})

    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))