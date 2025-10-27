# 🌧️ Rainfall Predictor — AI-Powered Weather Intelligence Web App

A modern full-stack web application that predicts rainfall using a trained ML model, provides live weather visualization, and offers an interactive chatbot powered by **Google Gemini API** — all wrapped in a sleek, responsive UI.

---

## 🌟 Overview

The **Rainfall Predictor** web app combines real-time weather data, AI-based rainfall prediction, and beautiful weather visualization to give users an immersive meteorological experience.

From fetching your live geolocation weather to generating rainfall predictions with interactive data visualizations, it’s built to impress both users and engineers.

---

# 🚀 Features

# 🧭 Dynamic Navigation Bar
- Elegant navbar with sections: **Home**, **Predict**, **About**, and **Contact**  
- Smooth scrolling and fully responsive design

# 🌍 Live Location Weather
- Automatically detects your **current location**
- Displays real-time **temperature, humidity, pressure**, and **rainfall probability**
- Powered by **OpenWeather API**

# 📍 Manual Weather Input
- Enter **latitude** and **longitude** to fetch weather for any region
- Real-time dynamic weather data updates via API

# ☁️ AI-Based Rainfall Prediction
- On clicking **Predict**, users input parameters like humidity, temperature, and pressure
- A trained **Machine Learning model** (Random Forest / XGBoost) predicts rainfall probability
- UI dynamically adapts to prediction results:
  - ☀️ **Sunny** → Bright blue background with sun animation  
  - 🌧️ **Rainy** → Rainfall background with thunder/lightning effects

# 📊 Interactive Data Visualizations
- **Radar Chart**: Displays user-entered weather parameters  
- **Circular Gauge**: Shows the model’s confidence score using **Chart.js**  
- Smooth, real-time animations for data transitions

# 🤖 Weather Chatbot (Gemini API)
- Integrated chatbot answering weather-related queries  
- Built using **Google Gemini API** for accurate, conversational responses  
- Floating, minimal, and user-friendly chat interface

# 📖 About & Footer
- Minimal **About section** with project context and tech stack  
- Elegant **Footer** with contact links and GitHub profile reference  

---

## 🧠 Tech Stack

| Category | Technologies |
|-----------|---------------|
| **Frontend** | HTML5, CSS3, JavaScript (ES6+), Chart.js, Tailwind / Bootstrap |
| **Backend** | Flask / Node.js |
| **Machine Learning** | Python, Scikit-learn, Pandas, NumPy |
| **APIs Used** | OpenWeather API, Google Gemini API |
| **Deployment** | Render / Vercel / Heroku |
| **Version Control** | Git & GitHub |

---
##
---

## ⚙️ Installation & Setup

1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/rainfall-predictor.git
cd rainfall-predictor

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Set up environment variables
Create a .env file in the root directory:



