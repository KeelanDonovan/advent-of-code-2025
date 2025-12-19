'''
Input looks like:

3-5
10-14
16-20
12-18

1
5
8
11
17
32

the gap line separates the fresh ingredient id ranges from the availble ingredient IDs
an id is fresh if it is in any of the ranges
the ranges can overlap
need to count how many of the available are fresh
that is how many fall within a range at least once
'''
import argparse
from pathlib import Path
from typing import Tuple

def preprocess_input(file_path: Path) -> Tuple[list[(int, int)], list[int]] | None:
  try:
    with open(file=file_path, mode="r") as f:
      content = f.read().strip().split("\n\n")
      all_ranges = content[0].split("\n")
      all_available_ids = [int(id) for id in content[1].split("\n")]
      formatted_ranges = []
      for r in all_ranges:
        r = r.strip().split('-')
        formatted_ranges.append((int(r[0]), int(r[1])))
    return formatted_ranges, all_available_ids
  except Exception as e:
    print("Error during preprocessing: ", e)
    return
  
def extract_fresh_ids(ranges: list[(int, int)], available_ids: list[int]) -> list[int]:
  fresh_ids: list[int] = []
  for r in ranges:
    for id in available_ids:
      if (id >= r[0] and id <= r[1]) and (id not in fresh_ids):
        fresh_ids.append(id)
  return fresh_ids
      
def cnt_possible_fresh_ids(ranges: list[(int, int)]) -> int:
  ranges.sort()
  if not ranges:
    return 0

  cnt: int = 0
  curr_min, curr_max = ranges[0]

  for start, end in ranges[1:]:
    if start <= curr_max:
      if end > curr_max:
        curr_max = end
    else:
      cnt += curr_max - curr_min + 1
      curr_min, curr_max = start, end

  cnt += curr_max - curr_min + 1
  return cnt

if __name__ == "__main__":
  parser = argparse.ArgumentParser("Day 5 AOC")
  parser.add_argument("-f", "--f", dest="filepath", required=True, help="Path to the input file to be processed")
  args = parser.parse_args()
  
  ranges, available_ids = preprocess_input(file_path=Path(args.filepath))
  fresh_id_list = extract_fresh_ids(ranges=ranges, available_ids=available_ids)
  possible_fresh_id_cnt = cnt_possible_fresh_ids(ranges=ranges)
  print("Fresh Id Count: ", len(fresh_id_list))
  print("Possible Fresh ID Count:", possible_fresh_id_cnt)  
  
