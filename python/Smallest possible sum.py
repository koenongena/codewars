from functools import reduce
import math


def solution(a):
    return reduce(math.gcd, a) * len(a)


def test_solution():
    assert solution([9]) == 9
    assert solution([6, 9, 21]) == 9
    assert solution([1, 21, 55]) == 3


def test_large_difference():
    assert solution(
        [3969, 138384, 196249, 25600, 31329, 4356, 4761, 26896, 119716, 75076, 195364, 49284, 184900, 12100, 103684,
         184900, 178929, 8281, 29584, 104329, 13689, 52900, 7744, 101761, 75076, 11664, 209764, 193600, 4096, 47524,
         24025, 5776, 93025, 17424, 220900, 211600, 118336, 217156, 90000, 5184, 15625, 3969, 113569, 13689]) == 44


def test_large_array():
    import random

    large_array = [random.randint(1, 100_000) for _ in range(1, 30_000)]

    assert solution(large_array) == 29999
