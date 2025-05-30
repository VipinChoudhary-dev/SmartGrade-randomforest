import tkinter as tk
from tkinter import ttk, messagebox
from db import add_student, update_student, delete_student, fetch_students

class StudentTab(ttk.Frame):  
    
    # a constructor is set up so that it can call the parent class for outer frame and setup
    def __init__(self, parent):
        super().__init__(parent) # call parent frame and attaches the frame to it's parent
        self.build()

    def build(self):
        frm = ttk.Frame(self)  # creates sub frame inside the frame of StudentTab
        frm.pack(fill=tk.X, pady=10)

        ttk.Label(frm, text="Name:").pack(side=tk.LEFT, padx=5)
        self.name_var = tk.StringVar()  # Creates a special variable that holds whatever text is in the entry box.
        ttk.Entry(frm, textvariable=self.name_var).pack(side=tk.LEFT, padx=5)
        ttk.Button(frm, text="Add", command=self.add).pack(side=tk.LEFT, padx=5)
        ttk.Button(frm, text="Update", command=self.update).pack(side=tk.LEFT, padx=5)
        ttk.Button(frm, text="Delete", command=self.delete).pack(side=tk.LEFT, padx=5)

        # Sets up a table-like widget with two columns: “ID” and “Name”
        self.tree = ttk.Treeview(self, columns=('ID','Name'), show='headings')
        for c in ('ID','Name'):
            self.tree.heading(c, text=c)
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)
        self.refresh()

    # A method to reload the table’s contents from the database
    def refresh(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for sid, name in fetch_students():
            self.tree.insert('',tk.END,values=(sid,name))

    def add(self):
        name = self.name_var.get().strip()
        if not name: return
        add_student(name); self.name_var.set(''); self.refresh()

    def update(self):
        sel = self.tree.selection()
        if not sel: return
        sid = self.tree.item(sel[0])['values'][0]
        name = self.name_var.get().strip()
        if not name: return
        update_student(sid,name); self.name_var.set(''); self.refresh()

    def delete(self):
        sel = self.tree.selection()
        if not sel: return
        sid = self.tree.item(sel[0])['values'][0]
        if messagebox.askyesno("Confirm","Delete this student?"):
            delete_student(sid); self.refresh()
