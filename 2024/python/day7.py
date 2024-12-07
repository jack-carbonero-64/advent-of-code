# https://adventofcode.com/2024/day/7


from typing import List, Tuple


def testing_operators(
    current_value: int, operands: List[int], expected_result: int, is_part_two: bool
) -> List[Tuple[int, int, int]]:
    final_results: List[Tuple[int, int, int]] = []

    current_operand = operands[0]
    next_operands = operands[1:]

    # Compute values depending on operation
    add_res = current_value + current_operand
    mul_res = current_value * current_operand
    concat_res = -1

    if is_part_two:
        concat_res = int(str(current_value) + str(current_operand))

    # Remaining operands
    if len(next_operands) > 0:
        if add_res <= expected_result:
            final_results.extend(testing_operators(add_res, next_operands, expected_result, is_part_two))

        if mul_res <= expected_result:
            final_results.extend(testing_operators(mul_res, next_operands, expected_result, is_part_two))

        if is_part_two and concat_res <= expected_result:
            final_results.extend(testing_operators(concat_res, next_operands, expected_result, is_part_two))

    else:
        final_results.append((add_res, mul_res, concat_res))

    return final_results


def solving_problems(expected_results: List[int], operands_list: List[List[int]]):
    sum_part_1 = 0
    sum_part_2 = 0

    for idx_result, result in enumerate(expected_results):
        operands = operands_list[idx_result]

        # Part 1
        results_part_1 = testing_operators(0, operands, result, False)

        count_res = 0
        while count_res < len(results_part_1):
            if result in results_part_1[count_res]:
                sum_part_1 += result
                break

            count_res += 1

        # Part 2
        results_part_2 = testing_operators(0, operands, result, True)

        count_res = 0
        while count_res < len(results_part_2):
            if result in results_part_2[count_res]:
                sum_part_2 += result
                break

            count_res += 1

    print("\t- Part 1:", sum_part_1)
    print("\t- Part 2:", sum_part_2)


def main():
    print("- Day 7:")

    # Read input
    file = open("../inputs/day7.txt", "r")
    lines = file.read().splitlines()
    file.close()

    expected_results: List[int] = []
    operands: List[List[int]] = []

    for line in lines:
        row_data = line.split(":")

        expected_results.append(int(row_data[0]))
        operands.append([int(x) for x in row_data[1].strip().split(" ")])

    # Solve the problems
    solving_problems(expected_results, operands)


if __name__ == "__main__":
    main()
