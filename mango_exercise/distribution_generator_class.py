from numpy import random


class DistributionGenerator:
    """
    Generate random data within a given distribution
    """

    def __init__(self, num_samples, mean=0, sd=1, interval=1, n=1, p=0.5):
        """

        :param num_samples: Int The number of samples to be returned
        :param mean: The Mean value for a normal distribution
        :param sd: The Standard Deviation for a normal distribution
        :param interval: The Interval for a poisson distribution
        :param n: The number of samples for a binomial distribution
        :param p: The probability for a binomial distribution
        """
        self.num_samples = num_samples
        self.mean = mean
        self.sd = sd
        self.interval = interval
        self.n = n
        self.p = p

        self.data = None

    def normal(self):
        """ Produce an array of values in a normal distribution

        :return: ndarray
        """
        self.data = random.normal(size=self.num_samples, loc=self.mean, scale=self.sd)
        return self.data

    def poisson(self):
        """ Produce an array of values in a poisson distribution

        :return: ndarray
        """
        self.data = random.poisson(size=self.num_samples, lam=self.interval)
        return self.data

    def binomial(self):
        """ Produce an array of values in a binomial distribution

        :return: ndarray
        """
        self.data = random.binomial(size=self.num_samples, n=self.n, p=self.p)
        return self.data

    def summarise(self):
        """ Print summary statistics about the last dataset created

        :return:
        """
        print("Min: " + str(self.data.min()))
        print("Max: " + str(self.data.max()))
        print("Mean: " + str(self.data.mean()))
        print("Standard deviation: " + str(self.data.std()))
