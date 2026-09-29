def list_courses(courses):
    for course in courses:
        print(
            f"ID: {course.course.id},"
            f"Name: {course.name}"
        )

def list_students(students):
    for student in students:
        print(
            f"ID: {student.student_id},"
            f"Name: {student.name},"
            f"DoB: {student.dob}"
        )

#decor
import curses


def curses_menu(stdscr, class_name, page_text=None):

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

    screen_height, screen_width = stdscr.getmaxyx()


    # Check terminal size
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


    # Center the window
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