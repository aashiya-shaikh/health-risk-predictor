# 🩺 Health Risk & BMI Assessment Platform

An end-to-end Machine Learning web application built to predict physical health risk categories and BMI status in real-time. Features a trained **K-Nearest Neighbors (KNN)** model served via a **Flask REST API**, paired with a modern, responsive medical dashboard UI.

---

## ✨ Key Features
* **AI-Powered Diagnostics**: Real-time classification into health risk categories based on physical parameters.
* **Dual Height Units**: Seamless support for both **Feet/Inches** and **Centimeters (cm)**.
* **Interactive Medical UI**: Modern light-themed dashboard built with Tailwind CSS, Font Awesome icons, and animated scale bars.
* **Instant State Reset**: Built-in "New Patient Checkup" workflow for quick consecutive evaluations.

---

## 🛠️ Tech Stack
* **Machine Learning**: Python, Scikit-Learn, Pandas, NumPy, Joblib
* **Backend**: Flask, Flask-CORS
* **Frontend**: HTML5, Tailwind CSS, JavaScript (Fetch API)

---

## 📂 Project Structure
```text
health-risk-predictor/
│
├── templates/
│   └── index.html           # UI Dashboard
├── notebook/
│   └── model_training.ipynb # Data Cleaning & KNN Model Training
├── app.py                   # Flask Backend API
├── knn_model.pkl            # Trained Model
├── requirements.txt         # Project Dependencies
├── .gitignore               # Unwanted Cache Filter
└── README.md                # Documentation