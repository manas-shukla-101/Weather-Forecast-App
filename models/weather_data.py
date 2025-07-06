"Made by manas-shukla-101"

from dataclasses import dataclass
from datetime import datetime

@dataclass
class WeatherData:
    city: str
    country: str
    temperature: float
    feels_like: float
    condition: str
    humidity: int
    pressure: float
    visibility: float
    wind_speed: float
    wind_direction: str
    sunrise: str
    sunset: str
    icon_code: int = 1
    last_updated: datetime = None

    def __post_init__(self):
        if self.last_updated is None:
            self.last_updated = datetime.now()

@dataclass
class ForecastData:
    date: str
    day_condition: str
    night_condition: str
    max_temp: float
    min_temp: float
    day_precipitation: int
    night_precipitation: int
    icon_code: int
