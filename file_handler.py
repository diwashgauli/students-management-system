import csv
import json
from database import get_connection

def export_to_csv():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    with open('students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Name', 'Age', 'Email'])
        writer.writerows(rows)
    print("Exported to students.csv")
    conn.close()

def export_to_json():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    students = [{"ID": row[0], "Name": row[1], "Age": row[2], "Email": row[3]} for row in rows]
    with open('students.json', 'w') as file:
        json.dump(students, file, indent=4)
    print("Exported to students.json")
    conn.close()
