import tkinter as tk
from tkinter import messagebox, ttk

import mysql.connector
from PIL import Image, ImageTk
from tkcalendar import DateEntry

root = tk.Tk()
root.title("Main Window")
root.geometry("487x380")

# Variable to store the fetched ID
fetched_id = 0


def show_product_menu(menu, button):
    menu.post(button.winfo_rootx(), button.winfo_rooty() + button.winfo_height())


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = int((screen_width - width) / 2)
    y_coordinate = int((screen_height - height) / 2)

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")


def fetch_next_id(leadNo_entry):
    global fetched_id
    # Connect to MySQL server
    db_connection = mysql.connector.connect(
        host="localhost", user="root", password="", database="salestracker"
    )

    # Create a cursor object
    cursor = db_connection.cursor()

    # Fetch the next available ID from the database
    cursor.execute("SELECT MAX(id) FROM leadlist")
    max_id = cursor.fetchone()[0]
    fetched_id = max_id + 1 if max_id else 1

    # Close the database connection
    cursor.close()
    db_connection.close()

    # Update leadNo_entry with the fetched ID
    leadNo_entry.delete(0, tk.END)
    leadNo_entry.insert(0, str(fetched_id))


def save_data(
    formatted_date,
    name_entry,
    sales_person_entry,
    address_entry,
    email_entry,
    source_entry,
    assignto_entry,
    status_entry,
):
    global fetched_id
    # Connect to MySQL server
    db_connection = mysql.connector.connect(
        host="localhost", user="root", password="", database="salestracker"
    )

    # Create a cursor object
    cursor = db_connection.cursor()

    # Insert data into the database using the fetched ID and formatted date
    cursor.execute(
        "INSERT INTO leadlist (id, date, name, salesperson, address, email, source, asignto, status) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (
            fetched_id,
            formatted_date,
            name_entry.get(),
            sales_person_entry.get(),
            address_entry.get("1.0", tk.END),
            email_entry.get(),
            source_entry.get(),
            assignto_entry.get(),
            status_entry.get(),
        ),
    )

    # Commit changes and close the database connection
    db_connection.commit()
    cursor.close()
    db_connection.close()

    # Show a message box indicating successful data storage
    tk.messagebox.showinfo(
        "Success", "Data stored successfully for ID: {}".format(fetched_id)
    )

    # Reset fetched_id for the next entry
    fetched_id = 0
    clear_input_fields(
        name_entry,
        sales_person_entry,
        address_entry,
        email_entry,
        source_entry,
        assignto_entry,
        status_entry,
    )


def clear_input_fields(
    date_entry,
    name_entry,
    sales_person_entry,
    address_entry,
    email_entry,
    source_entry,
    assignto_entry,
    status_entry,
):
    date_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    sales_person_entry.delete(0, tk.END)
    address_entry.delete("1.0", tk.END)
    email_entry.delete(0, tk.END)
    source_entry.delete(0, tk.END)
    assignto_entry.delete(0, tk.END)
    status_entry.delete(0, tk.END)


