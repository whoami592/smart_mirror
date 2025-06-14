import tkinter as tk
from time import strftime
import requests
from datetime import datetime

# OpenWeatherMap API key and city (replace with your own API key)
API_KEY = "your_openweathermap_api_key_here"
CITY = "Islamabad"  # Default city, can be changed

# Function to get weather data
def get_weather():
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            return f"{temp}°C, {desc.capitalize()}"
        else:
            return "Weather data unavailable"
    except:
        return "Error fetching weather"

# Function to update time and date
def update_time():
    time_string = strftime("%H:%M:%S")
    date_string = datetime.now().strftime("%B %d, %Y")
    time_label.config(text=time_string)
    date_label.config(text=date_string)
    root.after(1000, update_time)  # Update every second

# Function to update weather
def update_weather():
    weather_string = get_weather()
    weather_label.config(text=weather_string)
    root.after(600000, update_weather)  # Update every 10 minutes

# Create main window
root = tk.Tk()
root.title("Smart Mirror by Mr Sabaz Ali Khan")
root.configure(bg="black")
root.attributes("-fullscreen", True)  # Full-screen mode

# Stylish banner
banner = """
   ╔════════════════════════════════════════════╗
   ║        SMART MIRROR PROJECT                ║
   ║   Coded by Pakistani Ethical Hacker        ║
   ║         Mr Sabaz Ali Khan                 ║
   ╚════════════════════════════════════════════╝
"""

# Create and configure banner label
banner_label = tk.Label(root, text=banner, font=("Courier", 14), fg="yellow", bg="black", justify="center")
banner_label.pack(pady=20)

# Create and configure time label
time_label = tk.Label(root, font=("Helvetica", 80), fg="white", bg="black")
time_label.pack(pady=20)

# Create and configure date label
date_label = tk.Label(root, font=("Helvetica", 30), fg="white", bg="black")
date_label.pack(pady=10)

# Create and configure weather label
weather_label = tk.Label(root, font=("Helvetica", 25), fg="white", bg="black")
weather_label.pack(pady=20)

# Start updating time and weather
update_time()
update_weather()

# Bind Escape key to exit full-screen
root.bind("<Escape>", lambda e: root.destroy())

# Start the main loop
root.mainloop()