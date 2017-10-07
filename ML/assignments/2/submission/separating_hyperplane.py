import numpy as np
import matplotlib.pyplot as plt

def plot_separating_hyperplane(clf, X, Y):
	w = clf.coef_[0]
	a = -w[0] / w[1]
	xx = np.linspace(-5, 5)
	yy = a * xx - (clf.intercept_[0]) / w[1]

	b = clf.support_vectors_[0]
	yy_down = a * xx + (b[1] - a * b[0])
	b = clf.support_vectors_[-1]
	yy_up = a * xx + (b[1] - a * b[0])

	plt.figure()
	plt.plot(xx, yy, 'k-')
	plt.plot(xx, yy_down, 'k--')
	plt.plot(xx, yy_up, 'k--')

	plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1],
	            s=80, facecolors='none')
	plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired)

	plt.axis('tight')
	plt.show()
