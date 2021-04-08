from abc import ABC
from dataclasses import dataclass
from types import TracebackType
from typing import Optional, TypeVar

from pymonad.either import Either


@dataclass(frozen=True)
class ConvertError(ABC):
    """Convert Error"""

    # message: str
    # tb: Optional[TracebackType]
    # org_value: str


class AttributeTypeError(ConvertError):
    """Type Error"""


class DuplicateAttributeError(ConvertError):
    """Duplicate"""


T = TypeVar("T")
ConvertResult = Either[ConvertError, T]
