import tkinter as tk
from tkinter import ttk
from db import fetch_predictions
from datetime import datetime

class PredictTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.tree = ttk.Treeview(self, columns=('Name','Pred','Reason','When'),
                                 show='headings')
        for h in ('Name','Pred','Reason','When'):
            self.tree.heading(h,text=h)
        self.tree.pack(fill=tk.BOTH,expand=True)
        ttk.Button(self, text="Refresh", command=self.refresh).pack(pady=5)
        self.refresh()

    def refresh(self):
        for i in self.tree.get_children(): self.tree.delete(i)
        for sid,name,pred,reason,when in fetch_predictions():
            self.tree.insert('',tk.END, values=(name,pred,reason,
                                                when.strftime("%Y-%m-%d %H:%M")))
