# Daily Sales Summary 💰

## The Story

At closing time you have two dictionaries: your `menu` (item -> price)
and today's `sales` (item -> how many sold). Time to find out how much
money you made.

## Your Task

Open [`solution.py`](solution.py) and finish `total_revenue(menu, sales)`.
For every item sold, multiply its price by how many were sold, and add it
all up.

If an item in `sales` somehow isn't on the `menu` (maybe a promo item),
treat its price as `0` instead of crashing.

## Example

```python
menu = {"Milk Tea": 4.5, "Taro": 5.0}
sales = {"Milk Tea": 3, "Taro": 2}

total_revenue(menu, sales)
# -> 23.5   (4.5*3 + 5.0*2)
```

## Check Your Work

```
python test_solution.py
```

## Hints

<details>
<summary>Hint 1: looping over a dictionary's key/value pairs</summary>

```python
for item, quantity in sales.items():
    ...
```

`.items()` gives you both the key (`item`) and the value (`quantity`) at
once, for every entry in the dictionary.
</details>

<details>
<summary>Hint 2: looking up the price safely</summary>

Just like the last exercise: `menu.get(item, 0)` gives you the price, or
`0` if `item` isn't on the menu at all.
</details>

<details>
<summary>Hint 3: putting it together</summary>

This is the accumulator pattern again: start `total = 0`, then inside the
loop do `total += menu.get(item, 0) * quantity`.
</details>

## What You're Practicing

Iterating a dictionary with `.items()`, combining two dictionaries, and
reusing the accumulator pattern and `.get()` from earlier exercises.

---
Next: [bubble_tea_loyalty_discount](../../functions/1_bubble_tea_loyalty_discount/)
