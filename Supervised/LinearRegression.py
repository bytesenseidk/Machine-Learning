import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets
plt.style.use("ggplot")

dataset = datasets.load_diabetes(return_X_y=True) # Loads diabetes dataset 
X = dataset[0] # Assigns the attributes to X
y = dataset[1] # Assigns the labels to y
X = X[:, np.newaxis, 2] # Sets X to a single attribute of the dataset
# Splits attributes into training and test sets
X_train, X_test = X[:-20], X[-20:] # All but the 20 last, All but the first 20
# Splits lables into training and test sets
y_train, y_test = y[:-20], y[-20:] # All but the 20 last, All but the first 20
# Selects the linear regression machine learning algorithm
model = linear_model.LinearRegression()
# Model trains on the given data
model.fit(X_train, y_train)
# Model predicts the features relative to the training set
prediction = model.predict(X_test)
# Scale the data to highest and lowest difference
data1 = max(max(prediction), max(y_test))
data2 = min(min(prediction), min(y_test))
# Plot our predicted values to the actual values
plt.title("Linear Regression")
plt.scatter(y_test, prediction, marker="x", color="black") # Dots on plot
plt.plot([data1, data2], [data1, data2]) # Line on plot
plt.ylabel("Predictions")
plt.xlabel("Actual")
plt.axis("equal")
plt.show()

