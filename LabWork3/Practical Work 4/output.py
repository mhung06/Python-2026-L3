"""
output.py
Module for curses output. Every "listing" function here draws its
result inside the curses window (instead of plain print).
"""

import curses


def display_lines(stdscr, lines, title=None):
    """Generic helper: show a title + a list of text lines in the
    curses window, then wait for a keypress before returning."""
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    y = 1

    if title:
        stdscr.addstr(y, max(0, (w - len(title)) // 2), title, curses.A_BOLD)
        y += 2

    if len(lines) == 0:
        lines = ["(nothing to show)"]

    for line in lines:
        if y < h - 2:
            stdscr.addstr(y, 2, line[: max(0, w - 4)])
            y += 1

    stdscr.addstr(h - 1, 2, "Press any key to continue...", curses.A_DIM)
    stdscr.refresh()
    stdscr.getch()


def list_students(stdscr, manager):
    lines = [str(s) for s in manager.students]
    display_lines(stdscr, lines, "STUDENT LIST")


def list_courses(stdscr, manager):
    lines = [str(c) for c in manager.courses]
    display_lines(stdscr, lines, "COURSE LIST")


def show_student_marks(stdscr, manager, course_id):
    course = manager.find_course(course_id)

    if course is None:
        display_lines(stdscr, ["Course not found!"])
        return

    lines = []
    for student in manager.students:
        mark = student.get_mark(course_id)
        if mark is None:
            lines.append(student.name + ": No mark")
        else:
            lines.append(student.name + ": " + str(mark))

    display_lines(stdscr, lines, "MARKS FOR: " + course.name)


def show_gpa_ranking(stdscr, manager):
    ranking = manager.gpa_ranking()
    lines = []
    for student, gpa in ranking:
        lines.append(student.name + " | GPA: " + str(round(gpa, 2)))

    display_lines(stdscr, lines, "STUDENTS RANKED BY GPA")


# ---------------- Main menu drawing ----------------

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

    title = "STUDENT MARK MANAGEMENT (PW4)"
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
