import numpy as np 
import nn

def gridSearch(training_data = None, test_data = None, learning_rate = [3.0], batch_size = [50]):
	max_correct, best_weights, best_bias = 0, 0, 0
	for eta in learning_rate:
		for bs in batch_size:
			net = nn.NeuralNetwork([784, 100, 50, 10], nn.sigmoid(), nn.sigmoid())
			correct, weights, bias = net.SGD(training_data, 30, bs, eta, test_data)
			if correct > max_correct:
				best_weights = weights
				best_bias = bias
				max_correct = correct
	print "The maximum training accuracy is : {0}".format(((max_correct * 1.0) / len(test_data)) * 100.0)
	
	net.weights = best_weights
	net.biases = best_bias
	return net
