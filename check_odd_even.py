import tkinter as tk

# Odd/Even check function
def check_odd_even():
    try:
        num = int(entry.get())
    except ValueError:
        result_label.config(text="Oops! Please enter a number! 😊", fg="#ff6b9d")
        fun_fact.config(text="")
        return

    if num < 0:
        result_label.config(text="Let's try positive numbers! 🌟", fg="#ff6b9d")
        fun_fact.config(text="")
        return

    if num % 2 == 0:
        result_label.config(text=f"🎉 {num} is an EVEN number!", fg="#4A90E2")
        fun_fact.config(text="Even numbers can be split into 2 equal groups! 👯")
    else:
        result_label.config(text=f"⭐ {num} is an ODD number!", fg="#FF6B9D")
        fun_fact.config(text="Odd numbers always have one left over! 🎈")


# UI Setup
root = tk.Tk()
root.title("🎪 Odd or Even Explorer!")
root.geometry("450x420")
root.resizable(False, False)

# Bright, cheerful background
root.config(bg="#FFF9E6")  # Soft yellow background

# Title with fun emoji
title_label = tk.Label(root,
                       text="🎲 Odd or Even Explorer! 🎲",
                       font=("Comic Sans MS", 20, "bold"),
                       bg="#FFF9E6",
                       fg="#FF6B35")
title_label.pack(pady=20)

# Instruction text
instruction = tk.Label(root,
                      text="Type a number and discover if it's odd or even!",
                      font=("Comic Sans MS", 11),
                      bg="#FFF9E6",
                      fg="#555555")
instruction.pack(pady=5)

# Input Field
entry = tk.Entry(root,
                 font=("Comic Sans MS", 26, "bold"),
                 width=8,
                 justify='center',
                 bd=4,
                 relief="solid",
                 bg="#FFFFFF",
                 fg="#FF6B35")
entry.pack(pady=15)

# Colorful Button
check_btn = tk.Button(root,
                      text="🔍 Find Out!",
                      font=("Comic Sans MS", 16, "bold"),
                      bg="#7FD8BE",
                      fg="#FFFFFF",
                      activebackground="#6BC7AD",
                      padx=30,
                      pady=10,
                      bd=3,
                      relief="raised",
                      command=check_odd_even)
check_btn.pack(pady=15)

# Result Label
result_label = tk.Label(root,
                        text="Ready to explore? 🚀",
                        font=("Comic Sans MS", 18, "bold"),
                        bg="#FFF9E6",
                        fg="#FF6B35")
result_label.pack(pady=15)

# Fun fact label
fun_fact = tk.Label(root,
                   text="",
                   font=("Comic Sans MS", 11),
                   bg="#FFF9E6",
                   fg="#666666",
                   wraplength=380)
fun_fact.pack(pady=5)

# Visual examples
examples = tk.Label(root,
                   text="💡 Examples: 2, 4, 6 are EVEN • 1, 3, 5 are ODD",
                   font=("Comic Sans MS", 10),
                   bg="#FFF9E6",
                   fg="#999999")
examples.pack(pady=10)

# Footer
footer = tk.Label(root,
                 text="🌟 Tip: Even numbers end in 0, 2, 4, 6, or 8!",
                 font=("Comic Sans MS", 9),
                 bg="#FFF9E6",
                 fg="#999999")
footer.pack(side="bottom", pady=10)

root.mainloop()