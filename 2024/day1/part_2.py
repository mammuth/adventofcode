import os
from typing import List
from collections import Counter, defaultdict

script_dir = os.path.dirname(__file__)
input_file_path = os.path.join(script_dir, "input.txt")


def main() -> None:
    with open(input_file_path, "r") as file:
        data = file.read().splitlines()

    list_1, list_2 = zip(*(map(int, line.split()) for line in data))

    list_1: List[int] = sorted(list(list_1))
    list_2: List[int] = sorted(list(list_2))

    list_2_counter: dict[int, int] = defaultdict(int, Counter(list_2))

    list_1_weighted: List[int] = [x * list_2_counter[x] for x in list_1]

    print(sum(list_1_weighted))


if __name__ == "__main__":
    main()
