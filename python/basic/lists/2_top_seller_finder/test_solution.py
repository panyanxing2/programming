"""
Test file for: Top Seller Finder

Just run:

    python test_solution.py
"""

from solution import best_selling_topping

# Each test case: (topping_names, sales_counts, expected)
TEST_CASES = [
    (["Pearls", "Pudding", "Aloe"], [10, 25, 7], "Pudding"),
    (["Pearls", "Pudding"], [5, 5], "Pearls"),
    (["Aloe"], [100], "Aloe"),
    (["A", "B", "C", "D"], [1, 2, 4, 3], "C"),
]


def run_tests():
    print("Testing your Top Seller Finder...\n")

    passed = 0

    for names, counts, expected in TEST_CASES:
        try:
            result = best_selling_topping(names, counts)
        except Exception as e:
            print(f"[CRASH] best_selling_topping({names}, {counts})")
            print(f"        Your code raised an error: {e}\n")
            continue

        if result is None:
            print(f"[EMPTY] best_selling_topping({names}, {counts})")
            print("        Your function didn't return anything yet "
                  "(did you forget `return`?)\n")
            continue

        if result == expected:
            print(f"[ OK  ] best_selling_topping({names}, {counts}) -> {result!r}")
            passed += 1
        else:
            print(f"[FAIL ] best_selling_topping({names}, {counts})")
            print(f"        expected {expected!r}, got {result!r}\n")

    total = len(TEST_CASES)
    print("\n" + "-" * 40)
    print(f"Score: {passed}/{total} passed")
    print("-" * 40)

    if passed == total:
        print("All tests passed! Time to make a little sign for the winner. 🏆")
    else:
        print(f"{total - passed} test(s) to go. Keep at it!")


if __name__ == "__main__":
    run_tests()
