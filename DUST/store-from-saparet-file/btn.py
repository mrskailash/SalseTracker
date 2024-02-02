import tkinter as tk

import mysql.connector
from entry import EntryFile


class BtnFile:
    @classmethod
    def create_button(cls, main_frame, entry_file, self, master):
        self.entry = EntryFile(master)
        button = tk.Button(
            main_frame,
            text="Save Entries",
            command=lambda: cls.save_entries(entry_file),
        )
        button.pack()

    @classmethod
    def save_entries(cls, entry_file):
        # Retrieve entries from EntryFile

        formatted_date = entry_file.date_entry.get_date().strftime("%Y-%m-%d")
        entry2_value = entry_file.entry2.get()
        # Database connection information

        db_connection = mysql.connector.connect(
            host="localhost", user="root", password="", database="salestracker"
        )
        # Create a cursor

        cursor = db_connection.cursor()
        # Example INSERT query

        insert_query = "INSERT INTO leadlist (date,name) VALUES (%s, %s)"
        data_to_insert = (formatted_date, entry2_value)
        # Execute the query

        cursor.execute(insert_query, data_to_insert)
        # Commit the changes and close the connection

        db_connection.commit()
        db_connection.close()
        # You can print a message or perform other actions after saving the entries
        print("Entries saved successfully.")
