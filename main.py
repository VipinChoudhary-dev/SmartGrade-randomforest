import tkinter as tk
from tkinter import ttk
from ui.student_tab import StudentTab
from ui.data_tab    import DataTab
from ui.train_tab   import TrainTab
from ui.predict_tab import PredictTab
from ui.report_tab  import ReportTab

def main():
    app = tk.Tk()
    app.title("🔍 Smart Exam Performance Analyzer")
    app.geometry("900x600")

    nb = ttk.Notebook(app)
    for cls, title in [
        (StudentTab, "Manage Students"),
        (DataTab,    "Enter Performance"),
        (TrainTab,   "Train Model"),
        (PredictTab, "View Predictions"),
        (ReportTab,  "Export Report")
    ]:
        frame = cls(nb)
        nb.add(frame, text=title)
    nb.pack(fill="both", expand=True)
    app.mainloop()

if __name__ == "__main__":
    main()
