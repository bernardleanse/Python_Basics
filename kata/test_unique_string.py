import unittest

class TestUniqueString(unittest.TestCase):
  def test_returns_string(self):
    ustr = UniqueString()
    self.assertIsInstance(UniqueString, str)