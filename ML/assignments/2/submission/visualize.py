import os
import argparse
import h5py
import matplotlib.pyplot as plt
from sklearn import svm

parser = argparse.ArgumentParser()
parser.add_argument("--data", type = str)
parser.add_argument("--save_data_dir", type = str)

args = parser.parse_args()

def load_h5py(filename):
	with h5py.File(filename, 'r') as hf:
		X = hf['x'][:]
		Y = hf['y'][:]
	return X, Y

X, Y = load_h5py(args.data)

img_name = args.data.split("/")[1].split(".")[0]
img_src = args.save_data_dir + img_name + ".png"

plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap='plasma')
plt.savefig(img_src)
plt.show()