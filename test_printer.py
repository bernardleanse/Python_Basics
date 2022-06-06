from printer import Printer

class TestPrinter:
  def test_it_returns_simple_format():
    ptr = Printer()
    assert ptr.print(3) == '1\n2\nthree'

