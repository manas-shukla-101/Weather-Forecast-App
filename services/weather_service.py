import configparser
import requests
from time import time
from datetime import datetime
from models.weather_data import WeatherData, ForecastData

class WeatherService:
    def __init__(self):
        self.last_api_call = 0
        self.cached_data = {}
        self._load_config()
    
    def _load_config(self):
        """Load configuration with error handling"""
        try:
            config = configparser.ConfigParser()
            config.read("config.ini")
            self.api_key = config['AccuWeather']['api']
            if not self.api_key or self.api_key == "YOUR_API_KEY_HERE":
                raise ValueError("Invalid API key in config.ini")
        except Exception as e:
            raise RuntimeError(f"Configuration error: {str(e)}")

    def get_weather(self, city):
        """Main method to get weather data"""
        if not city or not isinstance(city, str):
            raise ValueError("Invalid city name")
        
        try:
            # Check cache first
            if self._should_use_cache(city):
                return self.cached_data['weather'], self.cached_data['forecast']
            
            # Get fresh data
            location_data = self._get_location_data(city)
            current = self._get_current_weather(location_data)
            forecast = self._get_forecast(location_data['key'])
            
            # Update cache
            self._update_cache(city, location_data, current, forecast)
            return current, forecast
            
        except requests.exceptions.RequestException as e:
            # Try to use cached data if available
            if self.cached_data.get('location') == city:
                return self.cached_data['weather'], self.cached_data['forecast']
            raise RuntimeError(f"Network error: {str(e)}")
        except Exception as e:
            if self.cached_data.get('location') == city:
                return self.cached_data['weather'], self.cached_data['forecast']
            raise RuntimeError(f"Weather data fetch failed: {str(e)}")

    def _should_use_cache(self, city):
        """Check if cached data is valid and complete"""
        return (time() - self.last_api_call < 600 and 
                self.cached_data.get('location') == city and
                'weather' in self.cached_data and
                'forecast' in self.cached_data)

    def _get_location_data(self, city):
        """Get location data including city/country info"""
        url = f"https://dataservice.accuweather.com/locations/v1/cities/search?apikey={self.api_key}&q={city}"
        response = requests.get(url)
        
        if response.status_code == 503:
            raise RuntimeError("API limit exceeded or invalid key")
        
        response.raise_for_status()
        
        data = response.json()
        if not data:
            raise ValueError("Location not found")
        
        return {
            'key': data[0]['Key'],
            'city': data[0]['LocalizedName'],
            'country': data[0]['Country']['LocalizedName'],
            'timezone': data[0].get('TimeZone', {}).get('Name', 'UTC')
        }

    def _get_current_weather(self, location_data):
        """Get current weather using location data"""
        url = f"https://dataservice.accuweather.com/currentconditions/v1/{location_data['key']}?apikey={self.api_key}&details=true"
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()[0]
        
        # Get sun times from daily forecast
        sunrise, sunset = self._get_sun_times(location_data['key'])
        
        return WeatherData(
            city=location_data['city'],
            country=location_data['country'],
            temperature=data['Temperature']['Metric']['Value'],
            feels_like=data['RealFeelTemperature']['Metric']['Value'],
            condition=data['WeatherText'],
            humidity=data['RelativeHumidity'],
            pressure=data['Pressure']['Metric']['Value'],
            visibility=data['Visibility']['Metric']['Value'],
            wind_speed=data['Wind']['Speed']['Metric']['Value'],
            wind_direction=data['Wind']['Direction']['Localized'],
            icon_code=data['WeatherIcon'],
            sunrise=sunrise,
            sunset=sunset
        )

    def _get_sun_times(self, location_key):
        """Get sunrise/sunset times from daily forecast"""
        try:
            url = f"https://dataservice.accuweather.com/forecasts/v1/daily/1day/{location_key}?apikey={self.api_key}&details=true"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            # Check if the expected data exists in the response
            if not data.get('DailyForecasts') or not data['DailyForecasts'][0].get('Sun'):
                raise KeyError("Sun data not available in API response")
                
            sunrise = datetime.strptime(
                data['DailyForecasts'][0]['Sun']['Rise'], 
                "%Y-%m-%dT%H:%M:%S%z"
            ).strftime("%I:%M %p")
            
            sunset = datetime.strptime(
                data['DailyForecasts'][0]['Sun']['Set'], 
                "%Y-%m-%dT%H:%M:%S%z"
            ).strftime("%I:%M %p")
            
            return sunrise, sunset
        except Exception as e:
            print(f"Error getting sun times: {e}")
            # Fallback to reasonable defaults based on current time
            now = datetime.now()
            # Adjust sunrise/sunset based on season (simple approximation)
            if 3 <= now.month <= 9:  # Spring/Summer
                sunrise = "6:00 AM"
                sunset = "8:00 PM"
            else:  # Fall/Winter
                sunrise = "7:00 AM"
                sunset = "5:00 PM"
            return sunrise, sunset

    def _get_forecast(self, location_key):
        """Get 5-day forecast data"""
        url = f"https://dataservice.accuweather.com/forecasts/v1/daily/5day/{location_key}?apikey={self.api_key}&details=true&metric=true"
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        forecasts = []
        for day in data['DailyForecasts']:
            forecasts.append(ForecastData(
                date=day['Date'],
                day_condition=day['Day']['IconPhrase'],
                night_condition=day['Night']['IconPhrase'],
                max_temp=day['Temperature']['Maximum']['Value'],
                min_temp=day['Temperature']['Minimum']['Value'],
                day_precipitation=day['Day']['PrecipitationProbability'],
                night_precipitation=day['Night']['PrecipitationProbability'],
                icon_code=day['Day']['Icon']
            ))
        return forecasts

    def _update_cache(self, city, location_data, current, forecast):
        """Update cache with complete data set"""
        self.last_api_call = time()
        self.cached_data = {
            'location': city,
            'location_data': location_data,
            'weather': current,
            'forecast': forecast
        }