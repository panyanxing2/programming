"""
Exercise: Cup Name Tag

Finish the function below. See README.md for the full story and rules.
"""


def format_cup_name(raw_name, max_length):
    """
    raw_name: a string, possibly messy (extra spaces, wrong case)
    max_length: an integer, the longest the final name is allowed to be

    Return the cleaned-up name, truncated with "..." if it's too long.
    """
    # TODO 1: strip extra whitespace and fix the capitalization

    # TODO 2: if the result is longer than max_length, cut it down to
    #         max_length characters and add "..."

    # TODO 3: return the result
    pass


# ------------------------------------------------------------------
# Run this file directly to try your function out by hand:
#
#     python solution.py
#
# ------------------------------------------------------------------
if __name__ == "__main__":
    print(format_cup_name("  john  ", 10))    # John
    print(format_cup_name("alexandria", 6))   # Alexan...
    print(format_cup_name("MEI LING", 20))    # Mei Ling
