# SECTION: TW21
# LEADER: Aerick Lee P. Alba
# MEMBERS:
# Cordero, Jose III
# De Guia, Jonash
# Lising, Romar 

import tkinter as tk
from tkinter import messagebox
from auth import register_user
from ui.login import show_login

def open_signup(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Signup").pack()

    entry_user = tk.Entry(root)
    entry_user.pack()

    entry_pass = tk.Entry(root, show="*")
    entry_pass.pack()

    def signup():
        username = entry_user.get()
        password = entry_pass.get()

        if not username or not password:
            messagebox.showerror("Error", "All fields required")
            return

        register_user(username, password)
        messagebox.showinfo("Success", "Account created!")
        show_login(root)

    tk.Button(root, text="Create Account", command=signup).pack()
    tk.Button(root, text="Back to Login", command=lambda: show_login(root)).pack()