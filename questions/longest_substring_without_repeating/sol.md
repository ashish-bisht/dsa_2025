# 3. Longest Substring Without Repeating Characters

## Problem Description
Given a string `s`, find the length of the longest substring without repeating characters.

**Example 1:**
- Input: `s = "abcabcbb"`
- Output: `3`
- Explanation: Longest substring is `"abc"`, length 3.

**Example 2:**
- Input: `s = "bbbbb"`
- Output: `1`
- Explanation: Longest substring is `"b"`, length 1.

**Constraints:**
- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols, spaces.

## Intuition
Find the longest substring with no duplicates. Instead of checking all substrings (slow), use a **variable-size sliding window**:
- Move `right` to add characters.
- Move `left` when a duplicate is found in the window.
- Track max window size with a dictionary for character indices.

## Approach
1. Initialize `max_length = 0`, `character_index = {}`, `left = 0`.
2. For `right` from `0` to `len(s) - 1`:
   - If `s[right]` is in `character_index` and its last index is `>= left`, move `left` past it.
   - Update `max_length` with `right - left + 1`.
   - Store `right` as `s[right]`’s index.
3. Return `max_length`.

## Sliding Window Pattern
Uses a **variable-size sliding window**, unlike **Find All Anagrams in a String**’s fixed-size window. The window grows with `right`, shrinks with `left` on duplicates to maximize length.

## Code Walkthrough
```python
character_index = {}
max_length = 0
left = 0
```
- `character_index`: Maps characters to latest index.
- `max_length`: Tracks longest substring.
- `left`: Window start.

```python
for right in range(len(s)):
    cur_character = s[right]
    if cur_character in character_index and character_index[cur_character] >= left:
        left = character_index[cur_character] + 1
    max_length = max(max_length, right - left + 1)
    character_index[cur_character] = right
```
- Expand with `right`.
- Check `cur_character in character_index and character_index[cur_character] >= left`:
  - `cur_character in character_index`: Was it seen?
  - `character_index[cur_character] >= left`: Is it in `s[left:right+1]`? If yes, duplicate, move `left` past it.
- Update `max_length`.
- Store `right` in `character_index`.

## Step-by-Step Example
For `s = "abcabcbb"`:
1. `right = 0` (`s[0] = 'a'`): No duplicate, `max_length = 1`, `character_index['a'] = 0`.
2. `right = 2` (`s[2] = 'c'`): Window `"abc"`, `max_length = 3`, `character_index = {'a': 0, 'b': 1, 'c': 2}`.
3. `right = 3` (`s[3] = 'a'`): `character_index['a'] = 0 >= left = 0`, duplicate. `left = 1`, `max_length = 3`, `character_index['a'] = 3`.
4. End: `max_length = 3`.

**Output**: `3`

## Time and Space Complexity
- **Time**: O(length_s), single pass.
- **Space**: O(min(length_s, m)), `m` is character set size.

## Common Pitfalls
- Skipping `character_index[cur_character] >= left`: Shrinks window for characters outside `s[left:right+1]`, reducing `max_length`.
- Empty string: Return `0`.
- Complex structures: Use simple `dict` for interviews.

## Key Takeaways
- `character_index[cur_character] >= left` checks duplicates in the window.
- Variable-size window maximizes length.
- Complements **Find All Anagrams in a String**’s fixed-size window.

## Related Problems
- 438. Find All Anagrams in a String (Week 1): Fixed-size window.
- 13. Longest Repeating Character Replacement (Week 1): Variable-size window.
- 76. Minimum Window Substring: Variable-size window.