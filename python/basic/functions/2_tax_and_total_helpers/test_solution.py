"""
Test file for: Tax & Total Helpers

Just run:

    python test_solution.py
"""

from solution import calculate_tax, final_total

# Each test case: (subtotal, expected_tax, expected_final)
TEST_CASES = [
    (10, 0.8, 10.8),
    (25.50, 2.04, 27.54),
    (0, 0.0, 0.0),
    (100, 8.0, 108.0),
]


def run_tests():
    print("Testing your Tax & Total Helpers...\n")

    passed = 0
    total_checks = len(TEST_CASES) * 2

    for subtotal, expected_tax, expected_final in TEST_CASES:
        try:
            tax_result = calculate_tax(subtotal)
        except Exception as e:
            print(f"[CRASH] calculate_tax({subtotal})")
            print(f"        Your code raised an error: {e}\n")
            tax_result = "CRASHED"
        else:
            if tax_result is None:
                print(f"[EMPTY] calculate_tax({subtotal})")
                print("        Did you forget `return`?\n")
            elif round(tax_result, 2) == round(expected_tax, 2):
                print(f"[ OK  ] calculate_tax({subtotal}) -> {tax_result}")
                passed += 1
            else:
                print(f"[FAIL ] calculate_tax({subtotal})")
                print(f"        expected {expected_tax}, got {tax_result}\n")

        try:
            final_result = final_total(subtotal)
        except Exception as e:
            print(f"[CRASH] final_total({subtotal})")
            print(f"        Your code raised an error: {e}\n")
            continue

        if final_result is None:
            print(f"[EMPTY] final_total({subtotal})")
            print("        Did you forget `return`?\n")
        elif round(final_result, 2) == round(expected_final, 2):
            print(f"[ OK  ] final_total({subtotal}) -> {final_result}")
            passed += 1
        else:
            print(f"[FAIL ] final_total({subtotal})")
            print(f"        expected {expected_final}, got {final_result}\n")

    print("\n" + "-" * 40)
    print(f"Score: {passed}/{total_checks} passed")
    print("-" * 40)

    if passed == total_checks:
        print("All tests passed! Tax season, handled. 🧮")
    else:
        print(f"{total_checks - passed} check(s) to go. Keep at it!")


if __name__ == "__main__":
    run_tests()
