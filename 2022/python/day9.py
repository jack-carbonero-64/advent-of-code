def ropeSimulation(partNumber, nbKnots, lines):
    """
    Simulate a rope composed of a certain number of knots given as argument

    Args:
        partNumber (int): Puzzle part number
        nbKnots (int): Number of knots on the rope
        lines (list[str]): Input lines
    """

    # Initialization
    tailPositionsVisited = []
    knotsPositions = []

    for _ in range(nbKnots):
        knotsPositions.append((0, 0))

    tailPositionsVisited.append((0, 0))

    # Loop on input lines
    for line in lines:
        moveData = line.split(" ")

        for _ in range(int(moveData[1])):
            # Move the rope head
            if moveData[0] == "U":
                move = (0, 1)
            elif moveData[0] == "R":
                move = (1, 0)
            elif moveData[0] == "D":
                move = (0, -1)
            elif moveData[0] == "L":
                move = (-1, 0)

            knotsPositions[0] = (knotsPositions[0][0] + move[0], knotsPositions[0][1] + move[1])

            # Move other knots on the rope
            for i in range(1, nbKnots):
                # Check if the current knot and the previous knot are touching each other
                if (knotsPositions[i-1][0] not in range(knotsPositions[i][0] - 1, knotsPositions[i][0] + 2)
                        or knotsPositions[i-1][1] not in range(knotsPositions[i][1] - 1, knotsPositions[i][1] + 2)):
                    # X axis
                    if knotsPositions[i-1][0] > knotsPositions[i][0]:
                        knotsPositions[i] = (knotsPositions[i][0] + 1, knotsPositions[i][1])
                    elif knotsPositions[i-1][0] < knotsPositions[i][0]:
                        knotsPositions[i] = (knotsPositions[i][0] - 1, knotsPositions[i][1])

                    # Y axis
                    if knotsPositions[i-1][1] > knotsPositions[i][1]:
                        knotsPositions[i] = (knotsPositions[i][0], knotsPositions[i][1] + 1)
                    elif knotsPositions[i-1][1] < knotsPositions[i][1]:
                        knotsPositions[i] = (knotsPositions[i][0], knotsPositions[i][1] - 1)

                    # Check if this is a new position for the rope tail
                    if i == (nbKnots - 1) and knotsPositions[i] not in tailPositionsVisited:
                        tailPositionsVisited.append(knotsPositions[i])

    print(f"\t- Part {partNumber}:", len(tailPositionsVisited))


def main():
    """
    Main function
    """

    print("- Day 9:")

    # Read input
    file = open("../inputs/day9.txt", "r")
    lines = file.read().splitlines()
    file.close()

    # Solve the problems
    ropeSimulation(1, 2, lines)
    ropeSimulation(2, 10, lines)


if __name__ == "__main__":
    main()
