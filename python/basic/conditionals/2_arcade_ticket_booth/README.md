# Arcade Ticket Booth 🎮

## The Story

You run the ticket booth at an arcade. Price depends on **age** and
whether it's a **weekend** (weekends cost more - surge pricing, arcade
style).

## Your Task

Open [`solution.py`](solution.py) and finish `ticket_price(age, is_weekend)`.

**Pricing rules:**

| Age group          | Weekday | Weekend |
|---------------------|---------|---------|
| under 5              | Free ($0) | Free ($0) |
| 5 to 12 (child)       | $8      | $10     |
| 13 to 64 (adult)      | $12     | $15     |
| 65 and up (senior)    | $6      | $8      |

`is_weekend` is either `True` or `False`.

## Example

```python
ticket_price(8, False)    # -> 8   (child, weekday)
ticket_price(8, True)     # -> 10  (child, weekend)
ticket_price(30, True)    # -> 15  (adult, weekend)
ticket_price(3, True)     # -> 0   (under 5 is always free)
```

## Check Your Work

```
python test_solution.py
```

## Hints

<details>
<summary>Hint 1: chaining conditions</summary>

You'll need more than one `elif` this time - one per age group, checked
in order from youngest to oldest (or oldest to youngest, your call).
</details>

<details>
<summary>Hint 2: using is_weekend inside a branch</summary>

Once you know the age group, you still need a second check for
`is_weekend` to pick the right price. That's a nested `if`/`else` inside
each age branch.
</details>

<details>
<summary>Hint 3: watch your boundaries</summary>

Is a 5-year-old a "child" or "under 5"? The table says 5-12 is child, so
`age < 5` is the free group and `age >= 5` starts the child pricing.
Double check your `<` vs `<=`.
</details>

## What You're Practicing

More `if` / `elif` / `else`, comparison operators (`<`, `>=`), and
booleans (`True` / `False`) as function inputs - building on what you used
in the bubble tea exercise.

---
Next: [shopping_basket_total](../../loops/1_shopping_basket_total/)
