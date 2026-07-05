"""
Test file for: Topping Inventory

Just run:

    python test_solution.py
"""

from solution import restock_and_check

# Each test case: (toppings_in_stock, new_arrivals, requested_topping, expected)
TEST_CASES = [
    (["pearls", "pudding"], ["taro balls"], "taro balls", True),
    (["pearls"], [], "pudding", False),
    ([], ["pearls", "aloe"], "aloe", True),
    (["pearls"], ["pudding"], "pearls", True),
]


def run_tests():
    print("Testing your Topping Inventory...\n")

    passed = 0

    for stock, new_arrivals, requested, expected in TEST_CASES:
        # Pass copies so a mutated list in one test doesn't affect the next.
        stock_copy = list(stock)
        new_arrivals_copy = list(new_arrivals)

        try:
            result = restock_and_check(stock_copy, new_arrivals_copy, requested)
        except Exception as e:
            print(f"[CRASH] restock_and_check({stock}, {new_arrivals}, {requested!r})")
            print(f"        Your code raised an error: {e}\n")
            continue

        if result is None:
            print(f"[EMPTY] restock_and_check({stock}, {new_arrivals}, {requested!r})")
            print("        Your function didn't return anything yet "
                  "(did you forget `return`?)\n")
            continue

        if result == expected:
            print(f"[ OK  ] restock_and_check({stock}, {new_arrivals}, {requested!r}) -> {result}")
            passed += 1
        else:
            print(f"[FAIL ] restock_and_check({stock}, {new_arrivals}, {requested!r})")
            print(f"        expected {expected}, got {result}\n")

    total = len(TEST_CASES)
    print("\n" + "-" * 40)
    print(f"Score: {passed}/{total} passed")
    print("-" * 40)

    if passed == total:
        print("All tests passed! Shelves fully stocked. 📦")
    else:
        print(f"{total - passed} test(s) to go. Keep at it!")


if __name__ == "__main__":
    run_tests()
