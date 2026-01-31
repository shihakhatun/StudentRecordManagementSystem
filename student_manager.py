import json
import os
from student import Student

FILE_PATH = "./Students/student_data.json"


class StudentManager:

    def __init__(self):
        self.students = self.load_students()

    def load_students(self):
        if not os.path.exists(FILE_PATH):
            return []

        try:
            with open(FILE_PATH, "r") as fp:
                return json.load(fp)
        except json.JSONDecodeError:
            return []

    def save_students(self):
        with open(FILE_PATH, "w") as fp:
            json.dump(self.students, fp, indent=4)

    def is_duplicate_roll(self, roll):
        for s in self.students:
            if s["roll"] == roll:
                return True
        return False

    def add_student(self, name, roll, email, department):
        if self.is_duplicate_roll(roll):
            print("Error: Roll number already exists.")
            return

        student = Student(name, roll, email, department)
        self.students.append(student.to_dict())
        self.save_students()
        print("Student record added successfully!")

    def view_students(self):
        if not self.students:
            print("No student records found.")
            return

        print("\n===== All Students =====")
        for i, s in enumerate(self.students, start=1):
            print(f"{i}. Name : {s['name']}")
            print(f"   Roll : {s['roll']}")
            print(f"   Email : {s['email']}")
            print(f"   Department : {s['department']}")
            print("------------------------")

    def search_student(self, term):
        found = False
        for s in self.students:
            if term.lower() in s["name"].lower() or term.lower() in s["email"].lower() or term == s["roll"]:
                print("\nSearch Result:")
                print(f"Name : {s['name']}")
                print(f"Roll : {s['roll']}")
                print(f"Email : {s['email']}")
                print(f"Department : {s['department']}")
                found = True

        if not found:
            print("No matching student found.")

    def remove_student(self, roll):
        for s in self.students:
            if s["roll"] == roll:
                confirm = input(f"Are you sure you want to delete roll {roll}? (y/n): ").lower()
                if confirm == "y":
                    self.students.remove(s)
                    self.save_students()
                    print("Student record deleted successfully!")
                return

        print("Student not found.")
