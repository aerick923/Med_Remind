# SECTION: TW21
# LEADER: Aerick Lee P. Alba
# MEMBERS:
# Cordero, Jose III
# De Guia, Jonash
# Lising, Romar 

import tkinter as tk
from ui.login import show_login 

root = tk.Tk()
root.title("MedRemind")
root.geometry("400x500")

show_login(root)

root.mainloop()