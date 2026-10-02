"""
domains/school_manager.py
Holds the list of students/courses, and the business-logic methods
(finding a course, computing GPA with numpy, ranking students by GPA).
Pure logic only - no input() and no curses/print here, so this class
can be reused/tested independently from the UI.
"""

import numpy as np


class SchoolManager:

    def __init__(self):
        self.students = []
        self.courses = []

    def find_course(self, course_id):
        for course in self.courses:
            if course.id == course_id:
                return course
        return None

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

        weighted_sum = np.sum(marks_array * credits_array)
        total_credits = np.sum(credits_array)

        gpa = weighted_sum / total_credits
        return float(gpa)

    def gpa_ranking(self):
        """Return a list of (student, gpa) sorted by gpa descending."""
        if len(self.students) == 0:
            return []

        gpa_array = np.array(
            [self.calculate_gpa(s) for s in self.students]
        )

        # argsort -> ascending indices; [::-1] reverses -> descending
        order = np.argsort(gpa_array)[::-1]

        ranking = []
        for idx in order:
            ranking.append((self.students[idx], float(gpa_array[idx])))
        return ranking
