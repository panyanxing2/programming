"""
Exercise: Shopping Basket Total

Finish the function below. See README.md for the full story and rules.
"""


def basket_total(prices):
    """
    prices: a list of numbers, e.g. [3.5, 2.0, 4.25]

    Return the sum of all prices in the list. An empty list returns 0.
    """
    # TODO 1: start a "total" variable at 0

    # TODO 2: loop over `prices`, adding each price to `total`

    # TODO 3: return `total`
    pass


# ------------------------------------------------------------------
# Run this file directly to try your function out by hand:
#
#     python solution.py
#
# ------------------------------------------------------------------
if __name__ == "__main__":
    print(basket_total([3.5, 2.0, 4.25]))   # 9.75
    print(basket_total([]))                  # 0
    print(basket_total([10]))                # 10
