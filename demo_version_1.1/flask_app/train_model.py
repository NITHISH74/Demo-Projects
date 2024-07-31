# train_model.py

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model to a pickle file
with open('flask_app/app/model/iris_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model training and saving completed.")
