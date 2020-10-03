import copy
from typing import List
from functools import lru_cache


@lru_cache()
def fib(target: int):
    result = []
    a, b = 1, 1
    while a <= target:
        result.append(a)
        a, b = b, a + b
    return result


def subset_sum(
        from_list: List[int],
        target: int,
        current_sum: int,
        output: List[List[int]],
        result: List[int]
):
    if current_sum == target:
        output.append(copy.copy(result))

    for i, v in enumerate(from_list):
        temp_sum = current_sum + v
        if temp_sum > target:
            return
        result.append(v)
        subset_sum(from_list[i:], target, temp_sum, output, result)
        result.pop()


@lru_cache()
def all_comb_sum(target: int) -> List[List[int]]:
    """
    Given a target, find all the possible combinations from
    Fibonacci series that sums to that target.
    :param target:
    :return:
    """
    output = []
    result = []
    from_list = fib(target)[2:]
    subset_sum(from_list, target, 0, output, result)
    return output
