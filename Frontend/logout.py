import tkinter as tk
from tkinter import messagebox

def logout(root):
    # Create a confirmation dialog
    confirmation = messagebox.askyesno("Logout Confirmation", "Are you sure you want to logout?")
    
    if confirmation: 
        root.destroy()
        exit()