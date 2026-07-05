# Bubble Tea Loyalty Discount 🧋💳

## The Story

Remember your bubble tea shop from the very first exercise? It's doing so
well you're launching a loyalty program: members get 10% off.

## Your Task

Open [`solution.py`](solution.py) and finish
`bubble_tea_total_with_discount(size, num_toppings, is_member=False)`.

It works exactly like the original `bubble_tea_total` you wrote before:

| Size   | Price |
|--------|-------|
| small  | $3.00 |
| medium | $4.00 |
| large  | $5.00 |

- Each topping costs $0.50.
- 5+ toppings adds a $1.00 "topping overload fee".

**New this time:** if `is_member` is `True`, take 10% off the total
*after* everything else is calculated. Round the final result to 2
decimal places.

Notice `is_member=False` in the function signature - that's a **default
value**. It means callers can leave it out entirely, and it'll act as if
they'd passed `False`.

## Example

```python
bubble_tea_total_with_discount("small", 0)
# -> 3.0   (is_member defaults to False)

bubble_tea_total_with_discount("medium", 2, True)
# -> 4.5   (base 5.0, minus 10%)

bubble_tea_total_with_discount("large", 5, True)
# -> 7.65  (base 8.5, minus 10%)
```

## Check Your Work

```
python test_solution.py
```

## Hints

<details>
<summary>Hint 1: it's the old exercise plus one step</summary>

Copy the logic from your original `bubble_tea_total` almost exactly - the
size pricing, the toppings, the overload fee. That part hasn't changed.
</details>

<details>
<summary>Hint 2: applying the discount</summary>

After you've computed the total the old way, add one more check:
`if is_member: total = total * 0.9`
</details>

<details>
<summary>Hint 3: rounding</summary>

`round(total, 2)` at the very end keeps the result clean (discounts can
produce numbers like `7.6499999999999995` due to how computers store
decimals).
</details>

## What You're Practicing

Default parameter values (`is_member=False`), and building on a function
you already understand rather than starting from scratch - a preview of
how real programs get extended over time.

---
Next: [tax_and_total_helpers](../2_tax_and_total_helpers/)
