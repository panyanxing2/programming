"""
Exercise: Temperature Display

Finish the function below. See README.md for the full story and rules.
"""


def celsius_to_fahrenheit_label(celsius):
    """
    celsius: a number (can be negative)

    Return a string formatted like:
        "0°C is 32.0°F"
    """
    # TODO 1: convert celsius to fahrenheit using the formula in the README

    # TODO 2: round the fahrenheit value to 1 decimal place

    # TODO 3: return the formatted string
    pass


# ------------------------------------------------------------------
# Run this file directly to try your function out by hand:
#
#     python solution.py
#
# ------------------------------------------------------------------
if __name__ == "__main__":
    print(celsius_to_fahrenheit_label(0))     # 0°C is 32.0°F
    print(celsius_to_fahrenheit_label(100))   # 100°C is 212.0°F
    print(celsius_to_fahrenheit_label(-18))   # -18°C is -0.4°F
