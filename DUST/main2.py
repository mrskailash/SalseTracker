import tkinter as tk
from PIL import ImageTk, Image
from tkinter import OptionMenu

class SalesTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("Sales Tracker")

        icon_image = Image.open("icon.png")  # Replace 'icon.png' with your image file
        icon_photo = ImageTk.PhotoImage(icon_image)

        # Get the screen width and height
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Calculate 80% of the screen width and height
        min_width = int(screen_width * 0.8)
        min_height = int(screen_height * 0.8)

        # Set the window size to be at least 80% of the screen width and height
        window_width = max(self.master.winfo_reqwidth(), min_width)
        window_height = max(self.master.winfo_reqheight(), min_height)

        # Calculate the x and y coordinates to center the window
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Set the window geometry
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Set the window icon
        self.master.iconphoto(True, icon_photo)

        # Maximize the window
        self.master.state('zoomed')

        header_bg = "#0086B3"
        header_frame = tk.Frame(master, bg=header_bg, height=100)
        header_frame.pack(fill=tk.X, side=tk.TOP)

        no_use = tk.Button(header_frame, text="..", font="5",bg=header_bg, borderwidth=0, padx=40,pady=6, command=self.toggle_box)
        no_use.grid(row=0 ,column=1)
        self.heading_button = tk.Button(header_frame, text="My", font="5",bg=header_bg, foreground="white", borderwidth=0, padx=10,pady=5, command=self.toggle_box)
        self.heading_button.grid(row=0 ,column=1)
         # Box
        self.dropdown_box = tk.Frame(master, bg=header_bg, height=0, width=100)
        self.dropdown_box.place(x=21, y=45)  # Initial position

        
        self.box_visible = False


        # Animation parameters
        self.animation_duration = 100  # in milliseconds
        self.animation_steps = 20
        self.animation_step_height = 100 / self.animation_steps
        self.animation_interval = self.animation_duration // self.animation_steps

        # Animation state
        self.animating = False

        self.heading_button.bind("<Enter>", lambda event: self.on_hover(True))
        self.heading_button.bind("<Leave>", lambda event: self.on_hover(False))
    
    def on_hover(self, is_hovered):
        if is_hovered:
            self.heading_button.configure(bg="#636363")  # Light black color on hover
        else:
            self.heading_button.configure(bg="#0086B3")  # Original color

    def toggle_box(self):
        if not self.animating:
            if self.box_visible:
                self.hide_box()
            else:
                self.show_box()

    def show_box(self):
        self.animating = True
        self.animate_step()

    def hide_box(self):
        self.dropdown_box.configure(height=0)  # Set height to zero without animation
        self.box_visible = False

    def animate_step(self, step=0, reverse=False):
        if reverse:
            new_height = max(0, self.dropdown_box.winfo_height() - self.animation_step_height)
        else:
            new_height = min(100, self.dropdown_box.winfo_height() + self.animation_step_height)

        self.dropdown_box.configure(height=new_height)

        if step < self.animation_steps:
            self.master.after(self.animation_interval, lambda: self.animate_step(step + 1, reverse))
        else:
            self.animating = False
            self.box_visible = not reverse

if __name__ == "__main__":
    root = tk.Tk()
    app = SalesTracker(root)
    root.mainloop()
