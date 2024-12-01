import numpy as np
from numpy.typing import NDArray


def part1(data: NDArray[np.int32]) -> None:
    """
    First puzzle part

    Args:
        data (NDArray[np.int32]): 2D array with 2 columns representing both list values
    """

    distance = 0

    for _ in range(data.shape[0]):
        minIndicesFromLists = data.argmin(axis=0)

        distance += abs(data[minIndicesFromLists[0], 0] - data[minIndicesFromLists[1], 1])

        data[minIndicesFromLists[0], 0] = np.iinfo(np.int32).max
        data[minIndicesFromLists[1], 1] = np.iinfo(np.int32).max

    print("\t- Part 1:", distance)


def part2(data: NDArray[np.int32]) -> None:
    """
    Second puzzle part

    Args:
        data (NDArray[np.int32]): 2D array with 2 columns representing both list values
    """

    score = 0

    for number in data[:, 0]:
        score += number * np.argwhere(data[:, 1] == number).shape[0]

    print("\t- Part 2:", score)


def main() -> None:
    """
    Main function
    """

    print("- Day 1:")

    data = np.loadtxt("../inputs/day1.txt", dtype=np.int32)

    # Solve the problems
    part1(data.copy())
    part2(data.copy())


if __name__ == "__main__":
    main()
