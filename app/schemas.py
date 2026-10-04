from pydantic import BaseModel, Field
from typing import Literal


class LoanApplication(BaseModel):
    Age: int = Field(
        ...,
        ge=18,
        le=100,
        description="Age of the loan applicant in years.",
        examples=[56]
    )

    Income: float = Field(
        ...,
        ge=0,
        description="Applicant's annual income.",
        examples=[106654]
    )

    Loan_Amount: float = Field(
        ...,
        ge=0,
        description="Requested loan amount.",
        examples=[43255]
    )

    Loan_Term: int = Field(
        ...,
        ge=1,
        le=50,
        description="Loan repayment term in years.",
        examples=[25]
    )

    Credit_Score: int = Field(
        ...,
        ge=300,
        le=850,
        description="Applicant's credit score, typically ranging from 300 to 850.",
        examples=[528]
    )

    Employment_Years: float = Field(
        ...,
        ge=0,
        description="Number of years the applicant has been employed.",
        examples=[36]
    )

    Dependents: int = Field(
        ...,
        ge=0,
        description="Number of dependents supported by the applicant.",
        examples=[3]
    )

    Education: Literal["phd", "graduate", "not graduate"] = Field(
        ...,
        description="Highest education level of the applicant.",
        examples=["phd"]
    )

    Self_employed: Literal["Yes", "No"] = Field(
        ...,
        description="Whether the applicant is self-employed.",
        examples=["No"]
    )

    Property_Area: Literal["urban", "semiurban", "rural"] = Field(
        ...,
        description="Type of area where the applicant's property is located.",
        examples=["semiurban"]
    )

    Marital_Status: Literal["married", "single"] = Field(
        ...,
        description="Marital status of the applicant.",
        examples=["married"]
    )

    PreviousDefault: Literal["yes", "no"] = Field(
        ...,
        description="Whether the applicant has previously defaulted on a loan.",
        examples=["no"]
    )