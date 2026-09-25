# ==========================================
# PRACTICAL WORK 1
# STUDENT MARK MANAGEMENT
# ==========================================


# ------------------------------------------
# 1. INPUT NUMBER OF STUDENTS
# ------------------------------------------

def input_number_of_students():
    # Ask the user to enter the number of students
    n = int(input("Enter number of students: "))

    # Return the number of students
    return n


# ------------------------------------------
# 2. INPUT STUDENT INFORMATION
# ------------------------------------------

def input_students(n):
    # Create an empty list to store students
    students = []

    # Repeat n times
    for i in range(n):

        print("\nStudent", i + 1)

        # Input student ID
        student_id = input("Enter student ID: ")

        # Input student name
        name = input("Enter student name: ")

        # Input date of birth
        dob = input("Enter date of birth: ")

        # Create a dictionary containing student information
        student = {
            "id": student_id,
            "name": name,
            "dob": dob
        }

        # Add the student to the students list
        students.append(student)

    # Return the list of students
    return students


# ------------------------------------------
# 3. INPUT NUMBER OF COURSES
# ------------------------------------------

def input_number_of_courses():
    # Ask the user to enter the number of courses
    n = int(input("\nEnter number of courses: "))

    # Return the number of courses
    return n


# ------------------------------------------
# 4. INPUT COURSE INFORMATION
# ------------------------------------------

def input_courses(n):
    # Create an empty list to store courses
    courses = []

    # Repeat n times
    for i in range(n):

        print("\nCourse", i + 1)

        # Input course ID
        course_id = input("Enter course ID: ")

        # Input course name
        course_name = input("Enter course name: ")

        # Create a dictionary containing course information
        course = {
            "id": course_id,
            "name": course_name
        }

        # Add the course to the courses list
        courses.append(course)

    # Return the list of courses
    return courses


# ------------------------------------------
# 5. LIST STUDENTS
# ------------------------------------------

def list_students(students):

    print("\n================================")
    print("          STUDENT LIST")
    print("================================")

    # Go through every student in the list
    for student in students:

        # Display student information
        print(
            "ID:", student["id"],
            "| Name:", student["name"],
            "| DoB:", student["dob"]
        )


# ------------------------------------------
# 6. LIST COURSES
# ------------------------------------------

def list_courses(courses):

    print("\n================================")
    print("           COURSE LIST")
    print("================================")

    # Go through every course
    for course in courses:

        # Display course information
        print(
            "ID:", course["id"],
            "| Name:", course["name"]
        )


# ------------------------------------------
# 7. INPUT MARKS
# ------------------------------------------

def input_marks(students, courses, marks):

    print("\n================================")
    print("           COURSE LIST")
    print("================================")

    # Display all courses
    for course in courses:
        print(
            course["id"],
            "-",
            course["name"]
        )

    # Ask the user to select a course
    course_id = input("\nEnter course ID: ")

    # Variable used to store the selected course
    selected_course = None

    # Search for the course
    for course in courses:

        if course["id"] == course_id:
            selected_course = course
            break

    # If the course does not exist
    if selected_course is None:

        print("Course not found!")

        return

    print(
        "\nEnter marks for course:",
        selected_course["name"]
    )

    # Enter marks for every student
    for student in students:

        # Ask for student's mark
        score = float(
            input(
                "Enter mark for "
                + student["name"]
                + ": "
            )
        )

        # If this student does not have marks yet
        if student["id"] not in marks:

            # Create an empty dictionary for this student
            marks[student["id"]] = {}

        # Save the mark
        marks[student["id"]][course_id] = score

    print("Marks saved successfully!")


# ------------------------------------------
# 8. SHOW STUDENT MARKS FOR A COURSE
# ------------------------------------------

def show_student_marks(students, courses, marks):

    print("\n================================")
    print("           COURSE LIST")
    print("================================")

    # Display all courses
    for course in courses:

        print(
            course["id"],
            "-",
            course["name"]
        )

    # Ask the user to select a course
    course_id = input("\nEnter course ID: ")

    # Find the selected course
    selected_course = None

    for course in courses:

        if course["id"] == course_id:
            selected_course = course
            break

    # If course does not exist
    if selected_course is None:

        print("Course not found!")

        return

    print("\n================================")
    print("MARKS FOR:", selected_course["name"])
    print("================================")

    # Go through every student
    for student in students:

        student_id = student["id"]

        # Check if the student has marks
        if student_id in marks:

            # Check if the student has a mark for this course
            if course_id in marks[student_id]:

                score = marks[student_id][course_id]

                print(
                    student["name"],
                    ":",
                    score
                )

            else:

                print(
                    student["name"],
                    ": No mark"
                )

        else:

            print(
                student["name"],
                ": No mark"
            )


# ------------------------------------------
# 9. MAIN MENU
# ------------------------------------------

def main():

    # Create empty student list
    students = []

    # Create empty course list
    courses = []

    # Create empty dictionary for marks
    marks = {}

    # Main program loop
    while True:

        print("\n")
        print("======================================")
        print("       STUDENT MARK MANAGEMENT")
        print("======================================")

        print("1. Input students")
        print("2. Input courses")
        print("3. List students")
        print("4. List courses")
        print("5. Input marks")
        print("6. Show student marks")
        print("0. Exit")

        # Ask user to choose an option
        choice = input("\nEnter your choice: ")

        # ----------------------------------
        # OPTION 1
        # ----------------------------------

        if choice == "1":

            n = input_number_of_students()

            students = input_students(n)

        # ----------------------------------
        # OPTION 2
        # ----------------------------------

        elif choice == "2":

            n = input_number_of_courses()

            courses = input_courses(n)

        # ----------------------------------
        # OPTION 3
        # ----------------------------------

        elif choice == "3":

            if len(students) == 0:

                print("No students available!")

            else:

                list_students(students)

        # ----------------------------------
        # OPTION 4
        # ----------------------------------

        elif choice == "4":

            if len(courses) == 0:

                print("No courses available!")

            else:

                list_courses(courses)

        # ----------------------------------
        # OPTION 5
        # ----------------------------------

        elif choice == "5":

            if len(students) == 0:

                print("Please input students first!")

            elif len(courses) == 0:

                print("Please input courses first!")

            else:

                input_marks(
                    students,
                    courses,
                    marks
                )

        # ----------------------------------
        # OPTION 6
        # ----------------------------------

        elif choice == "6":

            if len(students) == 0:

                print("Please input students first!")

            elif len(courses) == 0:

                print("Please input courses first!")

            else:

                show_student_marks(
                    students,
                    courses,
                    marks
                )

        # ----------------------------------
        # OPTION 0
        # ----------------------------------

        elif choice == "0":

            print("Program ended.")

            break

        # ----------------------------------
        # INVALID CHOICE
        # ----------------------------------

        else:

            print("Invalid choice! Please try again.")


# ------------------------------------------
# START PROGRAM
# ------------------------------------------

main()