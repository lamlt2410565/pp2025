
students = []     
courses = []      
marks = {}       


def input_number_of_students():
    n = int(input("Enter number of students: "))
    return n


def input_student_information(n):
    for i in range(n):
        print(f"\n--- Student {i+1} ---")
        sid = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("Date of Birth: ")

        students.append({
            "id": sid,
            "name": name,
            "dob": dob
        })


def input_number_of_courses():
    m = int(input("Enter number of courses: "))
    return m


def input_course_information(m):
    for i in range(m):
        print(f"\n--- Course {i+1} ---")
        cid = input("Course ID: ")
        name = input("Course Name: ")

        courses.append({
            "id": cid,
            "name": name
        })


def input_marks_for_course():
    print("\nAvailable courses:")
    for c in courses:
        print(f"- {c['id']}: {c['name']}")

    cid = input("Select course ID to input marks: ")

    if cid not in marks:
        marks[cid] = []

    print("\nEnter marks for students:")
    for s in students:
        mark = float(input(f"Mark for {s['name']} ({s['id']}): "))
        marks[cid].append((s["id"], mark))



def list_courses():
    print("\n=== Course List ===")
    for c in courses:
        print(f"{c['id']} - {c['name']}")


def list_students():
    print("\n=== Student List ===")
    for s in students:
        print(f"{s['id']} - {s['name']} - DoB: {s['dob']}")


def show_student_marks():
    print("\nAvailable courses:")
    for c in courses:
        print(f"- {c['id']}: {c['name']}")

    cid = input("Enter course ID to show marks: ")

    if cid not in marks:
        print("No marks for this course yet.")
        return

    print(f"\n=== Marks for course {cid} ===")
    for sid, mark in marks[cid]:
        name = ""
        for s in students:
            if s["id"] == sid:
                name = s["name"]
                break
        print(f"{sid} - {name}: {mark}")



def main():
    print("===== STUDENT MARK MANAGEMENT =====")

    n = input_number_of_students()
    input_student_information(n)

    m = input_number_of_courses()
    input_course_information(m)

    while True:
        print("\n------ MENU ------")
        print("1. List courses")
        print("2. List students")
        print("3. Input marks for a course")
        print("4. Show student marks for a course")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            list_courses()
        elif choice == "2":
            list_students()
        elif choice == "3":
            input_marks_for_course()
        elif choice == "4":
            show_student_marks()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

main()
