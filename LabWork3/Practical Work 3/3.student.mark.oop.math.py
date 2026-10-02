# ==========================================
# PRACTICAL WORK 3
# STUDENT MARK MANAGEMENT (OOP + MATH + NUMPY + CURSES)
#
# Built on top of practical work 1/2 (lab1b.py), converted to OOP,
# then decorated with:
#   - math.floor()  -> round DOWN marks to 1 decimal digit on input
#   - numpy         -> compute weighted GPA (credit x mark) and sort by GPA
#   - curses        -> nicer terminal menu
# ==========================================

import math
import curses
import numpy as np


# ------------------------------------------
# CLASS: Student
# ------------------------------------------

class Student:

    def __init__(self, student_id, name, dob):
        # Basic info, same fields as the original dict version
        self.id = student_id
        self.name = name
        self.dob = dob

        # marks: dictionary {course_id: mark}, replaces the old
        # separate "marks" dict keyed by student_id in lab1b.py
        self.marks = {}

    def set_mark(self, course_id, score):
        # Round DOWN to 1 decimal digit, e.g. 8.97 -> 8.9
        rounded_down_score = math.floor(score * 10) / 10
        self.marks[course_id] = rounded_down_score

    def get_mark(self, course_id):
        # Return the mark for a course, or None if not graded yet
        return self.marks.get(course_id)

    def display(self):
        print(
            "ID:", self.id,
            "| Name:", self.name,
            "| DoB:", self.dob
        )


# ------------------------------------------
# CLASS: Course
# ------------------------------------------

class Course:

    def __init__(self, course_id, name, credit):
        self.id = course_id
        self.name = name
        # credit is needed to compute the weighted GPA later
        self.credit = credit

    def display(self):
        print(
            "ID:", self.id,
            "| Name:", self.name,
            "| Credit:", self.credit
        )


# ------------------------------------------
# CLASS: SchoolManager
# This class replaces all the loose functions from lab1b.py,
# keeping the exact same logic, just organized as methods.
# ------------------------------------------

class SchoolManager:

    def __init__(self):
        self.students = []
        self.courses = []

    # ---------- 1. INPUT NUMBER OF STUDENTS ----------
    def input_number_of_students(self):
        n = int(input("Enter number of students: "))
        return n

    # ---------- 2. INPUT STUDENT INFORMATION ----------
    def input_students(self, n):
        for i in range(n):
            print("\nStudent", i + 1)

            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter date of birth: ")

            student = Student(student_id, name, dob)
            self.students.append(student)

    # ---------- 3. INPUT NUMBER OF COURSES ----------
    def input_number_of_courses(self):
        n = int(input("\nEnter number of courses: "))
        return n

    # ---------- 4. INPUT COURSE INFORMATION ----------
    def input_courses(self, n):
        for i in range(n):
            print("\nCourse", i + 1)

            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            # New field required for GPA calculation (PW3)
            credit = float(input("Enter course credit: "))

            course = Course(course_id, course_name, credit)
            self.courses.append(course)

    # ---------- 5. LIST STUDENTS ----------
    def list_students(self):
        print("\n================================")
        print("          STUDENT LIST")
        print("================================")

        for student in self.students:
            student.display()

    # ---------- 6. LIST COURSES ----------
    def list_courses(self):
        print("\n================================")
        print("           COURSE LIST")
        print("================================")

        for course in self.courses:
            course.display()

    # ---------- helper: find course by id ----------
    def find_course(self, course_id):
        for course in self.courses:
            if course.id == course_id:
                return course
        return None

    # ---------- 7. INPUT MARKS ----------
    def input_marks(self):
        print("\n================================")
        print("           COURSE LIST")
        print("================================")

        for course in self.courses:
            print(course.id, "-", course.name)

        course_id = input("\nEnter course ID: ")
        selected_course = self.find_course(course_id)

        if selected_course is None:
            print("Course not found!")
            return

        print("\nEnter marks for course:", selected_course.name)

        for student in self.students:
            score = float(
                input("Enter mark for " + student.name + ": ")
            )
            # math.floor rounding happens inside set_mark()
            student.set_mark(course_id, score)

        print("Marks saved successfully! (rounded down to 1 decimal)")

    # ---------- 8. SHOW STUDENT MARKS FOR A COURSE ----------
    def show_student_marks(self):
        print("\n================================")
        print("           COURSE LIST")
        print("================================")

        for course in self.courses:
            print(course.id, "-", course.name)

        course_id = input("\nEnter course ID: ")
        selected_course = self.find_course(course_id)

        if selected_course is None:
            print("Course not found!")
            return

        print("\n================================")
        print("MARKS FOR:", selected_course.name)
        print("================================")

        for student in self.students:
            score = student.get_mark(course_id)

            if score is None:
                print(student.name, ": No mark")
            else:
                print(student.name, ":", score)

    # ---------- 9. CALCULATE GPA (numpy) ----------
    def calculate_gpa(self, student):
        # Weighted sum of credits and marks, using numpy arrays
        marks_list = []
        credits_list = []

        for course in self.courses:
            score = student.get_mark(course.id)
            if score is not None:
                marks_list.append(score)
                credits_list.append(course.credit)

        # No marks yet -> GPA is 0
        if len(credits_list) == 0:
            return 0.0

        marks_array = np.array(marks_list, dtype=float)
        credits_array = np.array(credits_list, dtype=float)

        # weighted sum = sum(mark_i * credit_i)
        weighted_sum = np.sum(marks_array * credits_array)
        total_credits = np.sum(credits_array)

        gpa = weighted_sum / total_credits
        return float(gpa)

    # ---------- 10. LIST STUDENTS SORTED BY GPA DESCENDING (numpy) ----------
    def list_students_by_gpa(self):
        if len(self.students) == 0:
            print("No students available!")
            return

        # Build a numpy array of GPA values, one per student
        gpa_array = np.array(
            [self.calculate_gpa(s) for s in self.students]
        )

        # argsort gives ascending order indices; [::-1] reverses -> descending
        order = np.argsort(gpa_array)[::-1]

        print("\n================================")
        print("     STUDENTS RANKED BY GPA")
        print("================================")

        for idx in order:
            student = self.students[idx]
            print(
                student.name,
                "| GPA:", round(gpa_array[idx], 2)
            )


