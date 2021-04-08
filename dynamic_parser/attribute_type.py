import sys
from abc import abstractmethod
from collections.abc import Callable
from datetime import date
from distutils.util import strtobool
from typing import Generic, TypeVar

from pymonad.either import Either, Left, Right

from dynamic_parser.convert_result import AttributeTypeError, ConvertResult

T = TypeVar("T")


def convert_value(value: str, f: Callable[[str], T]) -> ConvertResult[T]:
    try:
        return Right(f(value))
    except ValueError as e:
        print(e.with_traceback(sys.exc_info()[2]))
        return Left(AttributeTypeError())


# TODO 独自型制約を表現する
class AttributeType(Generic[T]):
    @abstractmethod
    def convert(self, value: str) -> ConvertResult[T]:
        """convert str value to specific type.

        :raises
            ConvertError: when value cannot convert.
        """
        raise NotImplementedError()


class StringAttributeType(AttributeType[str]):
    def convert(self, value: str) -> ConvertResult[str]:
        return Either.insert(value)


class NumberAttributeType(AttributeType[int]):
    def convert(self, value: str) -> ConvertResult[int]:
        return convert_value(value, int)


class BooleanAttributeType(AttributeType[bool]):
    def convert(self, value: str) -> ConvertResult[bool]:
        return convert_value(value, strtobool)


class DateAttributeType(AttributeType[date]):
    def convert(self, value: str) -> ConvertResult[date]:
        return convert_value(value, date.fromisoformat)
