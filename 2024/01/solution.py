from aoc_base import AOC

class Day01(AOC):
    def part1(self, data: str) -> any:
        data = data.strip().splitlines()
        list1 = []
        list2 = []
        for line in data:
            l, r = line.split()
            list1.append(int(l))
            list2.append(int(r))

        list1.sort()
        list2.sort()
        sum_diff = 0
        for i in range(len(list1)):
            sum_diff += abs(list1[i] - list2[i])

        return sum_diff

    def part2(self, data) -> any:
        data = data.strip().splitlines()
        list1 = []
        list2 = []
        for line in data:
            l, r = line.split()
            list1.append(int(l))
            list2.append(int(r))

        similarity_score = 0
        for num1 in list1:
            count = 0
            for num2 in list2:
                if num1 == num2:
                    count += 1
            similarity_score += (num1 * count)

        return similarity_score


sample_input = '''3   4
4   3
2   5
1   3
3   9
3   3
'''
expected_part1 = 11
expected_part2 = 31
Day01(
    year=2024,
    day=1,
    sample_input=sample_input,
    expected_part1=expected_part1,
    expected_part2=expected_part2
).run()
