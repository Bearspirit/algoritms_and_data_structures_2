import unittest
from EvenTrees import *

class DefTest(unittest.TestCase):

    def setUp(self):
        self.Node1 = SimpleTreeNode(1, None)
        self.Node2 = SimpleTreeNode(2, None)
        self.Node3 = SimpleTreeNode(3, None)
        self.Node4 = SimpleTreeNode(4, None)
        self.Node5 = SimpleTreeNode(5, None)
        self.Node6 = SimpleTreeNode(6, None)
        self.Node7 = SimpleTreeNode(7, None)
        self.Node8 = SimpleTreeNode(8, None)
        self.Node9 = SimpleTreeNode(9, None)
        self.Node10 = SimpleTreeNode(1, None)
       
        self.my_tree = SimpleTree(self.Node1)
        self.my_tree.AddChild(self.Node1, self.Node2)
        self.my_tree.AddChild(self.Node1, self.Node3)
        self.my_tree.AddChild(self.Node1, self.Node6)

        self.my_tree.AddChild(self.Node2, self.Node5)
        self.my_tree.AddChild(self.Node2, self.Node7)

        self.my_tree.AddChild(self.Node3, self.Node4)

        self.my_tree.AddChild(self.Node6, self.Node8)
        self.my_tree.AddChild(self.Node8, self.Node9)
        self.my_tree.AddChild(self.Node8, self.Node10)


    def test_event(self):
        self.assertEqual(self.my_tree.EvenTrees(), [1,3,1,6])



if __name__ == '__main__':
    unittest.main()