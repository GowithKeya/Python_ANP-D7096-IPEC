# SQL Practice Workspace

Welcome to your SQL Practice workspace! This folder contains a database schema definition, sample data, and tools to practice SQL queries locally.

## Files In This Folder

- [college_db.sql](file:///c:/Users/Kartik/OneDrive/Documents/Desktop/AI%20project/Python_ANP-D7096-IPEC/SQL%20Practice/college_db.sql) — The SQL DDL & DML script containing the table definitions, constraints, descriptions, and mock data.
- [setup_db.py](file:///c:/Users/Kartik/OneDrive/Documents/Desktop/AI%20project/Python_ANP-D7096-IPEC/SQL%20Practice/setup_db.py) — A Python helper script that creates a local SQLite database file `college_db.db` and loads the schema and data.
- [sql_terminal.py](file:///c:/Users/Kartik/OneDrive/Documents/Desktop/AI%20project/Python_ANP-D7096-IPEC/SQL%20Practice/sql_terminal.py) — An interactive SQL Command Line Interface to run queries directly in your shell.

---

## Schema Overview

The database is named **`college_db`** and consists of 5 related tables:

### 1. `Students`
Stores info about enrolled students.
- `student_id` (INT, PRIMARY KEY)
- `first_name` (VARCHAR)
- `last_name` (VARCHAR)
- `gender` (VARCHAR) — Male/Female
- `age` (INT)
- `city` (VARCHAR)
- `course` (VARCHAR) — Enrolled Course Name
- `email` (VARCHAR, UNIQUE)
- `phone` (VARCHAR)
- `admission_date` (DATE)

### 2. `Courses`
Available courses at the college.
- `course_id` (INT, PRIMARY KEY)
- `course_name` (VARCHAR)
- `duration` (VARCHAR)
- `fees` (DECIMAL)
- `trainer_name` (VARCHAR) — Faculty Name

### 3. `Faculty`
College teaching staff.
- `faculty_id` (INT, PRIMARY KEY)
- `faculty_name` (VARCHAR)
- `department` (VARCHAR)
- `qualification` (VARCHAR)
- `experience` (INT) — Years of experience
- `salary` (DECIMAL) — Monthly salary

### 4. `Departments`
College administrative/academic departments.
- `dept_id` (INT, PRIMARY KEY)
- `dept_name` (VARCHAR)
- `hod_name` (VARCHAR) — Head of Department
- `building` (VARCHAR)

### 5. `Attendance`
Daily student attendance logs.
- `attendance_id` (INT, PRIMARY KEY)
- `student_id` (INT, FOREIGN KEY referencing `Students`)
- `attendance_date` (DATE)
- `status` (VARCHAR) — Present/Absent

---

## How to Set Up & Use

### Option 1: Run the Interactive SQL Terminal (Recommended)
You can open an interactive command prompt directly in your console to execute SQL queries on the database:
```bash
python "SQL Practice/sql_terminal.py"
```
Once opened, you can run queries (remember to end them with a semicolon `;`):
```sql
sqlite> SELECT * FROM Students;
sqlite> .tables
sqlite> .schema Students
sqlite> exit
```

### Option 2: Reset / Setup Database via Python Script
If you ever want to reset the database back to its default sample data:
```bash
python "SQL Practice/setup_db.py"
```
This script will recreate the `college_db.db` file and output verified queries.

### Option 3: Use an external SQLite Client
You can open `college_db.db` in any external client like **DB Browser for SQLite** or a VS Code SQLite extension.

---

## SQL Practice Questions

Try to write and run the following queries to test your SQL skills!

### 1. Basic Selection
**Question:** Get a list of all students who live in Delhi.
<details>
<summary>Answer</summary>

```sql
SELECT * FROM Students WHERE city = 'Delhi';
```
</details>

### 2. Aggregation & Grouping
**Question:** Find the total number of students enrolled in each course.
<details>
<summary>Answer</summary>

```sql
SELECT course, COUNT(*) AS student_count 
FROM Students 
GROUP BY course;
```
</details>

### 3. Joining Tables
**Question:** Display student names and their attendance status along with the date.
<details>
<summary>Answer</summary>

```sql
SELECT s.first_name, s.last_name, a.attendance_date, a.status 
FROM Attendance a
JOIN Students s ON a.student_id = s.student_id;
```
</details>

### 4. Conditional Updates & Queries
**Question:** Get the name of courses that cost more than 20,000 INR.
<details>
<summary>Answer</summary>

```sql
SELECT course_name, fees 
FROM Courses 
WHERE fees > 20000;
```
</details>

### 5. String Manipulation & Pattern Matching
**Question:** Retrieve all faculty members whose qualification contains 'Ph.D.'.
<details>
<summary>Answer</summary>

```sql
SELECT faculty_name, qualification 
FROM Faculty 
WHERE qualification LIKE '%Ph.D.%';
```
</details>
