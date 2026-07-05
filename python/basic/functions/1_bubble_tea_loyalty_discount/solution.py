"""
Exercise: Bubble Tea Loyalty Discount

Finish the function below. See README.md for the full story and rules.
"""


def bubble_tea_total_with_discount(size, num_toppings, is_member=False):
    """
    size: a string, one of "small", "medium", "large"
    num_toppings: an integer
    is_member: True or False (defaults to False if not given)

    Same pricing as the original bubble tea calculator, but members
    (is_member=True) get 10% off the total. Round the result to 2
    decimal places.
    """
    # TODO 1: figure out the base price depending on `size`

    # TODO 2: add $0.50 per topping

    # TODO 3: if 5+ toppings, add the $1.00 overload fee

    # TODO 4: if is_member is True, take 10% off the total

    # TODO 5: return the total, rounded to 2 decimal places
    pass


# ------------------------------------------------------------------
# Run this file directly to try your function out by hand:
#
#     python solution.py
#
# ------------------------------------------------------------------
if __name__ == "__main__":
    print(bubble_tea_total_with_discount("small", 0))            # 3.0
    print(bubble_tea_total_with_discount("medium", 2, True))     # 4.5
    print(bubble_tea_total_with_discount("large", 5, True))      # 7.65
