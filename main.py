from database import initialize_db
from students import Student
from file_handler import export_to_csv, export_to_json

def menu():
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Export to CSV")
    print("7. Export to JSON")
    print("8. Exit")

def main():
    initialize_db()
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            Student.add_student()
        elif choice == '2':
            Student.view_students()
        elif choice == '3':
            Student.search_student()
        elif choice == '4':
            Student.update_student()
        elif choice == '5':
            Student.delete_student()
        elif choice == '6':
            export_to_csv()
        elif choice == '7':
            export_to_json()
        elif choice == '8':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":   #if i have to import this main.py anywhere else in future
    main()
