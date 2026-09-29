<<<<<<< HEAD
# Ask for the class name and the number of students.
def input_number_of_students():
    class_name = input("Input class name: ")
    number_of_students = int(input("Input number of students: "))

    # Return both values so they can be used outside this function.
    return class_name, number_of_students


# Collect information about every student.
def input_students_information(number_of_students):
    students = []  # This list will contain all student dictionaries.

    # Repeat the input process once for each student.
    for i in range(number_of_students):
        print(f"\nStudent {i + 1}:")
        student_id = input("Input student ID: ")
        name = input("Input student name: ")
        dob = input("Input date of birth: ")

        # Store the information of one student in a dictionary.
        student = {
            "id": student_id,
            "name": name,
            "dob": dob
        }

        # Add this student's dictionary to the students list.
        students.append(student)

    return students


# Ask how many courses the class has.
def input_number_of_courses():
    number_of_courses = int(input("Input number of courses: "))
    return number_of_courses


# Collect the ID and name of every course.
def input_courses(number_of_courses):
    courses = []  # This list will contain all course dictionaries.

    for i in range(number_of_courses):
        print(f"\nCourse {i + 1}:")
        course_id = input("Input course ID: ")
        course_name = input("Input course name: ")

        # Store one course's information in a dictionary.
        course = {
            "id": course_id,
            "name": course_name
        }

        courses.append(course)

    return courses


# Select a course and enter marks for all students in that course.
def input_marks(students, courses, marks):
    course_id = input("Input course ID to enter marks: ")

    # Search for the selected course in the courses list.
    for course in courses:
        if course["id"] == course_id:

            # Create a dictionary for this course if it does not exist yet.
            # Example: marks = {"PY01": {}}
            if course_id not in marks:
                marks[course_id] = {}

            # Enter one mark for each student.
            for student in students:
                mark = float(
                    input(f"Input mark for {student['name']}: ")
                )

                # Save the mark using the course ID and student ID.
                # Example: marks["PY01"]["S01"] = 8.5
                marks[course_id][student["id"]] = mark

            # The course was found, so the function can finish here.
            return marks

    # This line runs only if no course has the entered ID.
    print("Course not found.")
    return marks


# Print the ID and name of every course.
def list_courses(courses):
    print("\nCOURSE LIST")

    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")


# Print the information of every student.
def list_students(students):
    print("\nSTUDENT LIST")

    for student in students:
        print(
            f"ID: {student['id']}, "
            f"Name: {student['name']}, "
            f"DoB: {student['dob']}"
        )


# Show all available student marks for a selected course.
def show_marks(students, courses, marks):
    course_id = input("Input course ID to show marks: ")

    # First, check whether the selected course exists.
    for course in courses:
        if course["id"] == course_id:
            print(f"\nMarks for {course['name']}:")

            # The course exists, but its marks may not have been entered.
            if course_id not in marks:
                print("No marks have been entered for this course.")
                return

            # Match each student ID with the mark stored for this course.
            for student in students:
                student_id = student["id"]

                if student_id in marks[course_id]:
                    mark = marks[course_id][student_id]
                    print(f"{student['name']} ({student_id}): {mark}")

            return

    # The loop finished without finding the course.
    print("Course not found.")


# ----- Main program -----

# Collect student and course information before showing the menu.
class_name, number_of_students = input_number_of_students()
students = input_students_information(number_of_students)

number_of_courses = input_number_of_courses()
courses = input_courses(number_of_courses)

# Marks are empty until the user chooses option 1.
marks = {}

# Keep showing the menu until the user chooses 0.
while True:
    print(f"\nCLASS: {class_name}")
    print("1. Input marks for a course")
    print("2. List courses")
    print("3. List students")
    print("4. Show marks for a course")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        marks = input_marks(students, courses, marks)
    elif choice == "2":
        list_courses(courses)
    elif choice == "3":
        list_students(students)
    elif choice == "4":
        show_marks(students, courses, marks)
    elif choice == "0":
        print("Goodbye!")
        break  # Stop the while loop and end the program.
    else:
