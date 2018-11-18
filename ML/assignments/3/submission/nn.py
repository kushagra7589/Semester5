import numpy as np
import random
import bigfloat
import matplotlib.pyplot as plt

class NeuralNetwork(object):

	def __init__(self, layers, last_layer_activation, hidden_layer_activation):
		#layers are the number of neurons in each layer of the multi-neuron perceptron
		self.N  = len(layers)
		self.layers = layers
		# w_kj = wieght from jth neuron in layer l - 1 to the kth neuron in layer l
		self.weights = [np.random.randn(k, j) for j, k in zip(layers[:-1], layers[1:])]
		# since there is no bias for the first layer, we skip it for our biases.
		self.biases = [np.random.randn(i, 1) for i in layers[1:]]
		self.last_layer_activation = last_layer_activation
		self.hidden_layer_activation = hidden_layer_activation

	def feedforward(self, a):
		"""Return the output of the network if ``a`` is input."""
		for b, w in zip(self.biases, self.weights):
			if np.array_equal(b, self.biases[-1]):
				a = self.last_layer_activation.forward(np.dot(w, a)+b)
			else:
				a = self.hidden_layer_activation.forward(np.dot(w, a)+b)
			# a = sigmoid(np.dot(w, a)+b)
		return a

	def SGD(self, training_data, epochs, mini_batch_size, eta,
			test_data=None):
		if test_data: 
			n_test = len(test_data)
		n = len(training_data)
		max_correct = 0
		best_weights = 0
		best_bias = 0
		ep = []
		res = []
		for j in range(epochs):
			random.shuffle(training_data)
			mini_batches = [
				training_data[k:k+mini_batch_size]
				for k in range(0, n, mini_batch_size)]
			for mini_batch in mini_batches:
				self.update_mini_batch(mini_batch, eta)
			if test_data:
				correct = self.evaluate(test_data)
				if correct > max_correct:
					max_correct = correct
					best_bias = self.biases
					best_weights = self.weights
				print "Epoch {0}: {1} / {2}".format(
					j, correct, n_test)
				ep.append(j)
				res.append(correct)
			else:
				print "Epoch {0} complete".format(j)
		if test_data:
			# fig = plt.figure()
			plt.plot(ep, res)
			plt.xlabel('Epoch')
			plt.ylabel('Number of correct predictions')
			plt.title('eta-{0} bs-{1}'.format(eta, mini_batch_size))
			plt.savefig('plots/eta-{0}_bs-{1}-{2}.png'.format(eta, mini_batch_size, "small"))
			plt.gcf().clear()
			# plt.show()
			print "The maximum accuracy is : {0}".format(((max_correct * 1.0) / n_test) * 100.0)
			return correct, best_weights, best_bias
		else:
			return 0, 0, 0

	def update_mini_batch(self, mini_batch, eta):
		nabla_b = [np.zeros(b.shape) for b in self.biases]
		nabla_w = [np.zeros(w.shape) for w in self.weights]
		X =[]
		Y = []

		for x, y in mini_batch:
			X.append(x.transpose())
			Y.append(y.transpose())

		X = np.array(X)
		Y = np.array(Y)
		X = X[:, 0, :]
		# print Y.shape
		Y = Y[:, 0, :]
		X = X.transpose()
		Y = Y.transpose()

		delta_nabla_b, delta_nabla_w = self.backprop(X, Y)
		nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
		nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]

		self.weights = [w-(eta/len(mini_batch))*nw
						for w, nw in zip(self.weights, nabla_w)]
		self.biases = [b-(eta/len(mini_batch))*nb
					   for b, nb in zip(self.biases, nabla_b)]



	def backprop(self,X, Y):
		mini_batch_size = X.shape[1]

		# initially the activation is same as the input matrix
		A = X
		Activations = [X]
		Zs = []

		#feed-forward
		for bias, weight in zip(self.biases, self.weights):
			B = np.array([bias, ] * mini_batch_size).transpose()
			W = weight
			Z = np.matmul(W, A) + B
			Z = Z[0, :, :]
			Zs.append(Z)
			if np.array_equal(bias, self.biases[-1]):
				A = self.last_layer_activation.forward(Z)
			else:
				A = self.hidden_layer_activation.forward(Z)
			Activations.append(A)

		# calculating delta according to BP1 (for cross-entropy cost function)
		Delta = (Activations[-1] - Y)
		add_B = [np.zeros(b.shape) for b in self.biases]
		add_W = [np.zeros(w.shape) for w in self.weights]

		add_B[-1] = np.sum(Delta, axis = 1).reshape(self.biases[-1].shape)
		add_W[-1] = np.dot(Delta, Activations[-2].transpose())

		for l in range(2, self.N):
			Z = Zs[-l]
			SP = self.hidden_layer_activation.prime(Z)
			Delta = np.dot(self.weights[-l + 1].transpose(), Delta) * SP
			add_B[-l] = np.sum(Delta, axis = 1).reshape(self.biases[-l].shape)
			add_W[-l] = np.dot(Delta, Activations[-l - 1].transpose())
		return add_B, add_W

	def evaluate(self, test_data):
		test_results = [(np.argmax(self.feedforward(x)), y)
						for (x, y) in test_data]
		return sum(int(x == y) for (x, y) in test_results)



class sigmoid:
	def forward(self, z):
		return .5 * (1 + np.tanh(.5 * z))

	def prime(self, z):
		return self.forward(z) * (1 - self.forward(z))

class softmax:
	def forward(self, z):
		a = np.exp(z)
		s = np.sum(a, axis = 0)
		return np.divide(a, s)

	def prime(self, z):
		return forward(z)

class ReLu:
	def forward(self, z):
		return np.maximum(z, 0.0, z)

	def prime(self, z):
		return z > 0


