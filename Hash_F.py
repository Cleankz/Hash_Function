class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        array = self.slots
        if array.index(value) != 0:
            return array.index(value)
        else:
            return None

    def seek_slot(self, value):
         # находит индекс пустого слота для значения, или None
         return None

    def put(self, value):
         # записываем значение по хэш-функции
         
         # возвращается индекс слота или None,
         # если из-за коллизий элемент не удаётся
         # разместить 
         return None

    def find(self, value):
         # находит индекс слота со значением, или None
         return None