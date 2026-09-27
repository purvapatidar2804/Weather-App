import requests
city=input("enter city name: ")
print("you entered city",city)
url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

response = requests.get(url)
data = response.json()

latitude=data["results"][0]["latitude"]
longitude=data["results"][0]["longitude"]


if data["results"][0]["name"].lower() != city.lower():
    print("City not found.")
    exit()

# print(latitude)
# print(longitude)

weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"

weather_response = requests.get(weather_url)
weather_data = weather_response.json()

# print(weather_data)
temperature=weather_data["current"]["temperature_2m"]
humidity=weather_data["current"]["relative_humidity_2m"]
weather_code = weather_data["current"]["weather_code"]
wind_speed=weather_data["current"]["wind_speed_10m"]

weather_conditions = {
    0: "Clear Sky",
    1: "Mainly Clear",
    2: "Partly Cloudy",
    3: "Cloudy",
    45: "Foggy",
    48: "Foggy",
    51: "Light Drizzle",
    53: "Drizzle",
    55: "Heavy Drizzle",
    61: "Light Rain",
    63: "Rain",
    65: "Heavy Rain",
    71: "Light Snow",
    73: "Snow",
    75: "Heavy Snow",
    80: "Rain Showers",
    81: "Rain Showers",
    82: "Heavy Rain Showers",
    95: "Thunderstorm"
}



print("\n--- Weather Report ---")
print("City:", city)
print("Temperature:", temperature, "°C")
print("Humidity:", humidity, "%")
#gives weather condition corresponding to a given code and if not available gives unknown
print("Condition:", weather_conditions.get(weather_code, "Unknown"))
print("Wind Speed:", wind_speed, "km/h")