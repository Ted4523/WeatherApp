from time import strftime

import requests
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from datetime import datetime, tzinfo
from dateutil import tz

root = tk.Tk()
root.title("Weather App")
city_label = tk.Label(root, text="City:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()
fetch_button = tk.Button()

fetch_button = tk.Button(root,text="Fetch Weather")
fetch_button.pack()

weather_label = tk.Label(root, text= "")
weather_label.pack()

def fetch_weather():
    city = city_entry.get()
    api_key = "ccdf6e3a31e9acb25a240c006b0b0645"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        sunset = data["sys"]["sunset"]
        sunsettime = datetime.utcfromtimestamp(int(sunset)).strftime('%Y-%m-%d %H:%M:%S')
        utc = datetime.strptime(sunsettime, '%Y-%m-%d %H:%M:%S')
        utc = utc.replace(tzinfo=tz.gettz('UTC'))
        local = utc.astimezone(tz.tzlocal())
        weather = data["weather"][0]["description"]
        weather_label.config(text=f"Temperature: {temperature}°C\nWeather: {weather}\nWind Speed: {wind_speed}\nSunset: {local.hour}:{local.minute}")
    except Exception as e:
        messagebox.showerror("Error", "Unable to fetch weather data")


fetch_button.config(command=fetch_weather)

# Start the GUI main loop
root.mainloop()
