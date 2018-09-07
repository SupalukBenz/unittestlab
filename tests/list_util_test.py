import unittest
from list_util import count_unique

class TestListUtilTest(unittest.TestCase):

    def test_list_empty(self):
      list = []
      self.assertEqual(0, len(list))

    def test_count_unique(self):
      list = ['a', 'b', 'a', 'c', 'b']
      self.assertEqual(2, count_unique(list))
      
      list = [1, 2, 3, 1, 5]
      self.assertEqual(1, count_unique(list))
    
    def test_all_same_element(self):
      list = ['a', 'a', 'a', 'a', 'a']
      self.assertEqual(1, count_unique(list))


if __name__ == '__main__':
    unittest.main()