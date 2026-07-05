# Bubble Tea Shop Calculator 🧋

## The Story

You just opened a tiny bubble tea shop. Customers order a **size** and pick
some **toppings**. Your only job: write the function that figures out how
much they owe.

## Your Task

Open [`solution.py`](solution.py) and finish the function
`bubble_tea_total(size, num_toppings)`.

**Pricing rules:**

| Size   | Price |
|--------|-------|
| small  | $3.00 |
| medium | $4.00 |
| large  | $5.00 |

- Each topping costs **$0.50**.
- If a customer orders **5 or more toppings**, add a **$1.00 "topping
  overload fee"** (we just made this up, but it's shop policy now).
- The function should `return` the total price.

## Example

```python
bubble_tea_total("medium", 2)   # -> 5.0   (4.00 base + 2 * 0.50)
bubble_tea_total("large", 5)    # -> 8.5   (5.00 base + 5 * 0.50 + 1.00 fee)
```

## Check Your Work

```
python test_solution.py
```

Run it as many times as you want — it won't judge you (much).

## Hints (only peek if stuck!)

<details>
<summary>Hint 1: how do I check the size?</summary>

Use `if` / `elif` / `else` to compare `size` against `"small"`, `"medium"`,
`"large"`.
</details>

<details>
<summary>Hint 2: how do I turn toppings into money?</summary>

Multiplication: `num_toppings * 0.5`
</details>

<details>
<summary>Hint 3: what about the overload fee?</summary>

After you've added up the base price and the toppings, check
`if num_toppings >= 5:` and add `1.0` more.
</details>

## What You're Practicing

Variables, `if` / `elif` / `else`, arithmetic, and writing a function that
`return`s a value. That's most of what you need to build much bigger things.

---
Next: [arcade_ticket_booth](../2_arcade_ticket_booth/)
