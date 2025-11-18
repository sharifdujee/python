import tkinter as tk
import random

# Game variables
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10


# Celebration bubbles
def create_celebration():
    """Create floating celebration bubbles from top to bottom"""
    colors = ["#FFD700", "#FF69B4", "#00CED1", "#FF6347", "#32CD32", "#FF1493", "#FFA500", "#9370DB","#FFD700", "#FF69B4", "#00CED1", "#FF6347", "#32CD32", "#FF1493", "#FFA500", "#9370DB"]
    emojis = ["🎉", "⭐", "🎊", "🏆", "🌟", "💫", "✨", "🎈", "🎁", "👏", "🌈", "🦄", "🍭", "🎪", "🎉", "⭐", "🎊", "🏆","🌟", "💫", "✨", "🎈", "🎁", "👏", "🌈", "🦄", "🍭", "🎪"]

    # Create 30 bubbles for more excitement
    for i in range(30):
        x = random.randint(20, 480)
        y = random.randint(-100, -20)  # Start from above the window

        # Create bubble label with larger emojis
        bubble = tk.Label(root,
                          text=random.choice(emojis),
                          font=("Arial", random.randint(25, 45)),
                          bg="#E8F5E9",
                          fg=random.choice(colors))
        bubble.place(x=x, y=y)

        # Animate bubble falling down with delay
        delay = random.randint(0, 1500)
        root.after(delay, lambda b=bubble, start_y=y: animate_bubble(b, start_y))


def animate_bubble(bubble, start_y):
    """Animate bubble falling downward"""
    current_y = start_y

    def move():
        nonlocal current_y
        if current_y < 600:
            current_y += random.randint(3, 8)  # Random falling speed
            bubble.place(y=current_y)
            root.after(30, move)
        else:
            bubble.destroy()

    move()

    # Auto-destroy after 5 seconds
    root.after(5000, lambda: bubble.destroy() if bubble.winfo_exists() else None)


def check_guess():
    global attempts

    try:
        guess = int(entry.get())
    except ValueError:
        result_label.config(text="Oops! Please enter a number! 🤔", fg="#ff6b9d")
        return

    if guess < 1 or guess > 100:
        result_label.config(text="Pick a number between 1 and 100! 🎯", fg="#ff6b9d")
        return

    attempts += 1
    attempts_label.config(text=f"🎮 Attempts: {attempts}/{max_attempts}")

    if guess == secret_number:
        result_label.config(text=f"🎉 YOU WON! The number was {secret_number}!", fg="#00d084")
        hint_label.config(text=f"Amazing! You did it in {attempts} tries! 🏆")
        check_btn.config(state="disabled")
        entry.config(state="disabled")
        create_celebration()  # Trigger celebration bubbles!
    elif attempts >= max_attempts:
        result_label.config(text=f"😅 Game Over! It was {secret_number}!", fg="#ff6b9d")
        hint_label.config(text="Don't worry! Click 'New Game' to try again!")
        check_btn.config(state="disabled")
        entry.config(state="disabled")
    elif guess < secret_number:
        result_label.config(text="📈 Too Low! Go Higher!", fg="#FFB84D")
        hint_label.config(text="The secret number is bigger! Keep trying! 💪")
    else:
        result_label.config(text="📉 Too High! Go Lower!", fg="#4A90E2")
        hint_label.config(text="The secret number is smaller! You can do it! 🌟")

    entry.delete(0, tk.END)


def new_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    attempts_label.config(text=f"🎮 Attempts: {attempts}/{max_attempts}")
    result_label.config(text="Ready to play? Make your first guess! 🚀", fg="#8B4789")
    hint_label.config(text="I'm thinking of a number between 1 and 100...")
    check_btn.config(state="normal")
    entry.config(state="normal")
    entry.delete(0, tk.END)
    entry.focus()


# UI Setup
root = tk.Tk()
root.title("🎯 Guess the Number Game!")
root.geometry("500x550")
root.resizable(False, False)
root.config(bg="#E8F5E9")  # Light green background

# Title
title_label = tk.Label(root,
                       text="🎯 Guess the Number! 🎯",
                       font=("Comic Sans MS", 22, "bold"),
                       bg="#E8F5E9",
                       fg="#2E7D32")
title_label.pack(pady=20)

# Game instructions
instruction = tk.Label(root,
                       text="I'm thinking of a number between 1 and 100!\nCan you guess it in 10 tries?",
                       font=("Comic Sans MS", 12),
                       bg="#E8F5E9",
                       fg="#555555",
                       justify="center")
instruction.pack(pady=10)

# Attempts counter
attempts_label = tk.Label(root,
                          text=f"🎮 Attempts: {attempts}/{max_attempts}",
                          font=("Comic Sans MS", 14, "bold"),
                          bg="#E8F5E9",
                          fg="#FF6B35")
attempts_label.pack(pady=10)

# Input Field
entry = tk.Entry(root,
                 font=("Comic Sans MS", 24, "bold"),
                 width=8,
                 justify='center',
                 bd=4,
                 relief="solid",
                 bg="#FFFFFF",
                 fg="#2E7D32")
entry.pack(pady=15)
entry.focus()

# Button Frame
button_frame = tk.Frame(root, bg="#E8F5E9")
button_frame.pack(pady=10)

# Guess Button
check_btn = tk.Button(button_frame,
                      text="🔍 Guess!",
                      font=("Comic Sans MS", 14, "bold"),
                      bg="#66BB6A",
                      fg="#FFFFFF",
                      activebackground="#4CAF50",
                      padx=25,
                      pady=8,
                      bd=3,
                      relief="raised",
                      command=check_guess)
check_btn.pack(side="left", padx=10)

# New Game Button
new_game_btn = tk.Button(button_frame,
                         text="🔄 New Game",
                         font=("Comic Sans MS", 14, "bold"),
                         bg="#FFB74D",
                         fg="#FFFFFF",
                         activebackground="#FFA726",
                         padx=20,
                         pady=8,
                         bd=3,
                         relief="raised",
                         command=new_game)
new_game_btn.pack(side="left", padx=10)

# Result Label
result_label = tk.Label(root,
                        text="Ready to play? Make your first guess! 🚀",
                        font=("Comic Sans MS", 16, "bold"),
                        bg="#E8F5E9",
                        fg="#8B4789",
                        wraplength=450)
result_label.pack(pady=20)

# Hint Label
hint_label = tk.Label(root,
                      text="I'm thinking of a number between 1 and 100...",
                      font=("Comic Sans MS", 12),
                      bg="#E8F5E9",
                      fg="#666666",
                      wraplength=450)
hint_label.pack(pady=10)

# Footer Tips
footer = tk.Label(root,
                  text="💡 Tip: Start with 50 and use the hints to narrow it down!",
                  font=("Comic Sans MS", 9),
                  bg="#E8F5E9",
                  fg="#999999",
                  wraplength=450)
footer.pack(side="bottom", pady=15)

# Bind Enter key to check guess
root.bind('<Return>', lambda event: check_guess())

root.mainloop()