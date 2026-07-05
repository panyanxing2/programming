# Review Vowel Counter 🔤

## The Story

You're building a (very silly, not scientifically valid) "review
enthusiasm" meter for your shop's reviews. Step one: count the vowels.

## Your Task

Open [`solution.py`](solution.py) and finish `count_vowels(text)`. Count
how many of the characters in `text` are vowels (`a`, `e`, `i`, `o`, `u`),
**ignoring case** - `"A"` and `"a"` both count.

## Example

```python
count_vowels("Bubble Tea")   # -> 4
count_vowels("Xyz")           # -> 0
count_vowels("AEIOU")         # -> 5
```

## Check Your Work

```
python test_solution.py
```

## Hints

<details>
<summary>Hint 1: ignoring case</summary>

`text.lower()` gives you a lowercase copy of the string, so you only have
to check for `a, e, i, o, u` instead of also `A, E, I, O, U`.
</details>

<details>
<summary>Hint 2: looping over a string</summary>

Strings can be looped over character by character, just like a list:

```python
for ch in text:
    ...
```
</details>

<details>
<summary>Hint 3: checking if a character is a vowel</summary>

`if ch in "aeiou":` is `True` when `ch` is one of those 5 letters. This
is the same `in` you might use to check if something is in a list.
</details>

## What You're Practicing

Looping over a string one character at a time, combined with `if` and the
accumulator pattern from the loops exercises - now applied to text
instead of numbers.

---
Next: [topping_inventory](../../lists/1_topping_inventory/)
