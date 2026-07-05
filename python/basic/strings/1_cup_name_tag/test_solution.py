"""
Test file for: Cup Name Tag

Just run:

    python test_solution.py
"""

from solution import format_cup_name

# Each test case: (raw_name, max_length, expected)
TEST_CASES = [
    ("  john  ", 10, "John"),
    ("alexandria", 6, "Alexan..."),
    ("MEI LING", 20, "Mei Ling"),
    ("   bo  ", 10, "Bo"),
    ("Bobae", 5, "Bobae"),
    ("bobae", 4, "Boba..."),
]


def run_tests():
    print("Testing your Cup Name Tag formatter...\n")

    passed = 0

    for raw_name, max_length, expected in TEST_CASES:
        try:
            result = format_cup_name(raw_name, max_length)
        except Exception as e:
            print(f"[CRASH] format_cup_name({raw_name!r}, {max_length})")
            print(f"        Your code raised an error: {e}\n")
            continue

        if result is None:
            print(f"[EMPTY] format_cup_name({raw_name!r}, {max_length})")
            print("        Your function didn't return anything yet "
                  "(did you forget `return`?)\n")
            continue

        if result == expected:
            print(f"[ OK  ] format_cup_name({raw_name!r}, {max_length}) -> {result!r}")
            passed += 1
        else:
            print(f"[FAIL ] format_cup_name({raw_name!r}, {max_length})")
            print(f"        expected {expected!r}")
            print(f"        got      {result!r}\n")

    total = len(TEST_CASES)
    print("\n" + "-" * 40)
    print(f"Score: {passed}/{total} passed")
    print("-" * 40)

    if passed == total:
        print("All tests passed! The marker is ready. ✍️")
    else:
        print(f"{total - passed} test(s) to go. Keep at it!")


if __name__ == "__main__":
    run_tests()
