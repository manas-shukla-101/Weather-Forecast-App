"Made by manas-shukla-101"

import tkinter as tk
from tkinter import ttk, messagebox
from services.weather_service import WeatherService
from services.file_service import FileService
from ui.components.search_bar import SearchBar
from ui.components.weather_card import WeatherCard
from ui.components.forecast_card import ForecastCard

class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather Forecast Pro")
        self.geometry("1200x800")
        self.resizable(False, False)
        
        self.weather_service = WeatherService()
        self.file_service = FileService()
        
        self._setup_ui()
        self._load_default_weather()
    
    def _setup_ui(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Search bar
        self.search_bar = SearchBar(self.main_frame, self._on_search)
        self.search_bar.pack(fill=tk.X, pady=(0, 20))
        
        # Weather display
        self.weather_display = ttk.Frame(self.main_frame)
        self.weather_display.pack(fill=tk.BOTH, expand=True)
        
        # Current weather
        self.weather_card = WeatherCard(self.weather_display)
        self.weather_card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 20))
        
        # Forecast
        self.forecast_frame = ttk.Frame(self.weather_display)
        self.forecast_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.forecast_cards = []
        for i in range(5):
            card = ForecastCard(self.forecast_frame)
            card.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=(0, 10))
            self.forecast_cards.append(card)
        
        # Buttons
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(fill=tk.X, pady=(20, 0))
        
        ttk.Button(self.button_frame, text="Refresh", command=self._on_refresh).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Save to CSV", command=self._on_save).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Exit", command=self.destroy).pack(side=tk.RIGHT, padx=5)
    
    def _load_default_weather(self):
        self._on_search("London")
    
    def _on_search(self, city):
        try:
            weather, forecast = self.weather_service.get_weather(city)
            self.weather_card.update(weather)
            
            for i, day in enumerate(forecast[:5]):
                self.forecast_cards[i].update(day)
                
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def _on_refresh(self):
        city = self.search_bar.get_search_text()
        if city:
            self._on_search(city)
    
    def _on_save(self):
        try:
            if not self.weather_service.cached_data:
                raise RuntimeError("No weather data to save")
            
            self.file_service.save_to_csv(
                self.weather_service.cached_data['weather'],
                self.weather_service.cached_data['forecast']
            )
        except Exception as e:
            messagebox.showerror("Error", str(e))
