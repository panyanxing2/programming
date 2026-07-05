"""
Exercise: Ice Cream Scoop Stacking

Finish the function below. See README.md for the full story and rules.
"""


def scoops_that_fit(scoop_height, max_height):
    """
    scoop_height: a number, the height of one scoop
    max_height: a number, the tallest the stack is allowed to be

    Return how many scoops fit without the total height going over
    max_height.
    """
    # TODO 1: start `total` and `count` at 0

    # TODO 2: while adding one more scoop would still fit, add it:
    #         increase `total` by scoop_height, increase `count` by 1

    # TODO 3: return `count`
    pass


# ------------------------------------------------------------------
# Run this file directly to try your function out by hand:
#
#     python solution.py
#
# ------------------------------------------------------------------
if __name__ == "__main__":
    print(scoops_that_fit(2, 9))   # 4
    print(scoops_that_fit(3, 9))   # 3
    print(scoops_that_fit(5, 4))   # 0
