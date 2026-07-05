"""
Exercise: Menu Price Lookup

Finish the function below. See README.md for the full story and rules.
"""


def get_menu_price(menu, item_name):
    """
    menu: a dictionary like {"Milk Tea": 4.5, "Taro": 5.0}
    item_name: a string

    Return the price of item_name if it's on the menu, otherwise -1.
    """
    # TODO: look up item_name in menu, returning -1 if it's not there
    pass


# ------------------------------------------------------------------
# Run this file directly to try your function out by hand:
#
#     python solution.py
#
# ------------------------------------------------------------------
if __name__ == "__main__":
    menu = {"Milk Tea": 4.5, "Taro": 5.0}
    print(get_menu_price(menu, "Milk Tea"))   # 4.5
    print(get_menu_price(menu, "Coffee"))     # -1
