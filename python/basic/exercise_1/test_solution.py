"""
Test file for Exercise 1: Bubble Tea Shop Calculator

Just run:

    python test_solution.py

You don't need to understand how this file works yet - that's a lesson for
another day. For now, just read the results it prints.
"""

from solution import bubble_tea_total

# Each test case: (size, num_toppings, expected_total, description)
TEST_CASES = [
    ("small", 0, 3.0, "small, no toppings"),
    ("medium", 2, 5.0, "medium, 2 toppings"),
    ("large", 0, 5.0, "large, no toppings"),
    ("medium", 4, 6.0, "medium, 4 toppings (right below the fee)"),
    ("large", 5, 8.5, "large, 5 toppings (overload fee kicks in!)"),
    ("small", 10, 9.0, "small, 10 toppings (fee + lots of toppings)"),
]


def run_tests():
    print("Testing your Bubble Tea Shop calculator...\n")

    passed = 0

    for size, num_toppings, expected, description in TEST_CASES:
        try:
            result = bubble_tea_total(size, num_toppings)
        except Exception as e:
            print(f"[CRASH] {description}")
            print(f"        Your code raised an error: {e}\n")
            continue

        if result is None:
            print(f"[EMPTY] {description}")
            print("        Your function didn't return anything yet "
                  "(did you forget `return`?)\n")
            continue

        if round(result, 2) == round(expected, 2):
            print(f"[ OK  ] {description} -> {result}")
            passed += 1
        else:
            print(f"[FAIL ] {description}")
            print(f"        expected {expected}, got {result}\n")

    total = len(TEST_CASES)
    print("\n" + "-" * 40)
    print(f"Score: {passed}/{total} passed")
    print("-" * 40)

    if passed == total:
        print("All tests passed! 🧋 Order yourself a real bubble tea.")
    else:
        print(f"{total - passed} test(s) to go. Keep at it, you've got this!")


if __name__ == "__main__":
    run_tests()
