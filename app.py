from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd
import requests
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# Load model and pipeline
model = joblib.load("cloudburst_model.pkl")
pipeline = joblib.load("cloudburst_pipeline.pkl")

def get_location_name(lat, lon):
    """Get location name from coordinates using reverse geocoding"""
    try:
        # Using OpenStreetMap Nominatim API for reverse geocoding
        url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}"
        headers = {'User-Agent': 'Cloudburst Predictor App'}  # Required by Nominatim
        response = requests.get(url, headers=headers)
        data = response.json()
        
        if 'address' in data:
            address = data['address']
            # Try to get city/town name, fallback to other location names
            if 'city' in address:
                return address['city']
            elif 'town' in address:
                return address['town']
            elif 'village' in address:
                return address['village']
            elif 'municipality' in address:
                return address['municipality']
            elif 'county' in address:
                return address['county']
            elif 'state' in address:
                return address['state']
            elif 'country' in address:
                return address['country']
        return f"{lat}, {lon}"  # Fallback to coordinates
    except Exception as e:
        print(f"Geocoding error: {e}")
        return f"{lat}, {lon}"  # Fallback to coordinates

# 🔹 Gemini API endpoint
@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    try:
        if not GEMINI_API_KEY:
            return jsonify({"error": "Gemini API not configured"}), 500
        
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({"error": "No message provided"}), 400
        
        # Get current weather data for context
        current_temp = data.get('current_temp', 'N/A')
        current_humidity = data.get('current_humidity', 'N/A')
        current_precipitation = data.get('current_precipitation', 'N/A')
        current_windspeed = data.get('current_windspeed', 'N/A')
        current_location = data.get('current_location', 'Unknown Location')
        
        # Create context with current weather data
        context = f"""
You are an AI assistant for a Rainfall Prediction application. Your primary expertise is in weather, climate, and rainfall-related topics, but you can also answer general questions.

Current Weather Data (for weather queries):
- Location: {current_location}
- Temperature: {current_temp}°C
- Humidity: {current_humidity}%
- Precipitation: {current_precipitation} mm
- Wind Speed: {current_windspeed} km/h

**Response Guidelines:**
1. For weather-related questions: Use the current data above and provide detailed, accurate information
2. For general/non-weather questions: Provide a helpful but brief answer, then gently guide the conversation back to weather topics
3. Always maintain a friendly, professional tone

User Question: "{user_message}"
"""
        
        # Initialize the Gemini model
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Generate response
        response = model.generate_content(context)
        
        return jsonify({"response": response.text})
        
    except Exception as e:
        print(f"Gemini API error: {e}")
        return jsonify({"error": "Failed to generate response"}), 500

# 🔹 HOME PAGE: Show real-time weather data
@app.route('/')
def home():
    try:
        # Get user's location from request headers or use default
        user_lat = request.args.get('lat', 13.0827)  # Default to Chennai if no location
        user_lon = request.args.get('lon', 80.2707)  # Default to Chennai if no location
        
        # Get location name
        location_name = get_location_name(user_lat, user_lon)
        
        # Open Meteo API for user's location - including humidity and precipitation
        url = f"https://api.open-meteo.com/v1/forecast?latitude={user_lat}&longitude={user_lon}&current_weather=true&hourly=relative_humidity_2m,precipitation&timezone=auto"
        response = requests.get(url, timeout=10)
        data = response.json()

        # Initialize default values
        weather_data = {
            "temperature": "N/A",
            "windspeed": "N/A", 
            "humidity": "N/A",
            "precipitation": "N/A",
            "location_name": location_name,
            "latitude": user_lat,
            "longitude": user_lon
        }
        
        times = []
        humidities = []
        rainfall = []

        # Check if API response has the required data
        if "current_weather" in data and "hourly" in data:
            current = data["current_weather"]
            hourly_data = data["hourly"]
            
            # Get current weather data
            if "temperature" in current:
                weather_data["temperature"] = current["temperature"]
            if "windspeed" in current:
                weather_data["windspeed"] = current["windspeed"]
            
            # Get current time to match with hourly data
            current_time = current.get("time")
            
            # Extract hourly data for charts
            times = hourly_data.get("time", [])
            humidities = hourly_data.get("relative_humidity_2m", [])
            rainfall = hourly_data.get("precipitation", [])
            
            # Find current humidity and precipitation
            if current_time and current_time in times:
                index = times.index(current_time)
                if index < len(humidities):
                    weather_data["humidity"] = humidities[index]
                if index < len(rainfall):
                    weather_data["precipitation"] = rainfall[index]
            elif humidities:  # If current time not found, use first available
                weather_data["humidity"] = humidities[0] if humidities else "N/A"
                weather_data["precipitation"] = rainfall[0] if rainfall else "N/A"
        
        # Ensure all arrays are the same length (take minimum length)
        min_length = min(len(times), len(humidities), len(rainfall), 24)
        
        return render_template(
            "index.html",
            weather=weather_data,
            times=times[:min_length],
            humidities=humidities[:min_length],
            rainfall=rainfall[:min_length]
        )
        
    except Exception as e:
        print(f"Error in home route: {e}")
        # Fallback data if anything fails
        weather_data = {
            "temperature": "N/A",
            "windspeed": "N/A", 
            "humidity": "N/A",
            "precipitation": "N/A",
            "location_name": "Unknown Location",
            "latitude": request.args.get('lat', 13.0827),
            "longitude": request.args.get('lon', 80.2707)
        }
        
        return render_template(
            "index.html", 
            weather=weather_data,
            times=[],
            humidities=[],
            rainfall=[]
        )

# 🔹 PREDICTION INPUT PAGE
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            temp = float(request.form['temperature'])
            humidity = float(request.form['humidity'])
            precipitation = float(request.form['precipitation'])
            visibility = float(request.form['visibility'])
            weather_type = request.form['weather_type']

            # ✅ Correct: create a DataFrame with one sample
            input_df = pd.DataFrame([{
                "Temperature": temp,
                "Relative Humidity": humidity,
                "Precipitation": precipitation,
                "Visibility": visibility,
                "Weather Type": weather_type
            }])

            # Transform and predict
            X_new = pipeline.transform(input_df)
            prediction = model.predict(X_new)[0]
            confidence = model.predict_proba(X_new)[0][1]

            result = "Yes" if prediction == 1 else "No"
            confidence_level = (
                "High" if confidence > 0.7 else
                "Medium" if confidence > 0.5 else
                "Low"
            )
            input_data = {
                "Temperature (°C)": temp,
                "Humidity (%)": humidity,
                "Precipitation (mm)": precipitation,
                "Visibility (km)": visibility
            }

            return render_template(
                "result.html",
                result=result,
                confidence=round(confidence, 3),
                confidence_level=confidence_level,
                input_data=input_data 
            )

        except Exception as e:
            return render_template("result.html", result=f"Error: {e}")

    return render_template("predict.html")

# 🔹 RESULT PAGE
@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)