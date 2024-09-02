from flask import Flask, request, render_template
from flask_cors import CORS  # Import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)  # Apply CORS to the app

# Load the pre-trained model
with open('linear_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Extract features from the form data
        features = [float(request.form[feature]) for feature in ['CRIM', 'ZN', 'RM', 'AGE', 'DIS']]
        final_features = np.array(features).reshape(1, -1)

        # Predict using the loaded model
        prediction = model.predict(final_features)

        # Return the prediction result to the frontend
        return render_template('index.html', prediction_text=f'Predicted House Price: ${prediction[0]:,.2f}')

if __name__ == '__main__':
    app.run(debug=True)