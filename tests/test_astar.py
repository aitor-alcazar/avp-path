import unittest
from src.grid import Grid
from src.astar import astar

class TestAStar(unittest.TestCase):
    def test_path_found(self):
        grid = Grid(10, 10, obstacles=[(1, 1), (1, 2), (2, 2)])
        start = (0, 0)
        end = (9, 9)
        path = astar(grid, start, end)
        self.assertIsNotNone(path)

    def test_no_path(self):
        grid = Grid(10, 10, obstacles=[(1, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2)])
        start = (0, 0)
        end = (9, 9)
        path = astar(grid, start, end)
        self.assertIsNone(path)

if __name__ == "__main__":
    unittest.main()
