from aoc_base import AOC
import re

# https://adventofcode.com/2024/day/3

class Day03(AOC):
    def part1(self, data) -> any:
        count = 0
        for match in re.findall(r'mul\(\d+,\d+\)', data):
            num1, num2 = match[4:-1].split(',')
            mul = int(num1) * int(num2)
            count += mul
        return count

    def part2(self, data) -> any:
        count = 0
        mul_enabled = True
        for match in re.findall(r"don't\(\)|do\(\)|mul\(\d+,\d+\)", data):
            if match == "don't()":
                mul_enabled = False
            if match == "do()":
                mul_enabled = True
            if "mul" in match and mul_enabled:
                num1, num2 = match[4:-1].split(',')
                mul = int(num1) * int(num2)
                count += mul
        return count



sample_input1 = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''
expected_part1 = 161
sample_input2 = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''
expected_part2 = 48
Day03(
    year=2024,
    day=3,
    sample_input1=sample_input1,
    expected_part1=expected_part1,
    sample_input2=sample_input2,
    expected_part2=expected_part2
).run()
