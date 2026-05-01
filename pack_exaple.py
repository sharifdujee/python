import tkinter as tk
root = tk.Tk()
root.title("pack example")
root.geometry("600x400")
label1 = tk.Label(root, text="Label one", bg="red", fg="white")
label2 = tk.Label(root, text = "Pack Layout", bg="green", fg="white")
label1.pack(side=tk.TOP,padx=10, pady=20)
label2.pack()
root.mainloop()