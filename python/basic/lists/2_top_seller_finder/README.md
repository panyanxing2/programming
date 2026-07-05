# Top Seller Finder 🏆

## The Story

At closing time, you want to know which topping sold the most today, so
you can brag about it tomorrow.

## Your Task

Open [`solution.py`](solution.py) and finish
`best_selling_topping(topping_names, sales_counts)`. Both are lists of the
same length - `sales_counts[i]` is how many times `topping_names[i]` sold.
Return the name of the topping with the highest count.

If there's a tie, return whichever one appears **first** in the list.

## Example

```python
best_selling_topping(["Pearls", "Pudding", "Aloe"], [10, 25, 7])
# -> "Pudding"

best_selling_topping(["Pearls", "Pudding"], [5, 5])
# -> "Pearls"   (tie - first one wins)
```

## Check Your Work

```
python test_solution.py
```

## Hints

<details>
<summary>Hint 1: tracking the best so far</summary>

Start by assuming index `0` is the best: `best_index = 0` and
`best_count = sales_counts[0]`. Then loop through the rest, updating
those two variables whenever you find something better.
</details>

<details>
<summary>Hint 2: looping with an index</summary>

Since you need to look at the *same position* in two lists at once,
`range(len(topping_names))` gives you the indexes `0, 1, 2, ...` to use
on both lists: `topping_names[i]` and `sales_counts[i]`.
</details>

<details>
<summary>Hint 3: keeping the tie-breaking rule</summary>

Use a strict `>` (not `>=`) when checking `sales_counts[i] > best_count`.
That way, later toppings only take over the lead if they're strictly
higher - ties keep the earlier one.
</details>

## What You're Practicing

Looping with an index (`range(len(...))`), comparing values across two
parallel lists, and the "track the best so far" pattern - a step up from
the simple accumulator you used before.

---
Next: [menu_price_lookup](../../dictionaries/1_menu_price_lookup/)
