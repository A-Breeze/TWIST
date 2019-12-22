"""Simulate data for the two explanatory variables and response variable based on input parameters"""
from typing import Any

import numpy as np
import numpy.random as npr


# noinspection PyAttributeOutsideInit
class SimulatedDataSet:
    """A data set consisting of two explanatory variables and a response variable"""

    MAX_SEED = 1000

    def __init__(
            self, sample_size: int = 10,
            true_means: Any = np.array([0., 0.]),
            true_sds: Any = np.array([0.5, 0.5]),
            true_corr: float = 0.,
            seed: int = None
    ) -> None:
        """
        :param int sample_size: Number of points in the data set
        :param true_means: True means of the explanatory variables
        :type true_means: 1-D array of length 2
        :param true_sds: True standard deviations of the explanatory variables. Both must be greater than zero
        :type true_sds: 1-D array of length 2
        :param float true_corr: True correlation between the explanatory variables. Must be between -1 and 1 inclusive.
        :param int seed: Random seed to allow reproducibility. If `None` then a seed is generated at random.
        """
        self.set_seed()
        self.generate_explanatory_data(sample_size, true_means, true_sds, true_corr, seed)

    def set_seed(self, seed: int = None) -> None:
        """If no seed is given, then generate a new one"""
        self.seed = seed
        if seed is None:
            self.seed = npr.randint(self.MAX_SEED)

    def generate_explanatory_data(self, sample_size=None, true_means=None, true_sds=None, true_corr=None, seed=None):
        """Generate simulations of the explanatory variables for any inputs that have changed"""
        if sample_size is not None:
            self.sample_size = sample_size
        if true_means is not None:
            self.true_means = true_means
        if true_sds is not None:
            self.true_sds = true_sds
        if true_corr is not None:
            self.true_corr = true_corr
        self.set_seed(seed)

        npr.seed(self.seed)
        self.explanatory_arr = npr.multivariate_normal(
            mean=self.true_means
            , cov=pow(np.array([[self.true_sds[0], self.true_corr], [self.true_corr, self.true_sds[1]]]), 2)
            , size=self.sample_size
        )
