from fastapi import FastAPI , Path
from typing import Optional

app= FastAPI()

students= {
    1: {
        "name" : "john" ,
        " age" : "21" ,
        "class" : " fourth"
    }
}

@app.get("/")
def index():
    return {"name" : "first fast api"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path( ...,description= "write an id to view ", gt=0 )):
    return  students[student_id]

@app.get("/get-by-name")
def get_student(name: Optional [str] = None):
    for student_id in students:
        if students[student_id][name] == name:
              return  students[student_id]
    return  {"Data" : " Data not found"}