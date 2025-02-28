import random
import tkinter as tk
from tkinter import messagebox

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = int(letter_entry.get())
    nr_symbols = int(symbol_entry.get())
    nr_numbers = int(number_entry.get())

    password_list = []

    for char in range(1, nr_letters + 1):
        password_list += random.choice(letters)

    for char in range(1, nr_symbols + 1):
        password_list += random.choice(symbols)

    for char in range(1, nr_numbers + 1):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("250x177")

tk.Label(root, text="Number of Letters:").grid(row=0, column=0)
letter_entry = tk.Entry(root)
letter_entry.grid(row=0, column=1)

tk.Label(root, text="Number of Symbols:").grid(row=1, column=0)
symbol_entry = tk.Entry(root)
symbol_entry.grid(row=1, column=1)

tk.Label(root, text="Number of Numbers:").grid(row=2, column=0)
number_entry = tk.Entry(root)
number_entry.grid(row=2, column=1,)

tk.Label(root, text="New Password:").grid(row=7, column=0)
password_entry = tk.Entry(root)
password_entry.grid(row=7, column=1)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=3, pady=10)

copy_button = tk.Button(root, text="Copy Password", command=copy_password)
copy_button.grid(row=8, column=0, columnspan=2, pady=10)

root.mainloop()
