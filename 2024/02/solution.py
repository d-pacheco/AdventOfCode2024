from aoc_base import AOC

class Day02(AOC):
    def part1(self, data: str) -> any:
        data_list = data.strip().splitlines()
        reports = []
        for report in data_list:
            reports.append(report.split())

        def check_is_safe(report_to_check):
            differences = [abs(int(report[i]) - int(report[i + 1])) for i in range(len(report) - 1)]
            if not all(1 <= diff <= 3 for diff in differences):
                return False

            increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
            decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))

            return increasing or decreasing



        count = 0
        for report in reports:
            if check_is_safe(report):
                count += 1
            else:
                pass

        return count


    def part2(self, data) -> any:
        pass


sample_input = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''
expected_part1 = 2
expected_part2 = None
Day02(
    year=2024,
    day=2,
    sample_input1=sample_input,
    expected_part1=expected_part1,
    expected_part2=expected_part2
).run()
