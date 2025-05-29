import sqlite3
from database import get_connection

class Student:
    @staticmethod
    def add_student():
        name = input("Enter name: ")
        age = input("Enter age: ")
        email = input("Enter email: ")
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO students (name, age, email) VALUES (?, ?, ?)", (name, age, email))
            conn.commit()
            print("Student added successfully.")
        except sqlite3.IntegrityError:
            print("Error: Email must be unique.")
        finally:
            conn.close()

    @staticmethod
    def view_students():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.close()

    @staticmethod
    def search_student():
        keyword = input("Enter name or ID to search: ")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE name LIKE ? OR id=?", (f"%{keyword}%", keyword))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.close()

    @staticmethod
    def update_student():
        student_id = input("Enter ID of student to update: ")
        new_name = input("Enter new name: ")
        new_age = input("Enter new age: ")
        new_email = input("Enter new email: ")
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE students SET name=?, age=?, email=? WHERE id=?", (new_name, new_age, new_email, student_id))
            conn.commit()
            print("Student updated successfully.")
        except sqlite3.IntegrityError:
            print("Error: Email must be unique.")
        finally:
            conn.close()

    @staticmethod
    def delete_student():
        student_id = input("Enter ID of student to delete: ")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
        conn.commit()
        print("Student deleted successfully.")
        conn.close()
