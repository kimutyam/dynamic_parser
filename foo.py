import time
from collections import deque
from itertools import combinations, permutations, product, groupby


def list_append():
    start = time.time()
    list_array = []
    for i in range(10000):
        list_array.append(1)
    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")


def list_bind_append():
    start = time.time()
    list_array = []
    for i in range(10000):
        list_array = [*list_array, 1]
    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")


def deque_append():
    start = time.time()
    deque_array = deque()
    for i in range(10000):
        deque_array.append(1)
    list(deque_array)
    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")


def a():
    print(list(combinations([1, 2, 3], 2)))
    c = permutations([1, 2, 3], 3)
    d = groupby([1, 2, 3, 4], lambda x: "gu" if x % 2 == 0 else "ki")
    print(list(c))
    for s, n in d:
        print(s, list(n))


if __name__ == '__main__':
    list_append()
    list_bind_append()
    deque_append()
    a()
