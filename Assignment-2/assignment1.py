# code 
score = int(input("Enter your score: "))

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
# code 2. Student Grades
students = {}

while True:
    print("\n1. Add Student")
    print("2. Update Grade")
    print("3. Print All Grades")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print("Student added successfully.")

    elif choice == "2":
        name = input("Enter student name: ")

        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print("Grade updated successfully.")
        else:
            print("Student not found.")

    elif choice == "3":
        print("\nStudent Grades:")

        if students:
            for name, grade in students.items():
                print(name, ":", grade)
        else:
            print("No students available.")

    elif choice == "4":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
# code 3. Write to a File
file = open("student.txt", "w")

file.write("This is my Tutedude assignment.\n")
file.write("I am learning Python programming.\n")
file.write("This file was created using Python.")

file.close()

print("Content written to the file successfully.")
# code for 4. Read from a File
file = open("student.txt", "r")

content = file.read()

print("File Content:")
print(content)

file.close()