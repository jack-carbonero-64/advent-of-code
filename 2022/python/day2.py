def part1(lines):
    """
    First puzzle part

    Args:
        lines (list[str]): Input lines
    """

    points = 0

    # Loop on input lines
    for line in lines:
        currentRound = line.split(" ")
        currentRound[0] = ord(currentRound[0]) - ord("A")
        currentRound[1] = ord(currentRound[1]) - ord("X")

        # Choice points
        points += currentRound[1] + 1

        # Draw
        if currentRound[0] == currentRound[1]:
            points += 3

        # Win
        elif currentRound[0] != ((currentRound[1] + 1) % 3):
            points += 6

    print("\t- Part 1:", points)


def part2(lines):
    """
    Second puzzle part

    Args:
        lines (list[str]): Input lines
    """

    points = 0

    # Loop on input lines
    for line in lines:
        currentRound = line.split(" ")
        opponentShape = ord(currentRound[0]) - ord("A")

        # Expected result points + Choice points
        if currentRound[1] == "X":
            points += ((opponentShape - 1) % 3) + 1

        elif currentRound[1] == "Y":
            points += 3
            points += opponentShape + 1

        elif currentRound[1] == "Z":
            points += 6
            points += ((opponentShape + 1) % 3) + 1

    print("\t- Part 2:", points)


def main():
    """
    Main function
    """

    print("- Day 2:")

    # Read input
    file = open("../inputs/day2.txt", "r")
    lines = file.read().splitlines()
    file.close()

    # Solve the problems
    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()
