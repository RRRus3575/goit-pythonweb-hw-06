from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Базовий клас для моделей
Base = declarative_base()

# Підключення до бази даних
DATABASE_URL = "postgresql://postgres:mysecretpassword@localhost:5432/postgres?client_encoding=UTF8"
engine = create_engine(DATABASE_URL)

# Сесія
Session = sessionmaker(bind=engine)
session = Session()

#Таблиця студентів
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)
    group = relationship('Group', back_populates='students')


#Таблиця груп
class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    students = relationship('Student', back_populates='group')

#Таблиця викладачів
class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subjects = relationship('Subject', back_populates='teacher')

#Таблиця предметів
class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship('Teacher', back_populates='subjects')
    grades = relationship('Grade', back_populates='subject')

#Таблиця оцінок
class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    grade = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    student = relationship('Student')
    subject = relationship('Subject', back_populates='grades')

