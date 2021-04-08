from pymonad.either import Left

from dynamic_parser.attribute_type import NumberAttributeType, BooleanAttributeType
from dynamic_parser.convert_result import AttributeTypeError


# クラスにすっかー


def test_invalid_number():
    typ = NumberAttributeType().convert("invalid number")
    assert typ == Left(AttributeTypeError())

def test_boolean():
    typ = BooleanAttributeType().convert('')