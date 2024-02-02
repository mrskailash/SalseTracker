# btn_file.py

import tkinter as tk


class BtnFile:
    @classmethod
    def create_button(cls, main_frame, callback):
        button = tk.Button(main_frame, text="Clear Entries", command=callback)
        button.pack()

    @staticmethod
    def clear_entries(entry_file):
        # Access entries through entry_file
        entry_file.entry1.delete(0, tk.END)
        entry_file.entry2.delete(0, tk.END)
