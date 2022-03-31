class Heap:

    def __init__(self):
        self.HeapArray = [] # хранит неотрицательные числа-ключи
		
    def MakeHeap(self, a, depth):
        self.Size = 2 ** (depth + 1) - 1
        self.HeapArray = [None] * self.Size
        for i in a: 
            self.Add(i)
	    # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth 

    def GetMax(self):
        def children_index(index):
            left_child = index * 2 + 1
            right_child = index * 2 + 2
            if self.HeapArray[right_child] and (self.HeapArray[right_child] > self.HeapArray[left_child]): 
                return right_child
            return left_child
        
        if self.HeapArray == [] or self.HeapArray[0] is None:
            return -1   # если куча пуста
      
        max_node = self.HeapArray[0]
        if self.Size == 1:
            self.HeapArray[0] = None
            return max_node

        first_none = self.node_index()
        if first_none is False:
            first_none = self.Size
        
        self.HeapArray[0] = self.HeapArray[first_none - 1]
        self.HeapArray[first_none - 1] = None

        child_index = children_index(0)
        i = 0
        while child_index and (self.HeapArray[i] < self.HeapArray[child_index]):
            self.HeapArray[i], self.HeapArray[child_index] = self.HeapArray[child_index], self.HeapArray[i]
            i = child_index
            if (child_index < (self.Size - 1) // 2) and self.HeapArray[(self.Size - 1) // 2]:
                child_index = children_index(i)
            else:
                child_index = 0
        
        return max_node
        # вернуть значение корня и перестроить кучу

    def Add(self, key):
        node_index = self.node_index()
        if node_index is not False:
            self.HeapArray[node_index] = key
            if node_index == 0:
                return
            parent_node = (node_index - 1) // 2
            while self.HeapArray[node_index] > self.HeapArray[parent_node] and node_index != 0:
                self.HeapArray[node_index], self.HeapArray[parent_node] = self.HeapArray[parent_node], self.HeapArray[node_index]
                node_index = parent_node
                parent_node = (node_index - 1) // 2
                if parent_node == -1: #если родительский узел выходит за рамки списка
                    return
        # добавляем новый элемент key в кучу и перестраиваем её
        return False # если куча вся заполнена
	

    def node_index(self):
        if self.HeapArray != []:
            for i in range(self.Size):
                if self.HeapArray[i] == None:
                    return i
        return False
