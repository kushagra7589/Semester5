import numpy as np

def read_data(filename, label_col, separator):
	f = open(filename, "r")
	L = f.readlines()
	X = []
	Y = []
	cnt = 1
	for i in L:
		i = i.strip()
		if i == "":
			break
		i = i.split(separator)
		x = i[:label_col] + i[label_col + 1:]
		cnt += 1
		x = map(float, x)
		y = i[label_col]
		X.append(x)
		Y.append(y)
	X = np.array(X)
	Y = np.array(Y)
	return X, Y