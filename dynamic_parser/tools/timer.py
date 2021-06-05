import time


def _print(elapsed_time: float):
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")


def timer(f) -> float:
    start = time.time()
    f()
    return time.time() - start


def timer_printer(f):
    _print(timer(f))
