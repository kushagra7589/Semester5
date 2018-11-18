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

C = [i[0] for i in Y]

X_new = TSNE(n_components = 2, perplexity = 40, n_iter = 1000).fit_transform(X)

# print(X_new)
# print
print(type(Y))
# print
# print C



xx = X_new[:, 0]
yy = X_new[:, 1]

y1 = []
for v in range(0, len(Y)):
	for i in range(0, Y[v].shape[0]):
		if Y[v][i] == 1:
			y1.append(i)


# plt.plot(xx, yy, 'o')

# plt.xlabel('time (s)')
# plt.ylabel('voltage (mV)')
# plt.title('About as simple as it gets, folks')
# # plt.axis([-50, 50, -1, 2])
# plt.grid(True)

# # dest_dir = "{}test.png".format({args.plots_save_dir[0]})

# plt.savefig("test.png")
# plt.show()
plt.scatter(xx, yy, c=y1) 	
# plt.colorbar(ticks=range(10))
# plt.clim(-0.5, 9.5)
plt.show()
# print(X,Y)