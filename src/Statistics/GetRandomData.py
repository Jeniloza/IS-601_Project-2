import random

def random_data():
    random_data_list = list(range(1, 500))
    random_values = random.sample(random_data_list, k=10)
    return random_values