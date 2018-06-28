from numpy import random


def distribution_generator(num_samples, distribution_type, mean=0, sd=1, interval=1, n=1, p=0.5):
    """ Generate random data within a given distribution

    :param num_samples: Int The number of samples to be returned
    :param distribution_type: String The type of distribution to be used
    :param mean: The Mean value for a normal distribution
    :param sd: The Standard Deviation for a normal distribution
    :param interval: The Interval for a poisson distribution
    :param n: The number of samples for a binomial distribution
    :param p: The probability for a binomial distribution
    :return: ndarray
    """
    if distribution_type == "normal":
        return random.normal(size=num_samples, loc=mean, scale=sd)
    elif distribution_type == "poisson":
        return random.poisson(size=num_samples, lam=interval)
    elif distribution_type == "binomial":
        return random.binomial(size=num_samples, n=n, p=p)
    else:
        raise ValueError(distribution_type + " is not a valid distribution type")
