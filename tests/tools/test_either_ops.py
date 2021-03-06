from dataclasses import dataclass
from types import TracebackType

from pymonad.either import Left, Right

from dynamic_parser.tools.either_ops import sequence, traverse, apply


@dataclass(frozen=True)
class TracebackTypeWrapper:
    tracebackType: TracebackType


def test_apply():
    result = apply(lambda: 1 / 0, lambda tt: TracebackTypeWrapper(tt))
    assert result.is_left()


def test_sequence_right():
    results = [Right(1), Right(3)]
    assert sequence(results) == Right([1, 3])


def test_sequence_left():
    results = [Left("str"), Right(1), Right(3)]
    assert sequence(results) == Left("str")


def test_traverse_right():
    results = [Right(1), Right(3)]
    actual = traverse(results, lambda a: a.map(lambda b: b * 10))
    assert actual == Right([10, 30])
