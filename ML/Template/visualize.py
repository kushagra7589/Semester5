import os
import os.path
import argparse
from sklearn.manifold import TSNE
import h5py
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--data", type = str  )
parser.add_argument("--plots_save_dir", type = str  )

args = parser.parse_args()

def load_h5py(filename):
	with h5py.File(filename, 'r') as hf:
		X = hf['X'][:]
		Y = hf['Y'][:]
	return X, Y

X, Y = load_h5py(args.data)

trainData = args.data.split("/")[1].split(".")[0]
# print trainData
dest_dir = '%stsne-%s' % (args.plots_save_dir, trainData)

X_transformed = TSNE(n_components = 2, perplexity = 50, n_iter = 1000).fit_transform(X)

xx = X_transformed[:, 0]
yy = X_transformed[:, 1]

colors = []
for v in range(0, len(Y)):
	for i in range(0, Y[v].shape[0]):
		if Y[v][i] == 1:
			colors.append(i)

plt.figure()
plt.scatter(xx, yy, c=colors)
plt.savefig(dest_dir)