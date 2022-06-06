INT_TO_WORDS = {
      1:"one",
      2:"two",
      3:"three",
      4:"four",
      5:"five",
      6:"six",
      7:"seven",
      8:"eight",
      9:"nine",
      0:"zero"
    }

class Printer:
  def create_ascending_array(number):
    numbers = []
    for num in range(1, number + 1):
      numbers.append(str(num) + '\n')
    return numbers

  def convert_int_to_word(int):
    return INT_TO_WORDS[int]

  def generate_string_to_print(self, number):
    numbers = Printer.create_ascending_array(number)
    numbers[-1] = Printer.convert_int_to_word(number)
    return ''.join(numbers)

  def print_list(self, num):
    print(Printer.generate_string_to_print(self, num))


ptr = Printer()
ptr.print_list(7)