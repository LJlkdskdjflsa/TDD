import unittest
from dataclasses import dataclass

from cd_warehouse import CD


class BuyCDTest(unittest.TestCase):
    def test_buy_cd_in_stock(self):
        cd = CD(_stock=10)
        cd.buy(5)
        self.assertEqual(5, cd.get_stock_count())


if __name__ == "__main__":
    unittest.main()
