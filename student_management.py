import mysql.connector

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="student_db"
)

cursor = conn.cursor()

def add_student():
    name = input("Enter name: ")
    dept = input("Enter department: ")
    year = int(input("Enter year: "))
    email = input("Enter email: ")

    query = "INSERT INTO students (name, department, year, email) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, dept, year, email))
    conn.commit()
    print("Student added successfully")


def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)


def update_student():
    sid = int(input("Enter student ID to update: "))
    email = input("Enter new email: ")

    query = "UPDATE students SET email=%s WHERE id=%s"
    cursor.execute(query, (email, sid))
    conn.commit()
    print("Student updated successfully")


def delete_student():
    sid = int(input("Enter student ID to delete: "))
    query = "DELETE FROM students WHERE id=%s"
    cursor.execute(query, (sid,))
    conn.commit()
    print("Student deleted successfully")


while True:
    print("\n1. Add Student\n2. View Students\n3. Update Student\n4. Delete Student\n5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        break
    else:
        print("Invalid choice")

conn.close()