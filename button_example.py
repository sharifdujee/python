import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x200')

def fn():
    print("Button clicked")

button = ttk.Button(root, text="Check", command=fn)
button.pack(pady=50)

root.mainloop()
