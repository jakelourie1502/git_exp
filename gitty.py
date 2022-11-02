import numpy as np
import pandas
import matplotlib as plt

a = 2
b = a+3
c = b+3


def sigmoid(x):
    return np.sign(x)


def plus_two(x):
    return x + 2


x = sigmoid(plus_two(np.random.randint(-10, 10)))
print(x)
