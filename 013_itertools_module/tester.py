import itertools


def more_than_two(x):
    if x > 2:
        return True
    return False


letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4]
numbers2 = [4, 5, 4, 3, 2, 1, 0, 4, 2, 1]
selectors = [True, False, False, True]

result = itertools.accumulate(numbers2)
for x in result:
    print(x)