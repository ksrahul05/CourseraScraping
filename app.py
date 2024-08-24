import os
from flask import Flask, request, jsonify
import pickle
import numpy as np

# Create a Flask object
app = Flask(__name__)

# Load the model from the pickle file
try:
    with open('Course_learners.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    print("Error: The file 'Course_learners.pkl' was not found.")
except pickle.PickleError as e:
    print(f"Error: Pickle file could not be loaded. {e}")

@app.route('/')
def home():
    return "Welcome to the Flask application!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)
        return jsonify({'prediction': prediction[0]})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)