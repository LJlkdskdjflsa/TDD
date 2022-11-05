import unittest
from dataclasses import dataclass

@dataclass
class CD:
    _stock: int = 0
    def get_stock_count(self)->int:
        return self._stock 
    def buy(self,quntity):
        self._stock -= quntity

class BuyCdTest(unittest.TestCase):
    def test_buy_cd_in_stock(self):
        cd = CD(_stock=10)
        cd.buy(5)
        self.assertEqual(5, cd.get_stock_count())


if __name__ == '__main__':
    unittest.main() 