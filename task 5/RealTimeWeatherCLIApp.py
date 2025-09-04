import requests

def get_weather(city, api_key):
    """Fetch weather data from OpenWeatherMap API"""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad status codes
        data = response.json()

        # If city is not found, OpenWeatherMap returns cod != 200
        if data.get("cod") != 200:
            print(f"❌ Error: {data.get('message', 'City not found')}")
            return

        # Extract weather info
        city_name = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"].title()

        print(f"\n🌍 Weather in {city_name}:")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"☁️ Condition: {condition}")

    except requests.exceptions.RequestException as e:
        print("⚠️ Network error:", e)


if __name__ == "__main__":
    print("=== Real-Time Weather CLI App ===")
    API_KEY = "ba5501937230cd886700bd65e445559a"  # ✅ Your API key
    city = input("Enter city name: ").strip()
    get_weather(city, API_KEY)
