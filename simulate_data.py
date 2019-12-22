"""Simulate data for the two explanatory variables X_1, X_2"""

import numpy as np
import numpy.random as npr

sample_size = 10
mean = np.array([0., 0.])
cov = np.array([[0.5, 0.], [0., 0.5]])

npr.seed(123)
explanatory_arr = npr.multivariate_normal(mean=mean, cov=cov, size=sample_size)
