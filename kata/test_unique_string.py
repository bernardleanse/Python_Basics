import unittest

from unique_string import UniqueString

class TestUniqueString(unittest.TestCase):
  def test_returns_string(self):
    ustr = UniqueString()
    self.assertIsInstance(ustr.get(), str)