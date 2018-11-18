import h5py
import argparse
import numpy as np
import os
import struct
from array import array as pyarray
from sklearn.model_selection import train_test_split


def load_h5py(filename):
	with h5py.File(filename, 'r') as hf:
		Y = hf['Y'][:]
		X = hf['X'][:]
	return X, Y

def load_data():

	X, Y = load_h5py("dataset_partA.h5")

	labels = []

	for i in Y:
		if i not in labels:
			labels.append(i)

	print "Number of data points : {0}".format(Y.shape[0])
	print "Number of classes {0}".format(len(labels))

	print "Output as vectorized result (i.e 2 == [0, 0, 1, 0, 0, 0, 0, 0, 0, 0])"

	X = np.array([np.divide(np.reshape(x, (784, 1)), 255.0) for x in X])

	X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.33, random_state=33)

	Y_train = np.array([make_vector(j) for j in Y_train])

	# training_data = zip(X_train, Y_train)
	# testing_data = zip(X_test, Y_test)

	return X_train, Y_train, X_test, Y_test

def make_vector(index):
	arr = np.zeros((10, 1))
	arr[index] = 1.0
	return arr

