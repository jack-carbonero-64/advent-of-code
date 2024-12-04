from typing import List


def part1(lines: List[str]):
    """
    First puzzle part

    Args:
        lines (List[str]): Input lines
    """

    nb_words = 0

    for idx_row, row in enumerate(lines):
        for idx_char, char in enumerate(row):
            if char == "X":
                # -X / +X
                if idx_char >= 3 and row[idx_char - 3 : idx_char + 1] in ["XMAS", "SAMX"]:
                    nb_words += 1

                if idx_char < len(row) - 3 and row[idx_char : idx_char + 4] in ["XMAS", "SAMX"]:
                    nb_words += 1

                # -Y / +Y
                if idx_row >= 3 or idx_row < len(lines) - 3:
                    new_words = ["", ""]

                    for i in range(4):
                        if idx_row >= 3:
                            new_words[0] += lines[idx_row - i][idx_char]

                        if idx_row < len(lines) - 3:
                            new_words[1] += lines[idx_row + i][idx_char]

                    for new_word in new_words:
                        if new_word in ["XMAS", "SAMX"]:
                            nb_words += 1

                # Diagonals
                for x_dir in [-1, +1]:
                    for y_dir in [-1, +1]:
                        count = 0
                        next_it = True

                        new_word = ""

                        while next_it and count < 4:
                            new_x = idx_char + (x_dir * count)
                            new_y = idx_row + (y_dir * count)

                            if new_x >= 0 and new_x < len(row) and new_y >= 0 and new_y < len(lines):
                                new_word += lines[new_y][new_x]
                            else:
                                next_it = False

                            count += 1

                        if new_word in ["XMAS", "SAMX"]:
                            nb_words += 1

    print("\t- Part 1:", nb_words)


def part2(lines: List[str]):
    """
    Second puzzle part

    Args:
        lines (List[str]): Input lines
    """

    nb_words = 0

    for idx_row, row in enumerate(lines[1:-1], start=1):
        for idx_char, char in enumerate(row[1:-1], start=1):
            if char == "A":
                if (
                    # Diagonals - Top left => Bottom right
                    (
                        (lines[idx_row - 1][idx_char - 1] == "M" and lines[idx_row + 1][idx_char + 1] == "S")
                        or (lines[idx_row - 1][idx_char - 1] == "S" and lines[idx_row + 1][idx_char + 1] == "M")
                    )
                    # Diagonals - Top right => Bottom left
                    and (
                        (lines[idx_row - 1][idx_char + 1] == "S" and lines[idx_row + 1][idx_char - 1] == "M")
                        or (lines[idx_row - 1][idx_char + 1] == "M" and lines[idx_row + 1][idx_char - 1] == "S")
                    )
                ):
                    nb_words += 1

    print("\t- Part 2:", nb_words)


def main():
    """
    Main function
    """

    print("- Day 4:")

    # Read input
    file = open("../inputs/day4.txt", "r")
    lines = file.read().splitlines()
    file.close()

    # Solve the problems
    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()
