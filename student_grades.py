# Task 2: Student Grades using a dictionary
students = {"Rahul": "A", "Priya": "B"}

while True:
    print("\n----- Student Grades Menu -----")
    print("1. Add a new student")
    print("2. Update a student's grade")
    print("3. Print all student grades")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        if name in students:
            print(name, "already exists. Use option 2 to update.")
        else:
            grade = input("Enter grade: ")
            students[name] = grade
            print(name, "added successfully with grade", grade)

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print(name + "'s grade updated to", grade)
        else:
            print(name, "not found!")

    elif choice == "3":
        if students:
            print("\nAll Student Grades:")
            for name, grade in students.items():
                print(name, ":", grade)
        else:
            print("No students yet.")

    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, 3 or 4.")
