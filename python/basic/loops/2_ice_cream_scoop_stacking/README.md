# Ice Cream Scoop Stacking 🍦

## The Story

Every scoop of ice cream has a height. Every cone has a max height before
it topples over. Your job: figure out how many scoops fit before disaster.

## Your Task

Open [`solution.py`](solution.py) and finish
`scoops_that_fit(scoop_height, max_height)`. Keep "adding" scoops one at a
time - as long as the next scoop wouldn't push the stack over
`max_height` - and return how many scoops you managed to fit.

If even one scoop doesn't fit, return `0`.

## Example

```python
scoops_that_fit(2, 9)    # -> 4   (2+2+2+2 = 8, fits; +2 more = 10, doesn't)
scoops_that_fit(3, 9)    # -> 3   (3+3+3 = 9, fits exactly)
scoops_that_fit(5, 4)    # -> 0   (a single scoop is already too tall)
```

## Check Your Work

```
python test_solution.py
```

## Hints

<details>
<summary>Hint 1: why a while loop?</summary>

You don't know ahead of time how many scoops it'll take - you keep going
*while* a condition holds. That's exactly what `while` loops are for
(unlike `for`, which loops a known number of times, e.g. once per item in
a list).
</details>

<details>
<summary>Hint 2: the loop condition</summary>

Track a running `total` height and a `count` of scoops, both starting at
`0`. Loop `while total + scoop_height <= max_height:` - if adding one more
scoop still fits, add it (update both `total` and `count`).
</details>

<details>
<summary>Hint 3: don't forget to update the loop variables</summary>

Every `while` loop needs something inside it that eventually makes the
condition false - otherwise it loops forever. Make sure `total` actually
increases each time through the loop.
</details>

## What You're Practicing

Your first `while` loop, plus reusing the accumulator pattern and
comparison operators from earlier exercises.

---
Next: [cup_name_tag](../../strings/1_cup_name_tag/)
