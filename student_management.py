import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",   # Replace with your MySQL password
    database="student_management"
)

cursor = conn.cursor()

# Function to add a student
def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, age, course))
    conn.commit()
    print("Student added successfully.")

# Function to view all students
def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    if rows:
        print("\nID | Name | Age | Course | Created At")
        print("-" * 50)
        for row in rows:
            print(row)
    else:
        print("No students found.")

# Function to update a student's course
def update_student():
    sid = int(input("Enter student ID to update: "))
    new_course = input("Enter new course: ")

    query = "UPDATE students SET course=%s WHERE id=%s"
    cursor.execute(query, (new_course, sid))
    conn.commit()
    print("Student updated successfully.")

def count_students_per_course():
    """Count how many students in each course"""
    query = "SELECT course, COUNT(*) as total_students FROM students GROUP BY course"
    cursor.execute(query)
    rows = cursor.fetchall()
    if rows:
        print("\nCourse | Total Students")
        print("-" * 30)
        for row in rows:
            print(f"{row[0]} | {row[1]}")
    else:
        print("No students found.")

def average_age_per_course():
    """Calculate average age per course"""
    query = "SELECT course, AVG(age) as avg_age FROM students GROUP BY course"
    cursor.execute(query)
    rows = cursor.fetchall()
    if rows:
        print("\nCourse | Average Age")
        print("-" * 30)
        for row in rows:
            print(f"{row[0]} | {row[1]:.2f}")
    else:
        print("No students found.")

# Function to delete a student
def delete_student():
    sid = int(input("Enter student ID to delete: "))

    query = "DELETE FROM students WHERE id=%s"
    cursor.execute(query, (sid,))
    conn.commit()
    print("Student deleted successfully.")

# Main menu loop
while True:
    print("\n--- Student Management Menu ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Count Students per Course(Aggregate)")
    print("6. Average Age per Course (Aggregate)")
    print("7. Exit")

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
        count_students_per_course()
    elif choice == '6':
        average_age_per_course()
    elif choice == '7':
        break
    else:
        print("Invalid choice. Try again.")

# Close the connection
conn.close()