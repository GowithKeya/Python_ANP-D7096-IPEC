import sqlite3
import os

def setup_database():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_file = os.path.join(script_dir, "college_db.db")
    sql_file = os.path.join(script_dir, "college_db.sql")
    
    # Remove the existing database file if it exists to start fresh
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"Removed existing database: {db_file}")

    print("Connecting to database...")
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    print("Reading SQL script...")
    if not os.path.exists(sql_file):
        print(f"Error: {sql_file} not found!")
        return

    with open(sql_file, 'r', encoding='utf-8') as f:
        sql_script = f.read()

    # Split the script by statements to execute them one by one
    # Note: SQLite doesn't easily support executing multiple DDL/DML with comments
    # using executescript in some older versions, but standard executescript works perfectly.
    try:
        print("Executing SQL script...")
        cursor.executescript(sql_script)
        conn.commit()
        print("Database college_db created and populated successfully!")
    except sqlite3.Error as e:
        print(f"An error occurred during DB initialization: {e}")
        conn.rollback()
        conn.close()
        return

    # Let's run a few sample queries to verify and show how it works
    print("\n--- Running Sample Queries to Verify Setup ---")
    
    # 1. Fetch Students
    print("\n1. Student List:")
    cursor.execute("SELECT student_id, first_name, last_name, course, email FROM Students;")
    students = cursor.fetchall()
    for s in students:
        print(f"ID: {s[0]} | Name: {s[1]} {s[2]} | Course: {s[3]} | Email: {s[4]}")
        
    # 2. Fetch Course Details
    print("\n2. Course List:")
    cursor.execute("SELECT course_id, course_name, trainer_name, fees FROM Courses;")
    courses = cursor.fetchall()
    for c in courses:
        print(f"Course ID: {c[0]} | Name: {c[1]} | Trainer: {c[2]} | Fee: INR {c[3]:,}")

    # 3. Fetch Attendance
    print("\n3. Attendance with Student Names:")
    cursor.execute("""
        SELECT a.attendance_date, s.first_name, s.last_name, a.status 
        FROM Attendance a
        JOIN Students s ON a.student_id = s.student_id
        ORDER BY a.attendance_date DESC;
    """)
    attendance_records = cursor.fetchall()
    for r in attendance_records:
        print(f"Date: {r[0]} | Student: {r[1]} {r[2]} | Status: {r[3]}")

    conn.close()

if __name__ == "__main__":
    setup_database()
