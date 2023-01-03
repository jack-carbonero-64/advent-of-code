import numpy as np


def part1(lines):
    """
    First puzzle part

    Args:
        lines (list[str]): Input lines
    """

    nbPairs = 0

    # Loop on input lines
    for line in lines:
        elfSections = []

        # Retrieve current elves sections
        for sectionsRange in line.split(","):
            sectionsId = sectionsRange.split("-")
            sectionsId[0] = (int)(sectionsId[0])
            sectionsId[1] = (int)(sectionsId[1])

            elfSections.append(sectionsId)

        # Retrieve the elves who have to clean the sections with the lowest and the highest ID
        minIdIndices = np.argwhere(elfSections == np.min(elfSections))[:, 0]
        maxIdIndices = np.argwhere(elfSections == np.max(elfSections))[:, 0]

        # Check if one elf's sections range fully contains the other elf one
        commonIdIndices = np.intersect1d(minIdIndices, maxIdIndices)

        if len(commonIdIndices) > 0:
            nbPairs += 1

    print("\t- Part 1:", nbPairs)


def part2(lines):
    """
    Second puzzle part

    Args:
        lines (list[str]): Input lines
    """

    nbPairs = 0

    # Loop on input lines
    for line in lines:
        elfSections = []

        # Retrieve current elves sections
        for sectionsRange in line.split(","):
            sectionsId = sectionsRange.split("-")
            sectionsId[0] = (int)(sectionsId[0])
            sectionsId[1] = (int)(sectionsId[1])

            elfSections.append(sectionsId)

        # Check if elves sections are overlapping with each other
        if ((elfSections[0][0] <= elfSections[1][0] <= elfSections[0][1])
                or (elfSections[0][0] <= elfSections[1][1] <= elfSections[0][1])
                or (elfSections[1][0] <= elfSections[0][0] <= elfSections[1][1])
                or (elfSections[1][0] <= elfSections[0][1] <= elfSections[1][1])):
            nbPairs += 1

    print("\t- Part 2:", nbPairs)


def main():
    """
    Main function
    """

    print("- Day 4:")

    # Read input
    file = open("../inputs/day4.txt", "r")
    lines = file.read().splitlines()
    file.close()

    # Solve the problems
    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()
