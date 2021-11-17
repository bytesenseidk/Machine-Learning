import os
import pandas as pd
import numpy as np
import sklearn
import pickle
import matplotlib.pyplot as pyplot
from sklearn import linear_model
from matplotlib import style

# Data set of students grades
data_sets = os.path.join(os.path.expanduser('~'),'Documents\\Filer\\Modules\\Datasets')
data = pd.read_csv(f"{data_sets}/student-mat.csv", sep=";")

# Selection of parameters
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

# Parameter which we wish to predict
predict = "G3"

# X & Y axis coordinates, given in an array
x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

# Pass the parameters to train
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

best = 0
for i in range(100):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)
    # Model selection
    linear = linear_model.LinearRegression()

    # pass the training data to the the prediction model
    linear.fit(x_train, y_train)

    # Saves the accuracy of the tests
    acc = linear.score(x_test, y_test)

    # Saves the best accuracy to the model
    if acc > best:
        best = acc
        # Save your training model
        with open("studentmodel.pickle", "wb") as f:
            pickle.dump(linear, f)

# Load in trained model
pickle_in = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_in)

# Results of the predictions
predictions = linear.predict(x_test)

# Print out the first 10 predictions
for x in range(10):
    print(f"Parameters: {x_test[x]}, \tPrediction: {int(predictions[x])}, \tActual grade: {y_test[x]}")

# Plot data to a graph
p = "G1"
style.use("ggplot")
pyplot.scatter(data[p], data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()
