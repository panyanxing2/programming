"""
Exercise: Review Vowel Counter

Finish the function below. See README.md for the full story and rules.
"""


def count_vowels(text):
    """
    text: a string

    Return how many characters in `text` are vowels (a, e, i, o, u),
    not counting case.
    """
    # TODO 1: make a lowercase copy of `text` so case doesn't matter

    # TODO 2: start a `count` variable at 0

    # TODO 3: loop over each character; if it's a vowel, add 1 to `count`

    # TODO 4: return `count`
    pass


# ------------------------------------------------------------------
# Run this file directly to try your function out by hand:
#
#     python solution.py
#
# ------------------------------------------------------------------
if __name__ == "__main__":
    print(count_vowels("Bubble Tea"))   # 4
    print(count_vowels("Xyz"))          # 0
    print(count_vowels("AEIOU"))        # 5
