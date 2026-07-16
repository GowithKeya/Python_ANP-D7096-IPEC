-- SQL Script for Setting Up college_db Database
-- This script contains table definitions with constraints, descriptions, and mock data for practice.

-- Create database if using systems like MySQL/PostgreSQL
-- CREATE DATABASE college_db;
-- USE college_db;

-- ============================================================================
-- 1. Table: Departments
-- ============================================================================
CREATE TABLE Departments (
    dept_id INT PRIMARY KEY,               -- Department ID
    dept_name VARCHAR(50) NOT NULL,        -- Department Name
    hod_name VARCHAR(50),                  -- Head of Department
    building VARCHAR(30)                   -- Building Name
);

-- ============================================================================
-- 2. Table: Faculty
-- ============================================================================
CREATE TABLE Faculty (
    faculty_id INT PRIMARY KEY,            -- Faculty ID
    faculty_name VARCHAR(50) NOT NULL,     -- Faculty Name
    department VARCHAR(50),                -- Department
    qualification VARCHAR(50),             -- Highest Qualification
    experience INT,                        -- Years of Experience
    salary DECIMAL(10,2)                   -- Monthly Salary
);

-- ============================================================================
-- 3. Table: Courses
-- ============================================================================
CREATE TABLE Courses (
    course_id INT PRIMARY KEY,             -- Course ID
    course_name VARCHAR(50) NOT NULL,      -- Course Name
    duration VARCHAR(20),                  -- Course Duration
    fees DECIMAL(10,2),                    -- Course Fee
    trainer_name VARCHAR(50)               -- Faculty Name
);

-- ============================================================================
-- 4. Table: Students
-- ============================================================================
CREATE TABLE Students (
    student_id INT PRIMARY KEY,            -- Unique Student ID
    first_name VARCHAR(50) NOT NULL,       -- Student First Name
    last_name VARCHAR(50) NOT NULL,        -- Student Last Name
    gender VARCHAR(10),                    -- Male/Female
    age INT,                               -- Student Age
    city VARCHAR(50),                      -- City Name
    course VARCHAR(50),                    -- Enrolled Course
    email VARCHAR(100) UNIQUE,             -- Student Email
    phone VARCHAR(15),                     -- Contact Number
    admission_date DATE                    -- Admission Date
);

-- ============================================================================
-- 5. Table: Attendance
-- ============================================================================
CREATE TABLE Attendance (
    attendance_id INT PRIMARY KEY,          -- Attendance ID
    student_id INT,                         -- Student ID (FK referencing Students)
    attendance_date DATE,                   -- Attendance Date
    status VARCHAR(10),                     -- Present/Absent
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);

-- ============================================================================
-- Sample Data Insertion for Practice
-- ============================================================================

-- Inserting into Departments
INSERT INTO Departments (dept_id, dept_name, hod_name, building) VALUES
(1, 'Computer Science', 'Dr. Ramesh Kumar', 'Block A'),
(2, 'Information Technology', 'Dr. Sunita Sharma', 'Block B'),
(3, 'Electronics', 'Dr. Anil Mehta', 'Block A'),
(4, 'Mechanical', 'Dr. Rajesh Patel', 'Workshop Block');

-- Inserting into Faculty
INSERT INTO Faculty (faculty_id, faculty_name, department, qualification, experience, salary) VALUES
(101, 'Prof. Amit Verma', 'Computer Science', 'Ph.D. in CSE', 12, 85000.00),
(102, 'Dr. Neha Gupta', 'Information Technology', 'Ph.D. in IT', 8, 75000.00),
(103, 'Prof. Suresh Rao', 'Electronics', 'M.Tech', 15, 90000.00),
(104, 'Mr. Vikas Singh', 'Mechanical', 'M.Tech', 5, 60000.00);

-- Inserting into Courses
INSERT INTO Courses (course_id, course_name, duration, fees, trainer_name) VALUES
(201, 'Python Programming', '3 Months', 15000.00, 'Prof. Amit Verma'),
(202, 'Web Development', '6 Months', 25000.00, 'Dr. Neha Gupta'),
(203, 'Data Science', '6 Months', 35000.00, 'Prof. Amit Verma'),
(204, 'Embedded Systems', '4 Months', 20000.00, 'Prof. Suresh Rao');

-- Inserting into Students
INSERT INTO Students (student_id, first_name, last_name, gender, age, city, course, email, phone, admission_date) VALUES
(1, 'Aarav', 'Sharma', 'Male', 20, 'Delhi', 'Python Programming', 'aarav.sharma@email.com', '9876543210', '2026-06-01'),
(2, 'Diya', 'Patel', 'Female', 21, 'Mumbai', 'Web Development', 'diya.patel@email.com', '8765432109', '2026-06-05'),
(3, 'Kabir', 'Singh', 'Male', 22, 'Delhi', 'Data Science', 'kabir.singh@email.com', '7654321098', '2026-06-10'),
(4, 'Ananya', 'Sen', 'Female', 19, 'Kolkata', 'Python Programming', 'ananya.sen@email.com', '6543210987', '2026-06-12'),
(5, 'Rohan', 'Das', 'Male', 20, 'Bangalore', 'Embedded Systems', 'rohan.das@email.com', '5432109876', '2026-06-15');

-- Inserting into Attendance
INSERT INTO Attendance (attendance_id, student_id, attendance_date, status) VALUES
(1, 1, '2026-07-01', 'Present'),
(2, 2, '2026-07-01', 'Present'),
(3, 3, '2026-07-01', 'Absent'),
(4, 4, '2026-07-01', 'Present'),
(5, 5, '2026-07-01', 'Present'),
(6, 1, '2026-07-02', 'Present'),
(7, 2, '2026-07-02', 'Absent'),
(8, 3, '2026-07-02', 'Present'),
(9, 4, '2026-07-02', 'Present'),
(10, 5, '2026-07-02', 'Absent');
