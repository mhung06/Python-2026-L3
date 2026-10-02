"""
storage.py
Module for Practical Work 5: persistent info.

- write_students / write_courses / write_marks: dump current data
  to plain text files (students.txt, courses.txt, marks.txt).
- compress_data: let the user pick a compression method, then zip
  the three .txt files into a single students.dat file.
- startup_load: on program start, if students.dat exists, decompress
  it and load the data back into the SchoolManager.
"""

import os
import zipfile

from domains import Student, Course

STUDENTS_TXT = "students.txt"
COURSES_TXT = "courses.txt"
MARKS_TXT = "marks.txt"
DATA_FILE = "students.dat"


# ---------------- WRITE (txt files) ----------------

def write_students(manager):
    with open(STUDENTS_TXT, "w", encoding="utf-8") as f:
        for s in manager.students:
            f.write(s.id + "," + s.name + "," + s.dob + "\n")


def write_courses(manager):
    with open(COURSES_TXT, "w", encoding="utf-8") as f:
        for c in manager.courses:
            f.write(c.id + "," + c.name + "," + str(c.credit) + "\n")


def write_marks(manager):
    with open(MARKS_TXT, "w", encoding="utf-8") as f:
        for s in manager.students:
            for course_id, mark in s.marks.items():
                f.write(s.id + "," + course_id + "," + str(mark) + "\n")


# ---------------- LOAD (txt files) ----------------

def load_students(manager):
    if not os.path.exists(STUDENTS_TXT):
        return

    with open(STUDENTS_TXT, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            student_id, name, dob = parts[0], parts[1], parts[2]
            manager.students.append(Student(student_id, name, dob))


def load_courses(manager):
    if not os.path.exists(COURSES_TXT):
        return

    with open(COURSES_TXT, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            course_id, name, credit = parts[0], parts[1], float(parts[2])
            manager.courses.append(Course(course_id, name, credit))


def load_marks(manager):
    if not os.path.exists(MARKS_TXT):
        return

    with open(MARKS_TXT, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            student_id, course_id, mark = parts[0], parts[1], float(parts[2])

            for s in manager.students:
                if s.id == student_id:
                    s.marks[course_id] = mark
                    break


def load_all(manager):
    load_students(manager)
    load_courses(manager)
    load_marks(manager)


# ---------------- COMPRESSION ----------------

COMPRESSION_METHODS = {
    "1": ("Stored (no compression)", zipfile.ZIP_STORED),
    "2": ("Deflate (standard zip)", zipfile.ZIP_DEFLATED),
    "3": ("Bzip2", zipfile.ZIP_BZIP2),
    "4": ("LZMA", zipfile.ZIP_LZMA),
}


def choose_compression_method():
    print("\nSelect a compression method:")
    for key in COMPRESSION_METHODS:
        print(" ", key, "-", COMPRESSION_METHODS[key][0])

    choice = input("Enter choice (1-4), default = 2: ").strip()

    if choice not in COMPRESSION_METHODS:
        choice = "2"

    return COMPRESSION_METHODS[choice][1]


def compress_data():
    """Compress students.txt, courses.txt, marks.txt into students.dat."""
    method = choose_compression_method()

    files_to_compress = [STUDENTS_TXT, COURSES_TXT, MARKS_TXT]

    with zipfile.ZipFile(DATA_FILE, "w") as zf:
        for filename in files_to_compress:
            if os.path.exists(filename):
                zf.write(filename, arcname=filename, compress_type=method)

    print("All data compressed into", DATA_FILE)


def decompress_data():
    """Decompress students.dat back into the three .txt files."""
    with zipfile.ZipFile(DATA_FILE, "r") as zf:
        zf.extractall()

    print("Data decompressed from", DATA_FILE)


def startup_load(manager):
    """Called once when the program starts."""
    if os.path.exists(DATA_FILE):
        print(DATA_FILE, "found. Decompressing and loading data...")
        decompress_data()
        load_all(manager)
        print(
            "Loaded", len(manager.students), "student(s) and",
            len(manager.courses), "course(s)."
        )
    else:
        print("No saved data found (" + DATA_FILE + " does not exist). Starting fresh.")
