import tkinter as tk
root = tk.Tk()
root.title("pack example")
root.geometry("600x400")
name = tk.Label(root, text="Name:", bg="lightblue", font=("Segoe UI", 10), border=2, relief="groove", padx=5, pady=5)
name.pack(side=tk.LEFT, expand=True, padx=10, fill = tk.X, ipadx=20,),
name_entry = tk.Entry(root, width=30, font=("Segoe UI", 10), border=2, cursor="xterm")
submit = tk.Button(root, text="Submit",)
name_entry.pack(side=tk.LEFT, padx=10, expand=True,fill= tk.X, anchor="center")
submit.pack(side=tk.LEFT, padx=10, expand=True, fill = tk.X)
root.mainloop()