import math
import numpy as np

class Student:
    def __init__(self, sid, name, dob):
        self.id = sid
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0

    def set_mark(self, course_id, mark):
        mark = math.floor(mark * 10) / 10
        self.marks[course_id] = mark

    def calculate_gpa(self, credits_dict):
        marks = np.array([self.marks[c] for c in self.marks])
        credits = np.array([credits_dict[c] for c in self.marks])
        weighted = marks * credits
        self.gpa = math.floor((weighted.sum() / credits.sum()) * 10) / 10


class Course:
    def __init__(self, cid, name, credit):
        self.id = cid
        self.name = name
        self.credit = credit

def input_student_list():
    n = int(input("Enter number of students: "))
    students = []

    for _ in range(n):
        sid = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("Date of Birth: ")
        students.append(Student(sid, name, dob))

    return students


def input_course_list():
    m = int(input("Enter number of courses: "))
    courses = []

    for _ in range(m):
        cid = input("Course ID: ")
        name = input("Course Name: ")
        credit = int(input("Credit: "))
        courses.append(Course(cid, name, credit))

    return courses


def input_marks(students, courses):
    print("\n--- ENTER MARKS ---")
    for course in courses:
        print(f"\nCourse: {course.name} ({course.id})")
        for stu in students:
            score = float(input(f"Enter mark for {stu.name}: "))
            stu.set_mark(course.id, score)


def calculate_gpas(students, courses):
    credit_dict = {c.id: c.credit for c in courses}
    for stu in students:
        stu.calculate_gpa(credit_dict)


def sort_students_by_gpa(students):
    return sorted(students, key=lambda s: s.gpa, reverse=True)


def show_students(students):
    print("\n--- STUDENT LIST (GPA Sorted) ---")
    for stu in students:
        print(f"{stu.id} - {stu.name} | GPA: {stu.gpa}")

def main():
    students = input_student_list()
    courses = input_course_list()

    input_marks(students, courses)
    calculate_gpas(students, courses)

    students = sort_students_by_gpa(students)
    show_students(students)


if __name__ == "__main__":
    main()
