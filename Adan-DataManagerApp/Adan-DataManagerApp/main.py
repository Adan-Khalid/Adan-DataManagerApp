import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import customtkinter as ctk
import pandas as pd
import sqlite3

# -------------------------------
# Adan's Data Manager App v1.0
# -------------------------------

DB_FILE = "database/data_manager.db"

class DataManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Adan's Data Manager App v1.0")
        self.create_ui()
        self.setup_database()

    def create_ui(self):
        tab_control = ttk.Notebook(self.root)
        self.data_tab = ttk.Frame(tab_control)
        self.uploads_tab = ttk.Frame(tab_control)
        self.leads_tab = ttk.Frame(tab_control)
        self.trash_tab = ttk.Frame(tab_control)

        tab_control.add(self.data_tab, text="Data Sheet")
        tab_control.add(self.uploads_tab, text="Uploads")
        tab_control.add(self.leads_tab, text="Leads")
        tab_control.add(self.trash_tab, text="Trash")
        tab_control.pack(expand=1, fill="both")

        # Example label
        tk.Label(self.data_tab, text="Welcome to Adan's Data Manager").pack(pady=20)

    def setup_database(self):
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS records (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        email TEXT,
                        location TEXT
                    )''')
        conn.commit()
        conn.close()

if __name__ == "__main__":
    root = ctk.CTk()
    app = DataManagerApp(root)
    root.mainloop()
