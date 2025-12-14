import argparse
import os

class Day1Solver:
  def __init__(self, path: str, dial_position: int=50):
    self.path = path
    self.dial_position = 50
    self.password = 0
  
  def solve(self):
    if not os.path.exists(self.path):
      print(f"Error: File not found at {self.path}")
      return 0
    
    self.dial_position = 50
    self.password = 0
    
    try:
      with open(self.path, "r") as f:
        for line in f:
          line = line.strip()
          # print(line)
          if not line:
            continue
          direction = line[0]
          # print(direction)
          try:
            change_value = int(line[1:])
            # (print(change_value))
            for i in range(change_value):
              if direction == 'L':
                if self.dial_position == 0:
                  self.dial_position += 99
                else:
                  self.dial_position -= 1 
              elif direction == 'R': 
                if self.dial_position == 99:
                  self.dial_position -= 99
                else:
                  self.dial_position += 1
              if self.dial_position == 0:
                self.password +=1
              # print(self.dial_position)
          except ValueError:
            print(f"Warning: Invalid line '{line}', skipping.")
            continue
            
      return self.password
    except Exception as e:
      print(f"An error occurred while reading the file: {e}")
      return 0
    
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Process Advent of Code Day 1 input file.")
  parser.add_argument(
        "-f", "--file",
        dest="filepath",
        required=True,
        help="Path to the input file to be processed."
  )

  args = parser.parse_args()
  solver = Day1Solver(path=args.filepath)
  print("Password:", solver.solve())