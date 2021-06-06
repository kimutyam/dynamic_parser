from pymonad.either import Right

from dynamic_parser.attribute_setting import (
    AttributeSetting,
    AttributeName,
    AttributeSettings
)
from dynamic_parser.attribute_type import (
    NumberAttributeType,
    StringAttributeType
)
from dynamic_parser.convert_result import AttributeTypeError, DuplicateAttributeError
from either_test_case import EitherTestCase


class AttributeSettingTest(EitherTestCase):
    __string_setting = AttributeSetting(
        name=AttributeName('rank'),
        attribute_type=StringAttributeType(),
        aliases=frozenset({AttributeName("ranking")})
    )

    def test_duplicate_attribute(self):
        attribute_map = {'rank': 'gold', 'ranking': 'silver'}
        result = self.__string_setting.convert_value(attribute_map)
        EitherTestCase().assert_left_type(result, DuplicateAttributeError)

    def test_convert(self):
        attribute_map = {'rank': 'gold'}
        result = self.__string_setting.convert_value(attribute_map)
        assert result.value == (AttributeName('rank'), 'gold')

    def test_none_convert(self):
        attribute_map = {'foo': 'gold'}
        result = self.__string_setting.convert_value(attribute_map)
        assert result == Right(None)


class AttributeSettingsTest(EitherTestCase):
    __string_setting = AttributeSetting(
        name=AttributeName('rank'),
        attribute_type=StringAttributeType(),
        aliases=frozenset({AttributeName("ranking")})
    )

    __number_setting = AttributeSetting(
        name=AttributeName('age'),
        attribute_type=NumberAttributeType()
    )

    __settings = AttributeSettings(
        string_settings=[__string_setting],
        number_settings=[__number_setting],
        boolean_settings=[],
        date_settings=[]
    )

    def test_attribute_type_error(self):
        result = self.__settings.convert_attribute_map(
            {'rank': 'gold', 'age': 'not number'}
        )
        self.assert_left_type(result, AttributeTypeError)
