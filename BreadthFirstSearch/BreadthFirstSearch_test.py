import unittest
from BreadthFirstSearch import *

class DefTest(unittest.TestCase):
    def setUp(self):
        self.graph = SimpleGraph(5)
        self.graph.AddVertex('A')
        self.graph.AddVertex('B')
        self.graph.AddVertex('C')
        self.graph.AddVertex('D')
        self.graph.AddVertex('E')
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(0, 2)
        self.graph.AddEdge(0, 3)
        self.graph.AddEdge(1, 3)
        self.graph.AddEdge(1, 4)
        self.graph.AddEdge(2, 3)
        self.graph.AddEdge(3, 4)

    def test_DepthFirstSearch(self):
        self.assertEqual(self.graph.DepthFirstSearch(0,1), [self.graph.vertex[0], self.graph.vertex[1]])
        self.assertEqual(self.graph.DepthFirstSearch(0,3), [self.graph.vertex[0], self.graph.vertex[3]])
        self.assertEqual(self.graph.DepthFirstSearch(0,4), [self.graph.vertex[0], self.graph.vertex[1], self.graph.vertex[4]])

    def test_DepthFirstSearch_empty_track(self):
        self.graph.RemoveEdge(1,4)
        self.graph.RemoveEdge(3,4)
        self.assertEqual(self.graph.DepthFirstSearch(0,1), [self.graph.vertex[0], self.graph.vertex[1]])
        self.assertEqual(self.graph.DepthFirstSearch(0,3), [self.graph.vertex[0], self.graph.vertex[3]])
        self.assertEqual(self.graph.DepthFirstSearch(0,4), [])

    



if __name__ == '__main__':
    unittest.main()