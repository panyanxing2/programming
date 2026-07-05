# Receipt Printer 🧾

## The Story

Your bubble tea shop got a fancy new receipt printer. Only problem: you
have to program it yourself.

## Your Task

Open [`solution.py`](solution.py) and finish `format_receipt_line(item_name,
unit_price, quantity)`. It should return one line of receipt text.

**Format:** `"<quantity>x <item_name> - $<total>"`, where `total` is
`unit_price * quantity`, shown with exactly 2 decimal places.

## Example

```python
format_receipt_line("Taro Milk Tea", 4.50, 2)
# -> "2x Taro Milk Tea - $9.00"

format_receipt_line("Mango Green Tea", 3.75, 3)
# -> "3x Mango Green Tea - $11.25"
```

## Check Your Work

```
python test_solution.py
```

## Hints

<details>
<summary>Hint 1: computing the total</summary>

`total = unit_price * quantity`
</details>

<details>
<summary>Hint 2: building the string</summary>

An f-string can mix variables and text: `f"hello {name}"`. You can put
more than one variable in the same f-string.
</details>

<details>
<summary>Hint 3: forcing 2 decimal places</summary>

Inside an f-string, `{value:.2f}` formats a number with exactly 2 digits
after the decimal point, e.g. `f"${total:.2f}"`.
</details>

## What You're Practicing

Variables, arithmetic, and formatting output with f-strings. This is the
foundation nearly everything else builds on.

---
Next: [temperature_display](../2_temperature_display/)
