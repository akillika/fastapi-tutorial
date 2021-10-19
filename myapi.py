from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

students = {

    1: {
        "name": "john",
        "age": 17,
        "year": "Year 12"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description = "The ID of the Student you want to view",gt=0)):
    return students[student_id]

@app.get("/get-by-name")
def get_student(name: str, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]

    return {"Data": "Not Found"}

@app.post("/create-student/{student_id}")
def create_students(student_id: int, student : Student):
    if student_id in students:
        return {"error": "Student exists"}
    
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Doesnt exist"}

    students[student_id] = student
    return students[student_id]

@app.delete("/update-student/{student_id}")
def  delete_student(student_id: int):
    if student_id not in students:
        return {"error" : "Student does not exist"}

    del students[student_id]
    return {"message" : "Student deleted"}
    