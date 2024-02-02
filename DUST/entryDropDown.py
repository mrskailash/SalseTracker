import tkinter as tk
from tkinter import ttk

def on_dropdown_change(event):
    selected_option = dropdown.get()
    entry_var.set(f"Selected Option: {selected_option}")

# Create the main window
root = tk.Tk()
root.title("Entry with Dropdown")

# Create a StringVar to store the selected option
entry_var = tk.StringVar()

# Create an Entry widget
entry = tk.Entry(root, textvariable=entry_var, state='readonly')
entry.pack(padx=10, pady=10)

# Create a Combobox widget
options = ["Option 1", "Option 2", "Option 3"]
dropdown = ttk.Combobox(root, values=options)
dropdown.pack(padx=10, pady=10)
dropdown.set(options[0])  # Set the default value

# Bind the event handler to the <<ComboboxSelected>> event
dropdown.bind("<<ComboboxSelected>>", on_dropdown_change)

# Run the Tkinter event loop
root.mainloop()
