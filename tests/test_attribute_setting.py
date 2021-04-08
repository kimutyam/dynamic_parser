# from unittest import TestCase, main
#
# from dynamic_parser.attribute_type import (
#     NumberAttributeType,
#     StringAttributeType
# )
#
# from dynamic_parser.convert_result import AttributeTypeError
#
# from dynamic_parser.attribute_setting import (
#     AttributeSetting,
#     AttributeName,
#     DuplicateAttributeError
# )
#
#
# class AttributeSettingTest(TestCase):
#     def test_illegal_number_do_not_convert(self):
#         value = NumberAttributeType() \
#             .convert('1a')
#         # __eq__で同値の確認ができるようになる..?
#         self.assertEqual(value, AttributeTypeError())
#
#     def test_duplicate_attribute(self):
#         setting = AttributeSetting(
#             name=AttributeName('rank'),
#             attribute_type=StringAttributeType(),
#             aliases={AttributeName("ranking")}
#         )
#         attribute_map = {'rank': 'gold', 'ranking': 'silver'}
#         actual = setting.convert_value(attribute_map)
#         self.assertEqual(actual, DuplicateAttributeError())
#
#     def test_convert_attribute(self):
#         setting = AttributeSetting(
#             name=AttributeName('rank'),
#             attribute_type=StringAttributeType(),
#             aliases={AttributeName("ranking")}
#         )
#         attribute_map = {'rank': 'gold', 'name': 'kimutyam'}
#         actual = setting.convert_value(attribute_map)
#         self.assertEqual(actual, (AttributeName(value='rank'), 'gold'))
#
#
# if __name__ == 'main':
#     main()
