# import tkinter as tk

# from PIL import Image, ImageTk


# class MainWindow:
#     def __init__(self, parent):
#         self.parent = parent
#         self.close_icon_photo = None  # Store a reference to close_icon_photo

#         def show_menu(menu, button):
#             menu.post(
#                 button.winfo_rootx(), button.winfo_rooty() + button.winfo_height()
#             )

#         def center_window(window, width, height):
#             screen_width = window.winfo_screenwidth()
#             screen_height = window.winfo_screenheight()
#             x_coordinate = int((screen_width - width) / 2)
#             y_coordinate = int((screen_height - height) / 2)
#             window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

#         def open_profile():
#             profile_window = tk.Toplevel(self.parent)
#             profile_window.title("Small Window")
#             profile_window.geometry("50x50")
#             center_window(profile_window, 487, 400)
#             profile_window.resizable(False, False)
#             profile_window.title("Profile")

#             close_img_path = "asset/check_icon/close.png"
#             close_icon = Image.open(close_img_path)
#             close_icon = close_icon.resize((25, 25))
#             self.close_icon_photo = ImageTk.PhotoImage(close_icon)

#             close_btn = tk.Button(
#                 profile_window,
#                 image=self.close_icon_photo,
#                 borderwidth=2,
#                 highlightthickness=0,
#                 relief="flat",
#             )
#             close_btn.pack(anchor="ne", padx=12, pady=7)

#             close_label = tk.Label(profile_window, text="close")
#             close_label.place(x=445, y=34)

#             separator1 = tk.Frame(profile_window, height=2, width=490, bg="black")
#             separator1.place(y=55)

#             profile_type_lable = tk.Label(
#                 profile_window, text="Admin", font=("Arial", 20)
#             )
#             profile_type_lable.place(y=85, x=15)

#             btn_clr = "#0086B3"
#             general_lable = tk.Label(
#                 profile_window,
#                 text="general",
#                 font=("Arial", 15),
#                 bg=btn_clr,
#                 padx=2,  # Adjust the padding on the x-axis
#                 pady=2,  # Adjust the padding on the y-axis
#             )
#             general_lable.place(y=120, x=17)

#             userinfo = tk.Frame(
#                 profile_window,
#                 width=1500,
#                 height=300,
#                 bg="white",
#                 borderwidth=0,
#                 relief=tk.GROOVE,
#                 highlightthickness=-0,
#             )
#             userinfo.pack(pady=100, padx=15)
#             userinfo.grid_propagate(False)

#             user_type_lable = tk.Label(userinfo, text="User type", font=("Arial,30"))
#             user_type_lable.grid(row=0, column=0, padx=15, pady=15)

#             user_type_entry_lable = tk.Entry(userinfo, width=50)
#             user_type_entry_lable.grid(row=0, column=1)

#             email_lable = tk.Label(userinfo, text="Email", font=("Arial,30"))
#             email_lable.grid(row=1, column=0, padx=15, pady=15)

#             email_entry_lable = tk.Entry(userinfo, width=50)
#             email_entry_lable.grid(row=1, column=1)

#             mobile_lable = tk.Label(userinfo, text="Mobile", font=("Arial,30"))
#             mobile_lable.grid(row=3, column=0, padx=15, pady=15)

#             mobile_entry_lable = tk.Entry(userinfo, width=50)
#             mobile_entry_lable.grid(row=3, column=1)

#         # my menu
#         header_frame = tk.Frame(self.parent, bg="lightgray", height=40)
#         header_frame.pack(fill=tk.X, side=tk.TOP)
#         menu_font = ("Arial", 12)
#         my_menu = tk.Menu(header_frame, tearoff=0, font=menu_font)
#         my_menu.add_command(label="My Profile", command=open_profile)

#         my_menu_button = tk.Button(
#             header_frame,
#             text="My",
#             font="Arial 12",
#             bg="gray",
#             borderwidth=0,
#             padx=10,
#             pady=6,
#             command=lambda: show_menu(my_menu, my_menu_button),
#         )
#         my_menu_button.pack(side=tk.LEFT)


# if __name__ == "__main__":
#     root = tk.Tk()
#     root.geometry("487x348")
#     app = MainWindow(root)
#     root.mainloop()


import tkinter as tk


def on_text_focus_in(event):
    if text_widget.get("1.0", "end-1c") == placeholder:
        text_widget.delete("1.0", tk.END)
        text_widget.config(foreground="black")


def on_text_focus_out(event):
    if not text_widget.get("1.0", "end-1c").strip():
        text_widget.insert("1.0", placeholder)
        text_widget.config(foreground="grey")


# Create the main window
root = tk.Tk()
root.title("Tkinter Text Placeholder Example")

# Placeholder text
placeholder = "Enter city or address"

# Create a Text widget
text_widget = tk.Text(root, height=5, width=30)
text_widget.insert("1.0", placeholder)
text_widget.config(foreground="grey")  # Set initial text color to grey for placeholder
text_widget.pack(pady=10)

# Bind events to handle placeholder behavior
text_widget.bind("<FocusIn>", on_text_focus_in)
text_widget.bind("<FocusOut>", on_text_focus_out)

# Start the Tkinter event loop
root.mainloop()
