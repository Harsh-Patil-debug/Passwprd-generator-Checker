import tkinter as tk
from tkinter import messagebox
import random
import string
import re


# Check password strength
def check_password():
    password = password_entry.get()

    if password == "":
        result_label.config(text="Please enter a password.", fg="#ff6b6b")
        strength_bar.config(width=0)
        update_requirements("")
        return

    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[0-9]", password):
        score += 1

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1

    # Classify password strength
    if score <= 2:
        result = "WEAK"
        result_color = "#ff5c5c"
        bar_width = 90
    elif score <= 4:
        result = "STRONG"
        result_color = "#ffb84d"
        bar_width = 180
    else:
        result = "EXCELLENT"
        result_color = "#42d392"
        bar_width = 270

    result_label.config(
        text=f"Password Strength: {result}",
        fg=result_color
    )

    strength_bar.config(
        width=bar_width,
        bg=result_color
    )

    update_requirements(password)


# Update password requirements
def update_requirements(password):

    if len(password) >= 8:
        length_label.config(text="✓ At least 8 characters", fg="#42d392")
    else:
        length_label.config(text="✗ At least 8 characters", fg="#888888")

    if re.search(r"[a-z]", password):
        lowercase_label.config(text="✓ Lowercase letter", fg="#42d392")
    else:
        lowercase_label.config(text="✗ Lowercase letter", fg="#888888")

    if re.search(r"[A-Z]", password):
        uppercase_label.config(text="✓ Uppercase letter", fg="#42d392")
    else:
        uppercase_label.config(text="✗ Uppercase letter", fg="#888888")

    if re.search(r"[0-9]", password):
        number_label.config(text="✓ Number", fg="#42d392")
    else:
        number_label.config(text="✗ Number", fg="#888888")

    if re.search(r"[^A-Za-z0-9]", password):
        special_label.config(text="✓ Special character", fg="#42d392")
    else:
        special_label.config(text="✗ Special character", fg="#888888")


# Generate a strong password
def suggest_password():

    length = random.randint(12, 16)

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    special = "!@#$%^&*"

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(numbers),
        random.choice(special)
    ]

    all_characters = lowercase + uppercase + numbers + special

    for i in range(length - 4):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    new_password = "".join(password)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, new_password)

    result_label.config(
        text="Password Strength: EXCELLENT",
        fg="#42d392"
    )

    strength_bar.config(
        width=270,
        bg="#42d392"
    )

    update_requirements(new_password)


# Show or hide password
def show_password():

    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        show_button.config(text="Hide")
    else:
        password_entry.config(show="*")
        show_button.config(text="Show")


# Copy password to clipboard
def copy_password():

    password = password_entry.get()

    if password == "":
        messagebox.showwarning(
            "No Password",
            "There is no password to copy."
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)

    messagebox.showinfo(
        "Copied",
        "Password copied to clipboard!"
    )


# Clear password
def clear_password():

    password_entry.delete(0, tk.END)

    result_label.config(
        text="Password Strength: -",
        fg="#aaaaaa"
    )

    strength_bar.config(width=0)

    update_requirements("")


# Create main window
root = tk.Tk()

root.title("Password Strength Checker")
root.geometry("700x650")
root.resizable(False, False)

BG_COLOR = "#10141c"
CARD_COLOR = "#181e29"
ENTRY_COLOR = "#222a38"
TEXT_COLOR = "#ffffff"
SECONDARY_TEXT = "#a9b1c1"
ACCENT_COLOR = "#6c63ff"

root.configure(bg=BG_COLOR)


# Create header
header_frame = tk.Frame(
    root,
    bg=BG_COLOR
)

header_frame.pack(pady=(30, 10))


