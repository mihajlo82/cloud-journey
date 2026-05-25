
#!/usr/bin/env python3
"""
Weather API client — fetches current weather for 3 cities.
Uses Open-Meteo API (free, no API key required).
"""

import requests
import sys
from datetime import datetime

# Lista gradova sa koordinatama
CITIES = [
    {"name": "Sarajevo", "lat": 43.85, "lon": 18.38},
    {"name": "Beograd",  "lat": 44.81, "lon": 20.46},
    {"name": "Zagreb",   "lat": 45.81, "lon": 15.98},
]

API_URL = "https://api.open-meteo.com/v1/forecast"
TIMEOUT = 10  # sekundi


def fetch_weather(city):
    """Dohvati trenutno vrijeme za grad. Vraća dict ili None ako greška."""
    params = {
        "latitude": city["lat"],
        "longitude": city["lon"],
        "current": "temperature_2m,wind_speed_10m,relative_humidity_2m,weather_code",
        "timezone": "Europe/Sarajevo",
    }

    try:
        response = requests.get(API_URL, params=params, timeout=TIMEOUT)
        response.raise_for_status()   # baci grešku ako status nije 2xx
        return response.json()
    except requests.exceptions.Timeout:
        print(f"  [ERROR] Timeout za {city['name']}", file=sys.stderr)
    except requests.exceptions.ConnectionError:
        print(f"  [ERROR] Nema mreže za {city['name']}", file=sys.stderr)
    except requests.exceptions.HTTPError as e:
        print(f"  [ERROR] HTTP greška za {city['name']}: {e}", file=sys.stderr)
    except Exception as e:
        print(f"  [ERROR] Neočekivana greška za {city['name']}: {e}", file=sys.stderr)
    return None


def weather_emoji(code):
    """Pretvori weather_code iz API-ja u opis."""
    # https://open-meteo.com/en/docs (Weather Variable Documentation)
    if code == 0: return "sunčano"
    if code in [1, 2, 3]: return "djelimično oblačno"
    if code in [45, 48]: return "magla"
    if code in [51, 53, 55, 56, 57]: return "rosulja"
    if code in [61, 63, 65, 66, 67, 80, 81, 82]: return "kiša"
    if code in [71, 73, 75, 77, 85, 86]: return "snijeg"
    if code in [95, 96, 99]: return "grmljavina"
    return f"kod {code}"


def main():
    now = datetime.now()
    print("=" * 60)
    print(f"  WEATHER REPORT   {now:%Y-%m-%d %H:%M}")
    print("=" * 60)
    print(f"{'Grad':<12} {'Temp':>8} {'Vjetar':>10} {'Vlažnost':>10}  {'Uslovi'}")
    print("-" * 60)

    for city in CITIES:
        data = fetch_weather(city)
        if data is None:
            print(f"{city['name']:<12}   [nedostupno]")
            continue

        current = data["current"]
        temp = current["temperature_2m"]
        wind = current["wind_speed_10m"]
        humid = current["relative_humidity_2m"]
        code = current["weather_code"]

        print(f"{city['name']:<12} {temp:>6.1f}°C {wind:>8.1f} km/h {humid:>8}%  {weather_emoji(code)}")

    print("=" * 60)


if __name__ == "__main__":
    main()
