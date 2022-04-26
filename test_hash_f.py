import unittest
import random
import sys
from Hash_F import HashTable
class MyTests(unittest.TestCase):

    def test_put(self):
        hash_t = HashTable(17,3)
        for i in range(20):
            hash_t.put(str(random.randint(0,17)))
    def test_find(self):
        hash_t = HashTable(17,3)
        for i in range(20):
            hash_t.put(str(i))
        for j in range(15):
            self.assertIn(str(hash_t.find(str(j))),hash_t.slots)
    def test_seek(self):
        hash_t = HashTable(17,3)
        self.assertEqual(0,hash_t.seek_slot("50"))
        for i in range(20):
            hash_t.put(str(i))
        self.assertEqual(None,hash_t.seek_slot("50"))
        
    def test_hash(self):
        hash_t = HashTable(17,3)
        for i in range(50):
            self.assertEqual(sys.getsizeof(str(i)),hash_t.hash_fun(str(i)))

if __name__ == '__main__':
    unittest.main()