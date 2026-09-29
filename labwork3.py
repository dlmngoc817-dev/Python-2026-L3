import math
import numpy as np
import curses


# Ask for the class name and the number of students.
def input_number_of_students():
    class_name = input("Input class name: ")
    number_of_students = int(input("Input number of students: "))

    return class_name, number_of_students


# Collect information about every student.
def input_students_information(number_of_students):
    students = []

    for i in range(number_of_students):
        print(f"\nStudent {i + 1}:")
        student_id = input("Input student ID: ")
        name = input("Input student name: ")
        dob = input("Input date of birth: ")

        student = {
            "id": student_id,
            "name": name,
            "dob": dob
        }

        students.append(student)

    return students


# Ask how many courses the class has.
def input_number_of_courses():
    number_of_courses = int(input("Input number of courses: "))
    return number_of_courses


# Collect the ID, name and credits of every course.
def input_courses(number_of_courses):
    courses = []

    for i in range(number_of_courses):
        print(f"\nCourse {i + 1}:")
        course_id = input("Input course ID: ")
        course_name = input("Input course name: ")
        credits = float(input("Input number of credits: "))

        course = {
            "id": course_id,
            "name": course_name,
            "credits": credits
        }

        courses.append(course)

    return courses


# Round a mark DOWN to 1 decimal place.
def round_down(mark):
    return math.floor(mark * 10) / 10


# Select a course and enter marks for all students.
def input_marks(students, courses, marks):
    course_id = input("Input course ID to enter marks: ")

    for course in courses:
        if course["id"] == course_id:

            if course_id not in marks:
                marks[course_id] = {}

            for student in students:
                mark = float(
                    input(f"Input mark for {student['name']}: ")
                )

                # Round DOWN to one decimal place.
                mark = round_down(mark)

                marks[course_id][student["id"]] = mark

            return marks

    print("Course not found.")
    return marks


# Print the ID, name and credits of every course.
def list_courses(courses):
    print("\nCOURSE LIST")

    for course in courses:
        print(
            f"ID: {course['id']}, "
            f"Name: {course['name']}, "
            f"Credits: {course['credits']}"
        )


# Print the information of every student.
def list_students(students):
    print("\nSTUDENT LIST")

    for student in students:
        print(
            f"ID: {student['id']}, "
            f"Name: {student['name']}, "
            f"DoB: {student['dob']}"
        )


# Show marks for a selected course.
def show_marks(students, courses, marks):
    course_id = input("Input course ID to show marks: ")

    for course in courses:
        if course["id"] == course_id:
            print(f"\nMarks for {course['name']}:")

            if course_id not in marks:
                print("No marks have been entered for this course.")
                return

            for student in students:
                student_id = student["id"]

                if student_id in marks[course_id]:
                    mark = marks[course_id][student_id]
                    print(f"{student['name']} ({student_id}): {mark}")

            return

    print("Course not found.")


# Calculate weighted GPA for one student.
def calculate_gpa(student_id, courses, marks):
    student_marks = []
    student_credits = []

    for course in courses:
        course_id = course["id"]

        if (
            course_id in marks
            and student_id in marks[course_id]
        ):
            student_marks.append(marks[course_id][student_id])
            student_credits.append(course["credits"])

    # Convert Python lists to NumPy arrays.
    mark_array = np.array(student_marks, dtype=float)
    credit_array = np.array(student_credits, dtype=float)

    if len(mark_array) == 0:
        return None

    # Weighted GPA:
    # sum(mark * credit) / sum(credit)
    gpa = np.sum(mark_array * credit_array) / np.sum(credit_array)

    return gpa


# Show the GPA of one selected student.
def show_student_gpa(students, courses, marks):
    student_id = input("Input student ID: ")

    for student in students:
        if student["id"] == student_id:

            gpa = calculate_gpa(student_id, courses, marks)

            if gpa is None:
                print("No marks available for this student.")
            else:
                print(
                    f"{student['name']} ({student_id}) "
                    f"GPA: {gpa:.2f}"
                )

            return

    print("Student not found.")


# Sort all students by GPA descending.
def sort_students_by_gpa(students, courses, marks):
    student_gpas = []

    for student in students:
        gpa = calculate_gpa(student["id"], courses, marks)

        if gpa is None:
            gpa = 0

        student_gpas.append(
            {
                "id": student["id"],
                "name": student["name"],
                "gpa": gpa
            }
        )

    student_gpas.sort(
        key=lambda student: student["gpa"],
        reverse=True
    )

    print("\nSTUDENTS SORTED BY GPA")

    for student in student_gpas:
        print(
            f"ID: {student['id']}, "
            f"Name: {student['name']}, "
            f"GPA: {student['gpa']:.2f}"
        )


# Curses decorated menu.
def curses_menu(stdscr, class_name):
    curses.curs_set(0)

    curses.start_color()

    curses.init_pair(
        1,
        curses.COLOR_CYAN,
        curses.COLOR_BLACK
    )

    curses.init_pair(
        2,
        curses.COLOR_YELLOW,
        curses.COLOR_BLACK
    )

    stdscr.clear()

    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(1, 5, "==============================")
    stdscr.addstr(2, 5, "   STUDENT MANAGEMENT SYSTEM")
    stdscr.addstr(3, 5, "==============================")
    stdscr.attroff(curses.color_pair(1))

    stdscr.attron(curses.color_pair(2))
    stdscr.addstr(5, 5, f"CLASS: {class_name}")
    stdscr.attroff(curses.color_pair(2))

    stdscr.addstr(7, 5, "1. Input marks for a course")
    stdscr.addstr(8, 5, "2. List courses")
    stdscr.addstr(9, 5, "3. List students")
    stdscr.addstr(10, 5, "4. Show marks for a course")
    stdscr.addstr(11, 5, "5. Show student GPA")
    stdscr.addstr(12, 5, "6. Sort students by GPA")
    stdscr.addstr(13, 5, "0. Exit")

    stdscr.addstr(15, 5, "Press any key to continue...")

    stdscr.refresh()
    stdscr.getch()


# ----- Main program -----

class_name, number_of_students = input_number_of_students()

students = input_students_information(
    number_of_students
)

number_of_courses = input_number_of_courses()

courses = input_courses(
    number_of_courses
)

marks = {}


while True:

    # Display decorated UI using curses.
    curses.wrapper(
        curses_menu,
        class_name
    )

    print(f"\nCLASS: {class_name}")
    print("1. Input marks for a course")
    print("2. List courses")
    print("3. List students")
    print("4. Show marks for a course")
    print("5. Show student GPA")
    print("6. Sort students by GPA")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        marks = input_marks(
            students,
            courses,
            marks
        )

    elif choice == "2":
        list_courses(courses)

    elif choice == "3":
        list_students(students)

    elif choice == "4":
        show_marks(
            students,
            courses,
            marks
        )

    elif choice == "5":
        show_student_gpa(
            students,
            courses,
            marks
        )

    elif choice == "6":
        sort_students_by_gpa(
            students,
            courses,
            marks
        )

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")