# Student ID : 52568
# Course     : Survey of Programming Languages — KU-SoPL-2026
#
# ╔══════════════════════════════════════════════════════════╗
# ║  YOUR TASK                                               ║
# ║                                                          ║
# ║  Return the product of digits at positions 0,2,4,... (0-indexed).║
# ║                                                          ║
# ║  - digits are extracted from your ID string              ║
# ║  - ignore the "-ex" suffix if present                    ║
# ╚══════════════════════════════════════════════════════════╝
#
# Implement solve() below and return an integer.
# Do NOT rename this file.
# Run with:  python task_52568.py


def solve(id: str) -> int:
    """
    Return the product of digits at positions 0,2,4,... (0-indexed).
    - digits are extracted from your ID string
    - ignore the "-ex" surfix if present
    """
    result = 1
    for i in range(0, len(id), 2):
        result *= int(id[i])
    return result 

if __name__ == "__main__":
    print(solve("52568"))
