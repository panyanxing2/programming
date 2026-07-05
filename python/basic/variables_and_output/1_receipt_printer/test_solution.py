"""
Test file for: Receipt Printer

Just run:

    python test_solution.py
"""

from solution import format_receipt_line

# Each test case: (item_name, unit_price, quantity, expected_string)
TEST_CASES = [
    ("Taro Milk Tea", 4.50, 2, "2x Taro Milk Tea - $9.00"),
    ("Mango Green Tea", 3.75, 3, "3x Mango Green Tea - $11.25"),
    ("Brown Sugar Boba", 5.00, 1, "1x Brown Sugar Boba - $5.00"),
]


def run_tests():
    print("Testing your Receipt Printer...\n")

    passed = 0

    for item_name, unit_price, quantity, expected in TEST_CASES:
        try:
            result = format_receipt_line(item_name, unit_price, quantity)
        except Exception as e:
            print(f"[CRASH] {item_name} x{quantity}")
            print(f"        Your code raised an error: {e}\n")
            continue

        if result is None:
            print(f"[EMPTY] {item_name} x{quantity}")
            print("        Your function didn't return anything yet "
                  "(did you forget `return`?)\n")
            continue

        if result == expected:
            print(f"[ OK  ] {item_name} x{quantity} -> {result!r}")
            passed += 1
        else:
            print(f"[FAIL ] {item_name} x{quantity}")
            print(f"        expected {expected!r}")
            print(f"        got      {result!r}\n")

    total = len(TEST_CASES)
    print("\n" + "-" * 40)
    print(f"Score: {passed}/{total} passed")
    print("-" * 40)

    if passed == total:
        print("All tests passed! The printer is ready for business. 🧾")
    else:
        print(f"{total - passed} test(s) to go. Keep at it!")


if __name__ == "__main__":
    run_tests()
