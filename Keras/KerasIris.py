from keras.models import Sequential
from keras.layers import Dense
from sklearn.datasets import load_iris
import numpy as np

np.random.seed(2018) # Setting seed for reproducibility
iris = load_iris()
indices = np.random.permutation(len(iris.data))
test_samples = 12

train_data = iris.data[indices[:-test_samples]] 
test_data = iris.data[indices[-test_samples:]]
labels = iris.target[indices[:-test_samples]]

model = Sequential()
model.add(Dense(5, input_dim=4, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(3, activation='relu'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(train_data, labels, epochs=10, batch_size=32)
predictions = model.predict(test_data)