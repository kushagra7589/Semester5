import nn
import model_selection
import load_data_subset
import load_data_complete
import numpy as np 
from sklearn.preprocessing import MinMaxScaler, normalize
from sklearn.model_selection import train_test_split

X_train, y_train = load_data_complete.load_mnist()
X_test, y_test = load_data_complete.load_mnist("testing")

# X_train, y_train, X_test, y_test = load_data_subset.load_data()

def scale(X_train, X_test):

	X_train = np.multiply(X_train, 255.0)
	X_test = np.multiply(X_test, 255.0)

	X_train = X_train.reshape((X_train.shape[0], X_train.shape[1]))
	X_test = X_test.reshape((X_test.shape[0], X_test.shape[1]))

	scaler = MinMaxScaler((-1, 1))

	X_train = scaler.fit_transform(X_train)
	X_test = scaler.transform(X_test)

	# X_train = normalize(X_train)
	# X_test = normalize(X_test)


	X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
	X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

	return X_train, X_test


X_t, X_val, y_t, y_val = train_test_split(X_train, y_train, test_size=0.1667, random_state=42)

train = zip(X_t, y_t)

y_val = np.array([np.argmax(y).reshape(1,) for y in y_val]) 

validate = zip (X_val, y_val)
test = zip(X_test, y_test)

# net = nn.NeuralNetwork([784, 100, 50, 10], nn.sigmoid, nn.sigmoid)
# net.SGD(train, 10, 50, 3.0, test)

lr = [2.0, 3.0, 5.0]

batch_size = [20, 30, 50]

best_model = model_selection.gridSearch(training_data = train, test_data = validate, learning_rate = lr, batch_size = batch_size)

print "Best weight :"
print best_model.weights
print
print "Best bias : "
print best_model.biases

print "Test accuracy : {0} / {1}".format(best_model.evaluate(test), len(test))

