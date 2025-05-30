import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from db import (
    fetch_attendance,
    fetch_assignments,
    fetch_exams,
    insert_prediction
)

class ExamModel:
    def __init__(self, csv_path='/Users/vipinchoudhary/Desktop/SmartGrade AI/exam_data3.csv'):
        self.csv_path = csv_path
        self.model = RandomForestClassifier(n_estimators=500, random_state=42)

    def load_training_data(self):
        df = pd.read_csv(self.csv_path)
        X = df[['attendance', 'assignment_score', 'exam_score']]
        y = df['target']
        return X, y

    def load_mysql_data(self):
       
        att = pd.DataFrame(fetch_attendance(), columns=['student_id','attendance'])
        ass = pd.DataFrame(fetch_assignments(), columns=['student_id','assignment_score'])
        exm = pd.DataFrame(fetch_exams(), columns=['student_id','exam_score'])
        # merge them with student ID
        df = att.merge(ass, on='student_id').merge(exm, on='student_id')
        return df

    def train(self):
        X_train, y_train = self.load_training_data()
        # calls model and train it for X and y
        self.model.fit(X_train, y_train)

    def predict_and_store(self):
        # Load the MySQL data
        df_mysql = self.load_mysql_data()
        X_live = df_mysql[['attendance', 'assignment_score', 'exam_score']]

        # Predict
        preds = self.model.predict(X_live)

        # Insert each prediction back into Predictions table
        for sid, p in zip(df_mysql.student_id, preds):
            text = 'Pass' if p == 1 else 'Fail'
            row = df_mysql[df_mysql.student_id == sid].iloc[0] #iloc to access row
            reason = (
                f"Att={row.attendance:.1f},"
                f"Asgn={row.assignment_score:.1f},"
                f"CIE={row.exam_score:.1f}"
            )
            insert_prediction(sid, text, reason)
