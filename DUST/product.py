import tkinter as tk

class product:
    def __init__(self,parent):
        self.parent = parent

        lable = tk.Label(self.parent,text="lead list")
        lable.place(x=15,y=15)

