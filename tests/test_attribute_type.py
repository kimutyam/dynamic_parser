from pymonad.either import Right

from dynamic_parser.attribute_type import NumberAttributeType, BooleanAttributeType, DateAttributeType
import pytest


def test_invalid_number():
    typ = NumberAttributeType().convert("invalid number")
    assert typ.is_left()


def test_invalid_boolean():
    typ = BooleanAttributeType().convert('')
    assert typ.is_left()


def test_invalid_date():
    typ = DateAttributeType().convert('200000')
    assert typ.is_left()


@pytest.mark.parametrize(
    "raw, converted",
    [('199', 199), ('01', 1)]
)
def test_number(raw, converted):
    typ = NumberAttributeType().convert(raw)
    assert typ == Right(converted)
