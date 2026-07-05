# Temperature Display 🌡️

## The Story

Your shaved ice shop has a walk-in freezer with a thermometer that only
reads Celsius. Half your customers only understand Fahrenheit. Fix that.

## Your Task

Open [`solution.py`](solution.py) and finish
`celsius_to_fahrenheit_label(celsius)`. It should return a string showing
both temperatures.

**Formula:** `fahrenheit = celsius * 9 / 5 + 32`

Round the Fahrenheit value to **1 decimal place**.

**Format:** `"<celsius>°C is <fahrenheit>°F"`

## Example

```python
celsius_to_fahrenheit_label(0)
# -> "0°C is 32.0°F"

celsius_to_fahrenheit_label(100)
# -> "100°C is 212.0°F"
```

## Check Your Work

```
python test_solution.py
```

## Hints

<details>
<summary>Hint 1: order of operations</summary>

Python follows normal math order of operations, so
`celsius * 9 / 5 + 32` works exactly like it looks.
</details>

<details>
<summary>Hint 2: rounding</summary>

`round(value, 1)` rounds `value` to 1 decimal place.
</details>

<details>
<summary>Hint 3: negative numbers</summary>

One of the test cases uses a negative temperature. Your formula should
handle it exactly the same way - no special-casing needed.
</details>

## What You're Practicing

More arithmetic, the `round()` function, and formatting output - the same
basics as the last exercise, applied to a new problem.

---
Next: [bubble_tea_calculator](../../conditionals/1_bubble_tea_calculator/)
