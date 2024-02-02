from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Simple Example")
root.state('zoomed')


def show_box(box_number):
    # Hide all containers
    details_container.place_forget()
    product_container.place_forget()
    note_container.place_forget()

    details_btn.config(bg="lightgray" if box_number != 1 else "#0086B3")
    product_btn.config(bg="lightgray" if box_number != 2 else "#0086B3")
    notes_btn.config(bg="lightgray" if box_number != 3 else "#0086B3")
    # Display the selected container
    if box_number == 1:
        details_container.place(x=0, y=40, height=475, width=1528)
    elif box_number == 2:
        product_container.place(x=0, y=40, height=475, width=1528)
    elif box_number == 3:
        note_container.place(x=0, y=40, height=475, width=1528)


lead_color = "white"
lead_container = tk.Frame(root, padx=2, pady=2, bg=lead_color, height=50)
lead_container.pack(fill=tk.BOTH, expand=True)



lead_entry = tk.Frame(lead_container,
                       borderwidth=2,
                       relief=tk.GROOVE,
                       highlightthickness=0,
                       highlightbackground="gray",
                       highlightcolor="gray",
                       bg="lightgray",
                       height=500,width=1500)
lead_entry.pack(fill=tk.BOTH,expand=True,pady=5)


add_lead_btn_row = tk.Frame(lead_entry,
                            height=50,
                            width=50,
                            bg="lightgray")
add_lead_btn_row.place(x=10,y=10)

details_btn_clr = "#0086B3"
details_btn = tk.Button(add_lead_btn_row,
                        text="Details",bg=details_btn_clr,
                        font=("Arial",12),
                        height=1,
                        width=12,command=lambda: show_box(1))
details_btn.grid(row=0,column=1,padx=5)

product_btn = tk.Button(add_lead_btn_row,
                        text="Products",
                        font=("Arial",12),
                        height=1,width=12,command=lambda: show_box(2))
product_btn.grid(row=0,column=2,padx=5)

notes_btn = tk.Button(add_lead_btn_row,
                      text="Notes",
                      font=("Arial",12),
                      height=1,width=12,command=lambda: show_box(3))
notes_btn.grid(row=0,column=3,padx=2)


details_container=tk.Frame(lead_entry,height=475,width=1528,bg="lightgray" ,borderwidth=2,
                      relief=tk.GROOVE,
                       highlightthickness=-0,)
details_container.place(x=0,y=40)

info_container = tk.Frame(details_container,height=475,width=1528,bg="lightgray",borderwidth=2,relief=tk.GROOVE,highlightthickness=-0)
info_container.pack(fill=tk.BOTH,expand=True)
info_container.grid_propagate(False)

leadNo_lable = tk.Label(info_container,text="Lead No",bg="lightgray",fg="black",font=("Arial",12))
leadNo_lable.place(x=10,y=10)

leadNo_entry = tk.Entry(info_container,borderwidth=2,highlightthickness=-0,relief=tk.GROOVE)
leadNo_entry.place(x=120,y=12)

date_lable = tk.Label(info_container,text="Date",bg="lightgray",fg="black",font=("Arial",12))
date_lable.place(x=280,y=10)

date_entry = tk.Entry(info_container,borderwidth=2,highlightthickness=-0,relief=tk.GROOVE)
date_entry.place(x=330,y=12)

name_lable = tk.Label(info_container,text="Name",bg="lightgray",fg="black",font=("Arial",13))
name_lable.place(x=12,y=50)

name_entry = tk.Entry(info_container,borderwidth=2,highlightthickness=-0,relief=tk.GROOVE,width=55)
name_entry.place(x=120,y=50)

sales_person_lable = tk.Label(info_container,text="Sales Person",bg="lightgray",fg="black",font=("Arial",13))
sales_person_lable.place(x=12,y=90)

sales_person_entry = tk.Entry(info_container,borderwidth=2,highlightthickness=-0,relief=tk.GROOVE,width=55)
sales_person_entry.place(x=120,y=90)

address_lable = tk.Label(info_container,text="Address",bg="lightgray",fg="black",font=("Arial",13))
address_lable.place(x=12,y=130)

address_entry = tk.Text(info_container,width=40, height=5, wrap=tk.WORD)
address_entry.place(x=120,y=130)

email_lable = tk.Label(info_container,text="Email",bg="lightgray",fg="black",font=("Arial",13))
email_lable.place(x=12,y=230)

email_entry = tk.Entry(info_container,borderwidth=2,highlightthickness=-0,relief=tk.GROOVE,width=55)
email_entry.place(x=120,y=230)

source_lable = tk.Label(info_container,text="Source ",bg="lightgray",fg="black",font=("Arial",13))
source_lable.place(x=12,y=270)

source_entry = tk.Entry(info_container,borderwidth=2,highlightthickness=-0,relief=tk.GROOVE,width=55)
source_entry.place(x=120,y=270)

assignto_lable = tk.Label(info_container,text="Assign To",bg="lightgray",fg="black",font=("Arial",13))
assignto_lable.place(x=12,y=310)

assignto_entry = tk.Entry(info_container,borderwidth=2,highlightthickness=-0,relief=tk.GROOVE,width=55)
assignto_entry.place(x=120,y=310)

status_lable = tk.Label(info_container,text="Status",bg="lightgray",fg="black",font=("Arial",13))
status_lable.place(x=12,y=350)

status_entry = tk.Entry(info_container,borderwidth=2,highlightthickness=-0,relief=tk.GROOVE,width=55)
status_entry.place(x=120,y=350)

product_container=tk.Frame(lead_entry,height=475,width=1528,bg="lightgray" ,borderwidth=2,
                      relief=tk.GROOVE,
                       highlightthickness=-0)
product_container.place(x=0,y=40)
product_container.place_forget()

note_container=tk.Frame(lead_entry,height=475,width=1528,bg="lightgray" ,borderwidth=2,
                      relief=tk.GROOVE,
                       highlightthickness=-0)
note_container.place(x=0,y=40)
note_container.place_forget()

# header = tk.Frame(root,height=40,width=55)
# header.place(x=10,y=15)
root.mainloop()
