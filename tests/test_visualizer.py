import unittest
import os
from src.grid import Grid
from src.visualizer import save_grid_image

class TestVisualizer(unittest.TestCase):
    def test_save_grid_image(self):
        grid = Grid(width=10, height=10, obstacles=[(1, 1), (1, 2), (2, 2)])
        path = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]
        start = (0, 0)
        end = (2, 2)
        filename = 'images/test_grid.png'
        
        save_grid_image(grid, path, start, end, filename)
        self.assertTrue(os.path.exists(filename))
        
        # Clean up
        if os.path.exists(filename):
            os.remove(filename)

if __name__ == "__main__":
    unittest.main()
