import unittest
from parameterized import parameterized
from mars_rover import Rover


class MarsRoverTest(unittest.TestCase):
    @parameterized.expand(
        [("R", "N", "E"), ("R", "E", "S"), ("R", "S", "W"), ("R", "W", "N")]
    )
    def test_turn_right(self, turns, start_facing: str, end_facing: str):
        rover = Rover(facing=start_facing)
        rover = rover.turn(turns)
        self.assertEqual(end_facing, rover.facing)

    @parameterized.expand(
        [("L", "N", "W"), ("L", "W", "S"), ("L", "S", "E"), ("L", "E", "N")]
    )
    def test_turn_left(self, turns, start_facing: str, end_facing: str):
        rover = Rover(facing=start_facing)
        rover = rover.turn(turns)
        self.assertEqual(end_facing, rover.facing)


if __name__ == "__main__":
    unittest.main()
