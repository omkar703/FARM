from fastapi import FastAPI , Path , HTTPException , Query
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
    raise HTTPException(status_code=404,detail="Patient not found")



## Add query params
# here assiding is default param
@app.get('/sort')
def sort_patient(sort_by: str = Query(...,description='sort by height ,weight , bmi'),
                 order_by: str = Query('asc',description='order by ascending or descending')):
    valid_fields = ['height','weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail="Invalid field")
    if order_by not in ['asc','desc']:
        raise HTTPException(status_code=400,detail="Invalid order")
    data = get_patient()


    sort_order = True if order_by == 'asc' else False
    sorted_data = sorted(data.values(),key=lambda x: x.get(sort_by , 0),reverse=sort_order)
    return sorted_data