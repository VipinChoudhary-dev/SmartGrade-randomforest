
CREATE DATABASE IF NOT EXISTS trial95;

USE trial95;

CREATE TABLE IF NOT EXISTS Student (
    student_id INT PRIMARY KEY AUTO_INCREMENT, /* assigns new integer when new names added */
    student_name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Attendance (
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    attendance_percentage DECIMAL(5,2) NOT NULL, /* up to 5 total digits, 2 of which are after the decimal point (max 999.99) */
    FOREIGN KEY (student_id) REFERENCES Student(student_id) ON DELETE CASCADE /* if a Student row is deleted, all their Attendance rows are automatically removed */
);

CREATE TABLE IF NOT EXISTS Assignments (
    assignment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    assignment_score DECIMAL(5,2) NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Student(student_id) ON DELETE CASCADE  
);

CREATE TABLE IF NOT EXISTS Exams (
    exam_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    exam_score DECIMAL(5,2) NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Student(student_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Predictions (
    prediction_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    prediction VARCHAR(10) NOT NULL, /* PASS or FAIL */
    reason TEXT NOT NULL,
    predicted_at DATETIME NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Student(student_id) ON DELETE CASCADE
);

SHOW TABLES;
