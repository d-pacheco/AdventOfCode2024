from pathlib import Path

def get_input() -> str:
    file_path = Path("input.txt")
    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    return file_path.read_text()

def check_stars():
    with open("stars.txt", 'r') as file:
        stars = file.read().strip()
        return len(stars)

def write_stars(star_count: int):
    with open("stars.txt", 'w') as file:
        file.write("*"*star_count)