# ------------------------------------------
# CURSES MENU (decoration layer)
# ------------------------------------------

MENU_ITEMS = [
    "Input students",
    "Input courses",
    "List students",
    "List courses",
    "Input marks",
    "Show student marks",
    "Show students ranked by GPA",
    "Exit",
]


def draw_menu(stdscr, selected_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    title = "STUDENT MARK MANAGEMENT (PW3)"
    stdscr.addstr(1, max(0, (w - len(title)) // 2), title, curses.A_BOLD)

    for idx, item in enumerate(MENU_ITEMS):
        y = 3 + idx
        x = 4
        text = str(idx + 1) + ". " + item

        if idx == selected_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, text)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, text)

    footer = "Use UP/DOWN + ENTER, or press number key. 'q' to quit."
    stdscr.addstr(h - 2, 2, footer, curses.A_DIM)
    stdscr.refresh()


def run_action(stdscr, manager, choice):
    # Leave curses mode temporarily so normal input()/print() work
    curses.endwin()
    print("\n" + "=" * 50)

    try:
        if choice == 0:
            n = manager.input_number_of_students()
            manager.input_students(n)

        elif choice == 1:
            n = manager.input_number_of_courses()
            manager.input_courses(n)

        elif choice == 2:
            if len(manager.students) == 0:
                print("No students available!")
            else:
                manager.list_students()

        elif choice == 3:
            if len(manager.courses) == 0:
                print("No courses available!")
            else:
                manager.list_courses()

        elif choice == 4:
            if len(manager.students) == 0:
                print("Please input students first!")
            elif len(manager.courses) == 0:
                print("Please input courses first!")
            else:
                manager.input_marks()

        elif choice == 5:
            if len(manager.students) == 0:
                print("Please input students first!")
            elif len(manager.courses) == 0:
                print("Please input courses first!")
            else:
                manager.show_student_marks()

        elif choice == 6:
            manager.list_students_by_gpa()

    except Exception as e:
        print("Error:", e)

    input("\nPress ENTER to go back to the menu...")


def main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)

    manager = SchoolManager()
    selected = 0

    while True:
        draw_menu(stdscr, selected)
        key = stdscr.getch()

        if key == curses.KEY_UP and selected > 0:
            selected -= 1

        elif key == curses.KEY_DOWN and selected < len(MENU_ITEMS) - 1:
            selected += 1

        elif key in (10, 13, curses.KEY_ENTER):
            if selected == len(MENU_ITEMS) - 1:
                break
            run_action(stdscr, manager, selected)

        elif ord('1') <= key <= ord('8'):
            choice = key - ord('1')
            if choice == len(MENU_ITEMS) - 1:
                break
            run_action(stdscr, manager, choice)

        elif key in (ord('q'), ord('Q')):
            break


# ------------------------------------------
# START PROGRAM
# ------------------------------------------

if __name__ == "__main__":
    curses.wrapper(main)
