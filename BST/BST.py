class BSTNode:
	
    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок


class BSTFind: # промежуточный результат поиска

    def __init__(self):
        self.Node = None # None если 
        # в дереве вообще нету узлов

        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо 
        # добавить новый узел левым потомком

class BST:

    def __init__(self, node):
        self.Root = node # корень дерева, или None

    def FindNodeByKey(self, key):
        find_result = BSTFind()
        Node = self.Root
        while Node:
            find_result.Node = Node
            if key == Node.NodeKey:
                find_result.NodeHasKey = True
                return find_result
            elif key > Node.NodeKey:
                Node = Node.RightChild
                find_result.ToLeft = False
            else:
                Node = Node.LeftChild
                find_result.ToLeft = True
        return find_result


    def AddKeyValue(self, key, val):
        find_result = self.FindNodeByKey(key)
        new_Node = BSTNode(key, val, None)
        if find_result.Node == None:
            self.Root = new_Node
            return True
        if find_result.ToLeft == True:
            new_Node.Parent = find_result.Node
            find_result.Node.LeftChild = new_Node
            return True
        if find_result.ToLeft == False:
            new_Node.Parent = find_result.Node
            find_result.Node.RightChild = new_Node
            return True
        return False # если ключ уже есть
  
    def FinMinMax(self, FromNode, FindMax):
        find_result = FromNode
        if find_result == None:
            return None
        if FindMax:
            while find_result.RightChild:
                find_result = find_result.RightChild
            return find_result
        else:
            while find_result.LeftChild:
                find_result = find_result.LeftChild
            return find_result
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
	
    def DeleteNodeByKey(self, key):
        find_del_Node = self.FindNodeByKey(key)
        if find_del_Node.NodeHasKey == False:
            return False # если узел не найден
        if find_del_Node.Node.LeftChild == None and find_del_Node.Node.RightChild == None:
            if find_del_Node.Node.Parent.LeftChild == find_del_Node.Node:
                find_del_Node.Node.Parent.LeftChild == None
            if find_del_Node.Node.Parent.RightChild == find_del_Node.Node:
                find_del_Node.Node.Parent.RightChild == None
            find_del_Node.Node.NodeKey = None
            find_del_Node.Node.NodeValue = None
            find_del_Node.Node.Parent = None
            return True
        if find_del_Node.Node.LeftChild == None:
            if find_del_Node.Node.Parent.LeftChild == find_del_Node.Node:
                find_del_Node.Node.Parent.LeftChild == find_del_Node.Node.RightChild
            if find_del_Node.Node.Parent.RightChild == find_del_Node.Node:
                find_del_Node.Node.Parent.RightChild == find_del_Node.Node.RightChild
            find_del_Node.Node.NodeKey = find_del_Node.Node.RightChild.NodeKey
            find_del_Node.Node.NodeValue = find_del_Node.Node.RightChild.NodeValue
            find_del_Node.Node.RightChild.Parent = find_del_Node.Node.Parent
            find_del_Node.Node.Parent = None
            return True
        if find_del_Node.Node.RightChild == None:
            if find_del_Node.Node.Parent.LeftChild == find_del_Node.Node:
                find_del_Node.Node.Parent.LeftChild == find_del_Node.Node.LeftChild
            if find_del_Node.Node.Parent.RightChild == find_del_Node.Node:
                find_del_Node.Node.Parent.RightChild == find_del_Node.Node.LeftChild
            find_del_Node.Node.NodeKey = find_del_Node.Node.LeftChild.NodeKey
            find_del_Node.Node.NodeValue = find_del_Node.Node.LeftChild.NodeValue
            find_del_Node.Node.LeftChild.Parent = find_del_Node.Node.Parent
            find_del_Node.Node.Parent = None
            return True
        right_child = find_del_Node.Node.RightChild
        new_Node = self.FinMinMax(right_child, False)
        if new_Node.RightChild == None:
            new_Node.Parent.LeftChhild = None
            find_del_Node.Node.NodeKey = new_Node.NodeKey
            find_del_Node.Node.NodeValue = new_Node.NodeValue
            new_Node.NodeKey = None
            new_Node.NodeValue = None
            new_Node.Parent = None
            return True
        else:
            find_del_Node.Node.NodeKey = new_Node.NodeKey
            find_del_Node.Node.NodeValue = new_Node.NodeValue
            new_Node.RightChild.Parent = new_Node.Parent
            new_Node.Parent.LeftChild = new_Node.RightChild
            return True
        # удаляем узел по ключу
    def Count(self):
        def RecursionNode(Node):
            if Node:
                self.count += 1
                RecursionNode(Node.LeftChild)
                RecursionNode(Node.RightChild)
        self.count = 0
        RecursionNode(self.Root)
        return self.count