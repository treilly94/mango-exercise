from unittest import TestCase
from mango_exercise.distribution_generator_function import distribution_generator


class TestDistribution_generator(TestCase):
    def test_normal_mean(self):
        mean = distribution_generator(200, "normal", mean=5).mean()
        print(mean)

        self.assertTrue(4 <= mean <= 6)

    def test_normal_sd(self):
        sd = distribution_generator(200, "normal", sd=10).std()
        print(sd)

        self.assertTrue(9 <= sd <= 11)

    def test_poisson(self):
        output = distribution_generator(200, "poisson", interval=20).mean()
        print(output)

        self.assertTrue(19 <= output <= 21)

