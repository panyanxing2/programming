"""
Test file for: Temperature Display

Just run:

    python test_solution.py
"""

from solution import celsius_to_fahrenheit_label

# Each test case: (celsius, expected_string)
TEST_CASES = [
    (0, "0°C is 32.0°F"),
    (100, "100°C is 212.0°F"),
    (-18, "-18°C is -0.4°F"),
    (20, "20°C is 68.0°F"),
    (37, "37°C is 98.6°F"),
]


def run_tests():
    print("Testing your Temperature Display...\n")

    passed = 0

    for celsius, expected in TEST_CASES:
        try:
            result = celsius_to_fahrenheit_label(celsius)
        except Exception as e:
            print(f"[CRASH] celsius={celsius}")
            print(f"        Your code raised an error: {e}\n")
            continue

        if result is None:
            print(f"[EMPTY] celsius={celsius}")
            print("        Your function didn't return anything yet "
                  "(did you forget `return`?)\n")
            continue

        if result == expected:
            print(f"[ OK  ] celsius={celsius} -> {result!r}")
            passed += 1
        else:
            print(f"[FAIL ] celsius={celsius}")
            print(f"        expected {expected!r}")
            print(f"        got      {result!r}\n")

    total = len(TEST_CASES)
    print("\n" + "-" * 40)
    print(f"Score: {passed}/{total} passed")
    print("-" * 40)

    if passed == total:
        print("All tests passed! The freezer is bilingual now. 🌡️")
    else:
        print(f"{total - passed} test(s) to go. Keep at it!")


if __name__ == "__main__":
    run_tests()
