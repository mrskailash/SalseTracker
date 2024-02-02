import tkinter as tk

root = tk.Tk()
root.title("Tkinter Example")

def open_frame():
    # Toggle frame visibility
    global frame_visible

    frame_visible = not frame_visible

    if frame_visible:
        frame.pack(expand=True, fill=tk.BOTH)
    else:
        frame.pack_forget()

# Create a button
button = tk.Button(root, text="Open Frame", command=open_frame)
button.pack(pady=10)

# Create a frame
frame = tk.Frame(root,bg="red")
frame.pack(fill=tk.BOTH,expand=True)
# Add widgets to the frame
label = tk.Label(frame, bg="red")
label.pack(pady=10)

# Set initial visibility to False
frame_visible = False
frame.pack_forget()

root.geometry("800x600")  # Set the initial size of the window
root.mainloop()
