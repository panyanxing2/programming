"""
Exercise 1: Bubble Tea Shop Calculator

Finish the function below. See README.md for the full story and rules.
"""


def bubble_tea_total(size, num_toppings):
    """
    size: a string, one of "small", "medium", "large"
    num_toppings: an integer, how many toppings were added

    Return the total price of the order as a number.
    """
    # TODO 1: figure out the base price depending on `size`.
    #         Hint: if / elif / else

    # TODO 2: add $0.50 for each topping.

    # TODO 3: if 5 or more toppings were ordered, add a $1.00
    #         "topping overload fee".

    # TODO 4: return the total.
    pass


# ------------------------------------------------------------------
# Run this file directly to try your function out by hand:
#
#     python solution.py
#
# ------------------------------------------------------------------
if __name__ == "__main__":
    print(bubble_tea_total("small", 0))    # should print 3.0
    print(bubble_tea_total("medium", 2))   # should print 5.0
    print(bubble_tea_total("large", 5))    # should print 8.5
