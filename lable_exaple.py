import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x200')
root.title("Label Widget Demo")
label = ttk.Label(root,   text="This is a label", font=("Helvetica", 14))
label.pack()

root.mainloop()
