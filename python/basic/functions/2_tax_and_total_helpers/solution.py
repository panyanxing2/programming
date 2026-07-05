"""
Exercise: Tax & Total Helpers

Finish the functions below. See README.md for the full story and rules.
"""


def calculate_tax(subtotal):
    """
    subtotal: a number

    Return 8% of subtotal, rounded to 2 decimal places.
    """
    # TODO: return subtotal * 0.08, rounded to 2 decimal places
    pass


def final_total(subtotal):
    """
    subtotal: a number

    Return subtotal plus its tax, rounded to 2 decimal places.
    Call calculate_tax() to get the tax amount - don't recompute it here.
    """
    # TODO 1: call calculate_tax(subtotal) to get the tax

    # TODO 2: return subtotal + tax, rounded to 2 decimal places
    pass


# ------------------------------------------------------------------
# Run this file directly to try your functions out by hand:
#
#     python solution.py
#
# ------------------------------------------------------------------
if __name__ == "__main__":
    print(calculate_tax(10))       # 0.8
    print(final_total(10))         # 10.8
    print(calculate_tax(25.50))    # 2.04
    print(final_total(25.50))      # 27.54
