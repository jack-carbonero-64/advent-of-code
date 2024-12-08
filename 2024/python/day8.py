# https://adventofcode.com/2024/day/8


import operator
from typing import Dict, List, Tuple


def is_position_in_bound(position: List[int], shape: Tuple[int, int]) -> bool:
    return (position[0] >= 0 and position[0] < shape[0]) and (position[1] >= 0 and position[1] < shape[1])


def get_antinodes_created_by_antennas(
    shape: Tuple[int, int], antennas_positions: List[List[int]], with_resonant_harmonics_effects: bool
) -> List[List[int]]:
    antinodes_positions: List[List[int]] = []

    dist_between_antennas = [
        antennas_positions[1][0] - antennas_positions[0][0],
        antennas_positions[1][1] - antennas_positions[0][1],
    ]

    for idx_antennas, op in enumerate([operator.sub, operator.add]):
        # Without resonant harmonics effects
        if not with_resonant_harmonics_effects:
            antinode_position_tmp = [
                op(antennas_positions[idx_antennas][0], dist_between_antennas[0]),
                op(antennas_positions[idx_antennas][1], dist_between_antennas[1]),
            ]

            if is_position_in_bound(antinode_position_tmp, shape):
                antinodes_positions.append(antinode_position_tmp)

        # With resonant harmonics effects
        else:
            antinodes_positions.extend(antennas_positions)

            antinote_position_tmp = antennas_positions[idx_antennas]
            is_in_bound = True

            while is_in_bound:
                antinote_position_tmp = [
                    op(antinote_position_tmp[0], dist_between_antennas[0]),
                    op(antinote_position_tmp[1], dist_between_antennas[1]),
                ]

                if not is_position_in_bound(antinote_position_tmp, shape):
                    is_in_bound = False
                else:
                    antinodes_positions.append(antinote_position_tmp)

    return antinodes_positions


def solving_problems(lines: List[str], antennas_positions: Dict[str, List[List[int]]]):
    data_shape = (len(lines[0]), len(lines))

    unique_positions_1: List[List[int]] = []
    unique_positions_2: List[List[int]] = []

    for _, positions in antennas_positions.items():
        for idx_pos_1, pos_1 in enumerate(positions):
            for pos_2 in positions[idx_pos_1 + 1 :]:
                # Without resonant harmonics effects
                antinodes = get_antinodes_created_by_antennas(data_shape, [pos_1, pos_2], False)

                for antinode in antinodes:
                    if antinode not in unique_positions_1:
                        unique_positions_1.append(antinode)

                # With resonant harmonics effects
                antinodes = get_antinodes_created_by_antennas(data_shape, [pos_1, pos_2], True)

                for antinode in antinodes:
                    if antinode not in unique_positions_2:
                        unique_positions_2.append(antinode)

    print("\t- Part 1:", len(unique_positions_1))
    print("\t- Part 2:", len(unique_positions_2))


def main():
    print("- Day 8:")

    # Read input
    file = open("../inputs/day8.txt", "r")
    lines = file.read().splitlines()
    file.close()

    # Retrieve antennas
    antennas_positions: Dict[str, List[List[int]]] = {}

    for idx_line, line in enumerate(lines):
        for idx_char, char in enumerate(line):
            if char != ".":
                if char not in antennas_positions:
                    antennas_positions[char] = []

                antennas_positions[char].append([idx_char, idx_line])

    # Solve the problems
    solving_problems(lines, antennas_positions)


if __name__ == "__main__":
    main()
