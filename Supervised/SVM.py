import sklearn
from sklearn import datasets, svm, metrics
from sklearn.neighbors import KNeighborsClassifier

cancer_data = datasets.load_breast_cancer()

# x & y is for supervised learning 
x = cancer_data.data
y = cancer_data.target

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)

# Classes from dataset (Cancer_data)
classes = ["malignant", "benign"]

# Support Vector Classifier
model_svm = svm.SVC(kernel="linear", C=3)
model_svm.fit(x_train, y_train)

svm_prediction = model_svm.predict(x_test)
svm_accuracy = str(round(metrics.accuracy_score(y_test, svm_prediction), 2) * 100) + "%"
print(svm_accuracy)

model_knn = KNeighborsClassifier(n_neighbors=9)
model_knn.fit(x_train, y_train)

knn_prediction = model_knn.predict(x_test)
knn_accuracy = str(round(model_knn.score(x_test, y_test), 2) * 100) + "%"
print(knn_accuracy)
