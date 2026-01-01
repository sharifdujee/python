import tkinter as tk

root = tk.Tk()
message = tk.Label(root, text="Happy New Year, Robayet Bin Rahat")

message.pack()
root.title("Python GUI Interface")
root.geometry('600x400+50+50')
root.resizable(False, False)
root.iconbitmap('./asset/pythontutorial-1-150x150.ico')


root.mainloop()