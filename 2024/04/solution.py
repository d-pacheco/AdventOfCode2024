from aoc_base import AOC

# https://adventofcode.com/2024/day/4

class Day04(AOC):
    def part1(self, data) -> any:
        def get_diagonals(grid):
            rows = len(grid)
            cols = len(grid[0])
            diagonals_found = []

            # Top-left to bottom-right diagonals
            for d in range(rows + cols - 1):
                diag1 = []
                for i in range(max(0, d - cols + 1), min(rows, d + 1)):
                    diag1.append(grid[i][d - i])
                diagonals_found.append("".join(diag1))

            # Top-right to bottom-left diagonals
            for d in range(rows + cols - 1):
                diag2 = []
                for i in range(max(0, d - cols + 1), min(rows, d + 1)):
                    diag2.append(grid[i][cols - 1 - (d - i)])
                diagonals_found.append("".join(diag2))

            return diagonals_found

        def count_string(string, word):
            string_count = 0
            if len(string) < 4:
                return string_count
            start = 0
            end = 4
            while end <= len(string):
                window = string[start:end]
                if window == word or window == word[::-1]:
                    string_count += 1
                start += 1
                end += 1
            return string_count

        def count_rows(grid, word):
            row_count = 0
            for row in grid:
                row_count += count_string(row, word)
            return row_count

        def count_cols(grid, word):
            col_count = 0
            cols = len(grid[0])
            for col in range(cols):
                column = ''.join(row[col] for row in grid)
                col_count += count_string(column, word)
            return col_count

        crossword = []
        word_to_find = "XMAS"
        lines = data.strip().splitlines()
        for line in lines:
            crossword.append(line.strip())
        count = 0
        count += count_rows(crossword, word_to_find)
        count += count_cols(crossword, word_to_find)
        diagonals = get_diagonals(crossword)
        for diag in diagonals:
            count += count_string(diag, word_to_find)
        return count

    def part2(self, data) -> any:
        crossword = []
        lines = data.strip().splitlines()
        for line in lines:
            crossword.append(line.strip())
        count = 0
        for row in range(len(crossword)):
            for col in range(len(crossword)):
                char = crossword[row][col]
                if char != "A":
                    continue

                if col == 0 or col == len(crossword) - 1:
                    continue
                if row == 0 or row == len(crossword) - 1:
                    continue

                if (
                    crossword[row - 1][col - 1] == "M"  # Top Left
                    and crossword[row + 1][col - 1] == "M"  # Bottom Left
                    and crossword[row - 1][col + 1] == "S"  # Top Right
                    and crossword[row + 1][col + 1] == "S"  # Bottom Right
                ):
                    count += 1

                if (
                    crossword[row - 1][col - 1] == "M"  # Top Left
                    and crossword[row + 1][col - 1] == "S"  # Bottom Left
                    and crossword[row - 1][col + 1] == "M"  # Top Right
                    and crossword[row + 1][col + 1] == "S"  # Bottom Right
                ):
                    count += 1

                if (
                    crossword[row - 1][col - 1] == "S"  # Top Left
                    and crossword[row + 1][col - 1] == "S"  # Bottom Left
                    and crossword[row - 1][col + 1] == "M"  # Top Right
                    and crossword[row + 1][col + 1] == "M"  # Bottom Right
                ):
                    count += 1

                if (
                    crossword[row - 1][col - 1] == "S"  # Top Left
                    and crossword[row + 1][col - 1] == "M"  # Bottom Left
                    and crossword[row - 1][col + 1] == "S"  # Top Right
                    and crossword[row + 1][col + 1] == "M"  # Bottom Right
                ):
                    count += 1

        return count


sample_input1 = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''
expected_part1 = 18
sample_input2 = None
expected_part2 = 9
Day04(
    year=2024,
    day=4,
    sample_input1=sample_input1,
    expected_part1=expected_part1,
    sample_input2=sample_input2,
    expected_part2=expected_part2
).run()
