import os
import zipfile

from domains import Student, Course


class_name = "12E4"


# =========================
# INPUT
# =========================

def input_number_of_students():
    number_of_students = int(
        input("Enter number of students: ")
    )

    return number_of_students


def input_students_information(number_of_students):
    students = []

    for i in range(number_of_students):
        print(f"\nStudent {i + 1}")

        student_id = input("Student ID: ")
        name = input("Name: ")
        dob = input("Date of birth: ")

        student = Student(
            student_id,
            name,
            dob
        )

        students.append(student)

    with open("students.txt", "w") as file:
        for student in students:
            file.write(
                f"{student.student_id},"
                f"{student.name},"
                f"{student.dob}\n"
            )

    return students


def input_number_of_courses():
    number_of_courses = int(
        input("Enter number of courses: ")
    )

    return number_of_courses


def input_courses(number_of_courses):
    courses = []

    for i in range(number_of_courses):
        print(f"\nCourse {i + 1}")

        course_id = input("Course ID: ")
        name = input("Course name: ")

        course = Course(
            course_id,
            name
        )

        courses.append(course)

    with open("courses.txt", "w") as file:
        for course in courses:
            file.write(
                f"{course.course_id},"
                f"{course.name}\n"
            )

    return courses


def input_marks(students, courses):
    marks = {}

    for course in courses:
        marks[course.course_id] = {}

        print(
            f"\nEnter marks for "
            f"{course.course_id} - {course.name}"
        )

        for student in students:
            mark = float(
                input(
                    f"{student.student_id} "
                    f"{student.name}: "
                )
            )

            marks[course.course_id][student.student_id] = mark

    with open("marks.txt", "w") as file:
        for course_id in marks:
            for student_id in marks[course_id]:
                file.write(
                    f"{course_id},"
                    f"{student_id},"
                    f"{marks[course_id][student_id]}\n"
                )

    return marks


# =========================
# COMPRESSION
# =========================

def compress_data():
    with zipfile.ZipFile(
        "students.dat",
        "w",
        zipfile.ZIP_DEFLATED
    ) as zip_file:

        zip_file.write("students.txt")
        zip_file.write("courses.txt")
        zip_file.write("marks.txt")


def decompress_data():
    with zipfile.ZipFile(
        "students.dat",
        "r"
    ) as zip_file:

        zip_file.extractall()


# =========================
# LOAD OLD DATA
# =========================

def load_students():
    students = []

    with open("students.txt", "r") as file:
        for line in file:
            student_id, name, dob = line.strip().split(",")

            student = Student(
                student_id,
                name,
                dob
            )

            students.append(student)

    return students


def load_courses():
    courses = []

    with open("courses.txt", "r") as file:
        for line in file:
            course_id, name = line.strip().split(",")

            course = Course(
                course_id,
                name
            )

            courses.append(course)

    return courses


def load_marks():
    marks = {}

    with open("marks.txt", "r") as file:
        for line in file:
            course_id, student_id, mark = line.strip().split(",")

            if course_id not in marks:
                marks[course_id] = {}

            marks[course_id][student_id] = float(mark)

    return marks


def data_file_exists():
    return os.path.exists("students.dat")