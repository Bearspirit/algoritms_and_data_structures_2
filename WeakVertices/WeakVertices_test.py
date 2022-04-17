import unittest
from WeakVertices import *

class DefTest(unittest.TestCase):
    def setUp(self):
        self.graph = SimpleGraph(9)
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.graph.AddVertex(3)
        self.graph.AddVertex(4)
        self.graph.AddVertex(5)
        self.graph.AddVertex(6)
        self.graph.AddVertex(7)
        self.graph.AddVertex(8)
        self.graph.AddVertex(9)
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(0, 2)
        self.graph.AddEdge(0, 3)
        self.graph.AddEdge(1, 3)
        self.graph.AddEdge(2, 3)
        self.graph.AddEdge(2, 4)
        self.graph.AddEdge(3, 5)
        self.graph.AddEdge(4, 5)
        self.graph.AddEdge(5, 6)
        self.graph.AddEdge(5, 7)
        self.graph.AddEdge(6, 7)
        self.graph.AddEdge(7, 8)

    def test_WeakVertices_2_vertex(self):
        self.assertEqual(self.graph.WeakVertices(), [4, 8])
    
    def test_WeakVertices_1_vertex(self):
        self.graph.AddEdge(3,4)
        self.assertEqual(self.graph.WeakVertices(), [8])
        
    def test_WeakVertices_0_vertex(self):
        self.graph.AddEdge(3,4)
        self.graph.AddEdge(5,8)
        self.assertEqual(self.graph.WeakVertices(), [])

    



if __name__ == '__main__':
    unittest.main()