from src.Calculator.Calculator import Calculator
from src.Statistics import Statistics

class random_values(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, data):
        self.result = Statistics.mean(data)
        return self.result
