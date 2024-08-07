import unittest
from src.node import Node

class TestNode(unittest.TestCase):
    def test_equality(self):
        node1 = Node((0, 0))
        node2 = Node((0, 0))
        self.assertEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()
