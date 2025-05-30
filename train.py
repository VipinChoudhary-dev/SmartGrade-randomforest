from model import ExamModel
from tkinter import messagebox
from tkinter import ttk, messagebox

class TrainTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Button(self, text="Train & Predict", command=self.train_and_predict).pack(pady=20)

    def train_and_predict(self):
        model = ExamModel(csv_path='exam_data.csv')
        model.train()
        model.predict_and_store()
        messagebox.showinfo("Done", "Model trained on CSV and predictions stored for MySQL data.")
