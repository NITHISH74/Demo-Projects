# app/routes.py

from flask import Blueprint, render_template, request
import numpy as np
import pickle
import os

# Create a Blueprint for main routes
main = Blueprint('main', __name__)

# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'model', 'iris_model.pkl')
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Define a dictionary to map prediction indices to species names
species_dict = {
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
}

@main.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Extract features from the form
        sepal_length = float(request.form.get('sepal_length', 0))
        sepal_width = float(request.form.get('sepal_width', 0))
        petal_length = float(request.form.get('petal_length', 0))
        petal_width = float(request.form.get('petal_width', 0))

        # Prepare features for prediction
        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

        # Perform prediction
        prediction = model.predict(features)[0]
        prediction_proba = model.predict_proba(features).tolist()[0]

        # Map prediction to species name
        species_name = species_dict[prediction]

        # Return prediction result
        return render_template(
            'index.html', 
            prediction=species_name,
            prediction_proba=prediction_proba,
            sepal_length=sepal_length,
            sepal_width=sepal_width,
            petal_length=petal_length,
            petal_width=petal_width
        )

    # Render the input form by default
    return render_template('index.html')
