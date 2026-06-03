from flask import Flask, request, render_template
import requests

app = Flask(__name__)
history = []

def get_weather(city):
    url = f"https://wttr.in/{city}?format=%t+%C"

    response = requests.get(url)

    data = response.text.strip()

    return data

def extract_temperature(weather_data):
    temp = weather_data.split("°C")[0]
    temp = temp.replace("+", "")
    return int(temp)

def get_condition(weather_data):
    return weather_data.split("°C")[1].strip()

def calculate_water(soil, crop, temperature):
    water = 0

    if soil == "sandy":
        water = 8
    elif soil == "clay":
        water = 5
    elif soil == "loamy":
        water = 7

    if crop == "rice":
        water += 3
    elif crop == "wheat":
        water += 2
    elif crop == "cotton":
        water += 1
    elif crop == "maize":
        water += 4

    if temperature > 35:
        water += 2

    return water


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        soil = request.form["soil"].lower()
        crop = request.form["crop"].lower()
        city = request.form["city"]

        weather_data = get_weather(city)
        temperature = extract_temperature(weather_data)
        condition = get_condition(weather_data)

        water = calculate_water(soil, crop, temperature)

        if "rain" in condition.lower():
            water -= 3

            if water < 0:
                water = 0

        result = f"""
        🌱 Smart Irrigation Recommendation<br><br>

        📍 City: {city}<br>
        🌦 Weather: {condition}<br>
        🌡 Temperature: {temperature}°C<br><br>

        💧 Recommended Water: {water} Litres
        """

        history.append({
            "city": city,
            "soil": soil.capitalize(),
            "crop": crop.capitalize(),
            "temperature": temperature,
            "water": water
        })

    return render_template("index.html", result=result, history=history)

if __name__ == "__main__":
    app.run(debug=True)