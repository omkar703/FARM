from fastapi import FastAPI
import json
app = FastAPI()

def get_patient():
    with open("patients.json") as f:
        patients = json.load(f)
        return patients

@app.get("/")
def hello():
    return {"message": "Patient Mannagemnet System API"}



@app.get("/about")
def about():
    return {"message": "A Fully funtional API to manage patients records "}



@app.get("/view")
def view():
    patients = get_patient()
    return patients