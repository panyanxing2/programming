# Menu Price Lookup 📋

## The Story

Your menu is now a proper dictionary: item name maps to price. A customer
walks up and asks for something - you need to look up the price, or
politely tell them you don't sell that.

## Your Task

Open [`solution.py`](solution.py) and finish
`get_menu_price(menu, item_name)`. `menu` is a dictionary like
`{"Milk Tea": 4.5, "Taro": 5.0}`.

- If `item_name` is on the menu, return its price.
- If it isn't, return `-1` (our signal for "not on the menu").

## Example

```python
menu = {"Milk Tea": 4.5, "Taro": 5.0}

get_menu_price(menu, "Milk Tea")   # -> 4.5
get_menu_price(menu, "Coffee")     # -> -1   (we don't sell that)
```

## Check Your Work

```
python test_solution.py
```

## Hints

<details>
<summary>Hint 1: dictionary lookup</summary>

`menu["Milk Tea"]` gets the price for `"Milk Tea"` - but it crashes if the
key doesn't exist.
</details>

<details>
<summary>Hint 2: a lookup that doesn't crash</summary>

`menu.get("Coffee", -1)` returns the value for `"Coffee"` if it exists,
or `-1` if it doesn't - no crash, no `if` needed. This one line can be
your whole function.
</details>

## What You're Practicing

Your first dictionary: key/value lookups, and handling a "key might not
exist" case gracefully with `.get()` and a default value.

---
Next: [daily_sales_summary](../2_daily_sales_summary/)
