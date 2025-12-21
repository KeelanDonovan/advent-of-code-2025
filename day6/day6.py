'''
Day 6:
- Math Homework
- Input is a list of math problems
- Example Input:
    123 328  51  64 
    45  64   387 23 
    6   98   215 314
    *   +    *   + 
- Vertical numbers in the same column index need to be combined using the operator in the last row
- Rows are space separated
- Part 1:
  - Solve each column
  - Sum each answer together to get the final answer
  
- Part 2:
- Problems are still per space separated columns
- now, the operands are top to bottom per column in each problem from right to left. 
- for example
  123
  45
  6
  *
  would compute as 3 * 25 * 146
'''
import argparse
from pathlib import Path
import numpy as np

def basic_solve(problems: list[list[int | str]]) -> list[int]:
  """Computes Part 1 Answer

  Args:
      problems (list[list[int  |  str]]): list of problems with each problem be a list of operands (ints) with the operator string at the end ("+" , "*")

  Returns:
      list[int]: list of answers (ints) to the problems
  """
  answers: list[int] = []
  operator_map = {
    "+": np.sum,
    "*": np.prod
  }
  for problem in problems:
    op_str = problem[-1]
    op = operator_map.get(op_str)
    answers.append(int(op(problem[:-1])))
  return answers

def extract_problems_simple(path: Path) -> list[list[int | str]]:
  problems: list[list[int | str]] = []
  operators = ['+', '*']
  try:
    with open(file=path, mode="r") as f:
      for line in f:
        nums = line.strip().split()
        for j, num in enumerate(nums):
          if num == ' ' or '':
            continue     
          if len(problems) > j:
            (problems[j].append(num if num in operators else int(num)))
          else:
            problems.append([num if num in operators else int(num)])
      return problems
  except FileNotFoundError as e:
    print("Input file not found at path")
    return

def main() -> None:
  parser = argparse.ArgumentParser(description="Day 6 AOC Processor")
  parser.add_argument(
    "-f", 
    "--file",
    dest="filepath",
    required=True,
    help="Enter the input file path"
  )
  args = parser.parse_args()
  problems: list[int | str] = extract_problems_simple(path=args.filepath)
  answers: list[int] = basic_solve(problems=problems)
  print("Part 1 Sum: ", np.sum(answers))
  
  
if __name__ == "__main__":
  main()