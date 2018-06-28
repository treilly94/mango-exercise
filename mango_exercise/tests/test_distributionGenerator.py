from unittest import TestCase
from mango_exercise.distribution_generator_class import DistributionGenerator


class TestDistributionGenerator(TestCase):
    d = DistributionGenerator(500)

    def test_normal_mean(self):
        self.d.mean = 5
        mean = self.d.normal().mean()
        print(mean)

        self.assertTrue(4 <= mean <= 6)

    def test_normal_sd(self):
        self.d.sd = 10
        sd = self.d.normal().std()
        print(sd)

        self.assertTrue(9 <= sd <= 11)

    def test_poisson(self):
        self.d.interval = 20
        output = self.d.poisson().mean()
        print(output)

        self.assertTrue(19 <= output <= 21)

    def test_binomial(self):
        self.d.n = 1
        self.d.p = 0.75
        output = self.d.binomial().mean()
        print(output)

        self.assertTrue(0.7 <= output <= 0.8)
