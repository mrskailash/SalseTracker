# main.py

import tkinter as tk
from tkinter import ttk

import mysql.connector
from btn import BtnFile
from entry import EntryFile
from PIL import Image, ImageTk


class myapp:
    def __init__(self, master):
        self.master = master

        self.lead_container = tk.Frame(self.master, bg="gray")
        self.lead_container.pack(fill=tk.BOTH, expand=True)

        self.entryfile = EntryFile(self.lead_container)
        BtnFile.create_button(self.lead_container, self.entryfile)

    def entryfile(self):
        # The callback will be called from BtnFile
        BtnFile.entryfile(self.entry_file)


if __name__ == "__main__":
    root = tk.Tk()
    app = myapp(root)
    root.state("zoomed")
    root.mainloop()
