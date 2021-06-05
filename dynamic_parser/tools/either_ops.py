from typing import Callable, Sequence, TypeVar, Optional

from pymonad.either import Either, Right, Left
from pymonad.tools import identity
from collections import deque
import sys
from types import TracebackType

E = TypeVar("E")
A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")

X = TypeVar("X")


# See:
# https://stackoverflow.com/questions/40775709/avoiding-too-broad-exception-clause-warning-in-pycharm/40775710#40775710
def apply(f: Callable[[], A], except_f: Callable[[Optional[TracebackType]], E]) -> Either[E, A]:
    # noinspection PyBroadException
    try:
        return Right(f())
    except BaseException:
        return Left(except_f(sys.exc_info()[2]))


# なぜかmypyでエラーになる「Cannot infer type argument 2」
def map2(e1: Either[E, A], e2: Either[E, B], f: Callable[[A, B], C]) -> Either[E, C]:
    return e1.bind(lambda a: e2.map(lambda b: f(a, b)))


def traverse(items: Sequence[A], f: Callable[[A], Either[E, B]]) -> Either[E, Sequence[B]]:
    """

    :param items: hash化可能な
    :param f:
    :return:
    """
    acc: Either[E, Sequence[B]] = Right(deque())
    for item in items:
        eb = f(item)
        if eb.is_left():
            return eb
        acc.bind(lambda a: eb.map(lambda b: a.append(b)))
    return acc.map(lambda e: list(e))


def sequence(items: Sequence[Either[E, A]]) -> Either[E, Sequence[A]]:
    return traverse(items, identity)
