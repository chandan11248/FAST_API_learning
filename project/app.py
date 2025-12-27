from fastapi import FastAPI
import pandas as pd 
import pickle
from typing import Annotated,Literal,Optional
from pydantic import BaseModel,Field,field_validator,computed_field

app=FastAPI()

# import the ml model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app.post("/predict")
def predict():''