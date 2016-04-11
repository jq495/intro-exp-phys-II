import numpy as np
from base_distribution import BaseDistribution

class Dist_jq495(BaseDistribution):
	def __init__(self):
		self.f_max = 10
		self.x_min = -10
		self.x_max = 10


	def pdf(self, x):
		"""This is your PDF"""
		return np.abs(5*x**3)

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.012124

	def std(self):
		"""This is the standard deviation of the pdf"""
		return 6.051246
