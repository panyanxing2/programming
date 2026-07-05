"""
Test file for: Shopping Basket Total

Just run:

    python test_solution.py
"""

from solution import basket_total

# Each test case: (prices, expected_total)
TEST_CASES = [
    ([3.5, 2.0, 4.25], 9.75),
    ([], 0),
    ([10], 10),
    ([1, 1, 1, 1, 1], 5),
]


def run_tests():
    print("Testing your Shopping Basket Total...\n")

    passed = 0

    for prices, expected in TEST_CASES:
        try:
            result = basket_total(prices)
        except Exception as e:
            print(f"[CRASH] basket_total({prices})")
            print(f"        Your code raised an error: {e}\n")
            continue

        if result is None:
            print(f"[EMPTY] basket_total({prices})")
            print("        Your function didn't return anything yet "
                  "(did you forget `return`?)\n")
            continue

        if round(result, 2) == round(expected, 2):
            print(f"[ OK  ] basket_total({prices}) -> {result}")
            passed += 1
        else:
            print(f"[FAIL ] basket_total({prices})")
            print(f"        expected {expected}, got {result}\n")

    total = len(TEST_CASES)
    print("\n" + "-" * 40)
    print(f"Score: {passed}/{total} passed")
    print("-" * 40)

    if passed == total:
        print("All tests passed! You can afford the whole basket. 🛒")
    else:
        print(f"{total - passed} test(s) to go. Keep at it!")


if __name__ == "__main__":
    run_tests()
