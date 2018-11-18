import numpy as np 

def gaussian_kernel(x, y):
	sigma = 0.7
	numerator = np.sum((x - y)**2)
	denominator = 2 * (sigma ** 2)
	return np.exp(-numerator/denominator)

def linear_kernel(x, y):
	return np.dot(x, y)

def generalised_kernel(X, Y, K):
	matrix = np.zeros((X.shape[0], Y.shape[0]))
	for i, x, in enumerate(X):
		for j, y in enumerate(Y):
			matrix[i][j] = K(x, y)
	return matrix


