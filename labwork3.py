import curses
import io
from contextlib import redirect_stdout


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


# =========================================
# LISTING FUNCTIONS
# =========================================

def list_courses(courses):
    print("\nCOURSE LIST")

    for course in courses:
        print(
            f"ID: {course['id']}, "
            f"Name: {course['name']}"
        )


def list_students(students):
    print("\nSTUDENT LIST")

    for student in students:
        print(
            f"ID: {student['id']}, "
            f"Name: {student['name']}, "
            f"DoB: {student['dob']}"
        )


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
# GET PRINT OUTPUT
# =========================================

def get_course_list():
    output = io.StringIO()

    with redirect_stdout(output):
        list_courses(courses)

    return output.getvalue()


def get_student_list():
    output = io.StringIO()

    with redirect_stdout(output):
        list_students(students)

    return output.getvalue()


def get_all_marks():
    output = io.StringIO()

    with redirect_stdout(output):

        show_marks(
            students,
            courses,
            marks,
            "C01"
        )

        show_marks(
            students,
            courses,
            marks,
            "C02"
        )

        show_marks(
            students,
            courses,
            marks,
            "C03"
        )

        show_marks(
            students,
            courses,
            marks,
            "C04"
        )

        show_marks(
            students,
            courses,
            marks,
            "C05"
        )

    return output.getvalue()


def get_class_information():

    return (
        f"CLASS: {class_name}\n\n"
        f"Number of students: "
        f"{input_number_of_students()}\n"
        f"Number of courses: "
        f"{input_number_of_courses()}"
    )


# =========================================
# CURSES DECORATION
# =========================================

def curses_menu(
    stdscr,
    class_name,
    page_text=None
):

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

    height = 20
    width = 60

    screen_height, screen_width = (
        stdscr.getmaxyx()
    )


    if (
        screen_height < height
        or screen_width < width
    ):

        stdscr.clear()

        message = (
            "Resize terminal to at least "
            "60 columns x 20 rows."
        )

        stdscr.addnstr(
            0,
            0,
            message,
            screen_width - 1
        )

        stdscr.refresh()
        stdscr.getch()

        return None


    top = max(
        0,
        (screen_height - height) // 2
    )

    left = max(
        0,
        (screen_width - width) // 2
    )


    window = curses.newwin(
        height,
        width,
        top,
        left
    )


    # =====================================
    # RESULT PAGE
    # =====================================

    if page_text is not None:

        page_lines = (
            page_text.splitlines()
            or [""]
        )

        content_height = height - 10

        first_line = 0


        while True:

            window.clear()

            window.attron(
                curses.color_pair(1)
            )

            window.box()

            window.addstr(
                2,
                14,
                "STUDENT MANAGEMENT SYSTEM"
            )

            window.hline(
                4,
                2,
                curses.ACS_HLINE,
                width - 4
            )

            window.attroff(
                curses.color_pair(1)
            )


            window.attron(
                curses.color_pair(2)
            )

            window.addstr(
                6,
                4,
                "RESULT"
            )

            window.attroff(
                curses.color_pair(2)
            )


            row = 8

            for line in page_lines[
                first_line:
                first_line + content_height
            ]:

                if row < height - 2:

                    window.addnstr(
                        row,
                        4,
                        line,
                        width - 8
                    )

                    row += 1


            if (
                len(page_lines)
                > content_height
            ):

                prompt = (
                    "UP/DOWN: Scroll | "
                    "Other key: Menu"
                )

            else:

                prompt = (
                    "Press any key to return."
                )


            window.addnstr(
                height - 2,
                4,
                prompt,
                width - 8
            )

            window.refresh()

            key = window.getch()


            if (
                key == curses.KEY_UP
                and first_line > 0
            ):

                first_line -= 1


            elif (
                key == curses.KEY_DOWN
                and first_line
                + content_height
                < len(page_lines)
            ):

                first_line += 1


            else:

                return -1


    # =====================================
    # MAIN MENU
    # =====================================

    window.clear()

    window.attron(
        curses.color_pair(1)
    )

    window.box()

    window.addstr(
        2,
        14,
        "STUDENT MANAGEMENT SYSTEM"
    )

    window.hline(
        4,
        2,
        curses.ACS_HLINE,
        width - 4
    )

    window.attroff(
        curses.color_pair(1)
    )


    window.attron(
        curses.color_pair(2)
    )

    window.addstr(
        6,
        4,
        f"CLASS: {class_name}"
    )

    window.attroff(
        curses.color_pair(2)
    )


    window.addstr(
        8,
        4,
        "1. Class information"
    )

    window.addstr(
        9,
        4,
        "2. List courses"
    )

    window.addstr(
        10,
        4,
        "3. List students"
    )

    window.addstr(
        11,
        4,
        "4. Show marks"
    )

    window.addstr(
        12,
        4,
        "0. Exit"
    )


    window.attron(
        curses.color_pair(2)
    )

    window.addstr(
        15,
        4,
        "Choose an option (0-4):"
    )

    window.attroff(
        curses.color_pair(2)
    )


    window.refresh()

    return window.getch()


# =========================================
# MAIN PROGRAM
# =========================================

page_text = None


while True:

    selection = curses.wrapper(
        curses_menu,
        class_name,
        page_text
    )


    if page_text is not None:

        page_text = None

        continue


    if selection is None:
        continue


    if (
        ord("0")
        <= selection
        <= ord("4")
    ):

        choice = chr(selection)

    else:

        choice = ""


    if choice == "1":

        page_text = (
            get_class_information()
        )


    elif choice == "2":

        page_text = (
            get_course_list()
        )


    elif choice == "3":

        page_text = (
            get_student_list()
        )


    elif choice == "4":

        page_text = (
            get_all_marks()
        )


    elif choice == "0":

        break


    else:

        page_text = (
            "Invalid option.\n"
            "Please choose from 0 to 4."
        )