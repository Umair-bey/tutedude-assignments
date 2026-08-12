# Python Basics — Tutedude Assignment 2

This is Assignment 2 of the Python course by Tutedude.

This assignment covers basic Python programming concepts such as conditional statements, dictionaries, user input, loops, and file handling.

---

# 🐍 Python Programming Practical

## Topics Covered

- Taking input and checking grades using `if-elif-else`
- Creating and managing dictionaries
- Adding and updating student grades
- Displaying dictionary contents
- Writing content to a text file
- Reading content from a text file
- Using basic Python file-handling functions

---

# 📋 Assignment Tasks

## 1. Grade Checker

Take a score as input and print the grade according to the following conditions:

| Score | Grade |
| ----- | ----- |
| 90+ | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| Below 60 | F |

Take a score as input:

score = int(input("Enter your score: "))

Check the grade using if-elif-else:

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

Example output:

Enter your score: 85
Grade: B
2. Student Grades

Create a dictionary to store student names and their grades:

students = {}

Add a new student and grade:

name = input("Enter student name: ")
grade = input("Enter grade: ")
students[name] = grade

Update an existing student's grade:

name = input("Enter student name: ")

if name in students:
    grade = input("Enter new grade: ")
    students[name] = grade
    print("Grade updated successfully.")
else:
    print("Student not found.")

Print all student grades:

for name, grade in students.items():
    print(name, ":", grade)

Example output:

Student Grades:
Umair : A
Rahul : B
Aman : A
Concepts Used
Dictionary
Dictionary keys and values
if-elif-else
in operator
items()
for loop
User input
3. Write to a File

Create or open a text file in write mode:

file = open("student.txt", "w")

Write content into the file:

file.write("This is my Tutedude assignment.\n")
file.write("I am learning Python programming.\n")
file.write("This file was created using Python.")

Close the file:

file.close()

Complete code:

file = open("student.txt", "w")

file.write("This is my Tutedude assignment.\n")
file.write("I am learning Python programming.\n")
file.write("This file was created using Python.")

file.close()

print("Content written to the file successfully.")

Expected output:

Content written to the file successfully.

The program creates a file named:

student.txt

File content:

This is my Tutedude assignment.
I am learning Python programming.
This file was created using Python.
4. Read from a File

Open the file in read mode:

file = open("student.txt", "r")

Read the contents of the file:

content = file.read()

Display the file contents:

print("File Content:")
print(content)

Close the file:

file.close()

Complete code:

file = open("student.txt", "r")

content = file.read()

print("File Content:")
print(content)

file.close()

Expected output:

File Content:
This is my Tutedude assignment.
I am learning Python programming.
This file was created using Python.
📚 Python Concepts Summary
Task / Concept	Python Function / Operation
Take input	input()
Convert input to integer	int()
Decision making	if / elif / else
Store student grades	Dictionary
Add or update grade	students[name] = grade
Check student existence	in
Display dictionary contents	items()
Open or create file	open()
Write to file	write()
Read from file	read()
Close file	close()
Repeat operations	for / while
📁 Assignment Files

The repository contains the following files:

File	Description
Assignment 2.docx	Complete assignment document containing explanations, Python code, expected outputs, and screenshots
assignment1.py	Python program used for the assignment tasks
student.txt	Text file created and used during the file-writing and file-reading tasks
README.md	Documentation and overview of the assignment
🛠️ Technologies Used
Python
Visual Studio Code
Git
GitHub
🎯 Learning Outcome

After completing this assignment, I practiced:

Taking user input
Type conversion
Conditional statements
if, elif, and else
Dictionaries
Adding and updating dictionary values
Checking dictionary keys
Using loops
File creation
Writing to files
Reading from files
Closing files
📂 Repository Structure
Assignment-2/
│
├── Assignment 2.docx
├── assignment1.py
├── student.txt
└── README.md
✅ Assignment Status

Completed

Course: Python

Assignment: 2

Topic: Python Basics

Student: Umair Khan
