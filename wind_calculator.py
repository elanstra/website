import requests
import math

def get_coordinates(place_name):
    """Zet een plaatsnaam om naar latitude en longitude via de Open-Meteo Geocoding API."""
    try:
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={place_name.strip()}&count=1&language=nl&format=json"
        response = requests.get(url)
        response.raise_for_status()  # Genereert een error bij een slechte response (4xx of 5xx)
        data = response.json()
        if "results" in data and len(data["results"]) > 0:
            location = data["results"][0]
            return location["latitude"], location["longitude"]
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Fout bij het ophalen van coördinaten: {e}")
        return None

def get_current_wind(lat, lon):
    """Haalt de huidige windsnelheid en -richting op voor een specifieke locatie."""
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&windspeed_unit=kmh"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        wind_speed = data["current_weather"]["windspeed"]
        wind_direction = data["current_weather"]["winddirection"]
        return wind_speed, wind_direction
    except requests.exceptions.RequestException as e:
        print(f"Fout bij het ophalen van weerdata: {e}")
        return None, None

def calculate_bearing(lat1, lon1, lat2, lon2):
    """Berekent de kompasrichting (bearing) van punt 1 naar punt 2."""
    # Omzetten naar radialen
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Berekening
    dLon = lon2_rad - lon1_rad
    x = math.cos(lat2_rad) * math.sin(dLon)
    y = math.cos(lat1_rad) * math.sin(lat2_rad) - math.sin(lat1_rad) * math.cos(lat2_rad) * math.cos(dLon)
    
    initial_bearing = math.atan2(x, y)
    
    # Omzetten naar graden
    initial_bearing_deg = math.degrees(initial_bearing)
    
    # Zorgen dat de bearing tussen 0 en 360 ligt
    compass_bearing = (initial_bearing_deg + 360) % 360
    
    return compass_bearing

def main():
    """Hoofdfunctie van de tool."""
    print("--- Tegenwind Calculator ---")
    
    # Vraag om input
    departure_place = input("Voer je vertrekplaats in: ")
    destination_place = input("Voer je bestemming in: ")

    # Haal coördinaten op
    departure_coords = get_coordinates(departure_place)
    if not departure_coords:
        print(f"Fout: Kon de vertrekplaats '{departure_place}' niet vinden.")
        return

    destination_coords = get_coordinates(destination_place)
    if not destination_coords:
        print(f"Fout: Kon de bestemming '{destination_place}' niet vinden.")
        return

    print(f"\nVertrekplaats gevonden: {departure_place} ({departure_coords[0]:.2f}, {departure_coords[1]:.2f})")
    print(f"Bestemming gevonden: {destination_place} ({destination_coords[0]:.2f}, {destination_coords[1]:.2f})")

    # Haal windgegevens op
    wind_speed, wind_direction = get_current_wind(departure_coords[0], departure_coords[1])
    if wind_speed is None:
        return
        
    print(f"\nActuele wind op vertrekplaats:")
    print(f"  - Snelheid: {wind_speed} km/u")
    print(f"  - Richting: {wind_direction}° (komt uit het {get_wind_compass_direction(wind_direction)})")

    # Bereken reisrichting
    travel_bearing = calculate_bearing(departure_coords[0], departure_coords[1], destination_coords[0], destination_coords[1])
    print(f"\nJe berekende reisrichting is: {travel_bearing:.1f}°")

    # Bereken tegenwind
    # Het verschil in hoek tussen windrichting en reisrichting
    angle_difference = wind_direction - travel_bearing
    
    # Cosinus van deze hoek geeft de factor van de tegenwind.
    # We moeten de hoek omzetten naar radialen voor de math.cos functie.
    headwind_factor = math.cos(math.radians(angle_difference))
    
    headwind_percentage = headwind_factor * 100

    print("\n--- Resultaat ---")
    if headwind_percentage > 5: # Kleine marge voor pure crosswind
        print(f"Je hebt {headwind_percentage:.1f}% tegenwind.")
    elif headwind_percentage < -5:
        print(f"Je hebt {-headwind_percentage:.1f}% meewind!")
    else:
        print("Je hebt voornamelijk zijwind.")

def get_wind_compass_direction(degrees):
    """Zet graden om naar een kompasrichting zoals N, NO, O, etc."""
    if degrees is None:
        return ""
    directions = ["N", "NNO", "NO", "ONO", "O", "OZO", "ZO", "ZZO", "Z", "ZZW", "ZW", "WZW", "W", "WNW", "NNW"]
    index = round(degrees / (360. / len(directions)))
    return directions[index % len(directions)]

if __name__ == "__main__":
    main()
