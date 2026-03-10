# Machine Learning Model Deployment

## Project Overview

This project demonstrates how to deploy a Machine Learning model using Flask.
The trained Logistic Regression model predicts the outcome based on input features provided by the user.

## Technologies Used

* Python
* Scikit-learn
* Flask
* NumPy
* Joblib

## Project Structure

machine_learning_deployment

* app.py → Flask web application
* logistic_regression_model.joblib → Trained Machine Learning model
* requirements.txt → Project dependencies
* README.md → Project documentation

## How It Works

1. A Logistic Regression model is trained using Scikit-learn.
2. The trained model is saved using Joblib.
3. A Flask web application loads the trained model.
4. Users send input features through a request.
5. The model returns a prediction.

## Installation

Clone the repository:

git clone https://github.com/yourusername/machine_learning_deployment.git

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

## Author
Machine Learning Engineer
Mariam Ayman
Machine Learning Engineer
