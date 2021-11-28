import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    """ Simple Logistic Sigmoid Function """
    return 1.0 / (1.0 + np.exp(-z))

if __name__ == "__main__":
    z = np.arange(-7, 7, 0.1)
    phi_z = sigmoid(z)
    # Plot function
    plt.plot(z, phi_z)
    plt.axvline(0.0, color="k")
    plt.ylim(-0.1, 1.1)
    plt.xlabel("z")
    plt.ylabel("$\phi{z}$")
    # y axis ticks and gridline
    plt.yticks([0.0, 0.5, 1.0])
    ax = plt.gca()
    ax.yaxis.grid(True)
    plt.show()