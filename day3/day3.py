import argparse
import os

'''
AOC Day 3 Problem:
  - Batteries with joltage rating (value from 1-9). Puzzle input is voltage of different batteries arranged into lines. - Lines represent battery "banks".
  - Within each bank, you need to turn on exactly two batteries; 
  - Given a bank 12345 and you turn on batteries 2 and 4, the bank produces 24 jolts. (You cannot rearrange batteries.)
  - Find the maximum joltage possible from each bank; sum the maxes together.

Input example:
987654321111111
811111111111119
234234234234278
818181911112111'

Example Solution:
In 987654321111111, 98.
In 811111111111119, 89.
In 234234234234278, 78.
In 818181911112111, 92.
98 + 89 + 78 + 92 = 357.

Part 2:
12 digit number same rules apply
'''

class JoltageMaximizer:
  def __init__(self, path: str='input.txt'):
    self.path=path
    self.banks=self._get_banks_from_path()
    self.max_joltages_basic=self._get_max_voltages_basic()
    self.total_joltage=self._sum_max_joltages(self.max_joltages_basic)
    self.max_joltages_adv=self._get_max_voltages_advanced()
    self.total_jotage_adv=self._sum_max_joltages(self.max_joltages_adv)
    
  def _get_max_voltages_advanced(self) -> list[int]:
    max_joltages = []
    try:
      for bank in self.banks:
        n = len(bank)
        best_joltages = bank[n-12:]
        for i in range(n-13, -1, -1):
          if bank[i] >= best_joltages[0]:
            best_joltages.insert(0, bank[i])
            for i in range(1, len(best_joltages)):
              if i == len(best_joltages)-1:
                del best_joltages[i]
                break
              elif best_joltages[i] < best_joltages[i+1]:
                del best_joltages[i]
                break
        max_joltages.append(int("".join([str(x) for x in best_joltages])))
      print(max_joltages)  
      return max_joltages
      
    except Exception as e:
      print("Error processing banks for max volatages (advanced):", e)
      return
    
  def _sum_max_joltages(self, joltages: list[int]) -> int:
    return sum(joltages)
    
  def _get_max_voltages_basic(self) -> list[int]:
    max_joltages = []
    for bank in self.banks:
      n = len(bank)
      highest = 0
      next_highest = 0
      for i, joltage in enumerate(bank):
        if (joltage > highest) and (i < n - 1):
          highest = joltage
          next_highest = 0
        elif joltage > next_highest:
          next_highest = joltage
      
      max_joltage = int(str(highest) + str(next_highest))
      print(max_joltage)
      max_joltages.append(max_joltage)
    return max_joltages
      
  def _get_banks_from_path(self) -> list[list[int]]:
    if not os.path.exists(self.path):
      print(f"Error: File not found at {self.path}")
      return

    try:
      with open(file=self.path, mode='r') as f:
        banks = []
        for line in f:
          line = line.strip()
          banks.append([int(character) for character in line])
      return banks
    except Exception as e:
      print("Error extracting banks from file:", e)
  
if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Process Advent of Code Day 3 input file.")
  parser.add_argument(
        "-f", "--file",
        dest="filepath",
        required=True,
        help="Path to the input file to be processed."
  )

  args = parser.parse_args()
  maximizer = JoltageMaximizer(path=args.filepath)
  print("Total Voltage:", maximizer.total_joltage)
  print("Total Voltage:", maximizer.total_jotage_adv)
  
      
    
    
    


