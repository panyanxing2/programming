"""
Test file for: Arcade Ticket Booth

Just run:

    python test_solution.py
"""

from solution import ticket_price

# Each test case: (age, is_weekend, expected_price, description)
TEST_CASES = [
    (3, False, 0, "under 5, weekday - free"),
    (3, True, 0, "under 5, weekend - still free"),
    (8, False, 8, "child, weekday"),
    (8, True, 10, "child, weekend"),
    (30, False, 12, "adult, weekday"),
    (30, True, 15, "adult, weekend"),
    (70, False, 6, "senior, weekday"),
    (70, True, 8, "senior, weekend"),
    (5, False, 8, "boundary: exactly 5 is a child"),
    (13, False, 12, "boundary: exactly 13 is an adult"),
    (65, False, 6, "boundary: exactly 65 is a senior"),
]


def run_tests():
    print("Testing your Arcade Ticket Booth...\n")

    passed = 0

    for age, is_weekend, expected, description in TEST_CASES:
        try:
            result = ticket_price(age, is_weekend)
        except Exception as e:
            print(f"[CRASH] {description}")
            print(f"        Your code raised an error: {e}\n")
            continue

        if result is None:
            print(f"[EMPTY] {description}")
            print("        Your function didn't return anything yet "
                  "(did you forget `return`?)\n")
            continue

        if result == expected:
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
        print("All tests passed! The line outside is moving smoothly. 🎮")
    else:
        print(f"{total - passed} test(s) to go. Keep at it!")


if __name__ == "__main__":
    run_tests()
