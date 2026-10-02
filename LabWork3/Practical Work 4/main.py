"""
main.py
Coordination script for Practical Work 4.
Brings together:
  - domains  (Student, Course, SchoolManager)
  - input.py (all data-entry functions)
  - output.py (all curses-based display functions)
"""

import curses

from domains import SchoolManager
import input as input_module
import output as output_module


def run_action(stdscr, manager, choice):
    # Leave curses mode temporarily so plain input()/print() work
    curses.endwin()
    print("\n" + "=" * 50)

    try:
        if choice == 0:
            n = input_module.input_number_of_students()
            input_module.input_students(manager, n)

        elif choice == 1:
            n = input_module.input_number_of_courses()
            input_module.input_courses(manager, n)

        elif choice == 2:
            pass  # handled after re-entering curses, see below

        elif choice == 3:
            pass  # handled after re-entering curses, see below

        elif choice == 4:
            if len(manager.students) == 0:
                print("Please input students first!")
            elif len(manager.courses) == 0:
                print("Please input courses first!")
            else:
                input_module.input_marks(manager)

        elif choice == 5:
            pass  # course id collected here, marks shown after re-entering curses

        elif choice == 6:
            pass  # shown after re-entering curses

    except Exception as e:
        print("Error:", e)

    if choice not in (2, 3, 5, 6):
        input("\nPress ENTER to go back to the menu...")


def main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)

    manager = SchoolManager()
    selected = 0

    while True:
        output_module.draw_menu(stdscr, selected)
        key = stdscr.getch()

        if key == curses.KEY_UP and selected > 0:
            selected -= 1

        elif key == curses.KEY_DOWN and selected < len(output_module.MENU_ITEMS) - 1:
            selected += 1

        elif key in (10, 13, curses.KEY_ENTER) or (ord('1') <= key <= ord('8')):
            if key in (10, 13, curses.KEY_ENTER):
                choice = selected
            else:
                choice = key - ord('1')

            if choice == len(output_module.MENU_ITEMS) - 1:  # Exit
                break

            if choice in (2, 3, 6):
                # Pure curses display, no text input needed
                if choice == 2:
                    output_module.list_students(stdscr, manager)
                elif choice == 3:
                    output_module.list_courses(stdscr, manager)
                elif choice == 6:
                    output_module.show_gpa_ranking(stdscr, manager)

            elif choice == 5:
                if len(manager.students) == 0 or len(manager.courses) == 0:
                    curses.endwin()
                    print("Please input students and courses first!")
                    input("\nPress ENTER to go back to the menu...")
                else:
                    curses.endwin()
                    course_id = input_module.input_course_id_for_marks(manager)
                    stdscr.refresh()
                    output_module.show_student_marks(stdscr, manager, course_id)

            else:
                run_action(stdscr, manager, choice)

        elif key in (ord('q'), ord('Q')):
            break


if __name__ == "__main__":
    curses.wrapper(main)
