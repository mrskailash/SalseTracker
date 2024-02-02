import tkinter as tk

class LoginComponent:
    def __init__(self, parent):
        self.parent = parent

        self.username_entry = tk.Entry(parent)
        self.password_entry = tk.Entry(parent, show="*")  # Mask the password
        self.login_button = tk.Button(parent, text="Login", command=self.login)

        # Place the components directly within the __init__ method
        self.username_entry.grid(row=0, column=0, padx=10, pady=10)
        self.password_entry.grid(row=1, column=0, padx=10, pady=10)
        self.login_button.grid(row=2, column=0, padx=10, pady=10)

    def login(self):
        # Placeholder for the login functionality
        print("Login button clicked!")
        # You can add your login logic here

# Additional code can be added to the LoginComponent as needed
