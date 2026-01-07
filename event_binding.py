import tkinter as tk
from tkinter import ttk

def return_pressed(event):
    print("Return Key Pressed")

root = tk.Tk()

btn = ttk.Button(root, text="Save", takefocus=True)
btn.bind("<Return>", return_pressed)  # ✅ correct key name
btn.focus_set()                       # ✅ proper focus method
btn.pack(expand=True)

root.mainloop()

