from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import json

app = FastAPI()


class Patient(BaseModel):

    id: Annotated[str, Field(..., description="ID of the Patient", examples=["P001"])]
    name: Annotated[str, Field(..., description="Name of the patient")]
    city: Annotated[str, Field(..., description="City Where Patient lives")]
    age: Annotated[int, Field(..., gt=0, lt=100, description="Age of the Patient")]
    gender: Annotated[
        Literal["male", "female", "others"],
        Field(..., description="Gender of the Patient"),
    ]
    height: Annotated[float, Field(..., gt=0, description="Height of the patient")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the patient")]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2), 2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return "underweight"
        elif self.bmi > 18.5 and self.bmi < 30:
            return "Normal"
        else:
            return "Overweight"


def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)

    return data


@app.get("/")
def hello():
    return {"Message": "Patient Management System API"}


@app.get("/about")
def about():
    return {"Message": "A fully functional API to manage patient records"}


@app.get("/view")
def view():
    data = load_data()

    return data


@app.get("/patient/{patient_id}")
def view_patient(
    patient_id: str = Path(
        ..., description="ID of the patient in the DB", example="P001"
    )
):
    # load all the patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    # return {'error':'patient not found'}
    raise HTTPException(status_code=404, detail="Patient not found")


@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description="Sort on the basis of height, weight or BMI"),
    order: str = Query("asc", description="sort in asc and desc order"),
):

    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid field. Select from valid fields {valid_fields}",
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400, detail="Invalid order select between asc and desc"
        )

    data = load_data()

    sort_order = True if order == "desc" else False

    sorted_data = sorted(
        data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order
    )

    return sorted_data
