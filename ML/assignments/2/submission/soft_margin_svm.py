import os
import argparse
import h5py
import matplotlib.pyplot as plt
from sklearn import svm
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, KFold
import confusionMatrix
import separating_hyperplane

parser = argparse.ArgumentParser()
parser.add_argument("--data", type = str)
parser.add_argument("--classifier", type = str)
parser.add_argument("--kernel", type = str)
parser.add_argument("--gs", type = bool)
parser.add_argument("--save_data_dir", type = str)

args = parser.parse_args()

def load_h5py(filename):
	"""
	Function used to read .h5 return X, Y such that X is the design matrix and Y is the label vector
	"""
	with h5py.File(filename, 'r') as hf:
		if "part" in filename:
			X = hf['X'][:]
			Y = hf['Y'][:]
		else:
			X = hf['x'][:]
			Y = hf['y'][:]			
	return X, Y

X, Y = load_h5py(args.data)

img_name = args.data.split("/")[1].split(".")[0]
img_src = args.save_data_dir + img_name + "-confusion-matrix1.png"

def calc_theta(clf, kernel, z):
	"""
	Calculate the distance of z from the decision boundary
	"""
	if kernel == 'linear':
		return np.dot(clf.coef_, z) + clf.intercept_					
	elif kernel == 'rbf':
		a = 0
		for j, sv in enumerate(clf.support_vectors_):
			a += clf.dual_coef_[0][j] * np.dot(sv, z)
		a += clf.intercept_
		return a
	else:
		print("Does not accept %s as kernel option. Only rbf and linear kernels are allowed" % (kernel))

def my_predict(clf, option,  X, Y, Z, classes, kernel):
	"""
	A custom predict function that uses svm as a binary classifier and performs ovr/ovo multiclass labelling
	"""
	if option == 'ovr':
		result = np.zeros((Z.shape[0], len(classes)))
		for k, i in enumerate(classes):			
			# creating a new label vector such that label i is +ve, and others are -ve.
			customY = np.zeros(Y.shape[0])
			for index, y in enumerate(Y):
				if y == i:
					customY[index] = 1.0
				else:
					customY[index] = 0.0

			# fit the learning algorithm to X, customY
			clf.fit(X, customY)

			# predict the label for unseen sample z
			for zi, z in enumerate(Z):
				result[zi][k] = calc_theta(clf, kernel, z) 

		ans = np.zeros(Z.shape[0], dtype=int)

		# predicted value for z = arg max(i) (d in distance(z))
		for ri, res in enumerate(result):
			d = -1e14
			a = 0
			for index, i in enumerate(res):
				if i > d:
					d = i
					a = index
			ans[ri] = classes[a]
		return ans

	elif option == 'ovo':
		k = len(classes)
		result = np.zeros((Z.shape[0], (k * (k - 1))/2))

		base = 0
		for i in range(k):
			for j in range(i + 1, k):
				tempX = []
				customY = []
				labelA, labelB = classes[i], classes[j]
				for index, y in enumerate(Y):
					if y == labelA or y == labelB:
						tempX.append(X[index])
						if(y == labelA):
							customY.append(1)
						else:
							customY.append(0)

				customX = np.array(tempX)

				clf.fit(customX, customY)

				for zi, z in enumerate(Z):
					ans = calc_theta(clf, kernel, z)
					if ans >= 0 :
						result[zi][base + j - i - 1] = labelA
					else :
						result[zi][base + j - i - 1] = labelB
			base += k - 1 - i

		ans = np.zeros(Z.shape[0])

		for ri, res in enumerate(result):
			cnt = {}
			for i in res:
				if i not in cnt :
					cnt[i] = 0
				cnt[i] += 1

			m = -1
			p = -1
			for i in cnt:
				if cnt[i] > m:
					p = i
					m = cnt[i]
			ans[ri] = p
		return ans

def calc_score(X, Y, kernel, c,  classifier, classes, g = None, splits = 3):
	kf = KFold(n_splits = splits)
	clf = svm.SVC(kernel = kernel, C = c, gamma = g)	
	cnt, score = 0, 0
	for train_index, test_index in kf.split(X):
		X_train, X_test = X[train_index], X[test_index]
		y_train, y_test = Y[train_index], Y[test_index]
		prediction = my_predict(clf, classifier, X_train, y_train, X_test, classes, kernel)
		cnt += 1.0
		score += accuracy_score(y_test, prediction, normalize = True)
	score /= cnt
	return score

def gridSearch(classifier, classes, parameters, X, Y, splits = 3):
	max_score = 0.0
	best_params = {}
	for c in parameters['C']:
		if 'gamma' in parameters:
			for g in parameters['gamma']:
				score = calc_score(X, Y, 'rbf', c, classifier, classes, g, splits)
				if score > max_score:
					max_score = score
					best_params['C'] = c
					best_params['gamma'] = g
		else:
			score = calc_score(X, Y, 'linear', c, classifier, classes, splits)
			if score > max_score:
				max_score = score
				best_params['C'] = c

	return best_params

if __name__ == "__main__":		
	ker = args.kernel
	classifier = args.classifier

	classes = []

	# split the data into train and test to test the accuracy
	X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42, shuffle=True)

	# to adjust to the data format of these files
	if "part" in args.data:
		y_train = np.argmax(y_train, axis = 1)
		y_test = np.argmax(y_test, axis = 1)

	# finding the distinct classes/labels
	for i in y_train:
		if i not in classes:
			classes.append(i)

	parameters = {'C' : (0.1, 0.3, 0.5)}
	if(args.kernel == 'rbf'):
		parameters['gamma'] = (0.5, 1.0)


	best_params = {}
	if args.gs:
		best_params = gridSearch(classifier, classes, parameters, X_train, y_train)
	else:
		best_params = {'C' : 0.3, 'gamma' : 0.5}

	clf = svm.SVC(kernel = ker, C = best_params['C'])
	if ker == 'rbf':
		clf.set_params(**{'gamma': best_params['gamma']})
	prediction = my_predict(clf, classifier, X_train, y_train, X_test, classes, ker)

	print prediction

	print "The best parameters after grid search are : ",
	print best_params

	print "The accuracy for ovr is : ", 
	print(accuracy_score(y_test, prediction, normalize=True) * 100)


	cnf_matrix = confusionMatrix.confusion_matrix(prediction, y_test)

	print (cnf_matrix)

	# cnf_matrix = confusion_matrix(y_test, prediction)	

	confusionMatrix.plot_confusion_matrix(cnf_matrix, classes=classes, normalize=True,
                      title='Normalized confusion matrix', img_name=img_src)
	if ker == 'linear':
		separating_hyperplane.plot_separating_hyperplane(clf, X_train, y_train)