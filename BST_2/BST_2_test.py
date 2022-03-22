import unittest
from BST_2 import *

class DefTest(unittest.TestCase):
    def setUp(self):
        self.bin_tree = aBST(3)
        self.empty_tree = aBST(0)

    def test_add_full_tree(self):
        self.bin_tree.AddKey(50)
        self.bin_tree.AddKey(75)
        self.bin_tree.AddKey(25)
        self.bin_tree.AddKey(37)
        self.bin_tree.AddKey(62)
        self.bin_tree.AddKey(84)
        self.bin_tree.AddKey(31)
        self.bin_tree.AddKey(43)
        self.bin_tree.AddKey(55)
        self.bin_tree.AddKey(92)
        self.assertEqual(self.bin_tree.Tree, [50,25,75,None,37,62,84,None,None,31,43,55,None,None,92])
        self.assertIsNone(self.bin_tree.FindKeyIndex(30))
        self.assertEqual(self.bin_tree.FindKeyIndex(77), -13)
        self.bin_tree.AddKey(77)
        self.assertEqual(self.bin_tree.FindKeyIndex(77), 13)
        self.assertEqual(self.bin_tree.AddKey(92), 14)

    def test_find_and_add(self):
        fst_index = self.empty_tree.FindKeyIndex(50)
        scd_index = self.empty_tree.FindKeyIndex(75)
        self.assertEqual(fst_index, 0)
        self.assertEqual(scd_index, 0)
        self.assertEqual(self.empty_tree.AddKey(50), 0)
        self.assertEqual(self.empty_tree.AddKey(75), -1)

    def test_add_in_bin_tree(self):
        self.bin_tree.AddKey(50)
        left_child = self.bin_tree.AddKey(25)
        right_child =self.bin_tree.AddKey(75)
        self.assertEqual(left_child, 1)
        self.assertEqual(right_child, 2)





if __name__ == '__main__':
    unittest.main()