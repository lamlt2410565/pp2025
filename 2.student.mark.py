
class Person:
    def __init__(self, id, name, dob):
        self._id = id
        self._name = name
        self._dob = dob

    def input(self):
        pass

    def list(self):
        pass


class Student(Person):
    def __init__(self, id, name, dob):
        super().__init__(id, name, dob)

    def list(self):
        print(f"{self._id} - {self._name} - DoB: {self._dob}")

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name


class Course:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def list(self):
        print(f"{self._id} - {self._name}")

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name


class Mark:
    def __init__(self, course, student, mark):
        self._course = course
        self._student = student
        self._mark = mark

    def list(self):
        print(f"{self._student.get_id()} - {self._student.get_name()}: {self._mark}")

    def get_course_id(self):
        return self._course.get_id()



class ManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_students(self):
        n = int(input("Enter number of students: "))
        for i in range(n):
            print(f"\n--- Student {i+1} ---")
            sid = input("Student ID: ")
            name = input("Student Name: ")
            dob = input("Date of Birth: ")
            self.students.append(Student(sid, name, dob))

    def list_students(self):
        print("\n=== Student List ===")
        for s in self.students:
            s.list()

    def input_courses(self):
        m = int(input("Enter number of courses: "))
        for i in range(m):
            print(f"\n--- Course {i+1} ---")
            cid = input("Course ID: ")
            name = input("Course Name: ")
            self.courses.append(Course(cid, name))

    def list_courses(self):
        print("\n=== Course List ===")
        for c in self.courses:
            c.list()

    def input_marks(self):
        print("\nAvailable courses:")
        for c in self.courses:
            c.list()

        cid = input("Select course ID: ")

        selected_course = None
        for c in self.courses:
            if c.get_id() == cid:
                selected_course = c
                break

        if selected_course is None:
            print("Course not found!")
            return

        print("\nEnter marks for each student:")
        for s in self.students:
            mark = float(input(f"Mark for {s.get_name()} ({s.get_id()}): "))
            self.marks.append(Mark(selected_course, s, mark))

    def show_marks(self):
        print("\nAvailable courses:")
        for c in self.courses:
            c.list()

        cid = input("Enter course ID to show marks: ")

        print(f"\n=== Marks for course {cid} ===")
        for m in self.marks:
            if m.get_course_id() == cid:
                m.list()

    def run(self):
        print("===== OOP Student Mark Management =====")

        self.input_students()
        self.input_courses()

        while True:
            print("\n------ MENU ------")
            print("1. List students")
            print("2. List courses")
            print("3. Input marks")
            print("4. Show marks")
            print("0. Exit")

            choice = input("Choose option: ")

            if choice == "1":
                self.list_students()
            elif choice == "2":
                self.list_courses()
            elif choice == "3":
                self.input_marks()
            elif choice == "4":
                self.show_marks()
            elif choice == "0":
                print("Exiting...")
                break
            else:
                print("Invalid choice!")

system = ManagementSystem()
system.run()
