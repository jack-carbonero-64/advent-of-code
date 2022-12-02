def part1(lines):
    """
    First puzzle part

    Args:
        lines (list[str]): Input lines
    """

    bestNbCalories = 0
    currentNbCalories = 0

    # Loop on input lines
    for line in lines:
        # New elf
        if line == "":
            if currentNbCalories > bestNbCalories:
                bestNbCalories = currentNbCalories

            currentNbCalories = 0

        # Add calories for the current elf
        else:
            currentNbCalories += int(line)

    print("\t- Part 1:", bestNbCalories)


def part2(lines):
    """
    Second puzzle part

    Args:
        lines (list[str]): Input lines
    """

    bestNbCalories = [0, 0, 0]
    currentNbCalories = 0

    # Loop on input lines
    for line in lines:
        # New elf
        if line == "":
            i = 0
            next = True

            # Check where current calories can be insert
            while i < len(bestNbCalories) and next:
                if currentNbCalories > bestNbCalories[i]:
                    bestNbCalories.insert(i, currentNbCalories)
                    bestNbCalories.pop()

                    next = False

                i = i + 1

            currentNbCalories = 0

        # Add calories for the current elf
        else:
            currentNbCalories += int(line)

    # Compute result
    result = 0

    for calories in bestNbCalories:
        result += calories

    print("\t- Part 2:", result)


def main():
    """
    Main function
    """

    print("- Day 1:")

    # Read input
    file = open("../inputs/day1.txt", "r")
    lines = file.read().splitlines()
    file.close()

    # Solve the problems
    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()
