import random
import string
import timeit

import pytest


setup = 'from leet import leet'
template = 'leet("%s")'


def make_random_string(length: int):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


@pytest.mark.parametrize("str_length, iterations_number, max_time", [
    (512, 1000, 0.01),
    (65536, 1000, 0.2),
    (1048576, 100, 0.2),
    (1048576, 10, 0.02),
    (10485760, 2, 0.04)
])
def test_perfomance(str_length: int, iterations_number: int, max_time: int):
    code = template % make_random_string(str_length)
    time = timeit.timeit(stmt=code, setup=setup, number=iterations_number)
    assert time < max_time, "Too slow for %d bytes, %d iterations" % (
        str_length, iterations_number
    )
