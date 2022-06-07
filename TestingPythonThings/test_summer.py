import unittest

from summer import Summer

class TestSummer(unittest.TestCase):

  def setUp(self):
    self.summer = Summer()

  def test_one(self):
    self.assertEqual(self.summer.sum([1,2],[3,4]), [4,6])

  def test_more_complex(self):
    self.assertEqual(self.summer.sum([3,8,7,6],[1,1,1,1]), [4,9,8,7])

  def test_edge_case(self):
    self.assertEqual(self.summer.sum([1,1,1], [1,2,3,4]), [2,3,4,4])