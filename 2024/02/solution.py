from aoc_base import AOC

def is_safe(report):
    levels = list(map(int, report.split()))
    n = len(levels)
    differences = [levels[i + 1] - levels[i] for i in range(n - 1)]

    is_increasing = all(0 < diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff < 0 for diff in differences)

    valid_differences = all(-3 <= diff <= 3 and diff != 0 for diff in differences)
    return (is_increasing or is_decreasing) and valid_differences

def is_safe_with_dampener(report):
    if is_safe(report):
        return True

    levels = list(map(int, report.split()))
    for i in range(len(levels)):
        modified_report = levels[:i] + levels[i + 1:]
        if is_safe(" ".join(map(str, modified_report))):
            return True

    return False

class Day02(AOC):
    def part1(self, data: str) -> any:
        reports = data.strip().split("\n")
        return sum(is_safe(report) for report in reports)


    def part2(self, data) -> any:
        reports = data.strip().split("\n")
        return sum(is_safe_with_dampener(report) for report in reports)


sample_input = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''
expected_part1 = 2
expected_part2 = 4
Day02(
    year=2024,
    day=2,
    sample_input1=sample_input,
    expected_part1=expected_part1,
    expected_part2=expected_part2
).run()
