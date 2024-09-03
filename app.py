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
        crim = float(request.args.get('CRIM', 0))
        zn = float(request.args.get('ZN', 0))
        indus = float(request.args.get('INDUS', 0))
        chas = float(request.args.get('CHAS', 0))
        nox = float(request.args.get('NOX', 0))
        rm = float(request.args.get('RM', 0))
        age = float(request.args.get('AGE', 0))
        dis = float(request.args.get('DIS', 0))
        rad = float(request.args.get('RAD', 0))
        tax = float(request.args.get('TAX', 0))
        ptratio = float(request.args.get('PTRATIO', 0))
        lstat = float(request.args.get('LSTAT', 0))

        final_features = [[crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, lstat]]

        prediction = model.predict(final_features)

        return jsonify(str("Predicted House Price: $" + f'{prediction[0]:,.2f}'))

if __name__ == '__main__':
    app.run(debug=True)
