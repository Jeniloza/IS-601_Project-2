import unittest
from src.Statistics.Statistics import Statistics
from src.Statistics.GetRandomData import random_data
from statistics import mean
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
        #pprint(mean(data))
        #pprint (self.statistics.mean(data))
        self.assertEqual(self.statistics.mean(data), mean(data))
        self.assertEqual(self.statistics.result, mean(data))

if __name__ == '__main__':
    unittest.main()
