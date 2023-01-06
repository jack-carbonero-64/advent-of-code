from copy import deepcopy


def getStacksEndLineIndex(lines):
    """
    Search the index of the line where stacks initialization ends

    Args:
        lines (list[str]): Input lines

    Returns:
        int: Index of the line where stacks initialization ends
    """

    stacksEndLineIndex = -1
    i = 0
    found = False

    while i < len(lines) and not found:
        if "[" not in lines[i]:
            found = True
            stacksEndLineIndex = i

        i += 1

    return stacksEndLineIndex


def getInitializedStacks(initializationLines, nbStacks):
    """
    Create and initialize the stacks using initialization lines

    Args:
        initializationLines (list[str]): Lines to initialize the stacks
        nbStacks (int): Number of stacks

    Returns:
        list[list[str]]: Initialized stacks
    """

    stacks = []

    for currentStackIndex in range(nbStacks):
        currentStack = []

        for line in initializationLines:
            currentCrate = line[1 + (4 * currentStackIndex)]

            if currentCrate != " ":
                currentStack.append(currentCrate)

        stacks.append(currentStack)

    return stacks


def moveCratesWithInstructions(multipleMovingMethod, instructions, stacks):
    """
    Move crates from the stacks according to the moving method and instructions given

    Args:
        multipleMovingMethod (int): Method to use when we are moving several crates (1: One crate at a time /
                                                                                     2: All crates at once)
        instructions (list[str]): Instructions to move the crates
        stacks (list[list[str]]): Stacks containing the crates to move

    Returns:
        list[list[str]]: Stacks after moving crates as instructed
    """

    # Loop on instructions
    for instruction in instructions:
        # Current move information
        moveData = instruction.split(" ")

        nbCratesToMove = (int)(moveData[1])
        stackFrom = (int)(moveData[3])
        stackTo = (int)(moveData[5])

        # Move crates
        for i in range(nbCratesToMove):
            if multipleMovingMethod == 1:
                stacks[stackTo - 1].insert(0, stacks[stackFrom - 1].pop(0))

            elif multipleMovingMethod == 2:
                stacks[stackTo - 1].insert(i, stacks[stackFrom - 1].pop(0))

    return stacks


def printTopCrates(partNumber, stacks):
    """
    Print the top crate from each stack

    Args:
        partNumber (int): Puzzle part number we want to display the result
        stacks (list[list[str]]): Stacks for which the top crate must be displayed
    """

    topCrates = ""

    for stack in stacks:
        topCrates += stack[0]

    print(f"\t- Part {partNumber}: {topCrates}")


def main():
    """
    Main function
    """

    print("- Day 5:")

    # Read input
    file = open("../inputs/day5.txt", "r")
    lines = file.read().splitlines()
    file.close()

    # Initialization
    stacksEndLineIndex = getStacksEndLineIndex(lines)
    nbStacks = (int)(lines[stacksEndLineIndex].strip().split(" ")[-1])
    stacks = getInitializedStacks(lines[:stacksEndLineIndex], nbStacks)

    # Solve the problems
    printTopCrates(1, moveCratesWithInstructions(1, lines[stacksEndLineIndex + 2:], deepcopy(stacks)))
    printTopCrates(2, moveCratesWithInstructions(2, lines[stacksEndLineIndex + 2:], deepcopy(stacks)))


if __name__ == "__main__":
    main()
