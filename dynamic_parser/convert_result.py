from abc import ABC
from dataclasses import dataclass
from types import TracebackType
from typing import Optional, TypeVar, Type

from pymonad.either import Either

A = TypeVar("A", bound='ConvertError')
T = TypeVar("T")


@dataclass(frozen=True)
class ConvertError(ABC):
    """Convert Error"""
    message: str
    tb: Optional[TracebackType]

    @classmethod
    def create(cls: Type[A], message: str) -> A:
        return cls(message, None)


class AttributeTypeError(ConvertError):
    """Type Error"""


class DuplicateAttributeError(ConvertError):
    """Duplicate"""


ConvertResult = Either[ConvertError, T]
