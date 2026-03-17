# SECTION: TW21
# LEADER: Aerick Lee P. Alba
# MEMBERS:
# Cordero, Jose III
# De Guia, Jonash
# Lising, Romar 

import tkinter as tk
from tkinter import messagebox
from auth import login_user
from ui.signup import open_signup
from ui.home import open_home

def show_login(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Login").pack()

    entry_user = tk.Entry(root)
    entry_user.pack()

    entry_pass = tk.Entry(root, show="*")
    entry_pass.pack()

    def login():
        username = entry_user.get()
        password = entry_pass.get()

        if not username or not password:
            messagebox.showerror("Error", "All fields required")
            return

        user = login_user(username, password)
        if user:
            open_home(root, user[0])
        else:
            messagebox.showerror("Error", "Invalid credentials")

    tk.Button(root, text="Login", command=login).pack()
    tk.Button(root, text="Signup", command=lambda: open_signup(root)).pack()