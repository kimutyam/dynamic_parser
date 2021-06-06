from typing import Any, Type
from unittest import TestCase

from pymonad.either import Either


class EitherTestCase(TestCase):

    def assert_right(
            self,
            first: Either[Any, Any],
            second: Any
    ):
        self.assertTrue(first.is_right())
        self.assertEqual(first.value, second)

    def assert_left(
            self,
            first: Either[Any, Any],
            second: Any
    ):
        self.assertTrue(first.is_left())
        self.assertEqual(first.monoid[0], second)

    def assert_left_instance(
            self,
            first: Either[Any, Any],
            second: Type[Any]
    ):
        print(second)
        assert first.is_left()
        self.assertIsInstance(
            first.monoid[0],
            second
        )
