from flask import Flask, jsonify, request
import pickle
import numpy as np
from flask_cors import CORS, cross_origin

# Initialize our Flask application
app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Load the pre-trained model
model = pickle.load(open('housing.pickle', 'rb'))

@app.route("/")
@cross_origin()
def hello_world():
    return "Hello, cross-origin-world!"

@app.route("/predict", methods=["GET"])
def predict():
    if request.method == 'GET':
        crim = float(request.args.get('CRIM'))
        zn = float(request.args.get('ZN'))
        rm = float(request.args.get('RM'))
        age = float(request.args.get('AGE'))
        dis = float(request.args.get('DIS'))

        final_features = [[crim, zn, rm, age, dis]]

        prediction = model.predict(final_features)

        return jsonify(str("Predicted House Price: $" + f'{prediction[0]:,.2f}'))

if __name__ == '__main__':
    app.run(debug=True)