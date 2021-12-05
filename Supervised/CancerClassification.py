import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split

breast = datasets.load_breast_cancer()
X = breast.data
y = breast.target

acc_list = []
misclassifications = 0
tumor_type = list(breast.target_names)

# Train and print model results
for i in range(50):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
    model = Perceptron(eta0=0.01, random_state=1)
    model.fit(X_train, y_train)

    cur_acc = model.score(X_test, y_test)
    acc_list.append(cur_acc)
    
    prediction = model.predict(X_test)
    if tumor_type[prediction[i]] != tumor_type[y_test[i]]:
        misclassifications += 1

    print(f"Prediction:\t{tumor_type[prediction[i]].ljust(10)}"\
          f"\tActual: {tumor_type[y_test[i]].ljust(10)}"\
          f"\tAccuracy: {str(round(cur_acc * 100, 2)).ljust(5)}%")

avg_acc = round(sum(acc_list) / len(acc_list), 2)

print(f"\nAverage Accuracy: {avg_acc * 100}%")
print(f"Misclassifications: {misclassifications}")

# Plot classifications
features = breast.data.T
plot_x = features[0]
plot_y = features[1]
area = 100 + features[3]
plt.scatter(plot_x, plot_y, alpha=0.2, s=area, c=breast.target, cmap="viridis")
plt.xlabel(breast.feature_names[0])
plt.ylabel(breast.feature_names[1])

