def part1(lines):
    """
    First puzzle part

    Args:
        lines (list[str]): Input lines
    """

    priorities = 0

    # Loop on input lines
    for line in lines:
        compartments = []

        # Separate compartments
        secondHalfStartIndex = len(line) // 2

        compartments.append(line[:secondHalfStartIndex])
        compartments.append(line[secondHalfStartIndex:])

        # Retrieve the Unicode code point of the common character from the current compartments
        commonCharCodePoint = ord("".join(set(compartments[0]).intersection(compartments[1])))

        # Update priorities value
        if commonCharCodePoint >= ord("a"):
            priorities += commonCharCodePoint + 1 - ord("a")
        else:
            priorities += commonCharCodePoint + 27 - ord("A")

    print("\t- Part 1:", priorities)


def part2(lines):
    """
    Second puzzle part

    Args:
        lines (list[str]): Input lines
    """

    priorities = 0

    # Loop on input lines
    for i in range(0, len(lines), 3):
        currentGroup = lines[i: i + 3]

        # Retrieve the Unicode code point of the common character from the current group
        commonChar = "".join(set(currentGroup[0]).intersection(currentGroup[1]))
        commonChar = "".join(set(commonChar).intersection(currentGroup[2]))

        commonCharCodePoint = ord(commonChar)

        # Update priorities value
        if commonCharCodePoint >= ord("a"):
            priorities += commonCharCodePoint + 1 - ord("a")
        else:
            priorities += commonCharCodePoint + 27 - ord("A")

    print("\t- Part 2:", priorities)


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
