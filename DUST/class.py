import tkinter as tk
from login_component import LoginComponent

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Main Window")

        # Create a box
        self.box = tk.Frame(master, width=500, height=500, bg="lightgray")
        self.box.pack()

        # Create and place the login component
        login_component = LoginComponent(self.box)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
