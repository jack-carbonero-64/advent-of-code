import numpy as np


def getTreeVisibilityLimitOnAxis(axis, treeHeight, treeIndex):
    """
    Get the tree's visibility limit on the given axis

    Args:
        axis (np.ndarray(np.dtype=np.int8, np.ndim=1)): Axis on which to obtain the tree's visibility limits
        treeHeight (int): Height of the tree
        treeIndex (int): Index of the tree

    Returns:
        (int, int): Indices of the tree's visibility limits on the axis
    """

    # Trees that can obstruct current tree's visibility
    obstructTreesIndices = np.where(axis >= treeHeight)[0]

    # Current tree index in obstructTreesIndices
    currentTreeObstructionIndex = np.where(obstructTreesIndices == treeIndex)[0][0]

    # Limit before the tree
    if currentTreeObstructionIndex == 0:
        limitBeforeIndex = 0
    else:
        limitBeforeIndex = obstructTreesIndices[currentTreeObstructionIndex - 1]

    # Limit after the tree
    if currentTreeObstructionIndex == (len(obstructTreesIndices) - 1):
        limitAfterIndex = len(axis) - 1
    else:
        limitAfterIndex = obstructTreesIndices[currentTreeObstructionIndex + 1]

    return (limitBeforeIndex, limitAfterIndex)


def part1(grid):
    """
    First puzzle part

    Args:
        grid (np.ndarray(np.dtype=np.int8, np.ndim=2)): Grid representing the forest with tree heights as values
    """

    nbVisibleTrees = (grid.shape[0] * 2) + ((grid.shape[1] - 2) * 2)

    # Loop on the trees of the grid
    for rowIndex in range(1, len(grid) - 1):
        row = grid[rowIndex]

        for colIndex in range(1, len(row) - 1):
            col = grid[:, colIndex]
            treeHeight = col[rowIndex]

            # Check if the current tree is visible from at least one direction
            if ((np.max(row[:colIndex]) < treeHeight) or (np.max(row[colIndex+1:]) < treeHeight)
                    or (np.max(col[:rowIndex]) < treeHeight) or (np.max(col[rowIndex+1:]) < treeHeight)):
                nbVisibleTrees += 1

    print("\t- Part 1:", nbVisibleTrees)


def part2(grid):
    """
    Second puzzle part

    Args:
        grid (np.ndarray(np.dtype=np.int8, np.ndim=2)): Grid representing the forest with tree heights as values
    """

    bestScore = 0

    # Loop on the trees of the grid
    for rowIndex in range(len(grid)):
        row = grid[rowIndex]

        for colIndex in range(len(row)):
            col = grid[:, colIndex]
            treeHeight = col[rowIndex]

            # Retrieve visibility limit of the current tree on each axis
            (rowLimitBeforeIndex, rowLimitAfterIndex) = getTreeVisibilityLimitOnAxis(row, treeHeight, colIndex)
            (colLimitBeforeIndex, colLimitAfterIndex) = getTreeVisibilityLimitOnAxis(col, treeHeight, rowIndex)

            # Compute the score of the current tree and update the best score if possible
            currentScore = ((rowIndex - colLimitBeforeIndex) * (colLimitAfterIndex - rowIndex)
                            * (colIndex - rowLimitBeforeIndex) * (rowLimitAfterIndex - colIndex))

            if currentScore > bestScore:
                bestScore = currentScore

    print("\t- Part 2:", bestScore)


def main():
    """
    Main function
    """

    print("- Day 8:")

    # Read input
    file = open("../inputs/day8.txt", "r")
    lines = file.read().splitlines()
    file.close()

    # Convert input lines into a 2D array
    grid = np.empty([len(lines), len(lines[0])], dtype=np.int8)

    for i in range(len(lines)):
        grid[i] = np.fromiter(lines[i], np.int8)

    # Solve the problems
    part1(grid)
    part2(grid)


if __name__ == "__main__":
    main()
