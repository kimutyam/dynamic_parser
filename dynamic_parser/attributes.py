from collections import Mapping
from dataclasses import dataclass
from datetime import date

from dynamic_parser.attribute_name import AttributeName


@dataclass(frozen=True)
class Attributes:
    string: Mapping[AttributeName, str]
    number: Mapping[AttributeName, int]
    boolean: Mapping[AttributeName, bool]
    date: Mapping[AttributeName, date]