title_label = tk.Label(
    header_frame,
    text="🔐 Password Security",
    font=("Arial", 26, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)

title_label.pack()


subtitle_label = tk.Label(
    header_frame,
    text="Check your password strength and generate a secure password",
    font=("Arial", 11),
    bg=BG_COLOR,
    fg=SECONDARY_TEXT
)

subtitle_label.pack(pady=8)


# Create main card
main_card = tk.Frame(
    root,
    bg=CARD_COLOR,
    width=600,
    height=430
)

main_card.pack(padx=50, pady=15)
main_card.pack_propagate(False)


password_title = tk.Label(
    main_card,
    text="Enter Password",
    font=("Arial", 12, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR
)

password_title.pack(
    anchor="w",
    padx=35,
    pady=(25, 8)
)


password_frame = tk.Frame(
    main_card,
    bg=CARD_COLOR
)

password_frame.pack(
    fill="x",
    padx=35
)


password_entry = tk.Entry(
    password_frame,
    font=("Arial", 14),
    bg=ENTRY_COLOR,
    fg=TEXT_COLOR,
    insertbackground=TEXT_COLOR,
    relief="flat",
    show="*"
)

password_entry.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=12,
    padx=(0, 8)
)


show_button = tk.Button(
    password_frame,
    text="Show",
    font=("Arial", 10, "bold"),
    bg="#30394a",
    fg=TEXT_COLOR,
    activebackground="#3d4759",
    activeforeground=TEXT_COLOR,
    relief="flat",
    width=8,
    cursor="hand2",
    command=show_password
)

show_button.pack(
    side="right",
    ipady=8
)


# Check password button
check_button = tk.Button(
    main_card,
    text="Check Password",
    font=("Arial", 11, "bold"),
    bg=ACCENT_COLOR,
    fg="white",
    activebackground="#574fd6",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=check_password
)

check_button.pack(
    pady=15,
    ipadx=30,
    ipady=7
)


result_label = tk.Label(
    main_card,
    text="Password Strength: -",
    font=("Arial", 15, "bold"),
    bg=CARD_COLOR,
    fg="#aaaaaa"
)

result_label.pack(pady=(0, 8))


# Create strength bar
strength_container = tk.Frame(
    main_card,
    bg="#303746",
    width=270,
    height=8
)

strength_container.pack()
strength_container.pack_propagate(False)


strength_bar = tk.Frame(
    strength_container,
    bg="#42d392",
    width=0,
    height=8
)

strength_bar.pack(side="left")


# Show password requirements
requirements_title = tk.Label(
    main_card,
    text="Password Requirements",
    font=("Arial", 11, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR
)

requirements_title.pack(
    anchor="w",
    padx=35,
    pady=(20, 5)
)


requirements_frame = tk.Frame(
    main_card,
    bg=CARD_COLOR
)

requirements_frame.pack(
    anchor="w",
    padx=35
)


length_label = tk.Label(
    requirements_frame,
    text="✗ At least 8 characters",
    font=("Arial", 10),
    bg=CARD_COLOR,
    fg="#888888"
)

length_label.grid(
    row=0,
    column=0,
    padx=(0, 35),
    pady=2,
    sticky="w"
)


lowercase_label = tk.Label(
    requirements_frame,
    text="✗ Lowercase letter",
    font=("Arial", 10),
    bg=CARD_COLOR,
    fg="#888888"
)

lowercase_label.grid(
    row=0,
    column=1,
    pady=2,
    sticky="w"
)


uppercase_label = tk.Label(
    requirements_frame,
    text="✗ Uppercase letter",
    font=("Arial", 10),
    bg=CARD_COLOR,
    fg="#888888"
)

uppercase_label.grid(
    row=1,
    column=0,
    padx=(0, 35),
    pady=2,
    sticky="w"
)


number_label = tk.Label(
    requirements_frame,
    text="✗ Number",
    font=("Arial", 10),
    bg=CARD_COLOR,
    fg="#888888"
)

number_label.grid(
    row=1,
    column=1,
    pady=2,
    sticky="w"
)


special_label = tk.Label(
    requirements_frame,
    text="✗ Special character",
    font=("Arial", 10),
    bg=CARD_COLOR,
    fg="#888888"
)

special_label.grid(
    row=2,
    column=0,
    padx=(0, 35),
    pady=2,
    sticky="w"
)


# Create bottom buttons
button_frame = tk.Frame(
    root,
    bg=BG_COLOR
)

button_frame.pack(pady=10)


suggest_button = tk.Button(
    button_frame,
    text="🎲 Generate Password",
    font=("Arial", 10, "bold"),
    bg="#30394a",
    fg=TEXT_COLOR,
    activebackground="#3d4759",
    activeforeground=TEXT_COLOR,
    relief="flat",
    cursor="hand2",
    command=suggest_password
)

suggest_button.grid(
    row=0,
    column=0,
    padx=5,
    ipadx=10,
    ipady=7
)


copy_button = tk.Button(
    button_frame,
    text="📋 Copy",
    font=("Arial", 10, "bold"),
    bg="#30394a",
    fg=TEXT_COLOR,
    activebackground="#3d4759",
    activeforeground=TEXT_COLOR,
    relief="flat",
    cursor="hand2",
    command=copy_password
)

copy_button.grid(
    row=0,
    column=1,
    padx=5,
    ipadx=10,
    ipady=7
)


clear_button = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 10, "bold"),
    bg="#30394a",
    fg=TEXT_COLOR,
    activebackground="#3d4759",
    activeforeground=TEXT_COLOR,
    relief="flat",
    cursor="hand2",
    command=clear_password
)

clear_button.grid(
    row=0,
    column=2,
    padx=5,
    ipadx=15,
    ipady=7
)


# Display footer
footer_label = tk.Label(
    root,
    text="Tip: Use a unique password with uppercase, lowercase, numbers and symbols.",
    font=("Arial", 9),
    bg=BG_COLOR,
    fg="#70798a"
)

footer_label.pack(pady=5)


# Start application
root.mainloop()