import unittest
from src.CsvReader.CsvReader import CsvReader
from src.Statistics.Statistics import Statistics
from pprint import pprint

class MyTestCase(unittest.TestCase):
    test_data = CsvReader('src/Tests/Data/Data.csv').data
    column1 = [int(row['value1']) for row in test_data]
    test_answer = CsvReader('src/Tests/Data/Data_Answers.csv').data

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_mean(self):
        for row in self.test_answer:
            pprint(row["mean"])
        self.assertEqual(self.statistics.mean(self.column1), float(row['mean']))
        self.assertEqual(self.statistics.result, float(row['mean']))

    def test_median(self):
        for row in self.test_answer:
            pprint(row["median"])
        self.assertEqual(self.statistics.median(self.column1), float(row['median']))
        self.assertEqual(self.statistics.result, float(row['median']))

    def test_mode(self):
        for row in self.test_answer:
            pprint(row["mode"])
        self.assertEqual(self.statistics.mode(self.column1), float(row['mode']))
        self.assertEqual(self.statistics.result, float(row['mode']))

    def test_standard_deviation(self):
        for row in self.test_answer:
            pprint(row["stddev"])
        self.assertEqual(self.statistics.stddev(self.column1), float(row['stddev']))
        self.assertEqual(self.statistics.result, float(row['stddev']))

    def test_variance(self):
        for row in self.test_answer:
            pprint(row['variance'])
        self.assertEqual(self.statistics.variance(self.column1), float(row['variance']))
        self.assertEqual(self.statistics.result, float(row['variance']))

if __name__ == '__main__':
    unittest.main()