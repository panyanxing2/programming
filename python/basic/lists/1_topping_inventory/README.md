# Topping Inventory 📦

## The Story

A delivery just arrived with new toppings for the shop. Add them to
what's already in stock, then check whether a customer's requested
topping is available.

## Your Task

Open [`solution.py`](solution.py) and finish
`restock_and_check(toppings_in_stock, new_arrivals, requested_topping)`:

1. Add every item in `new_arrivals` to `toppings_in_stock`.
2. Return `True` if `requested_topping` is now in `toppings_in_stock`,
   otherwise `False`.

## Example

```python
restock_and_check(["pearls", "pudding"], ["taro balls"], "taro balls")
# -> True   (it just arrived)

restock_and_check(["pearls"], [], "pudding")
# -> False  (never showed up)
```

## Check Your Work

```
python test_solution.py
```

## Hints

<details>
<summary>Hint 1: adding items one at a time</summary>

`some_list.append(item)` adds `item` to the end of `some_list`. Loop over
`new_arrivals` and append each one to `toppings_in_stock`.
</details>

<details>
<summary>Hint 2: checking if something is in a list</summary>

`"pearls" in some_list` gives you `True` or `False` directly - you can
`return` that expression straight away, no `if` needed.
</details>

## What You're Practicing

Growing a list with `.append()` inside a loop, and checking membership
with `in` - list versions of things you've already done with strings and
loops.

---
Next: [top_seller_finder](../2_top_seller_finder/)
