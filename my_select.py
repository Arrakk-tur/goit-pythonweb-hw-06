from sqlalchemy import func, desc, and_
from db.db import Session
from db.models import Group, Student, Grade, Subject

session = Session()

# 1. 5 студентів із найбільшим середнім балом з усіх предметів.
def select_1():
    return session.query(
        Student.first_name, Student.last_name,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

# 2. Студент із найвищим середнім балом з певного предмета.
def select_2(subject_id: int):
    return session.query(
        Student.first_name, Student.last_name,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Grade).filter(Grade.subject_id == subject_id
    ).group_by(Student.id).order_by(desc('avg_grade')).first()

# 3. Середній бал у групах з певного предмета.
def select_3(subject_id: int):
    return (
        session.query(
            Group.name,
            func.round(func.avg(Grade.grade), 2).label('avg_grade')
        )
        .select_from(Group)
        .join(Student, Student.group_id == Group.id)
        .join(Grade, Grade.student_id == Student.id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.id)
        .all()
    )

# 4. Середній бал на потоці (по всій таблиці оцінок)
def select_4():
    return session.query(
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).scalar()


# 5. Які курси читає певний викладач
def select_5(teacher_id: int):
    return session.query(
        Subject.name
    ).filter(Subject.teacher_id == teacher_id).all()


# 6. Список студентів у певній групі
def select_6(group_id: int):
    return session.query(
        Student.first_name, Student.last_name
    ).filter(Student.group_id == group_id).all()


# 7. Оцінки студентів у окремій групі з певного предмета
def select_7(group_id: int, subject_id: int):
    return session.query(
        Student.first_name, Student.last_name, Grade.grade
    ).join(Grade).filter(
        and_(
            Student.group_id == group_id,
            Grade.subject_id == subject_id
        )
    ).all()


# 8. Середній бал, який ставить певний викладач зі своїх предметів
def select_8(teacher_id: int):
    return session.query(
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Grade.subject).filter(
        Subject.teacher_id == teacher_id
    ).scalar()


# 9. Список курсів, які відвідує певний студент
def select_9(student_id: int):
    return session.query(
        Subject.name
    ).join(Grade).filter(
        Grade.student_id == student_id
    ).distinct().all()


# 10. Список курсів, які певному студенту читає певний викладач
def select_10(student_id: int, teacher_id: int):
    return session.query(
        Subject.name
    ).join(Grade).filter(
        and_(
            Grade.student_id == student_id,
            Subject.teacher_id == teacher_id
        )
    ).distinct().all()