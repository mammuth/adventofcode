import os
import re
from typing import List
from functools import reduce

script_dir = os.path.dirname(__file__)
input_file_path = os.path.join(script_dir, "input.txt")


def main(debug: bool) -> None:
    with open(input_file_path, "r") as file:
        input = file.read()

    regex = r"mul\((\d{1,3},\d{1,3})\)"

    multiplicands: List[str] = re.findall(regex, input)
    mult_results: List[int] = [
        reduce(lambda a, b: a * b, map(int, pair.split(","))) for pair in multiplicands
    ]

    result = sum(mult_results)
    print(result)


if __name__ == "__main__":
    main(debug=False)
