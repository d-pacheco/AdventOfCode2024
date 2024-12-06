from aoc_base import AOC

# https://adventofcode.com/2024/day/6

def set_value_at(grid, r, c, char = "X"):
    row = list(grid[r])
    row[c] = char
    grid[r] = ''.join(row)
    return grid

def get_starting_position(grid) -> tuple:
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "^":
                return r, c

def simulate(grid, r, c, max_visits = False):
    counts = []
    for row in grid:
        counts.append([0 for _ in range(len(row))])

    facing = "N"
    while True:
        grid = set_value_at(grid, r, c)
        counts[r][c] += 1

        if max_visits and counts[r][c] > 10:
            return grid, True

        if facing == "N":
            if r == 0:
                break
            elif grid[r - 1][c] == "#":
                facing = "E"
            else:
                r -= 1

        if facing == "E":
            if c == len(grid[r]) - 1:
                break
            elif grid[r][c + 1] == "#":
                facing = "S"
            else:
                c += 1

        if facing == "S":
            if r == len(grid) - 1:
                break
            elif grid[r + 1][c] == "#":
                facing = "W"
            else:
                r += 1

        if facing == "W":
            if c == 0:
                break
            elif grid[r][c - 1] == "#":
                facing = "N"
            else:
                c -= 1

    return grid, False


class Day06(AOC):
    def part1(self, data) -> any:
        grid = [line.strip() for line in data.strip().splitlines()]
        r, c = get_starting_position(grid)
        grid, _ = simulate(grid, r, c)

        count = 0
        for row in grid:
            for c in row:
                if c == "X":
                    count += 1
        return count

    def part2(self, data: str) -> any:
        grid = [line.strip() for line in data.strip().splitlines()]
        s_r, s_c = get_starting_position(grid)

        loop_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "^" or grid[r][c] == "#":
                    continue

                sim_grid = grid[:]
                sim_grid = set_value_at(sim_grid, r, c, "#")

                _, in_loop = simulate(sim_grid, s_r, s_c, True)
                if in_loop:
                    loop_count += 1

        return loop_count





sample_input1 = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''
expected_part1 = 41
expected_part2 = 6
Day06(
    year=2024,
    day=6,
    sample_input1=sample_input1,
    expected_part1=expected_part1,
    expected_part2=expected_part2
).run()
