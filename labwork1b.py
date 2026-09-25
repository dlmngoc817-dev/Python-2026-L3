




#input number of students in a class:
def input_number_of_students():
    class_name = input("Input class name:")
    number_of_students = int(input("Input number of students: "))
    return class_name, number_of_students

#input student information: id. name, DoB
def input_students_information(number_of_students):
    students = []
    for i in range(number_of_students):
        print(f"\nStudent {i+1}:")
        student_id = input("Input student ID: ")
        name = input("Input student name:")
        dob = input("Input date of birth:")
        student = {
            "id": student_id,
            "name": name,
            "dob": dob
        }
        students.append(student) #Store that student in a list of multiple students.
    return students 

class_name, number_of_students = input_number_of_students()
students = input_students_information(number_of_students)
print("Class Name:", class_name)
print("Students Information:", students)

# input number of courses in a class:
def input_number_of_courses():
    number_of_courses = int(input("Input number of courses: "))
    return number_of_courses 

#Input course information: id, name
def input_courses(number_of_courses):
    courses = []
    for i in range(number_of_courses):
        print(f"\nCourse {i+1}")
        course_id = input("Input course ID: ")
        course_name = input("Input course name: ")
        course = {
        "id": course_id,
        "name": course_name 
        }
        courses.append(course)
    return courses 

#Select a course, input marks for student in this course
def input_marks(students, courses): #khai báo hàm, hàm nhận 2 dữ liệu students (danh sách sinh viên) và courses(danh sách môn học)
    course_id = input("Input course ID to enter marks: ") #nhập mã môn muốn nhập điểm 
    marks = {} #tạo dictionary rỗng để lưu điểm 
    for course in courses: #duyệt qua từng môn trong danh sách courses
        if course["id"] == course_id: #kiểm tra mã môn trong danh sách có giống mã bạn vừa nhập không ?, hàm true hoặc false 
            marks[course_id] = {} #tạo dictionary rỗng để lưu điểm cho môn, nếu bạn chọn môn PY01 -> "PYO1": {} -> MÔN PY01 có chỗ để lưu điểm

            for student in students: #lấy từng students trong danh sách ra 
                mark = float( #kiểu dữ liệu float vì điểm có thể là số thập phân
                    input(f"Input mark for {student['name']}: ") #nhập điểm 
                )

                marks[course_id][student["id"]] = mark

            return marks

    print("Course not found.")
    return marks


number_of_courses = input_number_of_courses()
courses = input_courses(number_of_courses)
marks = input_marks(students, courses)

print("Courses:", courses)
print("Marks:", marks)




       
    

