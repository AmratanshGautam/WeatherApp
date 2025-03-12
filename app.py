import os 
import requests 
from flask import Flask, render_template, request 


app = Flask(__name__) 

# Get API key from environment variable 
API_KEY = os.getenv("ba6ab82197a412e33ea8744d6bce72dc") 

@app.route("/", methods=["GET", "POST"]) 
def index(): 
    weather_data = None 
    error_message = None # To store error messages 
    
    if request.method == "POST": 
        city = request.form["city"] 
        if city: 
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric" 
            
            response = requests.get(url) 
            if response.status_code == 200: # If request is successful 
                weather_data = response.json() 
                else: 
                error_message = "City not found or API error. Please try again." 

    return render_template("index.html", weather=weather_data, error=error_message) 
if __name__ == "__main__": 
    port = int(os.environ.get("PORT", 10000)) # Use Render's port 
    app.run(host="0.0.0.0", port=port, debug=True)