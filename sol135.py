# Link - https://edabit.com/challenge/3DAkZHv2LZjgqWbvW

from __future__ import annotations
import unittest


def is_adjacent(matrix: list[list[int]], node_1: int, node_2: int) -> bool:
    return False  # Put your code here!!!


class Test(unittest.TestCase):
    matrix1 = [[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]]
    matrix2 = [[0, 1, 0, 1, 1], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [1, 0, 0, 1, 0]]

    def test_1(self):
        self.assertEqual(is_adjacent(self.matrix1, 0, 1), True)

    def test_2(self):
        self.assertEqual(is_adjacent(self.matrix1, 0, 2), False)

    def test_3(self):
        self.assertEqual(is_adjacent(self.matrix1, 2, 1), True)

    def test_4(self):
        self.assertEqual(is_adjacent(self.matrix2, 0, 3), True)

    def test_5(self):
        self.assertEqual(is_adjacent(self.matrix2, 1, 4), False)

    def test_6(self):
        self.assertEqual(is_adjacent(self.matrix2, 3, 2), True)


if __name__ == "__main__":
    unittest.main()