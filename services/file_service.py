"Made by manas-shukla-101"

import csv
from tkinter import filedialog
from datetime import datetime

class FileService:
    def save_to_csv(self, weather_data, forecast_data):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            title="Save Weather Data As"
        )
        
        if not file_path:
            return
            
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            # Current weather
            writer = csv.writer(csvfile)
            writer.writerow(["Current Weather"])
            writer.writerow([
                "City", "Country", "Temperature (°C)", "Feels Like (°C)",
                "Condition", "Humidity (%)", "Pressure (hPa)", "Visibility (km)",
                "Wind Speed (km/h)", "Wind Direction", "Sunrise", "Sunset", "Last Updated"
            ])
            
            writer.writerow([
                weather_data.city,
                weather_data.country,
                weather_data.temperature,
                weather_data.feels_like,
                weather_data.condition,
                weather_data.humidity,
                weather_data.pressure,
                weather_data.visibility,
                weather_data.wind_speed,
                weather_data.wind_direction,
                weather_data.sunrise,
                weather_data.sunset,
                weather_data.last_updated.strftime("%Y-%m-%d %H:%M:%S")
            ])
            
            # Forecast
            csvfile.write("\n5-Day Forecast\n")
            writer.writerow([
                "Date", "Day Condition", "Night Condition", "Max Temp (°C)",
                "Min Temp (°C)", "Day Precip (%)", "Night Precip (%)"
            ])
            
            for day in forecast_data:
                writer.writerow([
                    day.date,
                    day.day_condition,
                    day.night_condition,
                    day.max_temp,
                    day.min_temp,
                    day.day_precipitation,
                    day.night_precipitation
                ])
