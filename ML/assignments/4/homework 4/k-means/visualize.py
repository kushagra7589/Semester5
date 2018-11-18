from sklearn.manifold import TSNE
import dataset
from matplotlib import pyplot as plt
from parser import parseOptions

def get_data(X, Y):
	"""
		A function to fit the data in 2-dimensions using TSNE
	"""
	labels = {}
	next_label = 0
	for i in Y:
		if i not in labels:
			labels[i] = next_label
			next_label += 1

	X_transform = TSNE(n_components = 2).fit_transform(X)

	x_axis = X_transform[:, 0]
	y_axis = X_transform[:, 1]

	label_list = [labels[i] for i in Y]

	return x_axis, y_axis, label_list

def plot_data(x_axis, y_axis, label_list, name, des):
	"""
		A function to plot a scatter graoh for the given data
		k = number of clusters
		name = name of image to save
		des = description of image
	"""
	plt.scatter(x_axis, y_axis, c = label_list)
	plt.colorbar(ticks = range(10))
	plt.savefig('plots/{}_{}.png'.format(name, des))
	plt.show()
