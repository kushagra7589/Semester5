import os
import argparse
import h5py
import matplotlib.pyplot as plt
from sklearn import svm
import numpy as np
import kernels
from functools import partial

parser = argparse.ArgumentParser()
parser.add_argument("--data", type = str)
parser.add_argument("--save_data_dir", type = str)
parser.add_argument("--kernel", type = str)
parser.add_argument("--rem_out", type = bool)
args = parser.parse_args()

def load_h5py(filename):
	with h5py.File(filename, 'r') as hf:
		X = hf['x'][:]
		Y = hf['y'][:]
	return X, Y

def remove_outlier(clf, X, Y):
	A = clf.decision_function(X)
	X_new, Y_new = [], []
	for index, i in enumerate(A):
		if i * Y[index] >= 0 :
			X_new.append(X[index])
			Y_new.append(Y[index])
	return np.array(X_new), np.array(Y_new)

X, Y = load_h5py(args.data)

img_name = args.data.split("/")[1].split(".")[0]
	
img_src = "%sdecision-bounary-%s.png" % (args.save_data_dir, img_name)
if args.rem_out:
	img_src = "%sdecision-bounary-rem-out%s.png" % (args.save_data_dir, img_name)

ker = 0

if args.kernel == 'rbf':
	ker = kernels.gaussian_kernel
elif args.kernel == 'linear':
	ker = kernels.linear_kernel
else:
	print "This kernel is not supported"

my_kernel = partial(kernels.generalised_kernel, K = ker)

clt = svm.SVC(kernel = my_kernel)

for i in range(Y.shape[0]):
	if Y[i] == 0:
		Y[i] = -1

clt.fit(X, Y)

print args.rem_out

if args.rem_out:
	print "Outliers have been removed"
	X, Y = remove_outlier(clt, X, Y)

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))

Z = clt.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure()
plt.contourf(xx, yy, Z, alpha = 0.4)
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap='plasma', s=20)
plt.savefig(img_src)
plt.show()