import numpy as np

class Perceptron(object):
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta # Learning rate (between 0.0 and 1.0)
        self.n_iter = n_iter # Passes over the training dataset.

    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1]) # Weights after fitting.
        self.errors_ = [] # Number of misclassifications (updates) in each epoch.

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0] # Calculate net input

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1) # Return class label after unit step

