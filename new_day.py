import os
from pathlib import Path
import requests

def main():
    year = 2024
    day = 3
    download_input(year, day)
    create_solution_file(year, day)
    create_file(year, day, "stars.txt")

def create_solution_file(year: int, day: int) -> None:
    day_formatted = f"{day:02d}"
    file_path = create_file(year, day, "solution.py")
    template = f"""from aoc_base import AOC

# https://adventofcode.com/{year}/day/{day}

class Day{day_formatted}(AOC):
    def part1(self, data) -> any:
        pass



sample_input = ''''''
expected_part1 = None
expected_part2 = None
Day{day_formatted}(
    year={year},
    day={day},
    sample_input=sample_input,
    expected_part1=expected_part1,
    expected_part2=expected_part2
).run()
"""
    file_path.write_text(template)

def download_input(year: int, day: int) -> None:
    file_path = create_file(year, day, "input.txt")

    session_cookie = os.getenv("AOC_SESSION_COOKIE")
    if not session_cookie:
        raise EnvironmentError("AOC_SESSION_COOKIE environment variable is not set.")

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {
        "Cookie": session_cookie,
        "User-Agent": "github.com/d-pacheco/adventofcode"
    }

    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code != 200:
        raise Exception(f"Non-200 status when downloading input file: {response.status_code}")

    file_path.write_text(response.text)

def create_file(year: int, day: int, file_name: str) -> Path:
    day_formatted = f"{day:02d}"
    file_path = Path(f"{year}/{day_formatted}/{file_name}")

    if file_path.exists():
        print(f"File already downloaded: {file_path}")
        return file_path

    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text("")
    print(f"File '{file_path}' has been created.")
    return file_path

main()
