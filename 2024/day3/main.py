import os
import re
from typing import List
from functools import reduce

import utils

script_dir = os.path.dirname(__file__)
input_file_path = os.path.join(script_dir, "input.txt")


def part_1(input) -> int:
    regex = r"mul\((\d{1,3},\d{1,3})\)"

    multiplicands: List[str] = re.findall(regex, input)
    mult_results: List[int] = [
        reduce(lambda a, b: a * b, map(int, pair.split(","))) for pair in multiplicands
    ]

    return sum(mult_results)


def part_2(input) -> int:
    regex = r"mul\((\d{1,3},\d{1,3})\)|do\(\)|don't\(\)"

    result = 0

    mul_allowed = True
    for match in re.finditer(regex, input):
        if match.group(0) == "do()":
            mul_allowed = True
        elif match.group(0) == "don't()":
            mul_allowed = False
        elif mul_allowed:
            pair = match.group(1)
            mult_result = reduce(lambda a, b: a * b, map(int, pair.split(",")))
            result += mult_result

    return result


def main(debug: bool) -> None:
    with open(input_file_path, "r") as file:
        input = file.read()

    print("Part 1:", part_1(input))
    print("Part 2:", part_2(input))


if __name__ == "__main__":
    main(debug=False)
