from typing import List


def isRowSafe(rowData: List[int]):
    """
    Check if a row is safe:
        1) Difference between each values should be between 1 and 3
        2) Should be only increasing or decreasing

    Args:
        rowData (List[int]): Row data

    Returns:
        bool: Whether row is safe or not
    """

    isIncreasing = rowData[0] < rowData[1]

    for idx, number in enumerate(rowData[1:], start=1):
        if (
            (not (1 <= abs(number - rowData[idx - 1]) <= 3))
            or (isIncreasing and number < rowData[idx - 1])
            or (not isIncreasing and number > rowData[idx - 1])
        ):
            return False

    return True


def part1(data: List[List[int]]):
    """
    First puzzle part

    Args:
        data (List[List[int]]): 2D array
    """

    nbSafe = 0

    for rowData in data:
        if isRowSafe(rowData):
            nbSafe += 1

    print("\t- Part 1:", nbSafe)


def part2(data: List[List[int]]):
    """
    Second puzzle part

    Args:
        data (List[List[int]]): 2D array
    """

    nbSafe = 0

    for rowData in data:
        isSafe = isRowSafe(rowData)

        if not isSafe:
            for idx in range(len(rowData)):
                tmp = rowData[:]
                tmp.pop(idx)

                isSafe = isRowSafe(tmp)

                if isSafe:
                    break

        if isSafe:
            nbSafe += 1

    print("\t- Part 2:", nbSafe)


def main():
    """
    Main function
    """

    print("- Day 2:")

    # Read input
    file = open("../inputs/day2.txt", "r")
    lines = file.read().splitlines()
    file.close()

    data: List[List[int]] = []

    for line in lines:
        rowData = [int(number) for number in line.strip().split(" ")]
        data.append(rowData)

    # Solve the problems
    part1(data)
    part2(data)


if __name__ == "__main__":
    main()
