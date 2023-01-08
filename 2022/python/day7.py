def getFileTree(lines):
    """
    Retrieve the file tree through the terminal output lines

    Args:
        lines (list[str]): Terminal output lines

    Returns:
        dict[str, Any]: File tree
    """

    treeRoot = {
        "parent": None,
        "children": {},
        "size": 0
    }

    currentDirectory = treeRoot
    currentCommand = ""

    # Loop on terminal output lines
    for line in lines:
        # Commands
        if line[0] == "$":
            commandData = line.split(" ")[1:]

            # Move to another directory
            if commandData[0] == "cd":
                currentCommand = "cd"

                # Moving to root directory
                if commandData[1] == "/":
                    currentDirectory = treeRoot

                # Moving to parent directory
                elif commandData[1] == "..":
                    currentDirectory = currentDirectory["parent"]

                # Moving to a specific directory inside the current one
                else:
                    currentDirectory = currentDirectory["children"][commandData[1]]

            # List items in the current directory
            elif commandData[0] == "ls":
                currentCommand = "ls"

        # Commands outputs
        else:
            # Item from the current directory
            if currentCommand == "ls":
                itemData = line.split(" ")

                # Directory
                if itemData[0] == "dir":
                    newDirectory = {
                        "parent": currentDirectory,
                        "children": {},
                        "size": 0
                    }

                    currentDirectory["children"][itemData[1]] = newDirectory

                # File
                else:
                    newFile = {
                        "parent": currentDirectory,
                        "children": {},
                        "size": int(itemData[0])
                    }

                    currentDirectory["children"][itemData[1]] = newFile

                    # Add file size to the size of all ancestral directories
                    currentParent = currentDirectory

                    while currentParent is not None:
                        currentParent["size"] += newFile["size"]
                        currentParent = currentParent["parent"]

    return treeRoot


def getTotalDirectoriesSizeBelowMaxSize(treeItem, maxSize):
    """
    Compute, starting from the current item, the sum of the sizes of the directories whose sizes are less than
    the given maximum size

    Args:
        treeItem (dict[str, Any]): Current tree item to check
        maxSize (int): Maximum possible size for a directory to add its size to the sum

    Returns:
        int: Total size of directories smaller than the given maximum size
    """

    sumValue = 0

    # Recursive call for each child item
    for child in treeItem["children"].values():
        sumValue += getTotalDirectoriesSizeBelowMaxSize(child, maxSize)

    # Check if the current item is a directory and if its size is less than the maximum possible size
    if len(treeItem["children"]) != 0 and treeItem["size"] <= maxSize:
        sumValue += treeItem["size"]

    return sumValue


def getSmallestDirectorySizeAboveMinSize(treeItem, minSize):
    """
    Get the smallest directory size above the given minimum size

    Args:
        treeItem (dict[str, Any]): Current tree item to check
        minSize (int): Minimum possible size for the directory

    Returns:
        int: The smallest directory size above the given minimum size
    """

    size = -1

    # Recursive call for each child item and update the smallest size if possible
    for child in treeItem["children"].values():
        tmp = getSmallestDirectorySizeAboveMinSize(child, minSize)

        if tmp >= minSize and (tmp < size or size == -1):
            size = tmp

    # Check if the current item is a directory and if its size is the smallest currently found
    if len(treeItem["children"]) != 0 and treeItem["size"] >= minSize and (size == -1 or treeItem["size"] < size):
        size = treeItem["size"]

    return size


def main():
    """
    Main function
    """

    print("- Day 7:")

    # Read input
    file = open("../inputs/day7.txt", "r")
    lines = file.read().splitlines()
    file.close()

    # Initialization
    treeRoot = getFileTree(lines)
    spaceToFreeUp = (70000000 - treeRoot["size"] - 30000000) * (-1)

    # Solve the problems
    print("\t- Part 1:", getTotalDirectoriesSizeBelowMaxSize(treeRoot, 100000))
    print("\t- Part 2:", getSmallestDirectorySizeAboveMinSize(treeRoot, spaceToFreeUp))


if __name__ == "__main__":
    main()
