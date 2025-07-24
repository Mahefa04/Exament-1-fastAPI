from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse



app = FastAPI()

@app.get("/hello")
def read_hello(request: Request):
    return JSONResponse(
        {"message": "Hello world"}, 
        status_code=200
        )

@app.get("/welcome")
def read_welcome(request: Request, name : str):
    return JSONResponse(
        {"message": f"Welcome {name}"}, status_code=200
    )

@app.post("/student")
def create_student(Reference: str, FirstName: str, LastName: str, age: int):
    return JSONResponse(
        {"message": f"Reference:  {Reference}"},
        {"message": f"FirstName: {FirstName}"},
        {"message": f"LastName: {LastName}"},
        {"message": f"Age: {age}"},
        status_code= CREATED
    )

@app.get("/students")
def get_students(Request: Request):
    return (
    create_student()
)