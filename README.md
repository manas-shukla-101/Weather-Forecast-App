# 🌤️ Weather Forecast Pro

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)

**Weather Forecast Pro** is a modern, modular Python application that provides a sleek interface for real-time weather tracking. Powered by the **AccuWeather API**, it offers detailed current conditions and a comprehensive 5-day forecast.

## ✨ Key Features

* **Real-time Data:** Get current temperature, humidity, wind speed, and pressure.
* **5-Day Forecast:** Plan ahead with a detailed daily weather breakdown.
* **Visual Analytics:** View weather trends in a clean, graphical format.
* **Location Management:** Save your favorite cities for instant access.
* **Data Export:** Save weather reports to CSV/Text files for later reference.
* **Responsive GUI:** Built with Tkinter and Pillow for a polished user experience.

---

## 🛠️ Built With

The project leverages the following technologies:

- **Language:** Python 3.x
- **GUI:** Tkinter, Pillow (PIL)
- **Networking:** Requests, JSON
- **Data:** CSV, Datetime, ConfigParser
- **API:** [AccuWeather API](https://developer.accuweather.com/)

## Steps to use:

Step 1: Install the required libraries in requirements.txt file.
Step 2: Run the script using python weather_forecast.py.
Step 3: Enter the city name when prompted.
Step 4: The script will display the current weather and forecast for the next 5 days.
Step 5: The script will also display the temperature and humidity for each day.
Step 6: The script will also display the wind speed and direction for each day.
Step 7: The script will also display the pressure and visibility for each day.
Step 8: The script will also display the sunrise and sunset time for each day.
Step 9: We can refresh the data by clicking on the refresh button.
Step 10: We can save the location by clicking on the save button.

## Project structure:
```text
Weather Forcast Pro/
│
├── main.py
├── config.ini
├── requirements.txt
├── README.md
│
├── models/
│   ├── __init__.py
│   └── weather_data.py
│
├── services/
│   ├── __init__.py
│   ├── weather_service.py
│   └── file_service.py
│
├── ui/
│   ├── __init__.py
│   ├── main_window.py
│   └── components/
│       ├── __init__.py
│       ├── forecast_card.py
│       ├── weather_card.py
│       └── search_bar.py
│
├── utils/
│   ├── __init__.py
│   ├── constants.py
│   └── helpers.py
│
└── assets/
    ├── icons/
    │   ├── clear.png
    │   ├── cloudy.png
    │   ├── main.png
    │   └── ... (all other icons)
    └── images/
        ├── sunrise.png
        ├── sunset.png
        └── ... (other images)
```

## 🤔Why?

The project is designed to be modular and easy to maintain. Each module has its own responsibilities and is loosely coupled to other modules. This makes it easy to add or remove features without affecting the rest of the application.

## 🪜Steps to obtain own API key:

 1. Go to [AccuWeather](https://developer.accuweather.com/) and sign up for an API key.
 2. Replace `YOUR_API_KEY` in `config.ini` with your actual API key.
 3. Run the application using
```bash
python main.py.
```
 5. If you encounter any issues, refer to the [README.md](README.md) file for troubleshooting tips.

## ⚙️Troubleshooting tips:

 1. Make sure you have the correct API key in `config.ini`.
 2. Check the console output for any error messages.
 3. If you're using a virtual environment, make sure it's activated before running the application.
 4. If you're still having issues, try running the application with the `--debug` flag to enable debug mode.
 5. If you're using a different operating system, make sure the application is compatible with it.
 6. If you're using a different Python version, make sure it's compatible with the application.
 7. If you're still having issues, try reinstalling the application or seeking help from a developer.
 8. If you're still having issues, try checking the [AccuWeather API documentation](https://developer.accuweather.com/) for any changes or updates.
 9. If you're still having issues, then you can try to contact me.


## 📱Contact:

 If you have any questions or need further assistance, feel free to contact me at [Email](shuklamanas8928@gmail.com) (Only if very important).


## 📃License:

 This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.


## ⭕Acknowledgments:

I would like to thank my family and friends for their support and encouragement. I would also like to thank my colleagues and mentors for their guidance and advice. I would like to thank the open-source community for their contributions and feedback. I would like to thank the developers of the libraries and frameworks used in this project for their contributions and maintenance. Thanks to [AccuWeather](https://developer.accuweather.com/) for providing the API and documentation. Thanks to [Python](https://www.python.org/) for providing the programming language. Thanks to [Visual Studio Code](https://code.visualstudio.com/) for providing the code editor. Thanks to [GitHub](https://github.com/) for providing the version control system. Thank You!


## 🕵️‍♀️Project details:
```Details
 Name: Weather Forecast App
 Start: 2025-07-06
 End: 2025-07-06
 API: AccuWeather
 Platform: Python
 Code-Editor: Visual Studio Code
 Help: AI
 Contact: shuklamanas8928@gmail.com
 Contribution: None

 Licence: MIT
 ```
