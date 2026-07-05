"""
Exercise: Arcade Ticket Booth

Finish the function below. See README.md for the full story and rules.
"""


def ticket_price(age, is_weekend):
    """
    age: an integer
    is_weekend: True or False

    Return the ticket price as a number, based on the pricing table
    in README.md.
    """
    # TODO 1: handle the "under 5, always free" case first

    # TODO 2: handle child (5-12), using is_weekend to pick $8 or $10

    # TODO 3: handle adult (13-64), using is_weekend to pick $12 or $15

    # TODO 4: handle senior (65+), using is_weekend to pick $6 or $8
    pass


# ------------------------------------------------------------------
# Run this file directly to try your function out by hand:
#
#     python solution.py
#
# ------------------------------------------------------------------
if __name__ == "__main__":
    print(ticket_price(3, True))     # 0
    print(ticket_price(8, False))    # 8
    print(ticket_price(30, True))    # 15
    print(ticket_price(70, False))   # 6
