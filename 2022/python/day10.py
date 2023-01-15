def drawPixelOnCRT(xValue, crt):
    """
    Draw a pixel on the given CRT screen

    Args:
        xValue (int): Value of X
        crt (list[list[str]]): CRT screen to draw on
    """

    if len(crt[-1]) == 40:
        crt.append([])

    if len(crt[-1]) in range(xValue - 1, xValue + 2):
        crt[-1].append("#")
    else:
        crt[-1].append(".")


def part1(lines):
    """
    First puzzle part

    Args:
        lines (list[str]): Input lines
    """

    cyclesToCheck = [20, 60, 100, 140, 180, 220]
    sumValue = 0

    xValue = 1
    cycleNumber = 0

    # Loop on input lines
    for line in lines:
        # Update current cycle number
        cycleNumber += 1

        instructionData = line.split(" ")

        # Addx instruction (2 cycles)
        if instructionData[0] == "addx":
            if cycleNumber in cyclesToCheck:
                sumValue += (cycleNumber * xValue)

            cycleNumber += 1

            if cycleNumber in cyclesToCheck:
                sumValue += (cycleNumber * xValue)

            xValue += int(instructionData[1])

        # Noop instruction (1 cycle)
        elif instructionData[0] == "noop":
            if cycleNumber in cyclesToCheck:
                sumValue += (cycleNumber * xValue)

    print("\t- Part 1:", sumValue)


def part2(lines):
    """
    Second puzzle part

    Args:
        lines (list[str]): Input lines
    """

    crt = [[]]
    xValue = 1

    # Loop on input lines
    for line in lines:
        instructionData = line.split(" ")

        # Addx instruction (2 cycles)
        if instructionData[0] == "addx":
            drawPixelOnCRT(xValue, crt)
            drawPixelOnCRT(xValue, crt)
            xValue += int(instructionData[1])

        # Noop instruction (1 cycle)
        elif instructionData[0] == "noop":
            drawPixelOnCRT(xValue, crt)

    print("\t- Part 2:")

    for crtLine in crt:
        print("\t\t" + "".join(crtLine))


def main():
    """
    Main function
    """

    print("- Day 10:")

    # Read input
    file = open("../inputs/day10.txt", "r")
    lines = file.read().splitlines()
    file.close()

    # Solve the problems
    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()
