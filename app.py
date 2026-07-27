from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

# template_folder='.' tells Flask to look for index.html in the same root folder
app = Flask(__name__)
CORS(app)

# Load Trained Model (No Scaler)
model = joblib.load('bmi_model.joblib')

CATEGORIES = [
    {'name': 'Extremely Weak', 'badge': 'bg-blue-500 text-white', 'color': 'border-blue-500', 'desc': 'Body mass is significantly below normal range. Clinical guidance recommended.'},
    {'name': 'Weak', 'badge': 'bg-sky-500 text-white', 'color': 'border-sky-500', 'desc': 'Slightly underweight. Focused caloric and nutritional planning advised.'},
    {'name': 'Normal', 'badge': 'bg-emerald-500 text-white', 'color': 'border-emerald-500', 'desc': 'Optimal body weight ratio. Excellent balance maintained.'},
    {'name': 'Overweight', 'badge': 'bg-amber-500 text-white', 'color': 'border-amber-500', 'desc': 'Slightly above recommended weight threshold. Regular exercise suggested.'},
    {'name': 'Obesity', 'badge': 'bg-orange-500 text-white', 'color': 'border-orange-500', 'desc': 'Elevated health risk category. Structured fitness & diet plan recommended.'},
    {'name': 'Extreme Obesity', 'badge': 'bg-rose-600 text-white', 'color': 'border-rose-600', 'desc': 'High clinical risk category. Immediate health evaluation recommended.'}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        unit_type = data.get('unit_type')
        weight_kg = float(data.get('weight'))

        if unit_type == 'ft':
            feet = float(data.get('feet') or 0)
            inches = float(data.get('inches') or 0)
            height_cm = (feet * 30.48) + (inches * 2.54)
        else:
            height_cm = float(data.get('height_cm'))

        if height_cm <= 0 or weight_kg <= 0:
            return jsonify({'status': 'error', 'message': 'Please enter valid positive numbers.'}), 400

        # Model Predict
        input_data = np.array([[height_cm, weight_kg]])
        pred_idx = int(model.predict(input_data)[0])

        # Formula BMI
        bmi_value = round(weight_kg / ((height_cm / 100) ** 2), 1)
        res_info = CATEGORIES[pred_idx]

        return jsonify({
            'status': 'success',
            'height_cm': round(height_cm, 1),
            'weight_kg': weight_kg,
            'bmi': bmi_value,
            'category': res_info['name'],
            'badge_style': res_info['badge'],
            'border_style': res_info['color'],
            'description': res_info['desc']
        })

    except Exception as e:
        return jsonify({'status': 'error', 'message': 'Please fill all required fields correctly.'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)