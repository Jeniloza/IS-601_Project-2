import unittest
from src.Statistics.Statistics import Statistics
from src.Statistics.GetRandomData import random_data
import statistics
from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_mean(self):
        data = []
        data = random_data()
        pprint(data)
        if len(data) > 10:
            raise Exception('sample should not exceed 10. The value of sample was: {}'.format(data))
        pprint(statistics.mean(data))
        #pprint (self.statistics.mean(data))
        self.assertEqual(self.statistics.mean(data), statistics.mean(data))
        self.assertEqual(self.statistics.result, statistics.mean(data))

    def test_median(self):
        data = []
        data = random_data()
        pprint(statistics.median(data))
        self.assertEqual(self.statistics.median(data), statistics.median(data))
        self.assertEqual(self.statistics.result, statistics.median(data))

    def test_mode(self):
        data = []
        data = random_data()
        pprint(statistics.mode(data))
        self.assertEqual(self.statistics.mode(data), statistics.mode(data))
        self.assertEqual(self.statistics.result, statistics.mode(data))

    def test_variance(self):
        data = []
        data = random_data()
        pprint(statistics.pvariance(data))
        self.assertEqual(self.statistics.variance(data), statistics.pvariance(data))
        self.assertEqual(self.statistics.result, statistics.pvariance(data))

    def test_std_dev(self):
        data = []
        data = random_data()
        pprint(round(statistics.pstdev(data), 5))
        self.assertEqual(self.statistics.stddev(data), round(statistics.pstdev(data), 5))
        self.assertEqual(self.statistics.result, round(statistics.pstdev(data), 5))

if __name__ == '__main__':
    unittest.main()
