import os
import os.path
import argparse
import h5py

parser = argparse.ArgumentParser()
parser.add_argument("--model_name", type = str  )
parser.add_argument("--weights_path", type = str)
parser.add_argument("--train_data", type = str  )
parser.add_argument("--plots_save_dir", type = str  )

args = parser.parse_args()


# Load the test data
def load_h5py(filename):
	with h5py.File(filename, 'r') as hf:
		X = hf['X'][:]
		Y = hf['Y'][:]
	return X, Y

# Preprocess data and split it

# Train the models

if args.model_name == 'GaussianNB':
	pass
elif args.model_name == 'LogisticRegression':
	pass
elif args.model_name == 'DecisionTreeClassifier':
	# define the grid here

	# do the grid search with k fold cross validation

	# model = DecisionTreeClassifier(  ...  )

	# save the best model and print the results
else:
	raise Exception("Invald Model name")
