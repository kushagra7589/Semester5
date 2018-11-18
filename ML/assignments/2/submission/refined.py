from sklearn import svm, preprocessing
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import json
import numpy as np
from sklearn.manifold import TSNE
from sklearn.decomposition import TruncatedSVD
import matplotlib.pyplot as plt
from sklearn.multiclass import OneVsOneClassifier

with open('data/train_kaggle.json') as train_file:
	train_data = json.load(train_file)

with open('data/test_kaggle.json') as test_file:
	test_data = json.load(test_file)

X, y, Z = [], [], []

for i in train_data:
	s = ""
	for j in i['X']:
		s += str(j) + " "
	X.append(s[:len(s) - 1])
	y.append(i['Y'])

for i in test_data:
	s = ""
	for j in i['X']:
		s += str(j) + " "
	Z.append(s[:len(s) - 1])

X1, y1, Z1 = np.array(X), np.array(y), np.array(Z)

def custom_tokenizer(s):
	return s.split()

#vectorize the data since the number of features are not a constant (using tfidvectorizer)
vect = TfidfVectorizer(ngram_range=(0, 3), tokenizer = custom_tokenizer)
X_vect = vect.fit_transform(X1)

# X_transformed = TruncatedSVD(n_components=20, n_iter=10).fit_transform(X_vect)
# xx = X_transformed[:, 0]
# yy = X_transformed[:, 1]


#uncomment to include parameters for grid search
parameters = {'C' : [i for i in np.arange(0.25, 0.501, 0.005)]}

# fit the data using linear SVC
clf = svm.LinearSVC(random_state = 0)

# uncomment for using clf without grid search
# clf.fit(X_vect, y1)


# uncomment to use grid search
gsf = GridSearchCV(clf, parameters, refit = True)
ovo = OneVsOneClassifier(gsf)
ovo.fit(X_vect, y1)

Z_vect = vect.transform(Z1)

# uncomment to reduce the dimensionality for visualisation
# Z_transformed = TruncatedSVD(n_components=20, n_iter=10).fit_transform(Z_vect)
# xx = X_transformed[:, 0]
# yy = X_transformed[:, 1]

res = ovo.predict(Z_vect)

# print "Id,Expected"

# for index, i in enumerate(res):
# 	print str(index + 1) + "," + str(i)

print gsf.best_params_

# uncomment to plot the data
# plt.figure()
# plt.scatter(xx, yy, c=res, cmap='plasma')
# plt.savefig("plots/kaggle_res.png")
