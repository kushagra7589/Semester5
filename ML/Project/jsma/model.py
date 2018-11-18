import numpy as np 
import sklearn
import NeuralNet
from sklearn.model_selection import train_test_split

def make_vector(index, total):
	arr = np.zeros(shape = (total, 1))
	arr[index] = 1.0
	return arr

class RBF_SVM:

	def __init__(self, X, y):
		self.model = sklearn.svm.SVC()
		self.model.fit(X, y)

	def predict(self, X):
		return self.model.decision_function(X)


class Linear_SVM:

	def __init__(self, X, y):
		self.model = sklearn.svm.LinearSVC()
		self.model.fit(X, y)

	def predict(self, X):
		return self.model.decision_function(X)

class Black_Box:

	def __init__(self, model):
		self.model = model
		self.subs_model = 0

	def __create_subsitute_model(self, X_train, X_test, y_test):
		y_train = self.model.predict(X_train)
		X_t, X_val, y_t, y_val = train_test_split(X_train, y_train, test_size=0.1667, random_state=42)
		labels = []
		for y in y_train:
			if y not in labels:
				labels.append(y)
		total_labels = len(labels)
		y_t = np.array([make_vector[j] for j in y_train])
		self.subs_model = NeuralNet.NeuarlNetwork([X_train.shape[1], 100, 50, total_labels], NeuralNet.sigmoid, NeuarlNet.sigmoid)
		correct, weight, bias = self.subs_model.SGD(zip(X_t, y_t), 50, 20, 2.5, zip(X_val, y_val))

		self.subs_model.weight = weight
		self.subs_model.bias = bias

		print "Testing accuracy : {}".format(self.subs_model.evaluate(zip(X_test, y_test)) / float(len(X_test)))

	def predict(self, X):
		return np.array([self.subs_model.feedforward(x) for x in X])