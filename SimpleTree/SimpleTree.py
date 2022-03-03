class SimpleTreeNode:
	
    def __init__(self, val, parent):
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов
	
class SimpleTree:

    def __init__(self, root):
        self.Root = root # корень, может быть None
	
    def AddChild(self, ParentNode, NewChild):
        if ParentNode is None:
            self.Root = NewChild
        else:
            NewChild.Parent = ParentNode
            ParentNode.Children.append(NewChild)
  
    def DeleteNode(self, NodeToDelete):
        def children_killer(NodeToDelete, ParentNode):
            for i in range(len(ParentNode.Children)):
                if ParentNode.Children[i] == NodeToDelete:
                    ParentNode.Children[i] = ParentNode.Children[-1]
                    return ParentNode.Children[:-1]


        ParentNode = NodeToDelete.Parent
        NodeToDelete.Parent = None 
        ParentNode.Children = children_killer(NodeToDelete, ParentNode)

    def GetAllNodes(self):
        if self.Root == None: 
            return []
        Node = self.Root
        all_nodes_list = []
        all_nodes_list.append(Node)
        count = 0
        while count < len(all_nodes_list):
            Node = all_nodes_list[count]
            for i in Node.Children:
                all_nodes_list.append(i)
            count += 1
        return all_nodes_list

    def FindNodesByValue(self, val):
        nodes_list = self.GetAllNodes()
        values_list = []
        for i in range(len(nodes_list)):
            if nodes_list[i].NodeValue == val:
                values_list.append(nodes_list[i])
        return values_list
    
   
    def MoveNode(self, OriginalNode, NewParent):
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)
   
    def Count(self):
        return len(self.GetAllNodes())

    def LeafCount(self):
        count = 0
        for node in self.GetAllNodes():
            if node.Children == []:
                count += 1
        return count