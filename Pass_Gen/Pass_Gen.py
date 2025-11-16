import tkinter as tk
import random
import string
import pyperclip
from tkinter import messagebox

# --- Functions ---
def generate_password():
    length_input = length_entry.get().strip()
    if not length_input.isdigit() or int(length_input) <= 0:
        messagebox.showerror("Error", "Please enter a valid positive number for password length.")
        return
    length = int(length_input)

    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_numbers = numbers_var.get()
    use_special = special_var.get()

    if not (use_upper or use_lower or use_numbers or use_special):
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    password = password_var.get()
    if password:
        pyperclip.copy(password)

def clear_password():
    password_var.set("")

def check_password_box(*args):
    if password_var.get():
        copy_button.config(state="normal")
    else:
        copy_button.config(state="disabled")

# --- Main window ---
root = tk.Tk()
root.title("Password Generator")
root.resizable(False, False)

# --- Length Frame ---
length_frame = tk.Frame(root)
length_frame.pack(pady=5)
tk.Label(length_frame, text="Password Length:").pack(side='left')
length_entry = tk.Entry(length_frame, width=5)
length_entry.pack(side='left')

# --- Character Types ---
char_frame = tk.Frame(root)
char_frame.pack(pady=5)
upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
special_var = tk.BooleanVar()

tk.Checkbutton(char_frame, text="Uppercase Letters (A-Z)", variable=upper_var).pack(anchor='w')
tk.Checkbutton(char_frame, text="Lowercase Letters (a-z)", variable=lower_var).pack(anchor='w')
tk.Checkbutton(char_frame, text="Numbers (0-9)", variable=numbers_var).pack(anchor='w')
tk.Checkbutton(char_frame, text="Special Characters (!,@,#, etc.)", variable=special_var).pack(anchor='w')

# --- Generate Button ---
tk.Button(root, text="Generate Password", command=generate_password, width=20).pack(pady=10)

# --- Password Output Frame ---
output_frame = tk.Frame(root)
output_frame.pack(pady=15)

# Label + Clear button
output_top_frame = tk.Frame(output_frame)
output_top_frame.pack(fill='x', padx=30)
tk.Label(output_top_frame, text="Generated Password:").pack(side='left')
tk.Button(output_top_frame, text="Clear", command=clear_password, width=6).pack(side='right', padx=5, pady=2)

# Password Entry
password_var = tk.StringVar()
password_entry = tk.Entry(output_frame, width=20, font=('Arial', 18, 'bold'),
                          justify='center', textvariable=password_var)
password_entry.pack(fill='x', padx=30)

# Copy Button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, width=20, state='disabled')
copy_button.pack(pady=5)

# --- Trace password box for enabling/disabling copy button ---
password_var.trace_add('write', check_password_box)

root.mainloop()
