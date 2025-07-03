import random
from faker import Faker
from db import Session
from models import Group, Student, Teacher, Subject, Grade


session = Session()
faker = Faker()

def adding_data_to_tables(data):
    session.add_all(data)
    session.flush()

# Clearing
models_list = [Grade, Student, Teacher, Subject, Group]

for model in models_list:
    session.query(model).delete()

# Groups
groups = []
for i in range(3):
    group = Group(name="Group " + str(i+1))
    groups.append(group)

# Teachers
teachers = []
for _ in range(4):
    teacher = Teacher(
        first_name=faker.first_name(),
        last_name=faker.last_name())
    teachers.append(teacher)

# Subjects
subjects = []
for _ in range(6):
    subject = Subject(
        name=faker.job(),
        teacher=random.choice(teachers))
    subjects.append(subject)

# Students
students = []
for _ in range(30):
    student = Student(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        group=random.choice(groups))
    students.append(student)

for data_model in [groups, teachers, subjects, students]:
    adding_data_to_tables(data_model)

# Grades
existing_keys = set()
for student in students:
    for subject in subjects:
        for _ in range(random.randint(10, 20)):
            date = faker.date_between(start_date='-1y', end_date='today')
            key = (student.id, subject.id, date)
            if key in existing_keys:
                continue
            existing_keys.add(key)
            grade = Grade(
                student=student,
                subject=subject,
                grade=random.randint(1, 100),
                grade_date=date
            )
            session.add(grade)

session.commit()
print("Seed complete.")
