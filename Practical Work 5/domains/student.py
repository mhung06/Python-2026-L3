"""
domains/student.py
Student data class.
"""

import math


class Student:

    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob

        # marks: dictionary {course_id: mark}
        self.marks = {}

    def set_mark(self, course_id, score):
        # Round DOWN to 1 decimal digit, e.g. 8.97 -> 8.9
        rounded_down_score = math.floor(score * 10) / 10
        self.marks[course_id] = rounded_down_score

    def get_mark(self, course_id):
        # Return the mark for a course, or None if not graded yet
        return self.marks.get(course_id)

    def __str__(self):
        return "ID: {} | Name: {} | DoB: {}".format(
            self.id, self.name, self.dob
        )
