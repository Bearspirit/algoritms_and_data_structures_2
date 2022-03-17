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
        if find_result.Node is None:
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
        if find_result is None:
            find_result = self.Root
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
	
    def ParentLeftChild(self, ReceivingNode, NodeToDelete):
            if ReceivingNode.LeftChild == NodeToDelete:
                return True 
            return False

    def DeleteNodeByKey(self, key):
        NodeToDelete = self.FindNodeByKey(key)
        if not NodeToDelete.NodeHasKey: 
            return False   
        NodeToDelete = NodeToDelete.Node 
        if not NodeToDelete.LeftChild and not NodeToDelete.RightChild:
            if not NodeToDelete.Parent: 
                self.Root = None
            else:
                ParentNode = NodeToDelete.Parent
                if self.ParentLeftChild(ParentNode, NodeToDelete):
                    ParentNode.LeftChild = None
                else: 
                    ParentNode.RightChild = None
        else:
            if NodeToDelete.LeftChild and NodeToDelete.RightChild:
                ReceivingNode = NodeToDelete.RightChild
                if ReceivingNode.LeftChild:
                    ReceivingNode = self.FinMinMax(ReceivingNode,False)
                    if ReceivingNode.RightChild:
                        ReceivingNode.RightChild.Parent = ReceivingNode.Parent
                        ReceivingNode.Parent.LeftChild = ReceivingNode.RightChild
                    else: 
                        ReceivingNode.Parent.LeftChild = None
                    ReceivingNode.RightChild = NodeToDelete.RightChild
                    NodeToDelete.RightChild.Parent = ReceivingNode
                NodeToDelete.LeftChild.Parent = ReceivingNode
                ReceivingNode.LeftChild = NodeToDelete.LeftChild
            elif NodeToDelete.RightChild:
                ReceivingNode = NodeToDelete.RightChild
            else: 
                ReceivingNode = NodeToDelete.LeftChild               
            if NodeToDelete.Parent:
                ReceivingNode.Parent = NodeToDelete.Parent
                ParentNode = NodeToDelete.Parent
                if self.ParentLeftChild(ParentNode,NodeToDelete): 
                    ParentNode.LeftChild = ReceivingNode
                else: 
                    ParentNode.RightChild = ReceivingNode
            else:
                self.Root = ReceivingNode
                ReceivingNode.Parent = None
        NodeToDelete.Parent = None
        NodeToDelete.LeftChild = None
        NodeToDelete.RightChild = None
        return True
        # удаляем узел по ключу

    def Count(self):
        def recurs_for_count(Node):
            if Node:
                self.count += 1
                recurs_for_count(Node.LeftChild)
                recurs_for_count(Node.RightChild)
        self.count = 0
        recurs_for_count(self.Root)
        return self.count

    def WideAllNodes(self):
        def recurs_travel(travel_list, nodes_list):
            if len(travel_list) == 0:
                return nodes_list
            Node = travel_list[0]
            if Node.LeftChild is not None:
                travel_list.append(Node.LeftChild)
            if Node.RightChild is not None:
                travel_list.append(Node.RightChild)
            nodes_list.append(travel_list.pop(0))
            recurs_travel(travel_list, nodes_list)
        nodes_list = []
        Node = self.Root
        travel_list = []
        if Node is not None: travel_list.append(Node)
        recurs_travel(travel_list, nodes_list)
        return tuple(nodes_list)

    def DeepAllNodes(self, parametr):
        def in_order_recurs(Node, nodes_list):
            if Node:
                in_order_recurs(Node.LeftChild, nodes_list)
                nodes_list.append(Node)
                in_order_recurs(Node.RightChild, nodes_list)
        def post_order_recurs(Node, nodes_list):
            if Node:
                in_order_recurs(Node.LeftChild, nodes_list)
                in_order_recurs(Node.RightChild, nodes_list)
                nodes_list.append(Node)
        def pre_order_recurs(Node, nodes_list):
            if Node:
                nodes_list.append(Node)
                in_order_recurs(Node.LeftChild, nodes_list)
                in_order_recurs(Node.RightChild, nodes_list)
                
        nodes_list = []
        if parametr == 0:
            in_order_recurs(self.Root, nodes_list)
        elif parametr == 1:
            post_order_recurs(self.Root, nodes_list)
        else:
            pre_order_recurs(self.Root, nodes_list)
        return tuple(nodes_list)


