class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        self.tree_size = 2**(depth+1)-1
        self.Tree = [None] * self.tree_size # массив ключей

	
    def FindKeyIndex(self, key):
        # ищем в массиве индекс ключа
        index = 0
        while index < self.tree_size:
            if self.Tree[index] == key:
                return index
            if self.Tree[index] == None:
                return index*-1
            if key > self.Tree[index]:
                index = 2*index+2
            else:
                index = 2*index+1
        return None # не найден
	
    def AddKey(self, key):
        # добавляем ключ в массив
        index = self.FindKeyIndex(key)
        if index == 0:
            if self.Tree[index] == None:
                self.Tree[index] = key
                return index
        if index < 0:
            self.Tree[index*-1] = key
            return index*-1
        return -1 
        # индекс добавленного/существующего ключа или -1 если не удалось