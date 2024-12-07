from aoc_base import AOC
from itertools import product

# https://adventofcode.com/2024/day/7

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '|':
            result = int(str(result) + str(numbers[i + 1]))
    return result

def process_line(line, possible_ops):
    test_value, numbers = line.split(":")
    test_value = int(test_value)
    numbers = list(map(int, numbers.split()))
    num_operators = len(numbers) - 1
    operator_combinations = product(possible_ops, repeat=num_operators)

    for operators in operator_combinations:
        result = evaluate_expression(numbers, operators)
        if result == test_value:
            return True, test_value
    return False, test_value

class Day07(AOC):
    def part1(self, data) -> any:
        total_calibration = 0
        lines = data.splitlines()
        for line in lines:
            line = line.strip()
            is_valid, test_value = process_line(line, "+*")

            if is_valid:
                total_calibration += test_value

        return total_calibration

    def part2(self, data: str) -> any:
        total_calibration = 0
        lines = data.splitlines()
        for line in lines:
            line = line.strip()
            is_valid, test_value = process_line(line, "+*|")

            if is_valid:
                total_calibration += test_value

        return total_calibration



sample_input1 = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''
expected_part1 = 3749
expected_part2 = 11387
Day07(
    year=2024,
    day=7,
    sample_input1=sample_input1,
    expected_part1=expected_part1,
    expected_part2=expected_part2
).run()
