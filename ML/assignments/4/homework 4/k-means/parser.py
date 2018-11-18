import argparse

def parseOptions():
	parser = argparse.ArgumentParser()
	parser.add_argument('--data', '-d', type=str, help="Provide the destination of the datafile to be read")
	parser.add_argument('--col', '-c', type=int, help="Provide the column number of the column containing label", default = 0)
	parser.add_argument('--sep', '-s', type=str, help="Provide the column separator of the text files", default=" ")
	parser.add_argument("-k", type=int, help="Provide the value of k for k-means")

	args = parser.parse_args()

	filename = args.data
	separator = args.sep
	column_no = args.col
	k = args.k

	return filename, column_no, separator, k