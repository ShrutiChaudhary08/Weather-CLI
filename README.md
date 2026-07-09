# CLI Weather App

A simple Python command-line tool that fetches real-time weather data for any city. It converts a city name into coordinates using the OpenStreetMap Nominatim API, then retrieves current weather conditions from the Open-Meteo API. No API key required.

## Features

- Converts a city name into latitude/longitude coordinates
- Fetches current temperature, windspeed, and weather condition
- Translates weather codes into human-readable descriptions
- Handles invalid cities, timeouts, and network errors gracefully

## Requirements

- Python 3
- `requests` library

Install dependencies:
```bash
pip install requests
```

## Usage

Run the script and enter a city name when prompted:

```bash
python weather.py
Enter City: London
```

Example output:
```
Temperature: 18.4°C
Windspeed: 11.2 km/h
Condition: Partly cloudy
```
