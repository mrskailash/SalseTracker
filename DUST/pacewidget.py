import tkinter as tk


def submit():
    # Retrieve values from entry widgets
    values = [entry.get() for entry in entry_widgets]

    # Display the values (you can customize this part based on your requirements)
    for i, value in enumerate(values):
        print(f"{labels[i]}: {value}")


# Create the main Tkinter window
root = tk.Tk()
root.title("Label and Entry Example")

# List of labels
labels = [
    "Date",
    "Fullname",
    "Address",
    "Mobile No",
    "Email",
    "Source",
    "Assign To",
    "Status",
    "Ref By",
    "Products",
    "Remark",
    "Company",
]

# Create labels and entries using a loop
label_widgets = [tk.Label(root, text=labels[i]) for i in range(0, len(labels), 2)]
entry_widgets = [tk.Entry(root) for _ in range(len(label_widgets))]

# Place labels and entries using the place method
for i, label in enumerate(label_widgets):
    label.place(x=50, y=20 + i * 30)
    entry_widgets[i].place(x=150, y=20 + i * 30)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.place(x=150, y=20 + len(label_widgets) * 30)

# Run the Tkinter event loop
root.mainloop()
