# Implementation of Logistic Regression Classifier
# Author: Ramzi Abdoch

# Numpy
import numpy as np

class LRClassifier():

	# X = examples
	# W = weights (from scikit-learn)
	# b = bias

	def classify(self, X, W, b):

		A = np.dot(X, W.T) + b
		y_hat = np.argmax(A, axis=1)

		Z = np.sum(A, axis=1)
		self.P = A / Z

		return y_hat
