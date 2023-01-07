def getStartMarkerIndex(partNumber, line, sequenceLength):
    """
    Find the start marker index depending of the sequence length given

    Args:
        partNumber (int): Puzzle part number
        line (str): Input line
        sequenceLength (int): Length of the unique characters sequence to find
    """

    startMarkerIndex = -1
    i = sequenceLength - 1
    currentChars = list(line[:i])
    nextChar = True

    while i < len(line) and nextChar:
        currentChars.append(line[i])

        if len(currentChars) == (sequenceLength + 1):
            currentChars.pop(0)

            if len("".join(set(currentChars))) == sequenceLength:
                startMarkerIndex = i + 1
                nextChar = False

        i += 1

    print(f"\t- Part {partNumber}: {startMarkerIndex}")


def main():
    """
    Main function
    """

    print("- Day 6:")

    # Read input
    file = open("../inputs/day6.txt", "r")
    lines = file.read().splitlines()
    file.close()

    # Solve the problems
    getStartMarkerIndex(1, lines[0], 4)
    getStartMarkerIndex(2, lines[0], 14)


if __name__ == "__main__":
    main()
