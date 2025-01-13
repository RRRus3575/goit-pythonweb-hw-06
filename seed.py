from faker import Faker
from sqlalchemy.orm import sessionmaker
from datetime import date, timedelta
from models import Base, engine, Student, Teacher, Subject, Group, Grade

fake = Faker()

Session = sessionmaker(bind=engine)
session = Session()

# Створення груп
groups = [Group(name=f"Group {i+1}") for i in range(3)]
session.add_all(groups)

# Створення викладачів
teachers = [Teacher(name=fake.name()) for _ in range(5)]
session.add_all(teachers)

# Створення предметів
subjects = [Subject(name=fake.job(), teacher=teachers[i % len(teachers)]) for i in range(8)]
session.add_all(subjects)

# Створення студентів
students = [Student(name=fake.name(), group=groups[i % len(groups)]) for i in range(50)]
session.add_all(students)

# Створення оцінок
for student in students:
    for subject in subjects:
        for _ in range(5):
            grade = Grade(
                student=student,
                subject=subject,
                grade=round(fake.random.uniform(60, 100), 2),
                date=fake.date_this_year()
            )
            session.add(grade)

session.commit()
print("База даних успішно заповнена!")
