USE trail95;

-- Sample Students
-- Sample Students
INSERT INTO Student (student_name) VALUES 
('Rohit'), ('Vipin'), ('Priya'), ('Suyash'), ('Loki'),
('Arjun'), ('Sneha'), ('Meera'), ('Nikhil'), ('Pooja');

-- Sample Attendance (for 10 students)
INSERT INTO Attendance (student_id, attendance_percentage) VALUES
(1, 55), (2, 0), (3, 60), (4, 45), (5, 50),
(6, 58), (7, 47), (8, 53), (9, 20), (10, 50);

-- Sample Assignments (for 10 students)
INSERT INTO Assignments (student_id, assignment_score) VALUES
(1, 50), (2, 45), (3, 0), (4, 55), (5, 48),
(6, 60), (7, 40), (8, 20), (9, 43), (10, 52);

-- Sample Exams (for 10 students)
INSERT INTO Exams (student_id, exam_score) VALUES
(1, 60), (2, 74), (3, 85), (4, 90), (5, 50),
(6, 93), (7, 49), (8, 70), (9, 45), (10, 48);

SELECT* FROM Student;
SELECT* FROM Attendance;
SELECT* FROM Assignments;
SELECT* FROM Exams;
SELECT* FROM Predictions;
