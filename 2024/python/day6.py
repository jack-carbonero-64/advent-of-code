# https://adventofcode.com/2024/day/6


from typing import List, Tuple


def is_next_pos_in_bound(position: List[int], direction: Tuple[int, int], shape: Tuple[int, int]):
    return (
        (position[0] + direction[0] >= 0)
        and (position[0] + direction[0] < shape[0])
        and (position[1] + direction[1] >= 0)
        and (position[1] + direction[1] < shape[1])
    )


def is_next_pos_obstruction(position: List[int], direction: Tuple[int, int], data: List[str]):
    return data[position[1] + direction[1]][position[0] + direction[0]] == "#"


def doing_patrol(
    data: List[str], start_pos: List[int], start_dir: Tuple[int, int], checking_loop: bool
) -> Tuple[List[List[int]], bool]:
    visited_pos: List[List[int]] = []
    visited_pos_dir: List[Tuple[int, int]] = []

    available_dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    current_pos = start_pos
    current_dir = start_dir

    visited_pos.append(current_pos)

    next_it = True

    while next_it:
        if not is_next_pos_in_bound(current_pos, current_dir, (len(data[0]), len(data))):
            break

        if is_next_pos_obstruction(current_pos, current_dir, data):
            current_dir = available_dir[(available_dir.index(current_dir) + 1) % 4]
        else:
            current_pos = [current_pos[0] + current_dir[0], current_pos[1] + current_dir[1]]

            if current_pos not in visited_pos:
                visited_pos.append(current_pos)
                visited_pos_dir.append(current_dir)
            elif checking_loop:
                idx_pos = visited_pos.index(current_pos)

                if idx_pos != 0 and current_dir == visited_pos_dir[idx_pos - 1]:
                    return (visited_pos, True)

    return (visited_pos, False)


def part_1(data: List[str], start_pos: List[int], start_dir: Tuple[int, int]) -> List[List[int]]:
    visited_pos, _ = doing_patrol(data, start_pos, start_dir, False)

    print("\t- Part 1:", len(visited_pos))

    return visited_pos


def part_2(data: List[str], visited_pos: List[List[int]], start_pos: List[int], start_dir: Tuple[int, int]):
    nb_positions = 0

    # Inserting an obstacle at each visited positions
    for current_pos in visited_pos[1:]:
        lines_copy = data.copy()

        line_copy = lines_copy[current_pos[1]]
        lines_copy[current_pos[1]] = line_copy[: current_pos[0]] + "#" + line_copy[(current_pos[0] + 1) :]

        _, is_loop = doing_patrol(lines_copy, start_pos, start_dir, True)

        if is_loop:
            nb_positions += 1

    print("\t- Part 2:", nb_positions)


def main():
    print("- Day 6:")

    # Read input
    file = open("../inputs/day6.txt", "r")
    lines = file.read().splitlines()
    file.close()

    # Retrieve start position and direction
    # Coordinates are in [X, Y] format
    start_pos: List[int] = [-1, -1]
    start_dir: Tuple[int, int] = (-1, -1)

    count_row = 0

    while count_row < len(lines):
        line = lines[count_row]

        if "v" in line:
            start_pos = [line.index("v"), count_row]
            start_dir = (0, 1)
            break
        elif "^" in line:
            start_pos = [line.index("^"), count_row]
            start_dir = (0, -1)
            break
        elif ">" in line:
            start_pos = [line.index(">"), count_row]
            start_dir = (1, 0)
            break
        elif "<" in line:
            start_pos = [line.index("<"), count_row]
            start_dir = (-1, 0)
            break

        count_row += 1

    # Solve the problems
    visited_pos = part_1(lines, start_pos, start_dir)
    part_2(lines, visited_pos, start_pos, start_dir)


if __name__ == "__main__":
    main()
