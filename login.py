import tkinter as tk
from tkinter import ttk


class Login:
    def __init__(self, master):
        self.master = master
        master.title("Login")

        login = tk.Label(master, text="Username")
        login.grid(row=0, column=0)
        login = tk.Entry(master)
        login.grid(row=0, column=1)

        password = tk.Label(master, text="Password")
        password.grid(row=1, column=0)
        password = tk.Entry(master)
        password.grid(row=1, column=1)

        role = tk.Label(master, text="Role")
        role.grid(row=2, column=0)
        role = ttk.Combobox(master)
        role.grid(row=2, column=1)

        login_btn = tk.Button(master, text="Login")
        login_btn.grid(row=3, column=1)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x250")
    app = Login(root)
    root.mainloop()
