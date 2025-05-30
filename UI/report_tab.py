import tkinter as tk
from tkinter import ttk, messagebox
from report import generate_report
import os

class ReportTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Button(self, text="Generate PDF Report", command=self.make).pack(pady=20)

    def make(self):
        path = generate_report()
        messagebox.showinfo("Done", f"Report saved to:\n{os.path.abspath(path)}")
