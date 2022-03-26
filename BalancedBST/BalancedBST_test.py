import unittest
from BalancedBST import *

class DefTest(unittest.TestCase):

    def setUp(self):
        self.Node_8 = BSTNode(8, None)
        self.Node_4 = BSTNode(4, self.Node_8)
        self.Node_12 = BSTNode(12, self.Node_8)
        self.Node_2 = BSTNode(2, self.Node_4)
        self.Node_6 = BSTNode(6, self.Node_4)

        self.Node_1 = BSTNode(1, self.Node_2)
        self.Node_3 = BSTNode(3, self.Node_2)
        self.Node_5 = BSTNode(5, self.Node_6)
        self.Node_7 = BSTNode(7, self.Node_6)


        self.Node_8.LeftChild = self.Node_4
        self.Node_8.RightChild = self.Node_12
        self.Node_4.LeftChild = self.Node_2
        self.Node_4.RightChild = self.Node_6


        self.Node_2.LeftChild = self.Node_1
        self.Node_2.RightChild = self.Node_3
        self.Node_6.LeftChild = self.Node_5
        self.Node_6.RightChild = self.Node_7

        
        self.my_tree = BalancedBST()
        self.my_tree.Root = self.Node_8


    def test_balance(self):
        self.assertEqual(self.my_tree.IsBalanced(self.my_tree.Root), True)
        

if __name__ == '__main__':
    unittest.main()