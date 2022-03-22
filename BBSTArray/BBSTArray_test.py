import unittest
from BST_2 import *
from BBSTArray import *

class DefTest(unittest.TestCase):

    def test_compare_metods_1(self):
        init_list = [132, 9, 25, 111, 192, 47, 128]
        BST_tree = aBST(len(init_list))
        for i in GenerateBBSTArray(init_list):
            BST_tree.AddKey(i)
        self.assertEqual(BST_tree.Tree, GenerateBBSTArray(init_list))

    def test_compare_metods_2(self):
        init_list = [7,9,11,47,30,53,25,90,145,128,132,111,192,180,195]
        BST_tree = aBST(len(init_list))
        for i in GenerateBBSTArray(init_list):
            BST_tree.AddKey(i)
        self.assertEqual(BST_tree.Tree, GenerateBBSTArray(init_list))
        

if __name__ == '__main__':
    unittest.main()