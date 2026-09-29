from domains import Student, Course #import class Student and Course from package domain
class_name = "12E4"
number_of_students = 5

students = [
    Student("S01", "Nguyen Minh Anh", "15/03/2008"),
    Student("S02", "Tran Hoang Nam", "21/07/2008"),
    Student("S02", "Tran Hoang Nam", "21/07/2008"),
    Student("S03", "Le Thu Ha", "09/11/2008"),
    Student("S04", "Pham Gia Bao", "27/01/2008"),
    Student("S05", "Do Ngoc Linh", "04/06/2008")
]
number_of_course = 5

courses = [
    Course("C01", "Mathematics"),
    Course("C02", "English"),
    Course("C03", "Physics"),
    Course("C04", "Chemistry"),
    Course("C05", "Computer Science")
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

def input_number_of_students():
    return number_of_students


def input_students_information():
    return students


def input_number_of_courses():
    return number_of_courses


def input_courses():
    return courses


def input_marks():
    return marks
