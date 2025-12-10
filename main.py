import json
import os

DATA_FILE = "students.json"


def load_students():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_students(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_student():
    data = load_students()
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    student = {"roll_no": roll, "name": name, "marks": marks}
    data.append(student)
    save_students(data)
    print("Student added successfully!")


def update_student():
    data = load_students()
    roll = input("Enter Roll No to update: ")

    for student in data:
        if student["roll_no"] == roll:
            print("Found:", student)
            student["name"] = input("Enter new name: ")
            student["marks"] = input("Enter new marks: ")
            save_students(data)
            print("Updated successfully!")
            return

    print("Student not found.")


def delete_student():
    data = load_students()
    roll = input("Enter Roll No to delete: ")

    new_data = [s for s in data if s["roll_no"] != roll]

    if len(new_data) == len(data):
        print("Student not found.")
    else:
        save_students(new_data)
        print("Deleted successfully!")


def display_students():
    data = load_students()
    if not data:
        print("No students found.")
        return

    print("\n----- Student List -----")
    for s in data:
        print(f"{s['roll_no']} | {s['name']} | {s['marks']}")
    print("-------------------------")


def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Display Students")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
