class Summer:

  def get_longest_array(self, arr_one, arr_two):
    if len(arr_one) > len(arr_two):
      return arr_one
    else:
      return arr_two

  def get_shortest_array(self, arr_one, arr_two):
    if len(arr_one) > len(arr_two):
      return arr_two
    else:
      return arr_one
  
  def sum(self, array_one, array_two):
    summed_array = []
    for a, b in zip(array_one, array_two):
      summed_array.append(a + b)
    
    longest = self.get_longest_array(array_one, array_two)
    shortest = self.get_shortest_array(array_one, array_two)
    to_join_on = longest[len(shortest):]
    summed_array += to_join_on

    return summed_array