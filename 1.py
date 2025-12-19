from fastapi import FastAPI
import json
app=FastAPI()
@app.get('/')
def fun():
    return {'messages':"hello"}
@app.get("/more")
def secret():
    return {"aiMessage":"hi,There!!",
            "humanMesssage":"hello ai, how are you?"}    

@app.get("/view")
def view():
    with open ("patients.json") as f:
        data=json.load(f)
        return data



