"""
Exercise: Daily Sales Summary

Finish the function below. See README.md for the full story and rules.
"""


def total_revenue(menu, sales):
    """
    menu: a dictionary like {"Milk Tea": 4.5, "Taro": 5.0}
    sales: a dictionary like {"Milk Tea": 3, "Taro": 2}

    Return the total revenue: for each item sold, price * quantity,
    all added up. Items missing from `menu` count as price 0.
    """
    # TODO 1: start `total` at 0

    # TODO 2: loop over sales.items() to get (item, quantity) pairs,
    #         adding menu.get(item, 0) * quantity to `total` each time

    # TODO 3: return `total`
    pass


# ------------------------------------------------------------------
# Run this file directly to try your function out by hand:
#
#     python solution.py
#
# ------------------------------------------------------------------
if __name__ == "__main__":
    menu = {"Milk Tea": 4.5, "Taro": 5.0}
    sales = {"Milk Tea": 3, "Taro": 2}
    print(total_revenue(menu, sales))   # 23.5
