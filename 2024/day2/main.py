import os
from typing import List

script_dir = os.path.dirname(__file__)
input_file_path = os.path.join(script_dir, "input.txt")


def is_safe(report: List[str], debug: bool) -> bool:
    """
    a report only counts as safe if both of the following are true:

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.
    """
    levels: List[int] = list(map(int, report.split()))

    # non-unique values -> not all increasing or decreasing
    if len(levels) != len(set(levels)):
        if debug:
            print(report, "unsafe because of duplicated values")
        return False

    # not all increasing or decreasing
    if levels != sorted(levels) and levels != sorted(levels, reverse=True):
        if debug:
            print(report, "unsafe because not consistently increasing or decreasing")
        return False

    # any two adjacent levels differ by at least one and at most three
    for i in range(1, len(levels)):
        if abs(levels[i] - levels[i - 1]) > 3:
            if debug:
                print(report, "unsafe because of difference between adjacent levels")
            return False

    if debug:
        print(report, "safe")
    return True


def is_safe_with_tolerance(report: List[str], debug: bool) -> bool:
    # todo this should rather be a recursive function with tolerance: int as a parameter
    #   but the is_safe function I wrote for part1 was annoying to refactor to support that...
    if is_safe(report, debug=debug):
        return True

    levels: List[int] = list(map(int, report.split()))
    for index, _ in enumerate(levels):
        modified_levels = levels.copy()
        del modified_levels[index]

        modified_report = " ".join(map(str, modified_levels))
        if is_safe(modified_report, debug=False):
            if debug:
                print(report, "safe after removing", levels[index])
            return True

    if debug:
        print(report, "unsafe")
    return False


def main(debug: bool) -> None:
    with open(input_file_path, "r") as file:
        reports = file.read().splitlines()

    safe_reports = len([report for report in reports if is_safe(report, debug=debug)])

    print("Part 1:", safe_reports)

    safe_reports = len(
        [report for report in reports if is_safe_with_tolerance(report, debug=debug)]
    )

    print("Part 2:", safe_reports)


if __name__ == "__main__":
    main(debug=False)
