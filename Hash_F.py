import sys
import random
class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
         idx_of_slot = sys.getsizeof(value)
         return idx_of_slot
    def seek_slot(self, value):
        IDX_EMPTY_SLOT = 0 # idx - IDX_EMPTY_SLOT
        for i in range(len(self.slots)):
            if self.slots[i] is not None:
                IDX_EMPTY_SLOT = (IDX_EMPTY_SLOT + self.hash_fun(self.slots[i]))
        IDX_EMPTY_SLOT = IDX_EMPTY_SLOT % self.size
        if IDX_EMPTY_SLOT == 0 and self.slots[IDX_EMPTY_SLOT] is None:
            return IDX_EMPTY_SLOT
        a = 0
        if IDX_EMPTY_SLOT > len(self.slots) - 1  or self.slots[IDX_EMPTY_SLOT] is not None:
            for i in range(1,len(self.slots)):
                a =  a + IDX_EMPTY_SLOT + (i * self.hash_fun(self.slots[i]))
                new_id = a % len(self.slots)
                if self.slots[new_id] is None:
                    return new_id
        if self.slots[IDX_EMPTY_SLOT] is None:
            return IDX_EMPTY_SLOT
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
            return slot_num
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
