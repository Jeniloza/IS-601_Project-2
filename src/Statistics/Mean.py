from src.Calculator.Division import division

def mean(num):
    try:
        num_values = len(num)
        total = sum(num)
        return round(division(total, num_values), 8)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")