from collections import deque
from dynamic_parser.tools.timer import timer_printer


def list_append():
    list_array = []
    for i in range(10000):
        list_array.append(1)


def list_bind_append():
    list_array = []
    for i in range(10000):
        list_array = [*list_array, 1]


def deque_append():
    deque_array = deque()
    for i in range(10000):
        deque_array.append(1)


if __name__ == '__main__':
    timer_printer(list_append)
    timer_printer(list_bind_append())
    timer_printer(deque_append())
