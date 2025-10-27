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
| **Frontend** | HTML5, CSS3, JavaScript (ES6+), Chart.js, |
| **Backend** | Flask  |
| **Machine Learning** | Python, Scikit-learn, Pandas, NumPy |
| **APIs Used** | Google Gemini API |
| **Deployment** | Render|
| **Version Control** | Git & GitHub |

---
##
---

## ⚙️ Installation & Setup

1️⃣ Clone the repository
git clone https://github.com/<your-username>/rainfall-predictor.git
cd rainfall-predictor

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Set up environment variables
Create a .env file in the root directory:

4️⃣ Run the Flask app
python app.py

5️⃣ Open in your browser
http://127.0.0.1:5000

---
🔮 Model Details

The Machine Learning model was trained on meteorological datasets using:
-Features: Humidity, Temperature, Pressure,Visibility,Weather Type
-Label: Rainfall (binary classification)
-Algorithms: Random Forest, XGBoost
-Best Accuracy: ~92%
-Metrics Used: Accuracy, F1 Score, ROC Curve
Model stored as rainfall_model.pkl and integrated into Flask backend.

---
💡 Future Enhancements
-🌡️ Add more predictive parameters (wind speed, cloud cover)
-📱 Convert to Progressive Web App (PWA)
-🌐 Add multilingual weather chatbot support
-🔔 Enable weather alerts via email/SMS
-🌈 Integrate AI-based weather visualizations using Gemini Vision

---
🧑‍💻 Developer

👤 Bidisha Kundu
Computer Science Student | ML & Web Developer | Passionate about AI-powered applications

📧 Email:kbidisha.2005@gmail.com
💼 LinkedIn:https://www.linkedin.com/in/bidisha-kundu-41706428b/

---

⭐ Support

If you liked this project, consider giving it a ⭐ on GitHub — it helps others discover it too!
Your support motivates me to keep building awesome AI-powered web apps 🚀

