# Tax & Total Helpers 🧮

## The Story

The shop has to charge sales tax now (welcome to running a business).
Rather than writing one big tangled function, you'll split the problem
into two small ones - and have one call the other.

## Your Task

Open [`solution.py`](solution.py) and finish **two** functions:

1. `calculate_tax(subtotal)` - returns 8% of `subtotal`, rounded to 2
   decimal places.
2. `final_total(subtotal)` - returns `subtotal` plus its tax, rounded to
   2 decimal places. **It should call `calculate_tax` to get the tax
   amount, not recompute the formula itself.**

## Example

```python
calculate_tax(10)      # -> 0.8
final_total(10)         # -> 10.8

calculate_tax(25.50)    # -> 2.04
final_total(25.50)      # -> 27.54
```

## Check Your Work

```
python test_solution.py
```

## Hints

<details>
<summary>Hint 1: calculate_tax</summary>

`round(subtotal * 0.08, 2)`
</details>

<details>
<summary>Hint 2: final_total calling calculate_tax</summary>

Inside `final_total`, call the other function just like any other
function: `tax = calculate_tax(subtotal)`. Then add `subtotal + tax`, and
round the sum.
</details>

<details>
<summary>Hint 3: why bother calling it instead of copy-pasting the formula?</summary>

If the tax rate ever changes, you'd only need to update it in one place
(`calculate_tax`) instead of everywhere it's used. That's the whole idea
behind breaking code into small functions.
</details>

## What You're Practicing

Writing more than one function in the same file, and having one function
call another - the last of the "most basic and important" building
blocks. From here, you know enough Python to build real things.

---
That's the whole curriculum for now! See [python/basic/README.md](../../README.md)
if you want to revisit anything.
