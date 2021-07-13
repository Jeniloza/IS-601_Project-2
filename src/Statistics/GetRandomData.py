import random

def random_data():
    random_data_list_1 = random.sample(range(1, 50), 8)
    random.seed(30)
    random_data_list_2 = random.sample(range(1, 50), 1)
    random.seed(30)
    random_data_list_3 = random.sample(range(1, 50), 1)
    random_data_list = random_data_list_1 + random_data_list_2 + random_data_list_3
    random_values = random.sample(random_data_list, k=10)
    return random_values