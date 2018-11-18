import dataset
import parser
import numpy as np
import visualize
import csv
import analysis


def obj_function(X, pred, centers):
	"""
		The objective function for the k-means algorithm that gives the distances for each data point from it's centroid.
	"""
	return np.sum(np.array([np.square(np.linalg.norm(X[i] - centers[pred[i]])) for i in range(X.shape[0])]))

def cluster(X, k = 2):
	# choosing random centers
	num_of_instances = X.shape[0]
	indices = np.random.permutation(num_of_instances)[:k]
	centers = X[indices]

	# initialising variables
	val = np.float64(-1.0)
	iteration = 0
	iterations = []
	results = []

	# repeat until convergence
	while True:	
		# assign labels according to the current centers
		pred = np.zeros(X.shape[0])
		for i, x in enumerate(X):
			# setting initial distance as infinity
			min_dist = np.float64(1e12)

			# iterate over all cluster centers to find the nearest one
			for j, c in enumerate(centers):
				# calculate distance of point x from cluster center c
				dist = 	np.linalg.norm(x - c)

				# update the label for x according to the nearest cluster center
				if(dist < min_dist):
					min_dist = dist
					pred[i] = j

		# calculate the objective function
		prev = val
		val = obj_function(X, pred, centers)

		# create iteration vs objective function data
		iterations.append(iteration)
		results.append(val)

		# increment the iteration counter
		iteration += 1

		# check if data has converged
		if(abs(val - prev) < 0.000001):
			break

		# calculate mean of clusters
		new_centers = np.array([X[np.where(pred == i)[0]].mean(0) for i in range(k)])
		
		# assign new centers
		centers = np.array(new_centers)

	data_to_plot = zip(iterations, results)

	return pred, data_to_plot

