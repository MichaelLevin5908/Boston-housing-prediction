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
        indus = float(request.args.get('INDUS'))
        chas = float(request.args.get('CHAS'))
        nox = float(request.args.get('NOX'))
        rm = float(request.args.get('RM'))
        age = float(request.args.get('AGE'))
        dis = float(request.args.get('DIS'))
        rad = float(request.args.get('RAD'))
        tax = float(request.args.get('TAX'))
        ptratio = float(request.args.get('PTRATIO'))
        lstat = float(request.args.get('LSTAT'))

        final_features = [[crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, lstat]]

        prediction = model.predict(final_features)

    return jsonify(str("Housing Price:  " + str(prediction[0])))

if __name__ == '__main__':
    app.run(debug=True)
