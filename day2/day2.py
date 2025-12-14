import argparse
import os

'''
Problem Notes:
  - There are invalid product IDs that were inputted into the database. Our goal is to identify them.
  - Invalid inputs are a sequence of digits repeated twice (i.e. 55, 101101, 43284328)
  - None of the numbers have leading 0s. 
  - Identify all invalid IDs and add them together

Input:
  - A file containing a list of ranges that still need to be checked. (i.e. 11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124)
'''

class InvalidIdIdentifier:
  def __init__(self, path: str='input.txt'):
    self.path = path
    self.ranges = self._get_range_tuples()
    self.invalid_ids_basic = self._extract_invalid_ids_basic()
    self.invalid_ids_sum_basic = self._sum_invalid_ids(ids=self.invalid_ids_basic)
    self.invalid_ids_advanced = self._extract_invalid_ids_adv()
    self.invalid_ids_sum_adv = self._sum_invalid_ids(ids=self.invalid_ids_advanced)
    
  def _sum_invalid_ids(self, ids: list[int]):
    return sum(ids)
  
  def _extract_invalid_ids_adv(self) -> list[int]:
    invalid_ids = []
    for r in self.ranges:
      for i in range(r[0], r[1] + 1):
        num_string = str(i)
        n = len(num_string)
        divisors = self.get_divisors(num=n)
        for divisor in divisors:
          values = [num_string[i:i+divisor] for i in range(0, n, divisor)]
          first_value = values[0]
          is_invalid = (all(value == first_value for value in values)) and (len(values) > 1)
          if is_invalid:
            invalid_ids.append(i)
            break
    return invalid_ids
        
  def get_divisors(self, num: int):
    divisors = []
    for i in range (1, num + 1):
      if num % i == 0:
        divisors.append(i)
    return divisors
          
  
  def _extract_invalid_ids_basic(self) -> list[int]:
    invalid_ids = []
    for r in self.ranges:
      for i in range(r[0], r[1] + 1):
        num_string = str(i)
        n = len(num_string)
        if (n % 2) != 0:
          continue
        else:
          mid = n // 2
          sub1 = num_string[:mid]
          sub2 = num_string[mid:]
          if sub1 == sub2:
            invalid_ids.append(i)
    return invalid_ids
  
  def _get_range_tuples(self) -> list[(int, int)]:
    if not os.path.exists(self.path):
      print(f"Error: File not found at {self.path}")
      return []
    range_tuples = []
    try:
      with open(file=self.path, mode="r") as f:
        ranges = f.read().split(",")
        
        for r in ranges:
          curr_range = r.split("-")
          range_tuples.append((int(curr_range[0]), int(curr_range[1])))
      return range_tuples
    
    except Exception as e:
      print(f"An error occurred while reading the file: {e}")
      return []
    
if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Process Advent of Code Day 2 input file.")
  parser.add_argument(
        "-f", "--file",
        dest="filepath",
        required=True,
        help="Path to the input file to be processed."
  )

  args = parser.parse_args()
  day2solver = InvalidIdIdentifier()
  print("The invalid ID sum is: ", day2solver.invalid_ids_sum_basic)
  print("The advanced invalid ID sum is: ", day2solver.invalid_ids_sum_adv)