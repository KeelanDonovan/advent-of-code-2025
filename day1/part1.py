import argparse
import os

def get_password(path: str) -> int:
    if not os.path.exists(path):
        print(f"Error: File not found at {path}")
        return 0

    dial_position = 50  # starting position
    password = 0        # number of times we land on 0

    try:
        with open(path, "r") as f:
            for raw_line in f:
                line = raw_line.strip()
                if not line:
                    continue  # skip empty lines

                direction = line[0]
                try:
                    change_value = int(line[1:]) % 100
                except ValueError:
                    print(f"Warning: Invalid line '{line}', skipping.")
                    continue

                if direction == "L":
                    dial_position = (dial_position - change_value) % 100
                elif direction == "R":
                    dial_position = (dial_position + change_value) % 100
                else:
                    print(f"Warning: Unknown direction '{direction}' in line '{line}', skipping.")
                    continue

                if dial_position == 0:
                    password += 1

        return password

    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process Advent of Code Day 1 input file.")
    parser.add_argument(
        "-f", "--file",
        dest="filepath",
        required=True,
        help="Path to the input file to be processed."
    )

    args = parser.parse_args()
    result = get_password(args.filepath)
    print(f"The password is: {result}")
