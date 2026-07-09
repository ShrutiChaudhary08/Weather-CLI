import requests
WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",

    45: "Fog",
    48: "Depositing rime fog",

    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",

    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",

    71: "Slight snowfall",
    73: "Moderate snowfall",
    75: "Heavy snowfall",
    77: "Snow grains",

    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",

    85: "Slight snow showers",
    86: "Heavy snow showers",

    95: "Thunderstorm (slight or moderate)",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail"
}
                
def get_coordinates(city):
    url="https://nominatim.openstreetmap.org/search"
    headers={
        "User-Agent":"MyWeatherApp/1.0",
        "Accept": "application/json"}
    try:
        response=requests.get(url, params={"q": city, "format":"json"}, headers=headers, timeout=10)
        response.raise_for_status()
        data=response.json()
        
        if not data:
            print("City not found")
            return None
        
        lat=float(data[0]["lat"])
        lon=float(data[0]["lon"])
        return lat, lon
    

    except requests.RequestException as e:
        print(f"Error fetching coordinates: {e}")
        return None
    


def fetch_weather(city):
    coords=get_coordinates(city)
    if not coords:
        return None
    lat, lon = coords
  
    url=f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    try:
        response=requests.get(url, timeout = 10.0)
        response.raise_for_status()
        data=response.json()

        weather=data.get("current_weather")
        if not weather:
            print("No data found")
            return None
        
        temp=weather.get("temperature")
        wind=weather.get("windspeed")
        condition=weather.get("weathercode")
        condition_text = WEATHER_CODES.get(condition, "Unknown")
        print(f"Temperature: {temp}°C")
        print(f"Windspeed: {wind} km/h")
        print(f"Condition: {condition_text}")

    except requests.RequestException as e:
        print(f"Error fetching Weather: {e}")
        return None
    
if __name__=="__main__":
    city=input("Enter City:")
    fetch_weather(city)