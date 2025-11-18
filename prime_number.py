import tkinter as tk
from tkinter import ttk

# Prime check function
def check_prime():
    try:
        num = int(entry.get())
    except ValueError:
        result_label.config(text="Oops! Please enter a number! 😊", fg="#ff6b9d")
        return

    if num < 0:
        result_label.config(text="Let's use positive numbers! 🌈", fg="#ff6b9d")
        return

    if num == 0 or num == 1:
        result_label.config(text=f"{num} is NOT a Prime Number 🎈", fg="#ff6b9d")
        return

    flag = False
    for i in range(2, num):
        if num % i == 0:
            flag = True
            break

    if flag:
        result_label.config(text=f"🎨 {num} is NOT Prime!", fg="#ff6b9d")
        fun_fact.config(text="It can be divided by other numbers!")
    else:
        result_label.config(text=f"⭐ {num} is Prime! Awesome!", fg="#00d084")
        fun_fact.config(text="It's only divisible by 1 and itself!")


# UI Setup
root = tk.Tk()
root.title("🎉 Prime Number Detective!")
root.geometry("450x400")
root.resizable(False, False)

# Bright, cheerful background
root.config(bg="#FFE5F3")  # Soft pink background

# Title with fun emoji
title_label = tk.Label(root,
                       text="🔍 Prime Number Detective 🔢",
                       font=("Comic Sans MS", 20, "bold"),
                       bg="#FFE5F3",
                       fg="#8B4789")
title_label.pack(pady=20)

# Instruction text
instruction = tk.Label(root,
                      text="Enter a number and let's find out!",
                      font=("Comic Sans MS", 12),
                      bg="#FFE5F3",
                      fg="#555555")
instruction.pack(pady=5)

# Input Field with rounded look
entry = tk.Entry(root,
                 font=("Comic Sans MS", 24, "bold"),
                 width=8,
                 justify='center',
                 bd=4,
                 relief="solid",
                 bg="#FFFFFF",
                 fg="#8B4789")
entry.pack(pady=10)

# Colorful Button
check_btn = tk.Button(root,
                      text="🚀 Check It!",
                      font=("Comic Sans MS", 16, "bold"),
                      bg="#FFD700",
                      fg="#8B4789",
                      activebackground="#FFC700",
                      padx=25,
                      pady=8,
                      bd=3,
                      relief="raised",
                      command=check_prime)
check_btn.pack(pady=15)

# Result Label
result_label = tk.Label(root,
                        text="Ready to explore? 🎈",
                        font=("Comic Sans MS", 18, "bold"),
                        bg="#FFE5F3",
                        fg="#8B4789")
result_label.pack(pady=10)

# Fun fact label
fun_fact = tk.Label(root,
                   text="",
                   font=("Comic Sans MS", 11),
                   bg="#FFE5F3",
                   fg="#666666")
fun_fact.pack(pady=5)

# Footer
footer = tk.Label(root,
                 text="💡 Did you know? 2 is the only even prime number!",
                 font=("Comic Sans MS", 9),
                 bg="#FFE5F3",
                 fg="#999999")
footer.pack(side="bottom", pady=10)

root.mainloop()