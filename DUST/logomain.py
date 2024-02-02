import tkinter as tk
from logo import LogoHandler

class LogoApp:
    def __init__(self, master):
        self.master = master

        # Create a canvas in the main window
        self.box = tk.Frame(master, width=500, height=500)
        self.box.pack()

        # Use LogoHandler to load and display the logo button in the canvas
        logo_button = LogoHandler.load_logo(self.box)

if __name__ == "__main__":
    root = tk.Tk()
    app = LogoApp(root)
    root.mainloop()
 