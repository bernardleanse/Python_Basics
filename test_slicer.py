from slicer import Slicer

class TestSlicer:
	def test_slice_takes_first_two_chars_of_string(self):
		slicer = Slicer()
		assert slicer.slice(0,2,"hello") == "he"
	def test_more_complex_example(self):
		slicer = Slicer()
		assert slicer.slice(2, 5, "bigboystring") == "gbo"