import tkinter as tk

from tkcalendar import DateEntry


class EntryFile:
    def __init__(self, parent):
        self.date_entry = DateEntry(parent)
        self.date_entry.pack()
        self.entry2 = tk.Entry(parent)
        self.entry2.pack()
