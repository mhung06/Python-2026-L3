"""
domains package
Exposes Student, Course, SchoolManager so other modules can do:
    from domains import Student, Course, SchoolManager
"""

from .student import Student
from .course import Course
from .school_manager import SchoolManager

__all__ = ["Student", "Course", "SchoolManager"]
