# logo.py
from PIL import Image, ImageTk
import tkinter as tk

class LogoHandler:
    logo_image = None  # class attribute to store the image reference

    @classmethod
    def load_logo(cls, canvas):
        # Load and resize the logo image
        cls.logo_image = Image.open("icon.png")
        cls.logo_image = cls.logo_image.resize((50, 55))
        cls.logo_image = ImageTk.PhotoImage(cls.logo_image)

        # Create a button with the resized logo image
        logo_button = tk.Button(canvas, image=cls.logo_image, command=cls.button_clicked, borderwidth=0, highlightthickness=0, relief="flat")
        logo_button.pack()

        return logo_button

    @staticmethod
    def button_clicked():
        print("Button clicked!")
