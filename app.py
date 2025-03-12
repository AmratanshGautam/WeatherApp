from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

import os
API_KEY = os.getenv("ba6ab82197a412e33ea8744d6bce72dc")  # Replace with your actual API key

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather")
def get_weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "City name is required"}), 400
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()

    if response.get("cod") != 200:
        return jsonify({"error": "City not found"}), 404

    weather_data = {
        "city": response["name"],
        "temp": response["main"]["temp"],
        "weather": response["weather"][0]["description"]
    }
    
    return jsonify(weather_data)

import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)