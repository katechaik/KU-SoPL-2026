# Student ID : 52785
# Course     : Survey of Programming Languages — KU-SoPL-2026
#
#
# | YOUR TASK
# |
# | Return the sum of digits that appear exactly once.
# |
# | - digits are extracted from your ID string
# | - ignore the "-ex" suffix if present
#
#
# Implement solve() below and return an integer.
# Do NOT rename this file.
# Run with:  python task_52785.py


def solve(id: str) -> int:
    """
    Implement your task here.
    Your id is passed as a string.
    Return an integer.
    """
    if id.endswith("-ex"):
        id = id[:-3]

    counts: dict[str, int] = {}
    for c in id:
        if c.isdigit():
            counts[c] = counts.get(c, 0) + 1

    return sum(int(d) for d, n in counts.items() if n == 1)


if __name__ == "__main__":
    print(solve("52785"))
