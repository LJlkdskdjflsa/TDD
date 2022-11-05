import unittest
from dataclasses import dataclass
from shopping_basket import Basket, Item


class ShoppingBasketTest(unittest.TestCase):
    def test_empty_basket_total(self):
        basket = Basket([])
        self.assertEqual(basket.total(), 0)

    def test_single_item_when_quantity_is_one(self):
        basket = Basket([Item(100.0, 1)])
        self.assertEqual(basket.total(), 100)

    def test_two_item_when_quantity_is_one(self):
        basket = Basket([Item(100.0, 1), Item(100.0, 1)])
        self.assertEqual(basket.total(), 200)

    def test_single_item_when_quantity_is_two(self):
        basket = Basket([Item(100.0, 2)])
        self.assertEqual(basket.total(), 200)


if __name__ == "__main__":
    unittest.main()
