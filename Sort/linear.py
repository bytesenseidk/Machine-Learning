import os
import sklearn
import numpy as np
import pandas as pd
from sklearn import linear_model, preprocessing

data_sets = os.path.join(os.path.expanduser('~'), 'Desktop/Modules/Datasets')
data = pd.read_csv(f"{data_sets}/abalone-data.txt", sep=",")

data = data[["length","diameter","height","whole-weight","shucked-weight","viscera-weight","shell-weight","rings"]]

predict = "rings"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

best = 0
for i in range(50):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

    model = linear_model.LinearRegression()
    model.fit(x_train, y_train)
    accuracy = model.score(x_test, y_test)
    print(accuracy)
    
    if accuracy > best:
        best = accuracy

prediction = model.predict(x_test)

for x in range(10):
    print(f"Prediction: {round(prediction[x], 2)},\t Parameters: {x_test[x]},\t Actual: {y_test[x]}")
print(best)