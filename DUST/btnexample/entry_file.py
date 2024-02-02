# entry_file.py

import tkinter as tk


class EntryFile:
    def __init__(self, parent):
        self.entry1 = tk.Entry(parent)
        self.entry1.pack()
        self.entry2 = tk.Entry(parent)
        self.entry2.pack()
