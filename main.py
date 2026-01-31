from student_manager import StudentManager


def show_menu():
    print("\n=========== Student Management System ===========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Exit")
    print("============================")


def main():
    manager = StudentManager()
    print("Welcome to the Student Record Management System!")
    print("Loading student records... Done!")

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Student Name: ").strip()
            roll = input("Enter Roll Number: ").strip()
            email = input("Enter Email: ").strip()
            dept = input("Enter Department: ").strip()

            if not name or not roll or not email or not dept:
                print("Empty input is not allowed.")
                continue

            if not roll.isdigit():
                print("Roll number must be an integer.")
                continue

            manager.add_student(name, roll, email, dept)

        elif choice == "2":
            manager.view_students()

        elif choice == "3":
            term = input("Enter search term (name/email/roll): ")
            manager.search_student(term)

        elif choice == "4":
            roll = input("Enter roll number to delete: ")
            manager.remove_student(roll)

        elif choice == "5":
            print("Thank you for using the Student Record Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1–5.")


if __name__ == "__main__":
    main()
