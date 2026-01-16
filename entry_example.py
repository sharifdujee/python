import tkinter as tk
from tkinter import ttk, filedialog
import re, os, tempfile
import qrcode
from PIL import Image, ImageTk, ImageDraw

# ================= WINDOW =================
root = tk.Tk()
root.title("Shahidul Islam Academy – Junior School")
root.geometry("520x900")
root.resizable(False, False)
root.configure(bg="#f4f6fb")

# ================= MAIN CONTAINER =================
main = tk.Frame(root, bg="#f4f6fb")
main.pack(fill="both", expand=True)

# ================= STYLE =================
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#f4f6fb", font=("Segoe UI", 10))
style.configure("Card.TFrame", background="white")
style.configure("TButton", font=("Segoe UI", 10, "bold"))

# ================= STUDENT ID =================
counter = 1
def generate_id():
    global counter
    sid = f"SIA-JR-{counter:04d}"
    counter += 1
    return sid

student_id = generate_id()

# ================= HEADER =================
ttk.Label(main, text="Shahidul Islam Academy",
          font=("Segoe UI", 18, "bold")).pack(pady=(15, 3))
ttk.Label(main, text="Junior School • Student Registration",
          font=("Segoe UI", 11)).pack()

id_label = ttk.Label(main, text=f"Student ID: {student_id}",
                     font=("Segoe UI", 10, "bold"))
id_label.pack(pady=8)

# ================= SCHOOL LOGO UPLOAD =================
logo_img = None

def upload_logo():
    global logo_img
    path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )
    if not path:
        return

    img = Image.open(path).convert("RGBA").resize((90, 90), Image.LANCZOS)
    mask = Image.new("L", (90, 90), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 90, 90), fill=255)
    img.putalpha(mask)

    logo_img = ImageTk.PhotoImage(img)
    logo_label.config(image=logo_img, text="")

logo_label = ttk.Label(main, text="School Logo")
logo_label.pack(pady=6)
ttk.Button(main, text="Upload School Logo", command=upload_logo).pack()

# ================= FORM CARD =================
card = ttk.Frame(main, style="Card.TFrame", padding=20)
card.pack(padx=30, pady=15, fill="x")

def field(label, show=None):
    ttk.Label(card, text=label, background="white").pack(anchor="w", pady=(8, 2))
    e = ttk.Entry(card, show=show)
    e.pack(fill="x")
    return e

name_entry = field("Student Name")
email_entry = field("Email Address")
password_entry = field("Password", show="*")
confirm_entry = field("Confirm Password", show="*")
name_entry.focus()

# ================= STUDENT PHOTO UPLOAD (FIXED) =================
student_photo = None
photo_frame = ttk.Frame(card)
photo_frame.pack(anchor="w", pady=(10, 5), fill="x")

ttk.Label(photo_frame, text="Student Photo", background="white").pack(anchor="w", pady=(0,4))

photo_label = ttk.Label(photo_frame, text="No Photo", width=12)
photo_label.pack(anchor="w")

def upload_student_photo():
    global student_photo
    path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )
    if not path:
        return

    img = Image.open(path).convert("RGBA").resize((80, 100), Image.LANCZOS)
    student_photo = ImageTk.PhotoImage(img)
    photo_label.config(image=student_photo, text="")

ttk.Button(photo_frame, text="Upload Photo",
           command=upload_student_photo).pack(anchor="w", pady=5)

# ================= SHOW / HIDE PASSWORD =================
show_var = tk.BooleanVar()

def toggle_password():
    char = "" if show_var.get() else "*"
    password_entry.config(show=char)
    confirm_entry.config(show=char)

ttk.Checkbutton(card, text="Show Password",
                variable=show_var,
                command=toggle_password).pack(anchor="w", pady=5)

# ================= PASSWORD STRENGTH =================
strength_label = ttk.Label(card)
strength_label.pack(anchor="w")

def check_strength(event=None):
    p = password_entry.get()
    if len(p) < 4:
        strength_label.config(text="Weak Password", foreground="red")
    elif len(p) < 8:
        strength_label.config(text="Medium Password", foreground="orange")
    else:
        strength_label.config(text="Strong Password", foreground="green")

password_entry.bind("<KeyRelease>", check_strength)

# ================= STATUS =================
status_label = ttk.Label(main, font=("Segoe UI", 11, "bold"))
status_label.pack(pady=10)

# ================= EMAIL VALIDATION =================
def valid_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

# ================= PRINT SLIP WITH QR & PHOTO =================
def print_slip():
    slip = tk.Toplevel(root)
    slip.title("Registration Slip")
    slip.geometry("420x560")

    canvas = tk.Canvas(slip, width=400, height=520)
    canvas.pack(pady=10)

    canvas.create_text(200, 30, text="Shahidul Islam Academy",
                       font=("Segoe UI", 16, "bold"))
    canvas.create_text(200, 60, text="Junior School Registration Slip",
                       font=("Segoe UI", 11))
    canvas.create_line(20, 80, 380, 80)

    if student_photo:
        canvas.photo = student_photo
        canvas.create_image(330, 120, image=student_photo)

    y = 120
    for label, value in [
        ("Student ID", student_id),
        ("Name", name_entry.get()),
        ("Email", email_entry.get())
    ]:
        canvas.create_text(30, y, text=f"{label}:",
                           anchor="w", font=("Segoe UI", 10, "bold"))
        canvas.create_text(150, y, text=value,
                           anchor="w", font=("Segoe UI", 10))
        y += 30

    qr = qrcode.make(f"{student_id}|{name_entry.get()}|{email_entry.get()}")
    qr = qr.resize((110, 110))
    qr_img = ImageTk.PhotoImage(qr)
    canvas.qr_img = qr_img
    canvas.create_image(200, y + 90, image=qr_img)
    canvas.create_text(200, y + 160, text="Scan to Verify Student",
                       font=("Segoe UI", 9))

    canvas.create_line(20, y + 190, 380, y + 190)
    canvas.create_text(200, y + 220,
                       text="Authorized Signature",
                       font=("Segoe UI", 10))

    def send_to_printer():
        temp = tempfile.mktemp(".ps")
        canvas.postscript(file=temp)
        os.startfile(temp, "print")

    ttk.Button(slip, text="🖨 Print Slip",
               command=send_to_printer).pack(pady=10)

# ================= SUBMIT =================
def submit():
    global student_id

    if not valid_email(email_entry.get()):
        status_label.config(text="❌ Invalid email format", foreground="red")
        return

    if password_entry.get() != confirm_entry.get():
        status_label.config(text="❌ Passwords do not match", foreground="red")
        return

    status_label.config(text="✔ Registration Successful", foreground="green")
    print_slip()

    student_id = generate_id()
    id_label.config(text=f"Student ID: {student_id}")

    for e in (name_entry, email_entry, password_entry, confirm_entry):
        e.delete(0, tk.END)

# ================= BUTTON =================
ttk.Button(main, text="Register Student",
           command=submit).pack(pady=10)

# ================= FOOTER =================
footer = tk.Frame(root, bg="#f4f6fb")
footer.pack(side="bottom", fill="x")
ttk.Label(footer, text="© Shahidul Islam Academy",
          font=("Segoe UI", 9)).pack(pady=6)

root.mainloop()
