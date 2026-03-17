# SECTION: TW21
# LEADER: Aerick Lee P. Alba
# MEMBERS:
# Cordero, Jose III
# De Guia, Jonash
# Lising, Romar 

import tkinter as tk
from ui.login import show_login
from medication import add_med, get_meds, delete_med
from appointment import add_appointment, get_appointments, delete_appointment

def open_home(root, user_id):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Home").pack()

    # MEDICATION SECTION
    tk.Label(root, text="Medication").pack()

    name = tk.Entry(root)
    name.pack()

    dosage = tk.Entry(root)
    dosage.pack()

    time = tk.Entry(root)
    time.pack()

    def add_medication():
        add_med(user_id, name.get(), dosage.get(), time.get())

    tk.Button(root, text="Add Medication", command=add_medication).pack()

    def view_meds():
        meds = get_meds(user_id)
        print(meds)

    tk.Button(root, text="View Medications", command=view_meds).pack()

    # APPOINTMENT SECTION
    tk.Label(root, text="Appointments").pack()

    title = tk.Entry(root)
    title.pack()

    date = tk.Entry(root)
    date.pack()

    time2 = tk.Entry(root)
    time2.pack()

    def add_app():
        add_appointment(user_id, title.get(), date.get(), time2.get())

    tk.Button(root, text="Add Appointment", command=add_app).pack()

    def view_app():
        apps = get_appointments(user_id)
        print(apps)

    tk.Button(root, text="View Appointments", command=view_app).pack()

    tk.Button(root, text="Logout", command=lambda: show_login(root)).pack()