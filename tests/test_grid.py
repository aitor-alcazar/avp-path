import unittest
from src.grid import Grid

class TestGrid(unittest.TestCase):
    def test_is_within_bounds(self):
        grid = Grid(10, 10)
        self.assertTrue(grid.is_within_bounds((0, 0)))
        self.assertFalse(grid.is_within_bounds((10, 10)))

    def test_is_walkable(self):
        grid = Grid(10, 10, obstacles=[(1, 1)])
        self.assertTrue(grid.is_walkable((0, 0)))
        self.assertFalse(grid.is_walkable((1, 1)))

if __name__ == "__main__":
    unittest.main()
