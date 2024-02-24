
import requests
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from dateutil import tz
import ttkbootstrap as ttk

app = ttk.Window(themename="superhero")
app.geometry("600x500")
label = ttk.Label(app, text="Weather App")
label.pack(pady=30)
label.config(font=("Helvetica",20, "bold"))
app.title("Weather App")
cityframe = ttk.Frame(app)
cityframe.pack(pady=15, padx=10, fill="x")
ttk.Label(cityframe, text="City:").pack(side="left", padx=5)
cname = ttk.Entry(cityframe)
cname.pack(side="left", fill="x", expand=True, padx=5)
button_frame = ttk.Frame(app)
button_frame.pack(pady=50, padx=10, fill="x")
fetch = ttk.Button(button_frame, text="Submit", bootstyle="success")
fetch.pack(side="left", padx=10)
ttk.Button(button_frame, text="Cancel", bootstyle="danger").pack(side="left", padx=10)

weather_label = ttk.Label(app, text="")
weather_label.pack()









def fetch_weather():
    city = cname.get()
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
        weather_label.config(
            text=f"Temperature: {temperature}°C\nWeather: {weather}\n"
                 f"Wind Speed: {wind_speed}\nSunset: {local.hour}:{local.minute}\nHumidity: {humidity}")
    except Exception:
        messagebox.showerror("Error", "Unable to fetch weather data")


fetch.config(command=fetch_weather)

# Start the GUI main loop
app.mainloop()
