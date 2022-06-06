from printer import Printer

class TestPrinter:
  def test_it_returns_simple_format(self):
    ptr = Printer()
    assert ptr.generate_string_to_print(3) == '1\n2\nthree'

  def test_more_complex(self):
    ptr = Printer()
    assert ptr.generate_string_to_print(7) == '1\n2\n3\n4\n5\n6\nseven'

