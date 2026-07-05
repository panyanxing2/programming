# Cup Name Tag ✍️

## The Story

Customers type their name for the cup, and it's always a mess: extra
spaces, all lowercase, all caps, whatever. You need to clean it up before
it hits the marker.

## Your Task

Open [`solution.py`](solution.py) and finish
`format_cup_name(raw_name, max_length)`:

1. Remove leading/trailing spaces.
2. Capitalize it properly (each word starts with a capital letter).
3. If the cleaned-up name is longer than `max_length` characters, cut it
   down to `max_length` characters and add `"..."` at the end.
4. Return the result.

## Example

```python
format_cup_name("  john  ", 10)     # -> "John"
format_cup_name("alexandria", 6)    # -> "Alexan..."
format_cup_name("MEI LING", 20)     # -> "Mei Ling"
```

## Check Your Work

```
python test_solution.py
```

## Hints

<details>
<summary>Hint 1: removing extra spaces</summary>

`"  hi  ".strip()` gives you `"hi"`.
</details>

<details>
<summary>Hint 2: fixing capitalization</summary>

`"mei ling".title()` gives you `"Mei Ling"` - it capitalizes the first
letter of every word.
</details>

<details>
<summary>Hint 3: checking the length</summary>

`len(some_string)` gives you the number of characters. Compare it to
`max_length` with an `if`.
</details>

<details>
<summary>Hint 4: cutting a string down to size</summary>

Slicing works like `some_string[:6]`, which gives you the first 6
characters. Then just add `"..."` on the end with `+`.
</details>

## What You're Practicing

String methods (`.strip()`, `.title()`), `len()`, slicing, and combining
them with an `if` from earlier - your first real string-processing
exercise.

---
Next: [review_vowel_counter](../2_review_vowel_counter/)
