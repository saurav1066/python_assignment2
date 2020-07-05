"""
Write a Python class to find the three elements that sum to zero
from a list of n real numbers. Input array : [-25, -10, -7, -3, 2, 4, 8, 10] Output : [[-10, 2, 8], [-7, -3, 10]]
"""
import itertools


def add_elem(j):
    sum = 0
    for i in j:
        sum += i
    return sum


class SumZero:
    input_value = [-25, -10, -7, -3, 2, 4, 8, 10]
    for i in range(0, len(input_value) + 1):
        for j in itertools.combinations(input_value, 3):
            if add_elem(j) == 0:
                print(j)


