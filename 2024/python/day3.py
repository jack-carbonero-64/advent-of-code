import re
from typing import List


def part1(lines: List[str]):
    """
    First puzzle part

    Args:
        lines (List[str]): Input lines
    """

    sum = 0

    for line in lines:
        multiplications = re.findall(r"mul\(\d+,\d+\)", line)

        for mul in multiplications:
            numbers = [int(x) for x in mul[4:-1].split(",")]

            sum += numbers[0] * numbers[1]

    print("\t- Part 1:", sum)


def part2(lines: List[str]):
    """
    Second puzzle part

    Args:
        lines (List[str]): Input lines
    """

    sum = 0
    doMultiplication = True

    for line in lines:
        operations = re.findall(r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))", line)

        for op in operations:
            if op[1] != "":
                doMultiplication = True
            elif op[2] != "":
                doMultiplication = False

            elif op[0] != "" and doMultiplication:
                mul = op[0]
                numbers = [int(x) for x in mul[4:-1].split(",")]

                sum += numbers[0] * numbers[1]

    print("\t- Part 2:", sum)


def main():
    """
    Main function
    """

    print("- Day 3:")

    # Read input
    file = open("../inputs/day3.txt", "r")
    lines = file.read().splitlines()
    file.close()

    # Solve the problems
    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()
