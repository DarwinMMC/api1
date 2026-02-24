from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def entry():
    return {"message": "Hello, World1!"}


@app.get("/hello")
def hello_world():
    return {"message": "Hello, World!"}


@app.get("/test")
def tets():
    return {"message": "Hello, World1!"}

