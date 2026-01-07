import tkinter as tk
from tkinter import ttk

root = tk.Tk()

'''def button_clicked():
    print("Clikced the Button")


button = ttk.Button(root, text="Click Me", command= button_clicked)
button.pack()'''

# argument inside function
def select(option):
    print(option)

ttk.Button(root, text="Rock", command=lambda:select("Rock")).pack()
ttk.Button(root, text="Pack ", command=lambda:select("Pack")).pack()
ttk.Button(root, text="Scissors", command=lambda:select("Scissors")).pack()



root.mainloop()
