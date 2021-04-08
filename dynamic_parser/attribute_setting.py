from dataclasses import dataclass
from datetime import date
from typing import Generic, Mapping, Optional, Sequence, Set, Tuple, TypeVar

from pampy import _, match
from pymonad.either import Either, Left, Right
from pymonad.tools import curry

from dynamic_parser.attribute_name import AttributeName
from dynamic_parser.attribute_type import AttributeType
from dynamic_parser.attributes import Attributes
from dynamic_parser.convert_result import ConvertResult, DuplicateAttributeError
from dynamic_parser.tools.collection_ops import head_option
from dynamic_parser.tools.either_ops import traverse

T = TypeVar("T", covariant=True)
AttributeMap = Mapping[str, str]


@dataclass(frozen=True)
class AttributeSetting(Generic[T]):
    name: AttributeName
    attribute_type: AttributeType[T]
    aliases: Set[AttributeName]

    def __validate_one_value(self, attribute_values: frozenset[str]) -> ConvertResult[Optional[str]]:
        if len(attribute_values) >= 2:
            return Left(DuplicateAttributeError())
        else:
            return Right(head_option(attribute_values))

    @curry(1)
    def __link_attribute_name(self, value: Optional[str]) -> Optional[Tuple[AttributeName, str]]:
        return match(value, str, (self.name, value), _, value)

    def __findValue(self, attribute_map: AttributeMap) -> ConvertResult[Optional[Tuple[AttributeName, str]]]:
        value_by_name = attribute_map.get(self.name.value)
        values_by_alias = frozenset({v for alias in self.aliases if (v := attribute_map.get(alias.value))})

        if value_by_name is not None:
            values = values_by_alias.union([value_by_name])
        else:
            values = values_by_alias

        return self.__validate_one_value(values).map(self.__link_attribute_name)

    @curry(1)
    def __convert(self, linked_value: Optional[Tuple[AttributeName, str]]):
        return match(
            linked_value, Tuple[AttributeName, str], lambda n, v: (n, self.attribute_type.convert(v)), _, linked_value
        )

    def convert_value(self, attribute_map: AttributeMap) -> Optional[ConvertResult[Tuple[AttributeName, T]]]:
        return self.__findValue(attribute_map).map(self.__convert)


@dataclass(frozen=True)
class AttributeSettings:
    string_settings: Sequence[AttributeSetting[str]]
    number_settings: Sequence[AttributeSetting[int]]
    boolean_settings: Sequence[AttributeSetting[bool]]
    date_settings: Sequence[AttributeSetting[date]]

    def convert_attribute_map(self, attribute_map: AttributeMap) -> ConvertResult[Attributes]:
        def convert_by(setting: AttributeSetting[T]) -> ConvertResult[Tuple[AttributeName, T]]:
            v = (setting.convert_value(attribute_map),)
            return match(v, None, Right(tuple()), _, v)

        @curry(2)
        def to_attributes(
            string_attributes: Sequence[Tuple[AttributeName, str]],
            number_attributes: Sequence[Tuple[AttributeName, int]],
            boolean_attributes: Sequence[Tuple[AttributeName, bool]],
        ) -> Attributes:
            return Attributes(
                string={n: v for n, v in string_attributes},
                number={n: v for n, v in number_attributes},
                boolean={n: v for n, v in boolean_attributes},
            )

        string_attributes = traverse(self.string_settings, convert_by)
        number_attributes = traverse(self.number_settings, convert_by)

        return Either.apply(to_attributes).to_arguments(string_attributes, number_attributes)
