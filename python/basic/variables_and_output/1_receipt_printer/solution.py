"""
Exercise: Receipt Printer

Finish the function below. See README.md for the full story and rules.
"""


def format_receipt_line(item_name, unit_price, quantity):
    """
    item_name: a string, e.g. "Taro Milk Tea"
    unit_price: a number, the price of ONE item
    quantity: an integer, how many were ordered

    Return a string formatted like:
        "2x Taro Milk Tea - $9.00"
    """
    # TODO 1: compute the total price (unit_price * quantity)

    # TODO 2: return an f-string in the format shown above.
    #         Use {total:.2f} to force 2 decimal places.
    pass


# ------------------------------------------------------------------
# Run this file directly to try your function out by hand:
#
#     python solution.py
#
# ------------------------------------------------------------------
if __name__ == "__main__":
    print(format_receipt_line("Taro Milk Tea", 4.50, 2))     # 2x Taro Milk Tea - $9.00
    print(format_receipt_line("Mango Green Tea", 3.75, 3))   # 3x Mango Green Tea - $11.25
