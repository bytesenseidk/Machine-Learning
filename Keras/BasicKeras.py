from keras.models import Sequential
from keras.layers import Dense
import numpy as np

np.random.seed(2018) # Setting seed for reproducibility

""" GETTING THE DATA READY """
train_data = np.random.random((1000, 3)) # Random dummy-train data for 1000 students
test_data = np.random.random((500, 3))   # Random dummy-test data for 500

labels = np.random.randint(2, size=(1000, 1)) # Dummy results for 100 students (pass or fail)

""" DEFINING MODEL STRUCTURE """
model = Sequential()
model.add(Dense(5, input_dim=3, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(train_data, labels, epochs=10, batch_size=32) # Train model and predict
predictions = model.predict(test_data) # Make predictions from the trained model