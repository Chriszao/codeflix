from dataclasses import is_dataclass
from datetime import datetime
from typing import Type
import unittest
from category.domain.entities import Category


class TestCategoryUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Category))

    def assert_common_props(
        self,
        category: Type[Category],
        name: str,
        description: str | None,
        is_active: bool | None
    ):
        self.assertEqual(category.name, name)
        self.assertEqual(category.description, description)
        self.assertEqual(category.is_active, is_active)

    def test_constructor(self):
        category = Category(name='Movie_1')

        self.assert_common_props(
            category=category,
            name="Movie_1",
            description=None,
            is_active=True,
        )
        self.assertIsInstance(category.created_at, datetime)

        created_at = datetime.now()

        category = Category(
            name='Movie_2',
            description='some description',
            is_active=False,
            created_at=created_at
        )

        self.assert_common_props(
            category=category,
            name="Movie_2",
            description='some description',
            is_active=False
        )
        self.assertEqual(category.created_at, created_at)

    def test_if_created_at_is_different(self):
        category1 = Category(name='Movie_1')
        category2 = Category(name='Movie_2')

        self.assertNotEqual(
            category1.created_at.timestamp(),
            category2.created_at.timestamp()
        )
