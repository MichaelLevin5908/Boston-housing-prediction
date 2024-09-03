from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)  # Apply CORS to the app

# Load the pre-trained model
with open('linear_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    # Extract features from the JSON data
    data = request.get_json()  # Get the JSON data from the request
    features = [float(data[feature]) for feature in ['CRIM', 'ZN', 'RM', 'AGE', 'DIS']]
    final_features = np.array(features).reshape(1, -1)

    # Predict using the loaded model
    prediction = model.predict(final_features)

    # Return the prediction result as JSON
    return jsonify(prediction=f'{prediction[0]:,.2f}')

if __name__ == '__main__':
    app.run(debug=True)