import numpy as np 
import matplotlib as plt


class JSMA:
	def __init__(self, model, epsilon, max_iter):
		self.model = model
		self.epsilon = epsilon
		self.max_iter = max_iter

	def __denormalize(self, X):
		"""
			The data used by model is normalized to range [-1, 1].
			This function denormalizes the data to range [0, 255].
		"""
		return 127.0 * (1.0 + X)

	def __showStats(self, X, directory, name):
		"""
			This function prints the confidence of the model in determining the label for X.
		"""
		predictions = self.model.predict(X)[0]
		print "Original Output Prediction = {}".format(predictions)
		self.__showSample(np.copy(X), "{}/{}".format(directory, name))
		return predictions

	def __showSample(self, X, filename):
		"""
			This function displays the image represented by X.
		"""

		# denormalize the data
		X = self.__denormalize(X)

		# plot the data
		X = np.reshape(X, (28, -1))
		plt.figure()
		plt.imshow(X, cmap = 'gray')
		plt.savefig(filename)

	def __misclassified(self, advX, target):
		"""
			This function checks whether the adversarial example advX has been misclassified to target class.
		"""
		prediction = self.model.predict(np.array([advX]))[0]
		if np.argmax(prediction) == np.argmax(target) and prediction.max() > 0.60:
			return True
		return False

	def __compute_forward_derivative(self, advX, target):
		"""
			This function computes the derivative for every feature in advX
		"""

		predict_base = self.model.predict(np.array([advX]))[0]
		F = np.zeros(shape = (targe.shape[0], advX.shape[0]))
		
		for feature in range(advX.shape[0]):
			tempX = np.copy(advX)
			tempX[feature] += self.epsilon

			predict_delta = self.model.predict(np.array([tempX]))[0]
			F[:, feature] = (predict_delta - predict_base) / self.epsilon

		return F

	def __compute_salience_map(self, F, target, numFeatures):
		"""
			This function computes the saliency map for JSMA attack
		"""

		print "\tComputing Saliency Map"

		S = np.zeros(shape = (numFeatures))

		t = np.argmax(target)

		total_summation = np.sum(F, axis = 0)
		total_summation -= F[t, :]

		S  = F[t, :] * (-1.0 * total_summation)
		S[np.where(F[t, :] < 0 or total_summation > 0)] = 0.0

		print "\tEnded Computed Saliency Map"
		return S

	def __generateAdversarialSample(self, X, target, directory):
		"""
			This function tries to perturbe the example X such that the model classifies as target
		"""

		# define a single unit of perturbation in the normalized space
		unit = (1.0 / 255.0) * 1.0

		# define total perturbation done on one pixel in one iteration
		theta = 5 * unit

		# start with X and try to misclassify it
		adversarialX = np.copy(X)

		# a counter to count the iterations
		iteration = 0

		confidence = [[], []]
		iterations = []
		gamma = {}
		cnt = {}


		while(not self.__misclassified(adversarialX, target)):
			F = self.__compute_forward_derivative(adversarialX, target)
			S = self.__compute_salience_map(F, target, X.shape[0])

			i_max = np.argmax(S)
			check = 2

			while(i_max in gamma and check <= S.shape[0]):
				i_max = np.argpartition(S, S.shape[0] - check + 1)[-check]
				check += 1
			else:
				if check > S.shape[0] : 
					print "All pixels perturbed. Limit Reached. Image not misclassified."
					break

			if i_max not in cnt:
				cnt[i_max] = 0.0

			cnt[i_max] += theta
			if(cnt[i_max] > 39.0 * unit or adversarialX[i_max] + theta > 255.0 * unit):
				gamma[i_max] = 0

			adversarialX[i_max] += theta

			print "Iteration = {}\n".format(iteration)

			iterations.append(iteration)
			pred = self.model.predict(np.array[adversarialX])[0]
			confidence[0].append(pred[0])
			confidence[1].append(pred[1])

			iteration += 1

			if iteration > self.max_iter:
				print "Could not misclassify in {} iterations".format(self.max_iter)
				break

			if iteration % 100 == 0:
				pred = self.model.predict(np.array([adversarialX]))[0]
				print "Prediction after {} iterations = {}".format(iteration, pred)

		plt.figure()
		plt.plot(iterations, confidence[0])
		plt.plot(iterations, confidence[1])
		plt.xlabel('Iterations')
		plt.ylable('Confidence')
		plt.savefig("{}/graph.png".format(directory))

		is_misclassified = False

		if self.__misclassified(adversarialX, target):
			print "Misclassified!"
			is_misclassified = True

		return adversarialX, is_misclassified


	def attack(self, X, y, directory):
		"""
			API that gives an analysis of the given attack
			X : Sample Data instance (single instance)
			y: Correct Label of the given data instance
			target: Target Label for misclassification
			directory: directory in which all paths are to be stored 
		"""

		# Initial stats
		prediction = self.__showStats(X, directory, "Actual.png")

		# Getting the target class
		targetClass = np.rint(1 - prediction)

		# creating the adversarial example
		adversarialX, is_misclassified = self.__generateAdversarialSample(X[0], targetClass, directory)

		# Stats after Adversarial Attack
		adv_predictions = self.__showStats(adversarialX, directory, "Adversarial.png")

		return is_misclassified
