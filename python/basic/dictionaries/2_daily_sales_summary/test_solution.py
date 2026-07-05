"""
Test file for: Daily Sales Summary

Just run:

    python test_solution.py
"""

from solution import total_revenue

# Each test case: (menu, sales, expected)
TEST_CASES = [
    ({"Milk Tea": 4.5, "Taro": 5.0}, {"Milk Tea": 3, "Taro": 2}, 23.5),
    ({"Milk Tea": 4.5}, {"Milk Tea": 2, "Mystery Item": 5}, 9.0),
    ({}, {}, 0),
    ({"A": 1.0, "B": 2.0}, {"A": 10, "B": 5}, 20.0),
]


def run_tests():
    print("Testing your Daily Sales Summary...\n")

    passed = 0

    for menu, sales, expected in TEST_CASES:
        try:
            result = total_revenue(menu, sales)
        except Exception as e:
            print(f"[CRASH] total_revenue({menu}, {sales})")
            print(f"        Your code raised an error: {e}\n")
            continue

        if result is None:
            print(f"[EMPTY] total_revenue({menu}, {sales})")
            print("        Your function didn't return anything yet "
                  "(did you forget `return`?)\n")
            continue

        if round(result, 2) == round(expected, 2):
            print(f"[ OK  ] total_revenue({menu}, {sales}) -> {result}")
            passed += 1
        else:
            print(f"[FAIL ] total_revenue({menu}, {sales})")
            print(f"        expected {expected}, got {result}\n")

    total = len(TEST_CASES)
    print("\n" + "-" * 40)
    print(f"Score: {passed}/{total} passed")
    print("-" * 40)

    if passed == total:
        print("All tests passed! Time to count the cash drawer. 💰")
    else:
        print(f"{total - passed} test(s) to go. Keep at it!")


if __name__ == "__main__":
    run_tests()
