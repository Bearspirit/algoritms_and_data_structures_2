class BSTNode:
	
    def __init__(self, key, parent):
        self.NodeKey = key # ключ узла
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок
        self.Level = 0 # уровень узла
        
class BalancedBST:
		
    def __init__(self):
    	self.Root = None # корень дерева

    def GenerateTree(self, a):
        def recurs_BBST_create(parent_node, a):
            if len(a) == 0: return
            node = BSTNode(a[len(a)//2], parent_node)
            if parent_node == None:
                self.Root = node
            elif node.NodeKey > parent_node.NodeKey:
                parent_node.RightChild = node
                node.Level = parent_node.Level + 1
            else:
                parent_node.LeftChild = node
                node.Level = parent_node.Level + 1
            left_branch = a[0:len(a)//2]
            right_branch = a[len(a)//2+1:]
            recurs_BBST_create(node, left_branch)
            recurs_BBST_create(node, right_branch)
            return node
        a = sorted(a)
        parent_node = None
        recurs_BBST_create(parent_node, a)
	# создаём дерево с нуля из неотсортированного массива a
	# ...      

    def IsBalanced(self, root_node):
        def key_balance(root_node):
            if root_node.RightChild:
                if root_node.NodeKey > root_node.RightChild.NodeKey:
                    return False
                key_balance(root_node.RightChild)
            if root_node.LeftChild:
                if root_node.NodeKey < root_node.LeftChild.NodeKey:
                    return False
                key_balance(root_node.LeftChild)
            return True
        if not key_balance(root_node):
            return False

        
        def depth_balance(root_node):
            if not root_node:
                return 0
            left_branch = depth_balance(root_node.LeftChild)
            right_branch = depth_balance(root_node.RightChild)
            return max(left_branch, right_branch) + 1
            
        left_dept = depth_balance(root_node.LeftChild)
        right_dept = depth_balance(root_node.RightChild)
        if abs(left_dept-right_dept) > 1:
            return False
        return True # сбалансировано ли дерево с корнем root_node
