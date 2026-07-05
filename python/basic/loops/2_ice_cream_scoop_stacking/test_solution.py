"""
Test file for: Ice Cream Scoop Stacking

Just run:

    python test_solution.py
"""

from solution import scoops_that_fit

# Each test case: (scoop_height, max_height, expected_count)
TEST_CASES = [
    (2, 9, 4),
    (3, 9, 3),
    (5, 4, 0),
    (1, 10, 10),
    (2, 0, 0),
]


def run_tests():
    print("Testing your Ice Cream Scoop Stacking...\n")

    passed = 0

    for scoop_height, max_height, expected in TEST_CASES:
        try:
            result = scoops_that_fit(scoop_height, max_height)
        except Exception as e:
            print(f"[CRASH] scoops_that_fit({scoop_height}, {max_height})")
            print(f"        Your code raised an error: {e}\n")
            continue

        if result is None:
            print(f"[EMPTY] scoops_that_fit({scoop_height}, {max_height})")
            print("        Your function didn't return anything yet "
                  "(did you forget `return`?)\n")
            continue

        if result == expected:
            print(f"[ OK  ] scoops_that_fit({scoop_height}, {max_height}) -> {result}")
            passed += 1
        else:
            print(f"[FAIL ] scoops_that_fit({scoop_height}, {max_height})")
            print(f"        expected {expected}, got {result}\n")

    total = len(TEST_CASES)
    print("\n" + "-" * 40)
    print(f"Score: {passed}/{total} passed")
    print("-" * 40)

    if passed == total:
        print("All tests passed! The cone is still standing. 🍦")
    else:
        print(f"{total - passed} test(s) to go. Keep at it!")


if __name__ == "__main__":
    run_tests()
