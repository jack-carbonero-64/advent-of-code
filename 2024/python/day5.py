# https://adventofcode.com/2024/day/5


from math import floor
from typing import List, Tuple


def is_update_valid(update: List[int], ordering_rules: List[List[int]]) -> Tuple[bool, List[int]]:
    count_rule = 0

    while count_rule < len(ordering_rules):
        rule = ordering_rules[count_rule]

        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                return (False, rule)

        count_rule += 1

    return (True, [])


def part_1(ordering_rules: List[List[int]], num_pages_updates: List[List[int]]):
    sum = 0

    for update in num_pages_updates:
        is_valid, _ = is_update_valid(update, ordering_rules)

        if is_valid:
            sum += update[floor(len(update) / 2)]

    print("\t- Part 1:", sum)


def part_2(ordering_rules: List[List[int]], num_pages_updates: List[List[int]]):
    sum = 0

    for update in num_pages_updates:
        is_valid, rule_error = is_update_valid(update, ordering_rules)

        if not is_valid:
            while not is_valid:
                num_page_2 = update.pop(update.index(rule_error[1]))
                update.insert((update.index(rule_error[0]) + 1), num_page_2)

                is_valid, rule_error = is_update_valid(update, ordering_rules)

            sum += update[floor(len(update) / 2)]

    print("\t- Part 2:", sum)


def main():
    print("- Day 5:")

    # Read input
    file = open("../inputs/day5.txt", "r")
    lines = file.read().splitlines()
    file.close()

    # Retrieve rules
    ordering_rules: List[List[int]] = []

    count_line = 0

    while lines[count_line] != "" and count_line < len(lines):
        ordering_rules.append([int(x) for x in lines[count_line].split("|")])

        count_line += 1

    count_line += 1

    # Retrieve updates
    num_pages_updates: List[List[int]] = []

    while count_line < len(lines):
        num_pages_updates.append([int(x) for x in lines[count_line].split(",")])

        count_line += 1

    # Solve the problems
    part_1(ordering_rules, num_pages_updates)
    part_2(ordering_rules, num_pages_updates)


if __name__ == "__main__":
    main()
