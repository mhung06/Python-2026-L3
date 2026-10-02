"""
input.py
Module for input. Every function here uses plain input()/print(),
no curses - curses is only handled in output.py / main.py.
"""

from domains import Student, Course


def input_number_of_students():
    n = int(input("Enter number of students: "))
    return n


def input_students(manager, n):
    for i in range(n):
        print("\nStudent", i + 1)

        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter date of birth: ")

        student = Student(student_id, name, dob)
        manager.students.append(student)


def input_number_of_courses():
    n = int(input("\nEnter number of courses: "))
    return n


def input_courses(manager, n):
    for i in range(n):
        print("\nCourse", i + 1)

        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        credit = float(input("Enter course credit: "))

        course = Course(course_id, course_name, credit)
        manager.courses.append(course)


def input_marks(manager):
    print("\n================================")
    print("           COURSE LIST")
    print("================================")

    for course in manager.courses:
        print(course.id, "-", course.name)

    course_id = input("\nEnter course ID: ")
    selected_course = manager.find_course(course_id)

    if selected_course is None:
        print("Course not found!")
        return

    print("\nEnter marks for course:", selected_course.name)

    for student in manager.students:
        score = float(
            input("Enter mark for " + student.name + ": ")
        )
        # math.floor rounding happens inside Student.set_mark()
        student.set_mark(course_id, score)

    print("Marks saved successfully! (rounded down to 1 decimal)")


def input_course_id_for_marks(manager):
    """Ask which course to display marks for; used by output.py."""
    print("\n================================")
    print("           COURSE LIST")
    print("================================")

    for course in manager.courses:
        print(course.id, "-", course.name)

    course_id = input("\nEnter course ID: ")
    return course_id
