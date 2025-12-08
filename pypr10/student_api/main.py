import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel, EmailStr

import models
from database import engine, get_db

from typing import Optional

# Створення таблиць у базі даних
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Management API")

# Pydantic схеми для валідації даних
class StudentCreate(BaseModel):
    name: str
    group: str
    grade: float
    email: EmailStr

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    group: Optional[str] = None
    grade: Optional[float] = None
    email: Optional[EmailStr] = None

class GradeUpdate(BaseModel):
    student_id: int
    new_grade: float

class StudentResponse(BaseModel):
    id: int
    name: str
    group: str
    grade: float
    email: str
    
    class Config:
        from_attributes = True  # Для SQLAlchemy моделей

# 1. CREATE - Створення нового студента
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    # Перевірка чи існує студент з таким email
    db_student = db.query(models.Student).filter(
        models.Student.email == student.email
    ).first()
    
    if db_student:
        raise HTTPException(status_code=400, detail="Email вже зареєстровано")
    
    # Створення нового студента
    new_student = models.Student(
        name=student.name,
        group=student.group,
        grade=student.grade,
        email=student.email
    )
    
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    
    return new_student

# 2. READ - Отримання всіх студентів
@app.get("/students/", response_model=List[StudentResponse])
def get_all_students(db: Session = Depends(get_db)):
    students = db.query(models.Student).all()
    return students

# 3. READ - Отримання студента за ID
@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()
    
    if not student:
        raise HTTPException(status_code=404, detail="Студента не знайдено")
    
    return student

# 4. UPDATE - Оновлення даних студента
@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int, 
    student_update: StudentCreate, 
    db: Session = Depends(get_db)
):
    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()
    
    if not student:
        raise HTTPException(status_code=404, detail="Студента не знайдено")
    
    # Оновлення полів
    student.name = student_update.name
    student.group = student_update.group
    student.grade = student_update.grade
    student.email = student_update.email
    
    db.commit()
    db.refresh(student)
    
    return student

# 5. DELETE - Видалення студента
@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()
    
    if not student:
        raise HTTPException(status_code=404, detail="Студента не знайдено")
    
    db.delete(student)
    db.commit()
    
    return {"message": f"Студента {student.name} видалено"}

# Додаткові endpoint'и

# Пошук студентів за групою
@app.get("/students/group/{group_name}", response_model=List[StudentResponse])
def get_students_by_group(group_name: str, db: Session = Depends(get_db)):
    students = db.query(models.Student).filter(
        models.Student.group == group_name
    ).all()
    return students

# Пошук студентів з оцінкою вище заданої
@app.get("/students/grade/above/{min_grade}", response_model=List[StudentResponse])
def get_students_above_grade(min_grade: float, db: Session = Depends(get_db)):
    students = db.query(models.Student).filter(
        models.Student.grade >= min_grade
    ).all()
    return students

#Пошук студентів за ім'ям
@app.get("/students/search/{name}", response_model=List[StudentResponse])
def search_students_by_name(name: str, db: Session = Depends(get_db)):
    students = db.query(models.Student).filter(
        models.Student.name.contains(name)
    ).all()
    return students

#Часткове оновлення студента PATCH
@app.patch("/students/{student_id}", response_model=StudentResponse)
def partial_update_student(
    student_id: int,
    student_update: StudentUpdate,
    db: Session = Depends(get_db)
):
    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()
    
    if not student:
        raise HTTPException(status_code=404, detail="Студента не знайдено")
    
    # Оновлюємо тільки передані поля
    if student_update.name is not None:
        student.name = student_update.name
    if student_update.group is not None:
        student.group = student_update.group
    if student_update.grade is not None:
        student.grade = student_update.grade
    if student_update.email is not None:
        student.email = student_update.email
    
    db.commit()
    db.refresh(student)
    
    return student

#Статистика по групах
@app.get("/statistics/groups")
def get_group_statistics(db: Session = Depends(get_db)):
    from sqlalchemy import func
    
    stats = db.query(
        models.Student.group,
        func.count(models.Student.id).label("student_count"),
        func.avg(models.Student.grade).label("average_grade"),
        func.max(models.Student.grade).label("max_grade"),
        func.min(models.Student.grade).label("min_grade")
    ).group_by(models.Student.group).all()
    
    result = []
    for stat in stats:
        result.append({
            "group": stat.group,
            "student_count": stat.student_count,
            "average_grade": round(stat.average_grade, 2),
            "max_grade": stat.max_grade,
            "min_grade": stat.min_grade
        })
    
    return result

#Оновити оцінки
@app.post("/students/bulk-update-grades")
def bulk_update_grades(updates: List[GradeUpdate], db: Session = Depends(get_db)):
    try:
        for update in updates:
            student = db.query(models.Student).filter(
                models.Student.id == update.student_id
            ).first()
            
            if student:
                student.grade = update.new_grade
        
        db.commit()
        return {"message": f"Оновлено {len(updates)} оцінок"}
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Помилка: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
