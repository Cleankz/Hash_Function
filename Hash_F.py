import sys
import random

from attr import has
class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
         idx_of_slot = sys.getsizeof(value)
         # в качестве value поступают строки!

         # всегда возвращает корректный индекс слота
         return idx_of_slot
    def seek_slot(self, value):
        idx = 0
        for i in range(len(self.slots)):
            if self.slots[i] is not None:
                idx = (idx + self.hash_fun(self.slots[i]))
        idx = idx % self.size
        if idx == 0 and self.slots[idx] is None:
            return idx
        a = 0
        if idx > len(self.slots) - 1  or self.slots[idx] is not None:
            for i in range(1,len(self.slots)):
                a =  a + idx + (i * self.hash_fun(self.slots[i]))
                new_id = a % len(self.slots)
                if self.slots[new_id] is None:
                    return new_id
        if self.slots[idx] is None:
            return idx
        x = 0
        for i in range(len(self.slots)):
            if self.slots[i] is not None:
                x += 1
        if len(self.slots)  - x == 1:
            for i in range(len(self.slots)):
                if self.slots[i] is None:
                    return i
        return None
         # находит индекс пустого слота для значения, или None

    def put(self, value):
         # записываем значение по хэш-функции
        slot_num = self.seek_slot(value)
        if slot_num is not None:
            self.slots[slot_num] = value
        else:
            return None
         # возвращается индекс слота или None,
         # если из-за коллизий элемент не удаётся
         # разместить 

    def find(self, value):
        for i in range(len(self.slots)):
            if self.slots[i] == value:
                return i
        return None
#hash = HashTable(17,3)
#for i in range(20):
    #print(hash.put(str(random.randint(0,17))))

#for i in range(17):
    #print(hash.find(str(random.randint(0,17))))