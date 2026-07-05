"""
Exercise: Top Seller Finder

Finish the function below. See README.md for the full story and rules.
"""


def best_selling_topping(topping_names, sales_counts):
    """
    topping_names: a list of strings
    sales_counts: a list of numbers, same length as topping_names

    Return the name (from topping_names) with the highest sales count.
    On a tie, return whichever one appears first.
    """
    # TODO 1: assume index 0 is the best so far (best_index, best_count)

    # TODO 2: loop through the remaining indexes with range(len(...)),
    #         updating best_index/best_count whenever you find a higher count

    # TODO 3: return the name at best_index
    pass


# ------------------------------------------------------------------
# Run this file directly to try your function out by hand:
#
#     python solution.py
#
# ------------------------------------------------------------------
if __name__ == "__main__":
    print(best_selling_topping(["Pearls", "Pudding", "Aloe"], [10, 25, 7]))  # Pudding
    print(best_selling_topping(["Pearls", "Pudding"], [5, 5]))               # Pearls
