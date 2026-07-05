# Shopping Basket Total 🛒

## The Story

You're at the night market with a basket full of stuff. Before you get to
the register, you want to know the damage.

## Your Task

Open [`solution.py`](solution.py) and finish `basket_total(prices)`.
`prices` is a list of numbers. Add them all up and return the total.

An empty basket costs `0`.

## Example

```python
basket_total([3.5, 2.0, 4.25])   # -> 9.75
basket_total([])                  # -> 0
basket_total([10])                # -> 10
```

## Check Your Work

```
python test_solution.py
```

## Hints

<details>
<summary>Hint 1: the accumulator pattern</summary>

Start a variable at `0` *before* the loop (e.g. `total = 0`). Then, for
each price in the list, add it to `total`. This "start at zero, add as you
go" pattern shows up constantly in programming.
</details>

<details>
<summary>Hint 2: looping over a list</summary>

```python
for price in prices:
    ...
```

This runs the loop body once for every item in `prices`, with `price`
holding the current one each time.
</details>

<details>
<summary>Hint 3: the empty list case</summary>

If `prices` is `[]`, the `for` loop simply never runs. As long as `total`
started at `0`, you'll return `0` automatically - no special case needed.
</details>

## What You're Practicing

Your first `for` loop, plus the "accumulator" pattern (a variable that
builds up a result across many loop iterations) - combined with the
variables and arithmetic from before.

---
Next: [ice_cream_scoop_stacking](../2_ice_cream_scoop_stacking/)
