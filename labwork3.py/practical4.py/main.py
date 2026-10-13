import curses

# Import predefined data from input.py
from input import (
    class_name,
    number_of_students,
    number_of_courses,
    students,
    courses,
    marks
)

# Import functions from output.py
from output import (
    curses_menu,
    get_class_information,
    get_course_list,
    get_student_list,
    get_all_marks
)


# Store the content that will be displayed on the result page.
page_text = None


# Keep the program running until the user chooses Exit.
while True:

    selection = curses.wrapper(
        curses_menu,
        class_name,
        page_text
    )


    # After displaying a result, reset page_text
    # so the program can return to the main menu.
    if page_text is not None:
        page_text = None
        continue


    # If no selection is returned, restart the loop.
    if selection is None:
        continue


    # Check whether the selected key is from 0 to 4.
    if (
        ord("0")
        <= selection
        <= ord("4")
    ):
        # Convert the key code into a string.
        choice = chr(selection)

    else:
        choice = ""


    # Show class information.
    if choice == "1":

        page_text = get_class_information(
            class_name,
            number_of_students,
            number_of_courses
        )


    # Show all courses.
    elif choice == "2":

        page_text = get_course_list(
            courses
        )


    # Show all students.
    elif choice == "3":

        page_text = get_student_list(
            students
        )


    # Show all marks.
    elif choice == "4":

        page_text = get_all_marks(
            students,
            courses,
            marks
        )


    # Exit the program.
    elif choice == "0":

        break


    # Handle an invalid menu option.
    else:

        page_text = (
            "Invalid option.\n"
            "Please choose from 0 to 4."
        )