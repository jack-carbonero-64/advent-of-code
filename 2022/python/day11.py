from functools import reduce
from math import floor
from copy import deepcopy
import operator


def readMonkeysData(lines):
    """
    Read monkeys data from the input lines

    Args:
        lines (list[str]): Input lines

    Returns:
        list[dict[str, Any]]: Monkeys data
    """

    monkeys = []

    # Loop on input lines
    for line in lines:
        line = line.strip()

        # New monkey
        if line.strip().startswith("Monkey"):
            currentMonkey = {}
            currentMonkey["nbInspections"] = 0
            monkeys.append(currentMonkey)

        # Worry levels for its starting items
        elif line.startswith("Starting items"):
            currentMonkey["items"] = [int(itemWorryLevel) for itemWorryLevel in line[16:].split(",")]

        # Operation to update the worry level following inspections of its items
        elif line.startswith("Operation"):
            currentMonkey["operation"] = line[11:]

        # Test to decide which monkey should receive the item
        elif line.startswith("Test"):
            currentMonkey["test"] = line[6:]

        # Monkey to receive the item if test is true
        elif line.startswith("If true"):
            currentMonkey["true"] = line[9:]

        # Monkey to receive the item if test is false
        elif line.startswith("If false"):
            currentMonkey["false"] = line[10:]

    return monkeys


def multiplicativeInverse(value, modulo):
    """
    Compute the multiplicative inverse of the given value for a specific modulo

    Args:
        value (int): Value whose multiplicative inverse must be found
        modulo (int): Modulo of linear congruence

    Returns:
        int: Multiplicative inverse of the value for the given modulo
    """

    if modulo == 1:
        return 1

    moduloCopy = modulo
    x0, x1 = 0, 1

    while value > 1:
        quotient = value // modulo

        value, modulo = modulo, (value % modulo)
        x0, x1 = (x1 - quotient * x0), x0

    if x1 < 0:
        x1 += moduloCopy

    return x1


def chineseRemainderTheory(moduli, remainders):
    """
    Solve a congruence system using the Chinese Remainder Theory

    Args:
        moduli (list[int]): Moduli of the congruence system
        remainders (list[int]): Desired remainders in the congruence system

    Returns:
        int: Congruence system solution
    """

    sumValue = 0

    moduliProduct = reduce((lambda accumulator, modulo: accumulator * modulo), moduli)

    for modulo, remainder in zip(moduli, remainders):
        productQuotient = moduliProduct // modulo
        sumValue += remainder * multiplicativeInverse(productQuotient, modulo) * productQuotient

    return sumValue % moduliProduct


def updateItemWorryLevel(isRelieved, itemWorryLevel, operator, secondOperand, moduli):
    """
    Compute the new item worry level of the one given as argument

    Args:
        isRelieved (bool): Indicates if we are relieved that the item is undamaged after an inspection
        itemWorryLevel (int): Old item worry level
        operator (builtin_function_or_method[[Any, Any], Any]): Operator in the operation to update the worry level
        secondOperand (str): Second operand of the operation to update the worry level
        moduli (list[int]): Moduli of the congruence system for the Chinese Remainder Theory
                            (Used only if we are not relieved after an inspection)

    Returns:
        int: New item worry level
    """

    # Solve the operation
    if secondOperand.isnumeric():
        itemWorryLevel = operator(itemWorryLevel, int(secondOperand))
    else:
        itemWorryLevel = operator(itemWorryLevel, itemWorryLevel)

    # Keep our worry levels manageable
    if isRelieved:
        itemWorryLevel = floor(itemWorryLevel / 3)
    else:
        remainders = [itemWorryLevel % modulo for modulo in moduli]
        itemWorryLevel = chineseRemainderTheory(moduli, remainders)

    return itemWorryLevel


def playKeepAway(partNumber, nbRounds, monkeys):
    """
    Play a version of the "Keep Away" game where the monkeys decide which monkey to throw their items to,
    depending on our worry levels

    Args:
        partNumber (int): Puzzle part number
        nbRounds (int): Number of rounds
        monkeys (list[dict[str, Any]]): Monkeys data
    """

    operatorTable = {
        "+": operator.add,
        "*": operator.mul
    }

    moduli = [int(monkey["test"].split(" ")[-1]) for monkey in monkeys]

    # Loop on game rounds
    for _ in range(nbRounds):
        for monkey in monkeys:
            operatorStr = monkey["operation"].split(" ")[-2]
            secondOperand = monkey["operation"].split(" ")[-1]

            monkeyTest = int(monkey["test"].split(" ")[-1])

            # Loop on items currently held by the monkey
            while len(monkey["items"]) > 0:
                monkey["nbInspections"] += 1

                currentItemWorryLevel = updateItemWorryLevel(partNumber == 1, monkey["items"].pop(0),
                                                             operatorTable[operatorStr], secondOperand, moduli)

                # Change the item owner
                if (currentItemWorryLevel % monkeyTest) == 0:
                    nextMonkeyIndex = int(monkey["true"].split(" ")[-1])
                else:
                    nextMonkeyIndex = int(monkey["false"].split(" ")[-1])

                monkeys[nextMonkeyIndex]["items"].append(currentItemWorryLevel)

    listNbInspections = [monkey["nbInspections"] for monkey in monkeys]
    listNbInspections.sort(reverse=True)

    print(f"\t- Part {partNumber}: {listNbInspections[0] * listNbInspections[1]}")


def main():
    """
    Main function
    """

    print("- Day 11:")

    # Read input
    file = open("../inputs/day11.txt", "r")
    lines = file.read().splitlines()
    file.close()

    # Initialization
    monkeys = readMonkeysData(lines)

    # Solve the problems
    playKeepAway(1, 20, deepcopy(monkeys))
    playKeepAway(2, 10000, deepcopy(monkeys))


if __name__ == "__main__":
    main()
