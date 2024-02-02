import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext

class NotepadApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Notepad")
        self.master.geometry("800x600")

        menubar = tk.Frame(self.master,height=40,bg="red")
        menubar.pack(fill=tk.BOTH,expand=True)
        # Create a style for ttk
        style = ttk.Style()
        style.configure('Custom.TButton', font=('Helvetica', 20))

        # Lead Button
        self.lead_button = ttk.Button(self.master, text="Lead", style='Custom.TButton', command=self.show_lead_menu)
        self.lead_button.place(x=10, y=10, width=150, height=40)

        # Lead Menu
        self.lead_menu = tk.Menu(self.master, tearoff=0, font=("Helvetica", 18))
        self.lead_menu.add_command(label="Follow Up", font=("Helvetica", 18), command=self.dummy_command)
        self.lead_menu.add_command(label="Closure", font=("Helvetica", 18), command=self.dummy_command)
        self.lead_menu.add_command(label="My Profile", font=("Helvetica", 18), command=self.dummy_command)

    def show_lead_menu(self):
        self.lead_menu.post(self.lead_button.winfo_rootx(), self.lead_button.winfo_rooty() + self.lead_button.winfo_height())

    def dummy_command(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()
