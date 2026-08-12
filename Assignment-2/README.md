# Python Basics Assignment 2

This repository contains my **Tutedude Python Basics Assignment 2**.

The assignment focuses on basic Python programming concepts such as conditional statements, dictionaries, user input, loops, and file handling.

---

# 📚 Assignment Overview

This assignment contains four main Python tasks:

1. Grade Checker
2. Student Grades
3. Write to a File
4. Read from a File

The repository also contains the complete assignment document and the text file used for file-handling tasks.

---

# 📁 Repository Files

| File | Description |
|---|---|
| `Assignment 2.docx` | Complete assignment document containing explanations, Python code, expected outputs, and screenshots |
| `assignment1.py` | Python program used for the assignment tasks |
| `student.txt` | Text file created and used during the file-writing and file-reading tasks |
| `README.md` | Documentation and overview of this assignment |

---

# 📝 Assignment 1 – Grade Checker

The Grade Checker program takes a score from the user and assigns a grade based on the following conditions:

| Score | Grade |
|---|---|
| 90 and above | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| Below 60 | F |

### Concepts Used

- `input()`
- `int()`
- `if`
- `elif`
- `else`

Example:

```text
Enter your score: 85
Grade: B
```text

👨‍🎓 Assignment 2 – Student Grades

The Student Grades program uses a Python dictionary to store student names and their grades.

The program allows the user to:

Add a new student
Add a student's grade
Update an existing student's grade
Check whether a student exists
Display all student grades
Concepts Used
Dictionary
Dictionary keys and values
if-elif-else
in operator
items()
for loop
User input

Example:

Student Grades:
Umair : A
Rahul : B
Aman : A
📄 Assignment 3 – Write to a File

This task demonstrates basic Python file handling.

The program creates a text file named:

student.txt

It then writes the following content into the file:

This is my Tutedude assignment.
I am learning Python programming.
This file was created using Python.
Concepts Used
open()
Write mode "w"
write()
close()

The program displays:

Content written to the file successfully.
📖 Assignment 4 – Read from a File

This task demonstrates how to read content from an existing text file.

The program opens:

student.txt

in read mode and reads its contents using the read() function.

Concepts Used
open()
Read mode "r"
read()
print()
close()

Example output:

File Content:
This is my Tutedude assignment.
I am learning Python programming.
This file was created using Python.
📄 Assignment Document
Assignment 2.docx

This is the complete Microsoft Word document submitted for the assignment.

It contains:

Assignment title
Student name
Course name
Task explanations
Python code
Expected outputs
Screenshots
Summary of concepts
Submission guidelines

The Word document provides the detailed written version of the work included in this repository.

🐍 Python Program
assignment1.py

This file contains the Python code used to perform the assignment tasks.

The programs demonstrate:

Taking input from the user
Conditional statements
Grade calculation
Dictionary operations
Adding and updating student grades
Loops
File creation
Writing to files
Reading from files

The file was developed and executed using Visual Studio Code.

📄 Text File
student.txt

This file is created during the file-handling portion of the assignment.

It contains:

This is my Tutedude assignment.
I am learning Python programming.
This file was created using Python.

The file is used in two tasks:

Write Operation

Python opens the file using:

open("student.txt", "w")

and writes content into it.

Read Operation

Python then opens the same file using:

open("student.txt", "r")

and reads its contents using:

file.read()
🛠️ Technologies Used
Python
Visual Studio Code
Git
GitHub
📚 Concepts Practiced

Through this assignment, I practiced the following Python concepts:

Variables
User input
Type conversion
Conditional statements
if
elif
else
Dictionaries
Dictionary keys and values
Dictionary operations
in operator
for loop
items()
File handling
File creation
Writing to files
Reading from files
Closing files
📂 Repository Structure
Assignment-2/
│
├── Assignment 2.docx
│
├── assignment1.py
│
├── student.txt
│
└── README.md
🎯 Learning Outcome

After completing this assignment, I gained practical experience with basic Python programming and learned how to:

Make decisions using conditional statements
Store and manage data using dictionaries
Take input from users
Update dictionary values
Work with loops
Create and write to text files
Read data from text files
Execute Python programs using Visual Studio Code
👨‍💻 Author

Umair Khan

Course: Python

Assignment: Tutedude Python Basics Assignment 2

✅ Assignment Status

Completed

The repository contains the assignment document, Python program, text file, and complete documentation.
