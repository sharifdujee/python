import tkinter as tk
from tkinter import ttk
root = tk.Tk()
ttk.Label(root, text="Hello Widget").pack()

# directory index
label = ttk.Label(root)
label['text'] = "Hello Rahat"
label.pack()

label.config(text="Hello Amit")

# config 

root.mainloop()