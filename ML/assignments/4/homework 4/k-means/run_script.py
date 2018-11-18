import visualize
import kmeans
import analysis
import dataset
import csv

F = ['data/column_3C.dat', 'data/iris.data', 'data/seeds_dataset.txt', 'data/segmentation.data']
S = [' ', ',', ' ', ',']
C = [6, 4, 7, 0]
A = [3, 3, 3, 7]

FCS = zip(F, C, S, A)

for i in FCS:
	X, Y = dataset.read_data(i[0], i[1], i[2])
	
	# plot the actual data 
	x, y, labels = visualize.get_data(X, Y)
	visualize.plot_data(x, y, labels, i[0].split("/")[1], "actual")
	K = [2, i[3], 12]
	
	for k in K:
		pred, data_to_plot = kmeans.cluster(X, k)
		visualize.plot_data(x, y, pred, i[0].split("/")[1], "k={}_predicted".format(k))

		# store quantitative measures for k-means
		ari = analysis.ARI(labels, pred)
		nmi = analysis.NMI(labels, pred)
		ami = analysis.AMI(labels, pred)

		# write the quantitative measures in file
		with open("plots/plot_data/k={}_{}".format(k, i[0].split("/")[1]), 'w') as writeFile:
			writeFile.write("{}, {}, {}".format(ari, nmi, ami))

		# store iteration vs obj_function values
		with open("plots/plot_data/{}_{}.csv".format(i[0].split("/")[1], k), 'w') as writeFile:
			writer = csv.writer(writeFile)
			writer.writerows(data_to_plot)

		
