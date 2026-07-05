"""
Test file for: Bubble Tea Loyalty Discount

Just run:

    python test_solution.py
"""

from solution import bubble_tea_total_with_discount

# Each test case: (args tuple, expected_total, description)
TEST_CASES = [
    (("small", 0), 3.0, "small, no toppings, default (non-member)"),
    (("medium", 2, True), 4.5, "medium, 2 toppings, member"),
    (("large", 5, True), 7.65, "large, 5 toppings (fee!), member"),
    (("small", 10, False), 9.0, "small, 10 toppings, non-member"),
    (("large", 5, False), 8.5, "large, 5 toppings, non-member (matches original)"),
]


def run_tests():
    print("Testing your Bubble Tea Loyalty Discount...\n")

    passed = 0

    for args, expected, description in TEST_CASES:
        try:
            result = bubble_tea_total_with_discount(*args)
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
        print("All tests passed! The loyalty program launches today. 🧋💳")
    else:
        print(f"{total - passed} test(s) to go. Keep at it!")


if __name__ == "__main__":
    run_tests()
