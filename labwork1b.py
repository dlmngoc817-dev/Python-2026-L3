# =========================================
# PREDEFINED DATA
# =========================================

class_name = "12E4"

number_of_students = 5

students = [
    {
        "id": "S01",
        "name": "Nguyen Minh Anh",
        "dob": "15/03/2008"
    },
    {
        "id": "S02",
        "name": "Tran Hoang Nam",
        "dob": "21/07/2008"
    },
    {
        "id": "S03",
        "name": "Le Thu Ha",
        "dob": "09/11/2008"
    },
    {
        "id": "S04",
        "name": "Pham Gia Bao",
        "dob": "27/01/2008"
    },
    {
        "id": "S05",
        "name": "Do Ngoc Linh",
        "dob": "04/06/2008"
    }
]

number_of_courses = 5

courses = [
    {
        "id": "C01",
        "name": "Mathematics"
    },
    {
        "id": "C02",
        "name": "English"
    },
    {
        "id": "C03",
        "name": "Physics"
    },
    {
        "id": "C04",
        "name": "Chemistry"
    },
    {
        "id": "C05",
        "name": "Computer Science"
    }
]

marks = {
    "C01": {
        "S01": 8.5,
        "S02": 7.8,
        "S03": 9.2,
        "S04": 6.9,
        "S05": 8.1
    },

    "C02": {
        "S01": 9.0,
        "S02": 8.2,
        "S03": 8.8,
        "S04": 7.4,
        "S05": 9.1
    },

    "C03": {
        "S01": 7.8,
        "S02": 8.7,
        "S03": 9.1,
        "S04": 7.2,
        "S05": 8.9
    },

    "C04": {
        "S01": 8.5,
        "S02": 7.6,
        "S03": 8.4,
        "S04": 6.9,
        "S05": 9.3
    },

    "C05": {
        "S01": 9.3,
        "S02": 8.8,
        "S03": 9.6,
        "S04": 7.7,
        "S05": 8.5
    }
}


# =========================================
# INPUT FUNCTIONS
# =========================================

# Return the predefined number of students.
def input_number_of_students():
    return number_of_students


# Return predefined student information.
def input_students_information():
    return students


# Return the predefined number of courses.
def input_number_of_courses():
    return number_of_courses


# Return predefined course information.
def input_courses():
    return courses


# Return predefined marks.
def input_marks():
    return marks


# =========================================
# LISTING FUNCTIONS
# =========================================

# List all courses.
def list_courses(courses):
    print("\nCOURSE LIST")

    for course in courses:
        print(
            f"ID: {course['id']}, "
            f"Name: {course['name']}"
        )


# List all students.
def list_students(students):
    print("\nSTUDENT LIST")

    for student in students:
        print(
            f"ID: {student['id']}, "
            f"Name: {student['name']}, "
            f"DoB: {student['dob']}"
        )


# Show marks for one given course.
def show_marks(students, courses, marks, course_id):

    for course in courses:

        if course["id"] == course_id:

            print(
                f"\nMarks for {course['name']}:"
            )

            for student in students:

                student_id = student["id"]

                mark = marks[course_id][student_id]

                print(
                    f"{student['name']} "
                    f"({student_id}): {mark}"
                )

            return

    print("Course not found.")


# =========================================
# MAIN PROGRAM
# =========================================

print(f"CLASS: {class_name}")
print(
    f"Number of students: "
    f"{input_number_of_students()}"
)
print(
    f"Number of courses: "
    f"{input_number_of_courses()}"
)

print("\nSTUDENT INFORMATION")
list_students(
    input_students_information()
)

print("\nCOURSE INFORMATION")
list_courses(
    input_courses()
)

print("\nMARKS")

show_marks(
    students,
    courses,
    input_marks(),
    "C01"
)

show_marks(
    students,
    courses,
    input_marks(),
    "C02"
)

show_marks(
    students,
    courses,
    input_marks(),
    "C03"
)

show_marks(
    students,
    courses,
    input_marks(),
    "C04"
)

show_marks(
    students,
    courses,
    input_marks(),
    "C05"
)