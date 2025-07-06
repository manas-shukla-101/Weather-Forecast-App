import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class WeatherCard(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, style='Card.TFrame')
        self.pack_propagate(False)
        
        # Store references to images to prevent garbage collection
        self.default_icon = None
        self.sunrise_img = None
        self.sunset_img = None
        
        self._setup_ui()
        self._load_icons()
    
    def _setup_ui(self):
        # Location and time
        self.location_label = ttk.Label(self, style='Header.TLabel')
        self.location_label.pack(pady=(20, 5))
        
        self.time_label = ttk.Label(self, style='Secondary.TLabel')
        self.time_label.pack()
        
        # Weather icon and temperature
        self.weather_icon_frame = ttk.Frame(self)
        self.weather_icon_frame.pack(pady=20)
        
        self.weather_icon = tk.Label(self.weather_icon_frame)
        self.weather_icon.pack(side=tk.LEFT, padx=10)
        
        self.temp_label = ttk.Label(self.weather_icon_frame, style='Temp.TLabel')
        self.temp_label.pack(side=tk.LEFT, padx=10)
        
        self.degree_label = ttk.Label(
            self.weather_icon_frame, 
            text="°C", 
            font=('Segoe UI', 24), 
            foreground='#2c3e50'
        )
        self.degree_label.pack(side=tk.LEFT, pady=(20, 0))
        
        # Weather details
        self.condition_label = ttk.Label(self, style='Data.TLabel')
        self.condition_label.pack()
        
        self.feels_like_label = ttk.Label(self, style='Secondary.TLabel')
        self.feels_like_label.pack()
        
        # Sun times
        self.sun_frame = ttk.Frame(self)
        self.sun_frame.pack(fill=tk.X, pady=10)
        
        self.sunrise_icon = tk.Label(self.sun_frame, image=self.sunrise_img)
        self.sunrise_icon.pack(side=tk.LEFT, padx=10)
        
        self.sunrise_label = ttk.Label(self.sun_frame, style='Data.TLabel')
        self.sunrise_label.pack(side=tk.LEFT, padx=10)
        
        self.sunset_icon = tk.Label(self.sun_frame, image=self.sunset_img)
        self.sunset_icon.pack(side=tk.LEFT, padx=30)
        
        self.sunset_label = ttk.Label(self.sun_frame, style='Data.TLabel')
        self.sunset_label.pack(side=tk.LEFT, padx=10)
    
    def _load_icons(self):
        try:
            self.default_icon = self._resize_image("assets/icons/main.png", 150, 150)
            self.sunrise_img = self._resize_image("assets/images/sunrise.png", 30, 30)
            self.sunset_img = self._resize_image("assets/images/sunset.png", 30, 30)
            self.weather_icon.config(image=self.default_icon)
        except Exception as e:
            print(f"Error loading icons: {e}")
            # Create blank images if the files aren't found
            blank_img = Image.new('RGBA', (150, 150), (0, 0, 0, 0))
            self.default_icon = ImageTk.PhotoImage(blank_img)
            blank_small = Image.new('RGBA', (30, 30), (0, 0, 0, 0))
            self.sunrise_img = ImageTk.PhotoImage(blank_small)
            self.sunset_img = ImageTk.PhotoImage(blank_small)
            self.weather_icon.config(image=self.default_icon)
    
    def _resize_image(self, path, width, height):
        try:
            img = Image.open(path)
            img = img.resize((width, height), Image.LANCZOS)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error loading image {path}: {e}")
            blank_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
            return ImageTk.PhotoImage(blank_img)
    
    def update(self, weather_data):
        self.location_label.config(text=f"{weather_data.city}, {weather_data.country}")
        self.temp_label.config(text=f"{weather_data.temperature:.1f}")
        self.condition_label.config(text=weather_data.condition)
        self.feels_like_label.config(text=f"Feels like {weather_data.feels_like:.1f}°C")
        self.sunrise_label.config(text=f"Sunrise: {weather_data.sunrise}")
        self.sunset_label.config(text=f"Sunset: {weather_data.sunset}")
        self.time_label.config(text=weather_data.last_updated.strftime("%A, %B %d %I:%M %p"))
        
        try:
            icon_path = f"assets/icons/{self._get_icon_name(weather_data.icon_code)}"
            img = self._resize_image(icon_path, 150, 150)
            self.weather_icon.config(image=img)
            self.weather_icon.image = img  # Keep reference to prevent garbage collection
        except Exception as e:
            print(f"Error updating weather icon: {e}")
            self.weather_icon.config(image=self.default_icon)
    
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