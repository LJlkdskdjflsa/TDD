from dataclasses import dataclass
from functools import reduce


@dataclass
class Item(object):
    unit_price: float
    quantity: int = 1


@dataclass
class Basket(object):
    items: list[Item]

    def total(self):
        return reduce(
            lambda sum_of_total, item: sum_of_total + item.unit_price * item.quantity,
            self.items,
            0,
        )
