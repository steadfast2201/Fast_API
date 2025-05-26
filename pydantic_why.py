from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the Patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish','Aniket'])]
    email: EmailStr
    linkdin_url: AnyUrl
    age:int = Field(gt=0 , lt=100)
    weight: float = Field(gt = 0)
    married: Annotated[bool, Field(default=None, description='Is the patient Married or not')]
    allergies: Optional[List[str]] = Field(max_length=5)
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Inserted into DataBase') 

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)

patient_info = {'name':'Aniket', 'email':'abc@gmail.com', 'linkdin_url':'http://linkdin.com/123223', 'age':30, 'weight':75.2, 'married':True, 'allergies':['pollen','dust'], 'contact_details': {'email':'abc@gmail.com','phone':'1234567890'}}

patient1 = Patient(**patient_info)