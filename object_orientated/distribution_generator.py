from numpy import random


class DistributionGenerator:

    def __init__(self, num_samples, mean=0, sd=1, interval=1, n=1, p=0.5):
        self.num_samples = num_samples
        self.mean = mean
        self.sd = sd
        self.interval = interval
        self.n = n
        self.p = p

        self.data = None

    def normal(self):
        self.data = random.normal(size=self.num_samples, loc=self.mean, scale=self.sd)
        return self.data

    def poisson(self):
        self.data = random.poisson(size=self.num_samples, lam=self.interval)
        return self.data

    def binomial(self):
        self.data = random.binomial(size=self.num_samples, n=self.n, p=self.p)
        return self.data

    def summarise(self):
        print("Min: " + str(self.data.min()))
        print("Max: " + str(self.data.max()))
        print("Mean: " + str(self.data.mean()))
        print("Standard deviation: " + str(self.data.std()))
