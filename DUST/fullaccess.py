import tkinter as tk


class SalesTracker:
    def __init__(self, root):
        # Your SalesTracker initialization code here
        pass


def open_new_window(event=None):
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    label = tk.Label(new_window, text="This is a new window!")
    label.pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1515x815+1+6")

    # Bind Alt+F to open_new_window function
    root.bind("<Alt-f>", open_new_window)

    app = SalesTracker(root)
    root.mainloop()
