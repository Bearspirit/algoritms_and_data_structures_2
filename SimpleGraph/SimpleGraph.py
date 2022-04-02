class Vertex:

    def __init__(self, val):
        self.Value = val
  
class SimpleGraph:
	
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        
    def AddVertex(self, v):
        new_vertex = Vertex(v)
        for i in range(0, self.max_vertex):
            if self.vertex[i] == None:
                self.vertex[i] = new_vertex
                return True
        return False

        # ваш код добавления новой вершины 
        # с значением value 
        # в свободное место массива vertex
	
    # здесь и далее, параметры v -- индекс вершины
    # в списке  vertex
    def RemoveVertex(self, v):
        if self.vertex[v] == None:
            return False
        for connect in self.m_adjacency[v]:
            connect = 0
        for i in range(0, self.max_vertex):
            self.m_adjacency[i][v] = 0
        self.vertex[v] = None
        # ваш код удаления вершины со всеми её рёбрами
        return True
	
    def IsEdge(self, v1, v2):
        if (self.m_adjacency[v1][v2] == 1) or (self.m_adjacency[v2][v1] == 1):
            return True
        # True если есть ребро между вершинами v1 и v2
        return False
	
    def AddEdge(self, v1, v2):
        if (self.vertex[v1] == None) or (self.vertex[v2] == None):
            return False
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
        # добавление ребра между вершинами v1 и v2
        return True
	
    def RemoveEdge(self, v1, v2):
        if (self.m_adjacency[v1][v2] == 1) or (self.m_adjacency[v2][v1] == 1):
            self.m_adjacency[v1][v2] = 0
            self.m_adjacency[v2][v1] = 0
            return True
        # удаление ребра между вершинами v1 и v2
        return False
