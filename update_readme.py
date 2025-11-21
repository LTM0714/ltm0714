import requests

API_KEY = "YOUR_API_KEY"
CITY = "Seoul"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=kr"
data = requests.get(url).json()

weather = data["weather"][0]["description"]
temp = data["main"]["temp"]

weather_text = f"{CITY} 날씨: {temp}°C, {weather}"

content = content.replace("{{WEATHER}}", weather_text)