def open_lead_details():
    global fetched_id
    product_window = tk.Toplevel(root)
    product_window.title("Small Window")
    product_window.geometry("50x50")
    center_window(product_window, 487, 450)
    product_window.title("product Details")
    product_window.grab_set()

    leadNo_label = tk.Label(
        product_window, text="Lead No", bg="lightgray", fg="black", font=("Arial", 12)
    )
    leadNo_label.place(x=10, y=10)

    leadNo_entry = tk.Entry(
        product_window, borderwidth=2, highlightthickness=-0, relief=tk.GROOVE
    )
    leadNo_entry.place(x=120, y=12)

    # Fetch the initial ID when the window is opened
    fetch_next_id(leadNo_entry)

    # Bind the function to the key release event
    leadNo_entry.bind("<KeyRelease>", lambda event: fetch_next_id(leadNo_entry))

    date_label = tk.Label(
        product_window, text="Date", bg="lightgray", fg="black", font=("Arial", 12)
    )
    date_label.place(x=280, y=10)

    date_entry = DateEntry(
        product_window,
        selectedmode="day",
        borderwidth=2,
        highlightthickness=-0,
        relief=tk.GROOVE,
    )
    date_entry.place(x=330, y=12)

    name_label = tk.Label(
        product_window, text="Name", bg="lightgray", fg="black", font=("Arial", 13)
    )
    name_label.place(x=12, y=50)

    name_entry = tk.Entry(
        product_window, borderwidth=2, highlightthickness=-0, relief=tk.GROOVE, width=55
    )
    name_entry.place(x=120, y=50)

    sales_person_label = tk.Label(
        product_window,
        text="Sales Person",
        bg="lightgray",
        fg="black",
        font=("Arial", 13),
    )
    sales_person_label.place(x=12, y=90)

    sales_person_entry = tk.Entry(
        product_window, borderwidth=2, highlightthickness=-0, relief=tk.GROOVE, width=55
    )
    sales_person_entry.place(x=120, y=90)

    address_label = tk.Label(
        product_window, text="Address", bg="lightgray", fg="black", font=("Arial", 13)
    )
    address_label.place(x=12, y=130)

    address_entry = tk.Text(product_window, width=40, height=5, wrap=tk.WORD)
    address_entry.place(x=120, y=130)

    email_label = tk.Label(
        product_window, text="Email", bg="lightgray", fg="black", font=("Arial", 13)
    )
    email_label.place(x=12, y=230)

    email_entry = tk.Entry(
        product_window, borderwidth=2, highlightthickness=-0, relief=tk.GROOVE, width=55
    )
    email_entry.place(x=120, y=230)

    source_label = tk.Label(
        product_window, text="Source ", bg="lightgray", fg="black", font=("Arial", 13)
    )
    source_label.place(x=12, y=270)

    source_entry = tk.Entry(
        product_window, borderwidth=2, highlightthickness=-0, relief=tk.GROOVE, width=55
    )
    source_entry.place(x=120, y=270)

    assignto_label = tk.Label(
        product_window, text="Assign To", bg="lightgray", fg="black", font=("Arial", 13)
    )
    assignto_label.place(x=12, y=310)

    assignto_entry = tk.Entry(
        product_window, borderwidth=2, highlightthickness=-0, relief=tk.GROOVE, width=55
    )
    assignto_entry.place(x=120, y=310)

    status_label = tk.Label(
        product_window, text="Status", bg="lightgray", fg="black", font=("Arial", 13)
    )
    status_label.place(x=12, y=350)

    status_entry = tk.Entry(
        product_window, borderwidth=2, highlightthickness=-0, relief=tk.GROOVE, width=55
    )
    status_entry.place(x=120, y=350)

    def save_data_wrapper():
        # Format the date using strftime
        formatted_date = date_entry.get_date().strftime("%Y-%m-%d")

        # Pass the formatted date to the save_data function
        save_data(
            formatted_date,
            name_entry,
            sales_person_entry,
            address_entry,
            email_entry,
            source_entry,
            assignto_entry,
            status_entry,
        )

    save_btn = tk.Button(product_window, text="Save", command=save_data_wrapper)
    save_btn.place(x=120, y=400)

    new_btn = tk.Button(
        product_window,
        text="New",
        command=lambda: clear_input_fields(
            date_entry,
            name_entry,
            sales_person_entry,
            address_entry,
            email_entry,
            source_entry,
            assignto_entry,
            status_entry,
        ),
    )
    new_btn.place(x=200, y=400)
    product_window.wait_window()


menu_font = ("Arial", 12)
product_menu = tk.Menu(root, tearoff=0, font=menu_font)
product_menu.add_command(label="Add", command=open_lead_details)
product_menu.add_command(label="Delete")
product_menu.add_command(label="Edit")

add_product = tk.Button(
    root,
    text="Add Product",
    command=lambda: show_product_menu(product_menu, add_product),
)
add_product.place(x=14, y=15)

root.mainloop()
