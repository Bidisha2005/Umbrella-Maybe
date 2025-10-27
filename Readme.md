# 🌧️ Rainfall Predictor - ML-Powered Weather Forecast
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=flat-square&logo=chartdotjs&logoColor=white)](https://www.chartjs.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)](https://numpy.org/)
[![Google Gemini API](https://img.shields.io/badge/Google_Gemini-FF6800?style=flat-square&logo=google&logoColor=white)](https://ai.google.dev/models/gemini)
[![Render](https://img.shields.io/badge/Render-46E3B7?style=flat-square&logo=render&logoColor=white)](https://render.com/)
[![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/)
An AI-powered web application that predicts rainfall using meteorological data and a trained Machine Learning model.

## ✨ Features

- 🎯 **Accurate Prediction**: Utilizes Random Forest and XGBoost for high-accuracy rainfall prediction.
- ⚙️ **Robust ML Model**: Trained on key meteorological features like humidity, temperature, and pressure.
- 🌐 **Web Interface**: Simple, interactive web application built with Flask.
- 📈 **Performance Metrics**: Achieved $\sim 92\%$ accuracy on the test set.

---

## 🔮 Model Details

The Machine Learning model was trained on meteorological datasets using:
- **Features**: Humidity, Temperature, Pressure, Visibility, Weather Type
- **Label**: Rainfall (binary classification)
- **Algorithms**: Random Forest, XGBoost
- **Best Accuracy**: $\sim 92\%$
- **Metrics Used**: Accuracy, $F1$ Score, ROC Curve

The final model is stored as `rainfall_model.pkl` and is integrated into the Flask backend for real-time predictions.

---

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10+** - [Download Python](https://www.python.org/downloads/)
- **Git** - [Download Git](https://git-scm.com/)

### Installation

```bash
git clone https://github.com/yourusername/rainfall-predictor.git
cd rainfall-predictor
pip install -r requirements.txt
python app.py
```
---
Now open in your browser at http://127.0.0.1:5000
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




