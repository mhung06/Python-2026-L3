"""
domains/course.py
Course data class.
"""


class Course:

    def __init__(self, course_id, name, credit):
        self.id = course_id
        self.name = name
        # credit is needed for the weighted GPA calculation
        self.credit = credit

    def __str__(self):
        return "ID: {} | Name: {} | Credit: {}".format(
            self.id, self.name, self.credit
        )
