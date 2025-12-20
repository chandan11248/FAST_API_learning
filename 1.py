from fastapi import FastAPI,Path,HTTPException,Query
import json
app=FastAPI()
@app.get('/')
def fun():
    return {'messages':"hello"}
@app.get("/more")
def secret():
    return {"aiMessage":"hi,There!!",
            "humanMesssage":"hello ai, how are you?"}    
def load():   
    with open ("patients.json") as f:
            data=json.load(f)
            return data

@app.get("/view")
def view():
     data=load()
     return data

    

@app.get("/patient/{patient_id}")
def patient_detail(patient_id:str=Path(...,example=("P001"),description=("enter the patient id"))):
    data=load()
    if patient_id in data:
         return data[patient_id]
    else:
         raise HTTPException( status_code=404,detail="patient not found")
         

@app.get("/sort")
def sort_patient(sort_by:str=Query(...,
                                   description="sort based on  height,bmi,weight")
                                   ,order:str=Query('asc',description="either 'asc' or 'desc' ")):
     valid_fields=["height",'weight','bmi']

     if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
     if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
     data = load()

     sort_order = True if order=='desc' else False

     sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

     return sorted_data
    

 