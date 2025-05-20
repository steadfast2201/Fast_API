from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data 

@app.get("/")
def hello():
    return {"Message":"Patient Management System API"}

@app.get("/about")
def about():
    return {"Message":"A fully functional API to manage patient records"}

@app.get("/view")
def view():
    data = load_data()

    return data