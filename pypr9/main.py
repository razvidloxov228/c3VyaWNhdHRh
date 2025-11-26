import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Головна сторінка"}

@app.get("/about")
def about():
    return {"page": "Про нас", "description": "Інформація про сайт"}

@app.get("/contact")
def contact():
    return {
        "email": "example@example.com",
        "phone": "+380123456789"
    }

@app.get("/info")
def contact():
    return {
        "author": "Вадим Кузьменко"
    }

@app.get("/student/{student_id}")
def get_student(student_id: int):
    return {
        "student_id": student_id,
        "name": f"Студент №{student_id}",
        "group": "КТ-23"
    }

@app.get("/greeting/{name}")
def greet_user(name: str):
    return {"message": f"Привіт, {name}!"}

@app.get("/search")
def search_items(query: str, limit: int = 10):
    return {
        "query": query,
        "limit": limit,
        "results": f"Знайдено результати для '{query}' (максимум {limit})"
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None, show_details: bool = False):
    result = {"item_id": item_id}
    
    if q:
        result["query"] = q
    if show_details:
        result["details"] = "Детальна інформація про товар"
    
    return result

@app.get("/calc/add/{a}/{b}")
def add(a: float, b: float):
    return {"operation": "додавання", "result": a + b}

@app.get("/calc/sub/{a}/{b}")
def subtract(a: float, b: float):
    return {"operation": "віднімання", "result": a - b}

@app.get("/calc/mul/{a}/{b}")
def multiply(a: float, b: float):
    return {"operation": "множення", "result": a * b}

@app.get("/calc/div/{a}/{b}")
def divide(a: float, b: float):
    if b == 0:
        return {"error": "Ділення на нуль неможливе"}
    return {"operation": "ділення", "result": a / b}

@app.get("/calc/{a}/{b}")
def calculate(a: float, b: float, operation: str):
    if operation == "add":
        result = a + b
        op_name = "додавання"
    elif operation == "sub":
        result = a - b
        op_name = "віднімання"
    elif operation == "mul":
        result = a * b
        op_name = "множення"
    elif operation == "div":
        if b == 0:
            return {"error": "Ділення на нуль неможливе"}
        result = a / b
        op_name = "ділення"
    else:
        return {"error": "Невідома операція. Використовуйте add, sub, mul або div."}
    
    return {"operation": op_name, "result": result}

# Тимчасове сховище даних
students_db = {
    1: {"name": "Іван Петренко", "group": "КІТ-21", "grade": 90},
    2: {"name": "Марія Коваленко", "group": "КІТ-21", "grade": 85},
    3: {"name": "Петро Сидоренко", "group": "АВТ-22", "grade": 88}
}

@app.get("/students")
def get_all_students():
    return students_db

@app.get("/students/{student_id}")
def get_student_by_id(student_id: int):
    if student_id in students_db:
        return students_db[student_id]
    return {"error": "Студента не знайдено"}

@app.get("/students/group/{group_name}")
def get_students_by_group(group_name: str):
    result = {}
    for sid, student in students_db.items():
        if student["group"] == group_name:
            result[sid] = student
    return result

@app.get("/students/grade/{min_grade}")
def get_students_by_grade(min_grade: int):
    result = {}
    for sid, student in students_db.items():
        if student["grade"] > min_grade:
            result[sid] = student
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
