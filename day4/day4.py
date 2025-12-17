'''
- Input from file looks like this:

..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

Part 1:
- Forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions
- How many rolls of paper can be accessed by a forklift

1. Load input into 2d list of char
2. iterate through grid, check if less than four @ around each @. If yes, add it to the forklift access count
'''

import argparse
from pathlib import Path

def get_floor_plan(file_path: Path) -> list[list[str]] | None:
  floor_plan: list[list[str]] = []
  try:
    with open(file=file_path, mode="r") as f:
      floor_plan = [list(line) for line in f.read().splitlines()]
      return floor_plan
  except FileNotFoundError as e:
    print("Error while getting floor plan from file: ", e)
    return
  
def calc_forklift_access_cnt(floor_plan: list[list[str]]) -> int:
  count = 0
  removing = True
  while removing:
    removing = False
    for row_idx, aisle in enumerate(floor_plan):
      for col_idx, symbol in enumerate(aisle):
        if symbol != '@':
          continue
        num_surrounding = 0
        for i in range (row_idx-1, row_idx + 2):
          for j in range (col_idx-1, col_idx + 2):
            if i < 0 or i >= len(floor_plan) or j < 0 or j >= len(floor_plan[i]) or (i == row_idx and j == col_idx):
              continue
            if floor_plan[i][j] == '@':
              num_surrounding += 1
        if num_surrounding < 4:
          count += 1
          floor_plan[row_idx][col_idx] = 'x'
          removing = True
  return count
  

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process Day 4 Input")
    parser.add_argument("-f", "--file", dest="filepath", required=True,
                        help="Path to the input file to be processed.")
    args = parser.parse_args()
    floor_plan = get_floor_plan(file_path=Path(args.filepath))
    forklift_access_count = calc_forklift_access_cnt(floor_plan=floor_plan)
    print("Forklift access count:", forklift_access_count)
