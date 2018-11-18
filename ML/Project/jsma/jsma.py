"""
@author hasankamal

implementation of JSMA attacker
"""

import numpy as np
import matplotlib.pyplot as plt
import heapq

class JSMA:

	def __init__(self):
		pass

	def attack(self, neuralNet, sampleData, sampleLabel, plot_save_filepath):

		# show stats before attack
		oracle = neuralNet.predict(sampleData, sampleLabel)
		print("original output prediction = {}".format(oracle))
		filename = "{}/actual.png".format(plot_save_filepath)
		self.showSample(np.copy(sampleData), filename)

		# attack to produce sampleDataAdversarial
		targetPrediction = np.rint(1 - oracle)
		print("target prediction = {}".format(targetPrediction))
		sampleDataAdversarial, is_misclassified = self.generateAdversarialSample(neuralNet, sampleData[0], targetPrediction[0], plot_save_filepath)

		# show stats after attack
		oracleAdversarial = neuralNet.predict(np.array([sampleDataAdversarial]), sampleLabel) # sampleLabel is not used by .predict() here
		print("attacked output prediction = {}".format(oracleAdversarial))
		filename = "{}/adversarial.png".format(plot_save_filepath)
		self.showSample(np.copy(sampleDataAdversarial), filename)

		# see differences
		self.scaleAndShow(sampleData[0], sampleDataAdversarial, plot_save_filepath)

		return is_misclassified

	def scaleAndShow(self, a, b, path):

		# print("a")
		# print(a)
		# print("b")
		# print(b)
		# print("difference")
		# print(a - b)

		for i in range(a.shape[0]):
			a[i] = int(127.0 * (1.0 + a[i]))

		for i in range(b.shape[0]):
			b[i] = int(127.0 * (1.0 + b[i]))

		filename = "{}/transform.txt".format(path)
		with open(filename, 'w') as f:
			f.write("a after transform:\n")
			f.write(a)
			f.write("\n\nb after transform:\n")
			f.write(b)
			f.write("\n\ndifference after transform:\n")
			f.write(a - b)

		return

	def generateAdversarialSample(self, neuralNet, sampleData, targetPrediction, plot_save_filepath):

		theta = (1.0 / 255.0) * 1.0; # change each pixel by +-5 (in original [0, 255] range)
		
		sampleAdversarial = np.copy(sampleData)
		perturbation = np.zeros(shape=sampleAdversarial.shape[0])
		iteration = 0

		# creating priority queue according to computer vision refined algorithm
		# gamma = np.copy(sampleData).tolist()
		# heapq.heapify(gamma)

		confidence1 = []
		confidence2 = []
		iterations = []

		gamma = {}
		cnt = {}

		while((not self.misclassified(neuralNet, sampleAdversarial, targetPrediction)) and self.perturbation_acceptable(perturbation)):
		# while(not self.misclassified(neuralNet, sampleAdversarial, targetPrediction) and len(gamma) > 0)
			F = self.compute_forward_derivative(neuralNet, sampleAdversarial, targetPrediction)
			S = self.compute_saliency_map(F, targetPrediction, sampleData.shape[0])
			i_max = np.argmax(S)
			check = 2
			
			while(i_max in gamma and check <= S.shape[0]):
				i_max = np.argpartition(S, S.shape[0] - check + 1)[-check]
				check += 1
			else:
				if check > S.shape[0] : 
					print "All pixels perturbed. Limit Reached. Image not misclassifiable. Exitting... "
					break
			
			if i_max not in cnt:
				cnt[i_max] = 0

			cnt[i_max] += theta * 5
			if(cnt[i_max] > 38.0 * theta or sampleAdversarial[i_max] + theta * 5 > 255.0 * theta):
				gamma[i_max] = 0

			sampleAdversarial[i_max] += theta * 5
			perturbation = sampleAdversarial - sampleData

			print("Iteration = {}".format(iteration))
			print("non-zero F has {}".format(np.count_nonzero(F)))
			print("non-zero S has {}".format(np.count_nonzero(S)))
			print("\n")

			iterations.append(iteration)
			prediction = neuralNet.predict(np.array([sampleAdversarial]), np.array([targetPrediction])) # targetPrediction won't be used here
			prediction = prediction[0]
			confidence1.append(prediction[0])
			confidence2.append(prediction[1])

			iteration += 1

			if iteration > 10000:
				print "Could not misclassify in 3000 iterations."
				break

			if iteration % 100 == 0:
				prediction = neuralNet.predict(np.array([sampleAdversarial]), np.array([targetPrediction])) # targetPrediction won't be used here
				prediction = prediction[0]
				print("prediction after {} iterations = {}".format(iteration, prediction))

				print("gamma keys={}".format(len(gamma.keys())))



		plt.plot(iterations, confidence1)
		plt.plot(iterations, confidence2)
		# plt.legend(['train accuracy', 'test accuracy'])
		plt.xlabel("Iterations")
		plt.ylabel('Confidence')
		# if plot_save_filepath is not None:
		plt.savefig("{}/graph.png".format(plot_save_filepath))
		plt.show()

		is_misclassified = False

		if self.misclassified(neuralNet, sampleAdversarial, targetPrediction):
			print("misclassified")
			is_misclassified = True
		if not self.perturbation_acceptable(perturbation):
			print("perturbation not acceptable")
		
		return sampleAdversarial, is_misclassified

	def perturbation_acceptable(self, perturbation):
		# epsilon_max = theta = (1.0 / 255.0) * 30.0; # +-15 infinity norm (in original [0, 255] range)
		# for i in range(perturbation.shape[0]):
		# 	if abs(perturbation[i]) > epsilon_max:
		# 		return False
		return True

	def misclassified(self, neuralNet, sampleAdversarial, targetPrediction):
		prediction = neuralNet.predict(np.array([sampleAdversarial]), np.array([targetPrediction])) # targetPrediction won't be used here
		prediction = prediction[0]
		if (np.argmax(prediction) == np.argmax(targetPrediction)) and (prediction.max() > 0.60):
			return True
		return False

	def compute_forward_derivative(self, neuralNet, sampleAdversarial, targetPrediction):
		epsilon = (1.0 / 255.0) * 0.5

		F = np.zeros(shape=(targetPrediction.shape[0], sampleAdversarial.shape[0]))
		for feature in range(sampleAdversarial.shape[0]):

			sampleStar = np.copy(sampleAdversarial)
			sampleStar[feature] += epsilon

			predictOne = neuralNet.predict(np.array([sampleStar]), np.array([targetPrediction]))
			predictOne = predictOne[0]
			predictTwo = neuralNet.predict(np.array([sampleAdversarial]), np.array([targetPrediction]))
			predictTwo = predictTwo[0]
			F[:, feature] = (predictOne - predictTwo) / epsilon # note that targetPrediction is not actually used here
			
			# if not np.array_equal(predictOne, predictTwo):
			# 	print(predictOne)
			# 	print(predictTwo)
			# 	print("\n")

		return F

	def compute_saliency_map(self, F, targetPrediction, numFeatures):
		print('\tcomputing saliency map')
		S = np.zeros(shape=(numFeatures))
		for i in range(numFeatures):

			t = np.argmax(targetPrediction)

			total_summation = np.sum(F[:, i])
			total_summation -= F[t, i]

			if F[t, i] < 0 or total_summation > 0:
				S[i] = 0.0
			else:
				S[i] = F[t, i] * (-1 * total_summation)
		print('\tended computing saliency map')
		return S

	def showSample(self, sample, filename):

		# denormalize features
		for i in range(sample.shape[0]):
			sample[i] = 127.0 * (1.0 + sample[i])

		# display sample
		sample = np.reshape(sample, (28, -1))
		plt.imshow(sample, cmap='gray')
		plt.savefig(filename)
		plt.show()