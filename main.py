from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {'data':{'name': 'John', 'age': 30}, 'status' : 'success', 'code' : 200}

@app.get("/about")
def about():
    return {'data':{'name': 'John', 'age': 30, 'about': 'My name is John'}, 'status' : 'success', 'code' : 200}