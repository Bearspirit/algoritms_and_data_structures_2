
class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None 

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
class Queue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, item):
        self.__queue.append(item)

    def dequeue(self):
        if self.size() > 0:
            return self.__queue.pop(0)
        return None # если очередь пустая

    def size(self):
        return len(self.__queue)

class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False
  
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

    def DepthFirstSearch(self, VFrom, VTo):
        for i in self.vertex:
            i.Hit = False
        track_list = Stack()
        start_vertex = VFrom
        finish_vertex = VTo
        if (self.vertex[start_vertex] == None) or (self.vertex[finish_vertex] == None):
            return track_list.stack
        self.vertex[start_vertex].Hit = True
        track_list.push(self.vertex[start_vertex])
        return self.recurs_depth_track_macker(track_list, start_vertex, finish_vertex)
        
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету


    def recurs_depth_track_macker(self, track_list, Vfrom, Vto):
        if self.m_adjacency[Vfrom][Vto] == 1:
            track_list.push(self.vertex[Vto])
            return track_list.stack
        for i in range(0, self.max_vertex):
            if (self.m_adjacency[Vfrom][i] == 1) and (self.vertex[i].Hit == False):
                self.vertex[i].Hit = True
                track_list.push(self.vertex[i])
                return self.recurs_depth_track_macker(track_list, i, Vto)
            continue
        track_list.pop()
        if track_list.size() == 0:
            return track_list.stack
        current_vertex = self.vertex.index(track_list.stack[-1])
        return self.recurs_depth_track_macker(track_list, current_vertex, Vto)

    def BreadthFirstSearch(self, VFrom, VTo): #обход в ширину
        vertex_queue = Queue()
        track = {}
        for i in self.vertex:
            i.Hit = False
        start_vertex = VFrom
        finish_vertex = VTo
        if (self.vertex[start_vertex] == None) or (self.vertex[finish_vertex] == None):
            return []
        self.vertex[start_vertex].Hit = True
        vertex_queue.enqueue(self.vertex[start_vertex])
        track[start_vertex] = [start_vertex]
        return self.recurs_breadth_track_macker(vertex_queue, track, start_vertex, finish_vertex)

    def recurs_breadth_track_macker(self, vertex_queue, track, Vfrom, Vto):
        if self.IsEdge(Vfrom, Vto):
            self.vertex[Vto].Hit = True
            track[Vto] = track[Vfrom].copy()
            track[Vto].append(Vto)
            track.pop(Vfrom)
            track_list = []
            for el in track[Vto]:
                track_list.append(self.vertex[el])
            return track_list
        new_queue = False
        for i in range(0, self.max_vertex):
            if (self.IsEdge(Vfrom, i)) and (self.vertex[i].Hit == False):
                new_queue = True
                self.vertex[i].Hit = True
                track[i] = track[Vfrom].copy()
                track[i].append(i)
                vertex_queue.enqueue(self.vertex[i])
            continue
        if new_queue:
            track.pop(Vfrom)
        if vertex_queue.size() == 0:
            return []
        current_vertex = self.vertex.index(vertex_queue.dequeue())
        return self.recurs_breadth_track_macker(vertex_queue, track, current_vertex, Vto)

    def WeakVertices(self):

        no_triangle_vertex = []
        for vertex in self.vertex:
            if vertex is not None:
                vertex.Hit = False
                index = self.vertex.index(vertex)
                edge_list = []
                for i in range(0, self.max_vertex):
                    if self.IsEdge(index, i):
                        edge_list.append(i)
                    continue
                if len(edge_list) >= 2:
                    count = 0
                    for k in edge_list:
                        for j in edge_list:
                            if self.IsEdge(k,j):
                                count += 1
                    if count >=2:
                        vertex.Hit = True
            if vertex.Hit == False:
                no_triangle_vertex.append(vertex)
        return no_triangle_vertex

        # возвращает список узлов вне треугольников

        


