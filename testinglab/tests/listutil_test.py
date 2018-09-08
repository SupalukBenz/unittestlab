import unittest
from testinglab.listutil import count_unique, binary_search

class TestListUtilTest(unittest.TestCase):

    def test_list_empty(self):
      list = []
      self.assertEqual(0, len(list))

    def test_count_unique(self):
      list = ['a', 'b', 'a', 'c', 'b']
      self.assertEqual(3, count_unique(list))
      
      list = [1, 2, 3, 1, 5]
      self.assertEqual(4, count_unique(list))
    
    def test_all_same_element(self):
      list = ['a', 'a', 'a', 'a', 'a']
      self.assertEqual(1, count_unique(list))
    
class TestBinarySearch(unittest.TestCase):

  def test_binary_search_small(self):
    list = [1, 4, 22, 25, 38, 40, 49, 250, 999]
    self.assertEqual(1, binary_search(list, 4))
    self.assertEqual(2, binary_search(list, 22))
    self.assertEqual(5, binary_search(list, 40))
    self.assertEqual(8, binary_search(list, 999))

  def test_binary_self_large(self):
    large_list = []
    for i in range(100):
      large_list.append(i*2)

    self.assertEqual(1, binary_search(large_list, 2))
    self.assertEqual(62, binary_search(large_list, 124))
    self.assertEqual(99, binary_search(large_list, 198))

  def test_same_element(self):
    list = [1, 1, 1, 1, 1, 1]
    self.assertEqual(2, binary_search(list, 1))
  
  def test_not_found(self):
    list = [20, 33, 130, 200]
    self.assertEqual(-1, binary_search(list, 21))

  def test_none_element(self):
    with self.assertRaises(TypeError): binary_search([1, 2, 3, 4], None)
    
if __name__ == '__main__':
    unittest.main()