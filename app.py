import numpy as np
import joblib
from flask import Flask, request, render_template

# تحميل الموديل
model = joblib.load("logistic_regression_model (1).joblib")

app = Flask(__name__)

@app.route("/")
def home():
    return "Machine Learning Model Deployment"

@app.route("/predict", methods=["POST"])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    return f"Prediction: {prediction[0]}"

if __name__ == "__main__":
    app.run(debug=True)

add app.py for model deployment
