"""
Exercise: Topping Inventory

Finish the function below. See README.md for the full story and rules.
"""


def restock_and_check(toppings_in_stock, new_arrivals, requested_topping):
    """
    toppings_in_stock: a list of strings already in stock
    new_arrivals: a list of strings that just got delivered
    requested_topping: a string a customer is asking for

    Add every item in new_arrivals to toppings_in_stock, then return
    whether requested_topping is now in stock (True or False).
    """
    # TODO 1: loop over new_arrivals, appending each one to
    #         toppings_in_stock

    # TODO 2: return whether requested_topping is in toppings_in_stock
    pass


# ------------------------------------------------------------------
# Run this file directly to try your function out by hand:
#
#     python solution.py
#
# ------------------------------------------------------------------
if __name__ == "__main__":
    print(restock_and_check(["pearls", "pudding"], ["taro balls"], "taro balls"))  # True
    print(restock_and_check(["pearls"], [], "pudding"))                             # False
