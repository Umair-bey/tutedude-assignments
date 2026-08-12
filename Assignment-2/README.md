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

The Grade Checker program takes a score as input and assigns a grade based on the given score range.

### 📝 Take a Score as Input

```python
score = int(input("Enter your score: "))
````

### 🔀 Check the Grade Using `if-elif-else`

```python
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
```

### 💻 Example Output

```text
Enter your score: 85
Grade: B
```

---

## 2. Student Grades

The Student Grades program uses a Python dictionary to store student names and their grades.

### 📦 Create a Dictionary

```python
students = {}
```

### ➕ Add a New Student and Grade

```python
name = input("Enter student name: ")
grade = input("Enter grade: ")
students[name] = grade
```

### 🔄 Update an Existing Student's Grade

```python
name = input("Enter student name: ")

if name in students:
    grade = input("Enter new grade: ")
    students[name] = grade
    print("Grade updated successfully.")
else:
    print("Student not found.")
```

### 📋 Print All Student Grades

```python
for name, grade in students.items():
    print(name, ":", grade)
```

### 💻 Example Output

```text
Student Grades:
Umair : A
Rahul : B
Aman : A
```

### 📚 Concepts Used

* Dictionary
* Dictionary keys and values
* `if-elif-else`
* `in` operator
* `items()`
* `for` loop
* User input

---

## 3. Write to a File

This task demonstrates basic Python file handling by creating a text file and writing content into it.

### 📂 Create or Open a Text File in Write Mode

```python
file = open("student.txt", "w")
```

### ✍️ Write Content into the File

```python
file.write("This is my Tutedude assignment.\n")
file.write("I am learning Python programming.\n")
file.write("This file was created using Python.")
```

### 🔒 Close the File

```python
file.close()
```

### 🧩 Complete Code

```python
file = open("student.txt", "w")

file.write("This is my Tutedude assignment.\n")
file.write("I am learning Python programming.\n")
file.write("This file was created using Python.")

file.close()

print("Content written to the file successfully.")
```

### 💻 Expected Output

```text
Content written to the file successfully.
```

### 📁 File Created

```text
student.txt
```

### 📖 File Content

```text
This is my Tutedude assignment.
I am learning Python programming.
This file was created using Python.
```

---

## 4. Read from a File

This task demonstrates how to open an existing text file, read its contents, and display them.

### 📂 Open the File in Read Mode

```python
file = open("student.txt", "r")
```

### 📖 Read the Contents of the File

```python
content = file.read()
```

### 🖥️ Display the File Contents

```python
print("File Content:")
print(content)
```

### 🔒 Close the File

```python
file.close()
```

### 🧩 Complete Code

```python
file = open("student.txt", "r")

content = file.read()

print("File Content:")
print(content)

file.close()
```

### 💻 Expected Output

```text
File Content:
This is my Tutedude assignment.
I am learning Python programming.
This file was created using Python.
```

---

# 📚 Python Concepts Summary

| Task / Concept              | Python Function / Operation |
| --------------------------- | --------------------------- |
| Take input                  | `input()`                   |
| Convert input to integer    | `int()`                     |
| Decision making             | `if / elif / else`          |
| Store student grades        | Dictionary                  |
| Add or update grade         | `students[name] = grade`    |
| Check student existence     | `in`                        |
| Display dictionary contents | `items()`                   |
| Open or create file         | `open()`                    |
| Write to file               | `write()`                   |
| Read from file              | `read()`                    |
| Close file                  | `close()`                   |
| Repeat operations           | `for / while`               |

---

# 📁 Assignment Files

The repository contains the following files:

| File                | Description                                                                                          |
| ------------------- | ---------------------------------------------------------------------------------------------------- |
| `Assignment 2.docx` | Complete assignment document containing explanations, Python code, expected outputs, and screenshots |
| `assignment1.py`    | Python program used for the assignment tasks                                                         |
| `student.txt`       | Text file created and used during the file-writing and file-reading tasks                            |
| `README.md`         | Documentation and overview of the assignment                                                         |

---

# 🛠️ Technologies Used

* 🐍 Python
* 💻 Visual Studio Code
* 🔧 Git
* 🐙 GitHub

---

# 🎯 Learning Outcome

After completing this assignment, I practiced:

* Taking user input
* Type conversion
* Conditional statements
* `if`, `elif`, and `else`
* Dictionaries
* Adding and updating dictionary values
* Checking dictionary keys
* Using loops
* File creation
* Writing to files
* Reading from files
* Closing files

---

# 📂 Repository Structure

```text
Assignment-2/
│
├── Assignment 2.docx
├── assignment1.py
├── student.txt
└── README.md
```

---

# ✅ Assignment Status

**Completed**

**Course:** Python

**Assignment:** 2

**Topic:** Python Basics

**Student:** Umair Khan
