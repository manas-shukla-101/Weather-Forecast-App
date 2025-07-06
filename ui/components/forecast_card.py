import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime

class ForecastCard(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, style='Card.TFrame')
        self.pack_propagate(False)
        
        self._setup_ui()
        self._load_default_icon()
    
    def _setup_ui(self):
        self.day_label = ttk.Label(self, style='Data.TLabel')
        self.day_label.pack(pady=(10, 5))
        
        self.icon_label = tk.Label(self)
        self.icon_label.pack()
        
        self.temp_frame = ttk.Frame(self)
        self.temp_frame.pack(pady=5)
        
        self.max_temp_label = ttk.Label(self.temp_frame, style='Forecast.TLabel')
        self.max_temp_label.pack(side=tk.LEFT, padx=5)
        
        self.min_temp_label = ttk.Label(self.temp_frame, style='Forecast.TLabel')
        self.min_temp_label.pack(side=tk.LEFT, padx=5)
        
        self.condition_label = ttk.Label(self, style='Secondary.TLabel')
        self.condition_label.pack()
    
    def _load_default_icon(self):
        self.default_icon = self._resize_image("assets/icons/main.png", 50, 50)
        self.icon_label.config(image=self.default_icon)
    
    def _resize_image(self, path, width, height):
        img = Image.open(path)
        img = img.resize((width, height), Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    
    def update(self, forecast_data):
        date = datetime.strptime(forecast_data.date, "%Y-%m-%dT%H:%M:%S%z")
        self.day_label.config(text=date.strftime("%a, %b %d"))
        
        icon_path = f"assets/icons/{self._get_icon_name(forecast_data.icon_code)}"
        img = self._resize_image(icon_path, 50, 50)
        self.icon_label.config(image=img)
        self.icon_label.image = img
        
        self.max_temp_label.config(text=f"↑{forecast_data.max_temp:.1f}°")
        self.min_temp_label.config(text=f"↓{forecast_data.min_temp:.1f}°")
        self.condition_label.config(text=forecast_data.day_condition)
    
    def _get_icon_name(self, icon_code):
        icon_map = {
            1: "sunny.png",
            2: "cloudy.png",
            3: "clear.png",
            6: "stormy.png",
            7: "snow.png",
            12: "rain.png",
            14: "snow.png",
            18: "haze.png",
            22: "fog.png",
        }
        return icon_map.get(icon_code, "main.png")