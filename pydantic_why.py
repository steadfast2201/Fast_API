from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional


class Patient(BaseModel):

    name: str = Field(max_length=50)
    email: EmailStr
    linkdin_url: AnyUrl
    age: int = Field(gt=0, lt=100)
    weight: float = Field(gt=0)
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted into DataBase")


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)


patient_info = {
    "name": "Aniket",
    "email": "abc@gmail.com",
    "linkdin_url": "http://linkdin.com/123223",
    "age": 30,
    "weight": 75.2,
    "married": True,
    "allergies": ["pollen", "dust"],
    "contact_details": {"email": "abc@gmail.com", "phone": "1234567890"},
}

patient1 = Patient(**patient_info)
