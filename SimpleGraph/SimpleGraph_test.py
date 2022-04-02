import unittest
from SimpleGraph import *

class DefTest(unittest.TestCase):
    def setUp(self):
        self.graph = SimpleGraph(5)
        self.graph.AddVertex(0)
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.graph.AddVertex(3)
        self.graph.AddVertex(4)

    def test_add_vertex(self):
        for i in range(0, self.graph.max_vertex):
            self.assertEqual(self.graph.vertex[i].Value, i)

    def test_add_edge(self):
        self.assertEqual(self.graph.m_adjacency[1][3], 0)
        self.assertEqual(self.graph.m_adjacency[3][1], 0)
        self.graph.AddEdge(1,3)
        self.assertEqual(self.graph.m_adjacency[1][3], 1)
        self.assertEqual(self.graph.m_adjacency[3][1], 1)

    def test_remove_edge(self):
        self.graph.AddEdge(1,3)
        self.assertEqual(self.graph.m_adjacency[1][3], 1)
        self.assertEqual(self.graph.m_adjacency[3][1], 1)
        self.graph.RemoveEdge(1,3)
        self.assertEqual(self.graph.m_adjacency[1][3], 0)
        self.assertEqual(self.graph.m_adjacency[3][1], 0)

    def test_remove_vertex(self):
        self.graph.AddEdge(1,0)
        self.graph.AddEdge(1,2)
        self.graph.AddEdge(1,4)
        self.assertEqual(self.graph.m_adjacency, [[0,1,0,0,0], [1,0,1,0,1], [0,1,0,0,0], [0,0,0,0,0], [0,1,0,0,0]])
        self.graph.RemoveEdge(1,0)
        self.assertEqual(self.graph.m_adjacency, [[0,0,0,0,0], [0,0,1,0,1], [0,1,0,0,0], [0,0,0,0,0], [0,1,0,0,0]])
        self.graph.RemoveEdge(1,2)
        self.assertEqual(self.graph.m_adjacency, [[0,0,0,0,0], [0,0,0,0,1], [0,0,0,0,0], [0,0,0,0,0], [0,1,0,0,0]])
        self.graph.RemoveEdge(1,4)
        self.assertEqual(self.graph.m_adjacency, [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]])

if __name__ == '__main__':
    unittest.main()