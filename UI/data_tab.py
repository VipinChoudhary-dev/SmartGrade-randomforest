import tkinter as tk
from tkinter import ttk, messagebox
from db import fetch_students, add_attendance, add_assignment, add_exam

class DataTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.build()

    def build(self):
        # for the friendly dropdown
        self.sid_map = {}
        
        frm = ttk.Frame(self)
        frm.pack(pady=10)

        ttk.Label(frm, text="Student:").grid(row=0, column=0)
        self.student_cb = ttk.Combobox(frm, values=[])
        self.student_cb.grid(row=0, column=1)

        ttk.Button(frm, text="⟳ Refresh Students", command=self.refresh_students)\
            .grid(row=0, column=2, padx=5)

        ttk.Label(frm, text="Attendance %:").grid(row=1, column=0)
        self.att_var = tk.DoubleVar()
        ttk.Entry(frm, textvariable=self.att_var).grid(row=1, column=1)

        ttk.Label(frm, text="Assignment score:").grid(row=2, column=0)
        self.asg_var = tk.DoubleVar()
        ttk.Entry(frm, textvariable=self.asg_var).grid(row=2, column=1)

        ttk.Label(frm, text="CIE marks:").grid(row=3, column=0)
        self.exam_var = tk.DoubleVar()
        ttk.Entry(frm, textvariable=self.exam_var).grid(row=3, column=1)

        ttk.Button(frm, text="Save", command=self.save).grid(
            row=4, column=0, columnspan=2, pady=5)

        self.refresh_students()

    def refresh_students(self):
        students = fetch_students()
        self.sid_map = {f"{sid} - {name}": sid for sid, name in students}
        self.student_cb['values'] = list(self.sid_map)
        self.student_cb.set('')

    def save(self):
        key = self.student_cb.get()
        if key not in self.sid_map:
            messagebox.showerror("Error", "Select a student"); return

        sid = self.sid_map[key]
        add_attendance(sid, self.att_var.get())
        add_assignment(sid, self.asg_var.get())
        add_exam(sid, self.exam_var.get())
        messagebox.showinfo("Saved", "Performance data saved")
