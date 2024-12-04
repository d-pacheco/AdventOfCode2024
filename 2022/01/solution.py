from aoc_base import AOC

# https://adventofcode.com/2022/day/1

class Day01(AOC):
    def part1(self, data: str) -> any:
        counts = []
        curr_count = 0
        for line in data.splitlines():
            if line == '':
                counts.append(curr_count)
                curr_count = 0
            else:
                curr_count += int(line.strip())
        counts.append(curr_count)
        return max(counts)

    def part2(self, data: str) -> any:
        counts = []
        curr_count = 0
        for line in data.splitlines():
            if line == '':
                counts.append(curr_count)
                curr_count = 0
            else:
                curr_count += int(line.strip())
        counts.append(curr_count)

        top_3 = 0
        for i in range(3):
            max_val = max(counts)
            counts.remove(max_val)
            top_3 += max_val
        return top_3



sample_input = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''
expected_part1 = 24000
expected_part2 = 45000
Day01(
    year=2022,
    day=1,
    sample_input1=sample_input,
    expected_part1=expected_part1,
    expected_part2=expected_part2
).run()
