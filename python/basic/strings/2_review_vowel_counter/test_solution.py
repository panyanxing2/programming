"""
Test file for: Review Vowel Counter

Just run:

    python test_solution.py
"""

from solution import count_vowels

# Each test case: (text, expected_count)
TEST_CASES = [
    ("Bubble Tea", 4),
    ("Milk Tea", 3),
    ("Xyz", 0),
    ("AEIOU", 5),
    ("", 0),
    ("Best boba in town!!", 5),
]


def run_tests():
    print("Testing your Review Vowel Counter...\n")

    passed = 0

    for text, expected in TEST_CASES:
        try:
            result = count_vowels(text)
        except Exception as e:
            print(f"[CRASH] count_vowels({text!r})")
            print(f"        Your code raised an error: {e}\n")
            continue

        if result is None:
            print(f"[EMPTY] count_vowels({text!r})")
            print("        Your function didn't return anything yet "
                  "(did you forget `return`?)\n")
            continue

        if result == expected:
            print(f"[ OK  ] count_vowels({text!r}) -> {result}")
            passed += 1
        else:
            print(f"[FAIL ] count_vowels({text!r})")
            print(f"        expected {expected}, got {result}\n")

    total = len(TEST_CASES)
    print("\n" + "-" * 40)
    print(f"Score: {passed}/{total} passed")
    print("-" * 40)

    if passed == total:
        print("All tests passed! Very enthusiastic reviews indeed. 🔤")
    else:
        print(f"{total - passed} test(s) to go. Keep at it!")


if __name__ == "__main__":
    run_tests()
