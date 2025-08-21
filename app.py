
import math
import requests
from flask import Flask, render_template, request

# --- Flask App Initialisatie ---
app = Flask(__name__)

# --- Kernfuncties (overgenomen uit wind_calculator.py) ---

def get_coordinates(place_name):
    """Zet een plaatsnaam om naar latitude en longitude via de Open-Meteo Geocoding API."""
    try:
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={place_name.strip()}&count=1&language=nl&format=json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if "results" in data and len(data["results"]) > 0:
            location = data["results"][0]
            return {
                "name": location.get("name", "Onbekend"),
                "lat": location["latitude"],
                "lon": location["longitude"]
            }
        return None
    except requests.exceptions.RequestException:
        return None

def get_current_wind(lat, lon):
    """Haalt de huidige windsnelheid en -richting op."""
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&windspeed_unit=kmh"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            "speed": data["current_weather"]["windspeed"],
            "direction": data["current_weather"]["winddirection"]
        }
    except requests.exceptions.RequestException:
        return None

def calculate_bearing(lat1, lon1, lat2, lon2):
    """Berekent de kompasrichting (bearing) van punt 1 naar punt 2."""
    lat1_rad, lon1_rad, lat2_rad, lon2_rad = map(math.radians, [lat1, lon1, lat2, lon2])
    dLon = lon2_rad - lon1_rad
    x = math.cos(lat2_rad) * math.sin(dLon)
    y = math.cos(lat1_rad) * math.sin(lat2_rad) - math.sin(lat1_rad) * math.cos(lat2_rad) * math.cos(dLon)
    initial_bearing = math.atan2(x, y)
    return (math.degrees(initial_bearing) + 360) % 360

def get_wind_compass_direction(degrees):
    """Zet graden om naar een kompasrichting (bijv. N, NO, O)."""
    if degrees is None: return ""
    directions = ["N", "NNO", "NO", "ONO", "O", "OZO", "ZO", "ZZO", "Z", "ZZW", "ZW", "WZW", "W", "WNW", "NW", "NNW"]
    index = round(degrees / (360. / len(directions)))
    return directions[index % len(directions)]

# --- Flask Routes ---

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    error = None
    
    if request.method == 'POST':
        departure_place = request.form.get('departure')
        destination_place = request.form.get('destination')

        if not departure_place or not destination_place:
            error = "Vul alstublieft zowel een vertrek- als bestemmingsplaats in."
        else:
            departure_coords = get_coordinates(departure_place)
            destination_coords = get_coordinates(destination_place)

            if not departure_coords:
                error = f"Kon de vertrekplaats '{departure_place}' niet vinden."
            elif not destination_coords:
                error = f"Kon de bestemming '{destination_place}' niet vinden."
            else:
                wind_data = get_current_wind(departure_coords["lat"], departure_coords["lon"])
                if not wind_data:
                    error = "Kon de actuele windgegevens niet ophalen."
                else:
                    travel_bearing = calculate_bearing(
                        departure_coords["lat"], departure_coords["lon"],
                        destination_coords["lat"], destination_coords["lon"]
                    )
                    
                    angle_difference = wind_data["direction"] - travel_bearing
                    headwind_factor = math.cos(math.radians(angle_difference))
                    headwind_percentage = headwind_factor * 100

                    results = {
                        "departure": departure_coords,
                        "destination": destination_coords,
                        "wind": wind_data,
                        "wind_compass": get_wind_compass_direction(wind_data["direction"]),
                        "travel_bearing": travel_bearing,
                        "headwind_percentage": headwind_percentage
                    }

    return render_template('index.html', results=results, error=error)

# --- Applicatie Starten ---

if __name__ == '__main__':
    app.run(debug=True)
