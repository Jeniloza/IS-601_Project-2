from src.Calculator.Addition import addition
from src.Calculator.Division import division
from src.Statistics.GetRandomData import random_data

def random_data_mean():
    total = 0
    # check that get sample returns the proper number of samples
    # check that sample size is not 0
    # check that sample size is not larger than the population
    # https://realpython.com/python-exceptions/
    # https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception
    sample = random_data()
    if len(sample) >= 10 or len(sample) <= 0:
            raise Exception('sample should not exceed 10. The value of sample was: {}'.format(sample))
    num_values = len(sample)
    for num in sample:
        total = addition(total, num)
    return division(total, num_values)
