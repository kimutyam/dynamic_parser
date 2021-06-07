from dataclasses import dataclass
from typing import Callable, Sequence, TypeVar, Union


@dataclass(frozen=True)
class ConvertError:
    """Convert Error"""
    # cause: Exception


class AttributeTypeError(ConvertError):
    """Type Error"""


class DuplicateAttributeError(ConvertError):
    """Duplicate"""


T = TypeVar("T", covariant=True)
ConvertResult = Union[T, ConvertError]

T1 = TypeVar("T1")
T2 = TypeVar("T2")
T3 = TypeVar("T3")
x = Union[T1, T2]


def flatmap(r1: ConvertResult[T1], f: Callable[[T1], ConvertResult[T2]]) -> ConvertResult[T2]:
    if isinstance(r1, ConvertError):
        return r1
    return f(r1)


def map(r1: ConvertResult[T1], f: Callable[[T1], T2]) -> ConvertResult[T2]:
    if isinstance(r1, ConvertError):
        return r1
    return f(r1)


def traverse(
        results: Sequence[ConvertResult[T1]], f: Callable[[T1], ConvertResult[T2]]
) -> ConvertResult[Sequence[T2]]:
    li = list()
    for result in results:
        if isinstance(result, ConvertError):
            return result
        r = f(result)
        if isinstance(r, ConvertError):
            return r
        li.append(r)
    return li


def sequence(results: Sequence[ConvertResult[T1]]) -> ConvertResult[Sequence[T1]]:
    li = list()
    for result in results:
        if isinstance(result, ConvertError):
            return result
        li.append(result)
    return li
