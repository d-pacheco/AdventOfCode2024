from bs4 import BeautifulSoup
import requests
import os
from util import get_input, check_stars, write_stars

class AOC:
    def __init__(self, year, day, sample_input = None, expected_part1 = None, expected_part2 = None):
        self.year = year
        self.day = day
        self.sample_input = sample_input
        self.expected_part1 = expected_part1
        self.expected_part2 = expected_part2

    def part1(self, data: str) -> any:
        """Override this method to implement Part 1 solution."""
        raise NotImplementedError("Part 1 solution not implemented")

    def part2(self, data: str) -> any:
        """Override this method to implement Part 2 solution."""
        raise NotImplementedError("Part 2 solution not implemented")

    def submit(self, answer, level):
        print(f"\nFor Day {self.day}, Part {level}, submitting answer: {answer}")
        response = requests.post(
            url=f"https://adventofcode.com/{self.year}/day/{self.day}/answer",
            headers={"cookie": os.environ['AOC_SESSION_COOKIE'], },
            data={"level": str(level), "answer": str(answer)}
        )
        soup = BeautifulSoup(response.text, "html.parser")
        message = soup.article.text

        if "that's the right answer" in message.lower():
            print(f"⭐️ Correct! ⭐️")
            write_stars(level)

        elif "not the right answer" in message.lower():
            print(f"❌ Wrong answer! For details:")
            print(message)
        elif "answer too recently" in message.lower():
            print(f"⚠️ You gave an answer too recently")
        elif "already complete it" in message.lower():
            print(f"⚠️ You have already solved this")

    def run(self):
        problem_input = get_input()
        stars = check_stars()

        try:
            if self.sample_input is not None and self.expected_part1 is not None:
                part1_sample_answer = self.part1(self.sample_input)
                if part1_sample_answer == self.expected_part1:
                    print("✅ Part 1 passed sample input ✅")
                else:
                    print("❗❗ Part 1 did not pass sample input ❗❗")
                    print(f"Expected: {self.expected_part1}, but got {part1_sample_answer}")
                    return
            part1_answer = self.part1(problem_input)
            if stars == 0:
                self.submit(part1_answer, 1)
            else:
                print(f"Already completed part 1. Your answer for part 1 is: {part1_answer}")
        except NotImplementedError:
            print("⚠️ Part 1 not implemented... Skipping... ⚠️")

        try:
            if self.sample_input is not None and self.expected_part2 is not None:
                part2_sample_answer = self.part2(self.sample_input)
                if part2_sample_answer == self.expected_part2:
                    print("✅ Part 2 passed sample input ✅")
                else:
                    print("❗❗ Part 2 did not pass sample input ❗❗")
                    print(f"Expected: {self.expected_part2}, but got {part2_sample_answer}")
                    return
            part2_answer = self.part2(problem_input)
            if stars == 1:
                self.submit(part2_answer, 2)
            else:
                print(f"Already completed part 2. Your answer for part 2 is: {part2_answer}")
        except NotImplementedError:
            print("⚠️ Part 2 not implemented... Skipping... ⚠️")
