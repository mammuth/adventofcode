import os
from typing import List

script_dir = os.path.dirname(__file__)
input_file_path = os.path.join(script_dir, "input.txt")


def main() -> None:
    with open(input_file_path, "r") as file:
        data = file.read().splitlines()

    list_1, list_2 = zip(*(line.split() for line in data))

    list_1 = sorted(list_1)
    list_2 = sorted(list_2)

    distances: List[int] = [abs(int(x) - int(y)) for x, y in zip(list_1, list_2)]

    print(sum(distances))


if __name__ == "__main__":
    main()
