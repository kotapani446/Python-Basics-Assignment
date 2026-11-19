
students = {
    "Rahul": "A",
    "Priya": "B",
    "Arun": "C"
}

print("1. Add a new student")
print("2. Update an existing student's grade")
print("3. Display all student grades")

choice = int(input("Enter your choice: "))

if choice == 1:
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")

    if name in students:
        print("Student already exists!")
    else:
        students[name] = grade
        print("Student added successfully!")

elif choice == 2:
    name = input("Enter student name: ")

    if name in students:
        grade = input("Enter new grade: ")
        students[name] = grade
        print("Grade updated successfully!")
    else:
        print("Student not found!")

elif choice == 3:
    print("\nStudent Grades:")
    for name, grade in students.items():
        print(name, ":", grade)

else:
    print("Invalid choice!")