=======
# Ask for the class name and the number of students.
def input_number_of_students():
    class_name = input("Input class name: ")
    number_of_students = int(input("Input number of students: "))

    # Return both values so they can be used outside this function.
    return class_name, number_of_students


# Collect information about every student.
def input_students_information(number_of_students):
    students = []  # This list will contain all student dictionaries.

    # Repeat the input process once for each student.
    for i in range(number_of_students):
        print(f"\nStudent {i + 1}:")
        student_id = input("Input student ID: ")
        name = input("Input student name: ")
        dob = input("Input date of birth: ")

        # Store the information of one student in a dictionary.
        student = {
            "id": student_id,
            "name": name,
            "dob": dob
        }

        # Add this student's dictionary to the students list.
        students.append(student)

    return students


# Ask how many courses the class has.
def input_number_of_courses():
    number_of_courses = int(input("Input number of courses: "))
    return number_of_courses


# Collect the ID and name of every course.
def input_courses(number_of_courses):
    courses = []  # This list will contain all course dictionaries.

    for i in range(number_of_courses):
        print(f"\nCourse {i + 1}:")
        course_id = input("Input course ID: ")
        course_name = input("Input course name: ")

        # Store one course's information in a dictionary.
        course = {
            "id": course_id,
            "name": course_name
        }

        courses.append(course)

    return courses


# Select a course and enter marks for all students in that course.
def input_marks(students, courses, marks):
    course_id = input("Input course ID to enter marks: ")

    # Search for the selected course in the courses list.
    for course in courses:
        if course["id"] == course_id:

            # Create a dictionary for this course if it does not exist yet.
            # Example: marks = {"PY01": {}}
            if course_id not in marks:
                marks[course_id] = {}

            # Enter one mark for each student.
            for student in students:
                mark = float(
                    input(f"Input mark for {student['name']}: ")
                )

                # Save the mark using the course ID and student ID.
                # Example: marks["PY01"]["S01"] = 8.5
                marks[course_id][student["id"]] = mark

            # The course was found, so the function can finish here.
            return marks

    # This line runs only if no course has the entered ID.
    print("Course not found.")
    return marks


# Print the ID and name of every course.
def list_courses(courses):
    print("\nCOURSE LIST")

    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")


# Print the information of every student.
def list_students(students):
    print("\nSTUDENT LIST")

    for student in students:
        print(
            f"ID: {student['id']}, "
            f"Name: {student['name']}, "
            f"DoB: {student['dob']}"
        )


# Show all available student marks for a selected course.
def show_marks(students, courses, marks):
    course_id = input("Input course ID to show marks: ")

    # First, check whether the selected course exists.
    for course in courses:
        if course["id"] == course_id:
            print(f"\nMarks for {course['name']}:")

            # The course exists, but its marks may not have been entered.
            if course_id not in marks:
                print("No marks have been entered for this course.")
                return

            # Match each student ID with the mark stored for this course.
            for student in students:
                student_id = student["id"]

                if student_id in marks[course_id]:
                    mark = marks[course_id][student_id]
                    print(f"{student['name']} ({student_id}): {mark}")

            return

    # The loop finished without finding the course.
    print("Course not found.")


# ----- Main program -----

# Collect student and course information before showing the menu.
class_name, number_of_students = input_number_of_students()
students = input_students_information(number_of_students)

number_of_courses = input_number_of_courses()
courses = input_courses(number_of_courses)

# Marks are empty until the user chooses option 1.
marks = {}

# Keep showing the menu until the user chooses 0.
while True:
    print(f"\nCLASS: {class_name}")
    print("1. Input marks for a course")
    print("2. List courses")
    print("3. List students")
    print("4. Show marks for a course")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        marks = input_marks(students, courses, marks)
    elif choice == "2":
        list_courses(courses)
    elif choice == "3":
        list_students(students)
    elif choice == "4":
        show_marks(students, courses, marks)
    elif choice == "0":
        print("Goodbye!")
        break  # Stop the while loop and end the program.
    else:
>>>>>>> b0e0a7e (submit labwork 3)
        print("Invalid option.")