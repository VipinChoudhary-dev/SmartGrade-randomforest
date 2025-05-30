import mysql.connector
from datetime import datetime

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Vipin091105',  
        database='trial95'
    )

def add_student(name):
    #conn is basically an connection object
    # connects and create cursor object for running SQL commands
    conn = get_connection(); c = conn.cursor()
    c.execute("INSERT INTO Student (student_name) VALUES (%s)", (name,))
    # save changes and closes
    conn.commit(); conn.close()
    

def update_student(sid, name):
    conn = get_connection(); c = conn.cursor()
    c.execute("UPDATE Student SET student_name=%s WHERE student_id=%s", (name, sid))
    conn.commit(); conn.close()


def delete_student(sid):
    conn = get_connection(); c = conn.cursor()
    c.execute("DELETE FROM Student WHERE student_id=%s", (sid,))
    conn.commit(); conn.close()
    

def fetch_students():
    conn = get_connection(); c = conn.cursor()
    c.execute("SELECT student_id, student_name FROM Student")
    # it fetches student ID & student Name from the Student table
    rows = c.fetchall(); conn.close()
    return rows


def add_attendance(sid, percent):
    conn = get_connection(); c = conn.cursor()
    c.execute("INSERT INTO Attendance (student_id, attendance_percentage) VALUES (%s,%s)", (sid, percent))
    conn.commit(); conn.close()
    

def add_assignment(sid, score):
    conn = get_connection(); c = conn.cursor()
    c.execute("INSERT INTO Assignments (student_id, assignment_score) VALUES (%s,%s)", (sid, score))
    conn.commit(); conn.close()
    

def add_exam(sid, score):
    conn = get_connection(); c = conn.cursor()
    c.execute("INSERT INTO Exams (student_id, exam_score) VALUES (%s,%s)", (sid, score))
    conn.commit(); conn.close()
    

def fetch_attendance():
    conn = get_connection(); c = conn.cursor()
    c.execute("SELECT student_id, attendance_percentage FROM Attendance")
    rows = c.fetchall(); conn.close()
    return rows


def fetch_assignments():
    conn = get_connection(); c = conn.cursor()
    c.execute("SELECT student_id, assignment_score FROM Assignments")
    rows = c.fetchall(); conn.close()
    return rows


def fetch_exams():
    conn = get_connection(); c = conn.cursor()
    c.execute("SELECT student_id, exam_score FROM Exams")
    rows = c.fetchall(); conn.close()
    return rows


def insert_prediction(sid, prediction, reason):
    conn = get_connection(); c = conn.cursor()
    now = datetime.now()
    c.execute("""INSERT INTO Predictions
                 (student_id, prediction, reason, predicted_at)
                 VALUES (%s,%s,%s,%s)""",
              (sid, prediction, reason, now))
    conn.commit(); conn.close()


def fetch_predictions():
    conn = get_connection(); c = conn.cursor()
    c.execute("""SELECT p.student_id, s.student_name, p.prediction, p.reason, p.predicted_at
                 FROM Predictions p
                 JOIN Student s ON p.student_id=s.student_id
                 ORDER BY p.predicted_at DESC""")
    rows = c.fetchall(); conn.close()
    return rows
