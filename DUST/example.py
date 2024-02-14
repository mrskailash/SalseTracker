import tkinter as tk
from tkinter import Canvas, Scrollbar, ttk

from PIL import Image, ImageTk


class SalesTracker:
    def __init__(self, master):
        self.master = master
        master.title("SalesTracker")
        master.geometry("800x600")

        # Create a canvas widget
        self.canvas = Canvas(master)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Create a vertical scrollbar
        self.scrollbar = ttk.Scrollbar(
            master, orient="vertical", command=self.canvas.yview
        )
        self.scrollbar.pack(side="right", fill="y")

        # Configure the canvas to use the scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create a frame to contain all the widgets
        self.main_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.main_frame, anchor="nw")

        # Add your widgets to the main frame
        self.setup_widgets()

        # Update the scroll region whenever the size of the frame changes
        self.main_frame.bind("<Configure>", self.on_frame_configure)

    def setup_widgets(self):
        dashbord_container = tk.Frame(
            self.main_frame, height=65, width=1520, bg="orange"
        )
        dashbord_container.pack(anchor="nw", fill=tk.X)

        dashbord_text = tk.Label(
            dashbord_container,
            text="Dashboard",
            bg="orange",
            font=("Arial", 25),
        )
        dashbord_text.place(x=5, y=10)

        self.refresh_icon = Image.open("asset/Lead_icon/refresh.png")
        self.refresh_icon = self.refresh_icon.resize((40, 40))
        self.refresh_icon = ImageTk.PhotoImage(self.refresh_icon)

        refresh_button = tk.Button(
            dashbord_container,
            image=self.refresh_icon,
            borderwidth=0,
            highlightthickness=0,
            bg="orange",
            height=40,
            width=40,
        )
        refresh_button.place(x=1400, y=10)

        lead_dash_container = tk.Frame(
            self.main_frame, height=65, width=50, bg="lightgray"
        )
        lead_dash_container.pack(anchor="nw", fill=tk.X, pady=5)
        lead_data_container = tk.Frame(
            self.main_frame,
            height=350,
            width=50,
            bg="white",
            borderwidth=2,
            relief=tk.GROOVE,
            highlightthickness=2,
            highlightbackground="black",
        )
        lead_data_container.pack(anchor="nw", fill=tk.X)

        follow_dash_container = tk.Frame(
            self.main_frame,
            height=65,
            width=50,
            bg="lightgray",
        )
        follow_dash_container.pack(anchor="nw", fill=tk.X, pady=5)
        Follow_data_container = tk.Frame(
            self.main_frame,
            height=250,
            width=50,
            bg="white",
            borderwidth=2,
            relief=tk.GROOVE,
            highlightthickness=2,
            highlightbackground="black",
        )
        Follow_data_container.pack(anchor="nw", fill=tk.X)

        close_dash_container = tk.Frame(
            self.main_frame, height=65, width=50, bg="lightgray", pady=25
        )
        close_dash_container.pack(anchor="nw", fill=tk.X)
        close_data_container = tk.Frame(
            self.main_frame,
            height=250,
            width=50,
            bg="white",
            borderwidth=2,
            relief=tk.GROOVE,
            highlightthickness=2,
            highlightbackground="black",
        )
        close_data_container.pack(anchor="nw", fill=tk.X)

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


if __name__ == "__main__":
    root = tk.Tk()
    app = SalesTracker(root)
    root.mainloop()
