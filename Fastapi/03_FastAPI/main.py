from fastapi import FastAPI , Path
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

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(...,description='id of the patient' , example='patient1')):
    patients = get_patient()
    if patient_id in patients:
        return patients[patient_id]
    else:
        return {"message": "Patient not found"}