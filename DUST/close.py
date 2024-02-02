import tkinter as tk
from tkinter import *

my_w = tk.Tk()
my_w.geometry("200x200")  # Size of the window
my_w.title("www.plus2net.com")  # Adding a title

# create one lebel
my_str = tk.StringVar()
l1 = tk.Label(my_w, textvariable=my_str)
l1.grid(row=1, column=2)
my_str.set("Hi I am main window")
# add one button
b1 = tk.Button(my_w, text="Clik me to open new window", command=lambda: my_open())
b1.grid(row=2, column=2)


def my_open():
    my_w_child = Toplevel(my_w)  # Child window
    my_w_child.geometry("200x200")  # Size of the window
    my_w_child.title("www.plus2net.com")
    my_str1 = tk.StringVar()
    l1 = tk.Label(my_w_child, textvariable=my_str1)
    l1.grid(row=1, column=2)
    my_str1.set("Hi I am Child window")

    def my_fun():
        my_w.config(bg="red")
        my_w_child.grab_set()

    b3 = tk.Button(
        my_w_child, text="Disable parent", command=lambda: my_w_child.grab_set()
    )
    b3.grid(row=2, column=2)
    b4 = tk.Button(
        my_w_child, text="Enable parent", command=lambda: my_w_child.grab_release()
    )
    b4.grid(row=2, column=3)


my_w.mainloop()
