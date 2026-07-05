"""
Test file for: Menu Price Lookup

Just run:

    python test_solution.py
"""

from solution import get_menu_price

MENU = {"Milk Tea": 4.5, "Taro": 5.0}

# Each test case: (menu, item_name, expected)
TEST_CASES = [
    (MENU, "Milk Tea", 4.5),
    (MENU, "Taro", 5.0),
    (MENU, "Coffee", -1),
    ({}, "Anything", -1),
]


def run_tests():
    print("Testing your Menu Price Lookup...\n")

    passed = 0

    for menu, item_name, expected in TEST_CASES:
        try:
            result = get_menu_price(menu, item_name)
        except Exception as e:
            print(f"[CRASH] get_menu_price(menu, {item_name!r})")
            print(f"        Your code raised an error: {e}\n")
            continue

        if result is None:
            print(f"[EMPTY] get_menu_price(menu, {item_name!r})")
            print("        Your function didn't return anything yet "
                  "(did you forget `return`?)\n")
            continue

        if result == expected:
            print(f"[ OK  ] get_menu_price(menu, {item_name!r}) -> {result}")
            passed += 1
        else:
            print(f"[FAIL ] get_menu_price(menu, {item_name!r})")
            print(f"        expected {expected}, got {result}\n")

    total = len(TEST_CASES)
    print("\n" + "-" * 40)
    print(f"Score: {passed}/{total} passed")
    print("-" * 40)

    if passed == total:
        print("All tests passed! No awkward menu moments today. 📋")
    else:
        print(f"{total - passed} test(s) to go. Keep at it!")


if __name__ == "__main__":
    run_tests()
