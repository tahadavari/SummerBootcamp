import uuid
import csv
from abc import ABC, abstractmethod


class Writable(ABC):
    @abstractmethod
    def get_write_content(self):
        pass


class CsvWriter:
    def write(self, obj: Writable, file_name):
        content = obj.get_write_content()
        with open(file_name, 'a') as csvfile:
            fieldnames = list(content.keys())
            csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
            csv_writer.writerow(content)


class Teacher(Writable):

    def __init__(self, name, teacher_id=None):
        self.id = str(uuid.uuid4()) if teacher_id is None else teacher_id
        self.name = name

    def get_write_content(self):
        return {'name': self.name, 'id': self.id}


class Student:
    def __init__(self, name, student_id=None):
        self.id = str(uuid.uuid4()) if student_id is None else student_id
        self.name = name


class Class(Writable):
    def __init__(self, name, teacher, students=[]):
        self.name = name
        self.teacher: Teacher = teacher
        self.students: [Student] = students


class KaroKamp:
    def __init__(self, classes: [Class] = [], student: [Student] = [], teachers=None):
        if teachers is None:
            teachers = []
        self.classes: [Class] = []
        self.students: [Student] = []
        self.teachers: [Teacher] = teachers
        self.load_teachers()

    def load_teachers(self):
        with open('teachers.csv', 'r') as csvfile:
            fieldnames = ['name', 'id']
            reader = csv.DictReader(csvfile, fieldnames=fieldnames, delimiter=',')
            for row in reader:
                self.teachers.append(Teacher(row['name'], row['id']))


karokamp = KaroKamp()
writer = CsvWriter()
while True:
    print("1. Add Teacher")
    print("2. Add a class")
    print("3. Show classes")
    print("4. Show teachers")
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        teacher_name = input("please enter teacher name: ")
        teacher = Teacher(teacher_name)
        writer.write(teacher, 'teachers.csv')
        karokamp.teachers.append(teacher)

    elif choice == 2:
        class_name = input("please enter class name: ")
        i = 1
        for t in karokamp.teachers:
            print(i, t.name)
            i += 1
        teacher_index = int(input("please choose teacher: "))
        teacher = karokamp.teachers[teacher_index - 1]
        c = Class(class_name, teacher)
        karokamp.classes.append(c)
    elif choice == 3:
        for c in karokamp.classes:
            print(c.name, c.teacher.name)
    elif choice == 4:
        for t in karokamp.teachers:
            print(t.name)
