import curses

from input import (
    input_number_of_students,
    input_students_information,
    input_number_of_courses,
    input_courses,
    input_marks,
    compress_data,
    decompress_data,
    load_students,
    load_courses,
    load_marks,
    data_file_exists
)

from output import (
    curses_menu,
    get_class_information,
    get_course_list,
    get_student_list,
    get_all_marks
)


# =========================
# CLASS NAME
# =========================

class_name = "12E4"


# =========================
# LOAD OLD DATA OR INPUT NEW DATA
# =========================

if data_file_exists():

    # students.dat already exists
    # -> extract old data
    decompress_data()

    students = load_students()
    courses = load_courses()
    marks = load_marks()

    number_of_students = len(students)
    number_of_courses = len(courses)

else:

    # No old data
    # -> input new information
    number_of_students = input_number_of_students()

    students = input_students_information(
        number_of_students
    )

    number_of_courses = input_number_of_courses()

    courses = input_courses(
        number_of_courses
    )

    marks = input_marks(
        students,
        courses
    )


# =========================
# MENU
# =========================

page_text = None


while True:

    selection = curses.wrapper(
        curses_menu,
        class_name,
        page_text
    )


    # After showing a result,
    # return to the main menu
    if page_text is not None:
        page_text = None
        continue


    # If no selection is returned,
    # restart the menu
    if selection is None:
        continue


    # Convert key 0-4 into a string
    if (
        ord("0")
        <= selection
        <= ord("4")
    ):
        choice = chr(selection)

    else:
        choice = ""


    # =========================
    # OPTION 1
    # CLASS INFORMATION
    # =========================

    if choice == "1":

        page_text = get_class_information(
            class_name,
            number_of_students,
            number_of_courses
        )


    # =========================
    # OPTION 2
    # COURSE LIST
    # =========================

    elif choice == "2":

        page_text = get_course_list(
            courses
        )


    # =========================
    # OPTION 3
    # STUDENT LIST
    # =========================

    elif choice == "3":

        page_text = get_student_list(
            students
        )


    # =========================
    # OPTION 4
    # MARKS
    # =========================

    elif choice == "4":

        page_text = get_all_marks(
            students,
            courses,
            marks
        )


    # =========================
    # OPTION 0
    # EXIT
    # =========================

    elif choice == "0":

        # Compress txt files into students.dat
        compress_data()

        break


    # =========================
    # INVALID OPTION
    # =========================

    else:

        page_text = (
            "Invalid option.\n"
            "Please choose from 0 to 4."
        )

