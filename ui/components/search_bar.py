"Made by manas-shukla-101"

import tkinter as tk
from tkinter import ttk

class SearchBar(ttk.Frame):
    def __init__(self, parent, search_callback):
        super().__init__(parent)
        self.search_callback = search_callback
        self._setup_ui()
    
    def _setup_ui(self):
        self.search_var = tk.StringVar()
        
        self.search_entry = ttk.Entry(
            self, 
            textvariable=self.search_var, 
            font=('Segoe UI', 12), 
            width=30
        )
        self.search_entry.pack(side=tk.LEFT, padx=(0, 10))
        
        self.search_btn = ttk.Button(
            self, 
            text="Search", 
            command=self._on_search
        )
        self.search_btn.pack(side=tk.LEFT)
        
        self.search_entry.bind("<Return>", lambda e: self._on_search())
    
    def _on_search(self):
        city = self.search_var.get().strip()
        if city:
            self.search_callback(city)
    
    def get_search_text(self):
        return self.search_var.get()
