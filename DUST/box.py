import tkinter as tk

def show_box(box_number):
    boxes = [box1, box2, box3]
    for i, box in enumerate(boxes):
        box.pack_forget() if i != box_number - 1 else box.pack(fill=tk.BOTH, expand=True)

root = tk.Tk()

# button_box = tk.Frame(root,width=50,height=50,bg="red")
# button_box.grid(row=0,column=0)
# Create the buttons
button1 = tk.Button(root, text="Show Box 1", command=lambda: show_box(1))
button2 = tk.Button(root, text="Show Box 2", command=lambda: show_box(2))
button3 = tk.Button(root, text="Show Box 3", command=lambda: show_box(3))

# Create the boxes (replace with your desired content for each box)
box1 = tk.Frame(root, width=200, height=100, bg="lightblue")
box2 = tk.Frame(root, width=200, height=100, bg="lightgreen")
box3 = tk.Frame(root, width=200, height=100, bg="yellow")

# Place buttons and the default box
button1.pack()
button2.pack()
button3.pack()
box1.pack(fill=tk.BOTH, expand=True)  # Show Box 1 by default

root.mainloop()
