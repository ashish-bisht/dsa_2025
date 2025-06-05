# 438. Find All Anagrams in a String

## Problem Description
Given two strings `s` and `p`, find all the starting indices of substrings in `s` that are anagrams of `p`. An anagram is a word or phrase formed by rearranging the letters of another, meaning they have the same characters with the same frequencies. The strings consist of lowercase English letters only, and the length of both strings `s` and `p` will not be larger than 20,100.

**Example 1:**
- Input: `s = "cbaebabacd"`, `p = "abc"`
- Output: `[0, 6]`
- Explanation: The substring starting at index 0 is "cba" (anagram of "abc"), and at index 6 is "bac" (anagram of "abc").

**Example 2:**
- Input: `s = "abab"`, `p = "ab"`
- Output: `[0, 1, 2]`
- Explanation: Substrings "ab", "ba", and "ab" are anagrams of "ab".

**Constraints:**
- `1 <= s.length, p.length <= 20,100`
- `s` and `p` consist of lowercase English letters.

## Intuition
To find all anagrams of `p` in `s`, we need to identify substrings in `s` of length `len(p)` that have the same characters with the same frequencies. A brute-force approach—checking every substring of length `len(p)`—would take O(n * m) time, where `n` is `len(s)` and `m` is `len(p)`. Instead, we use a **fixed-size sliding window** technique:

- Anagrams have identical character frequencies, so we can compare the frequency map of `p` with a window of size `len(p)` in `s`.
- Instead of recomputing frequencies for each window, slide the window by removing the leftmost character and adding the rightmost one, updating the frequency map efficiently.
- Use Python’s `Counter` to store and compare frequencies, leveraging the fixed alphabet (26 lowercase letters) for O(1) operations.

## Approach
1. **Edge Case**: If `len(p) > len(s)`, return an empty list since no anagrams are possible.
2. **Initialize**:
   - Create a `Counter` for `p` (`p_count`) to store its character frequencies.
   - Create a `Counter` for the first window of `s` (`s[0:len(p)]`) (`window_count`).
   - Check if the first window is an anagram (`window_count == p_count`). If true, append `0` to the result.
3. **Slide the Window**:
   - For each index `idx` from `1` to `len(s) - len(p)`:
     - Remove the leftmost character (`s[idx - 1]`) from `window_count`.
     - Add the new rightmost character (`s[idx + len(p) - 1]`) to `window_count`.
     - Check if the updated `window_count` equals `p_count`. If true, append `idx` to the result.
4. **Return**: The list of starting indices.

## Sliding Window Pattern
This problem uses a **fixed-size sliding window** pattern, where the window size is `len(p)`. Here’s a generic template for fixed-size sliding window problems:

```python
def sliding_window_fixed(arr, k):
    # Handle edge cases
    if len(arr) < k:
        return []
    
    result = []
    window_state = Counter(arr[:k])  # Initialize window state
    if check_condition(window_state):  # Check first window
        result.append(0)
    
    for idx in range(1, len(arr) - k + 1):
        # Remove leftmost element
        update_window_remove(window_state, arr[idx - 1])
        # Add rightmost element
        update_window_add(window_state, arr[idx + k - 1])
        # Check condition
        if check_condition(window_state):
            result.append(idx)
    
    return result
```

For this problem:
- **Window Size**: `len(p)`.
- **Window State**: `Counter` for character frequencies.
- **Condition**: `window_count == p_count`.
- **Updates**: Remove `s[idx - 1]`, add `s[idx + len(p) - 1]`.

This pattern applies to other Grind 108 problems like **Longest Substring Without Repeating Characters** (variable-size window) and **Longest Repeating Character Replacement** (variable-size window).

## Code Walkthrough
Let’s break down the Python code:

```python
p_count = Counter(p)
window_count = Counter(s[:len(p)])
```
- `p_count` stores the frequency of characters in `p` (e.g., for `p = "abc"`, `p_count = {'a': 1, 'b': 1, 'c': 1}`).
- `window_count` stores the frequency of the first `len(p)` characters in `s` (e.g., for `s = "cbaebabacd"`, `window_count = {'c': 1, 'b': 1, 'a': 1}`).

```python
if window_count == p_count:
    result.append(0)
```
- Checks if the first window (`s[0:len(p)]`) is an anagram by comparing frequency maps. If true, appends `0`.
- This uses the same anagram-checking logic (`window_count == p_count`) as in the loop, but is done separately for clarity, as no character is removed for the first window.

```python
for idx in range(1, len(s) - len(p) + 1):
    char_to_remove = s[idx - 1]
    window_count[char_to_remove] -= 1
    if window_count[char_to_remove] == 0:
        del window_count[char_to_remove]
    char_to_add = s[idx + len(p) - 1]
    window_count[char_to_add] += 1
    if window_count == p_count:
        result.append(idx)
```
- Slides the window:
  - `idx` ranges from `1` to `len(s) - len(p)` to cover all windows after the first.
  - Removes `s[idx - 1]` (leftmost character of previous window).
  - Adds `s[idx + len(p) - 1]` (rightmost character of new window).
  - Checks if the updated `window_count` equals `p_count`, appending `idx` if true.
- The anagram check is identical to the first window’s check, ensuring consistent logic.

## Step-by-Step Example
For `s = "cbaebabacd"`, `p = "abc"`:

1. **Initialization**:
   - `p_count = {'a': 1, 'b': 1, 'c': 1}`
   - `window_count = Counter("cba") = {'c': 1, 'b': 1, 'a': 1}`
   - `window_count == p_count`, so append `0` to `result = [0]`.

2. **idx = 1** (window: `s[1:4] = "bae"`):
   - Remove `s[0] = 'c'`: `window_count = {'b': 1, 'a': 1}`
   - Add `s[3] = 'e'`: `window_count = {'b': 1, 'a': 1, 'e': 1}`
   - `window_count != p_count`, no append.

3. **idx = 6** (window: `s[6:9] = "bac"`):
   - After updates: `window_count = {'b': 1, 'a': 1, 'c': 1}`
   - `window_count == p_count`, append `6` to `result = [0, 6]`.

4. **Continue until idx = 7** (last window: `s[7:10] = "acd"`):
   - No further anagrams found.

**Output**: `[0, 6]`

## Time and Space Complexity
- **Time Complexity**: O(length_s), where `length_s` is `len(s)`. We process each character once, and `Counter` operations (update, compare) are O(1) due to the fixed alphabet (26 lowercase letters).
- **Space Complexity**: O(1), as `Counter` stores at most 26 characters. The result list is excluded from space complexity as it’s part of the output.

## Common Pitfalls
- **Missing the First Window**: Forgetting to check `s[0:len(p)]` before sliding misses anagrams at index `0`. The solution checks this explicitly using the same logic (`window_count == p_count`) as in the loop.
- **Incorrect Window Updates**: Removing/adding wrong characters (e.g., `s[idx]` instead of `s[idx - 1]`) corrupts the frequency map. Always remove `s[idx - 1]` and add `s[idx + len(p) - 1]`.
- **Edge Case Handling**: Returning `None` instead of `[]` when `len(p) > len(s)` is incorrect.
- **Using While Loop**: A `while` loop with manual pointers (e.g., `left`, `right`) is error-prone compared to `for` with `range`.

## Key Takeaways
- **Sliding Window Power**: Fixed-size sliding window optimizes substring problems by avoiding recomputation, reducing time from O(n * m) to O(n).
- **Consistent Logic**: The anagram check (`window_count == p_count`) is the same for all windows; the first window is checked separately for clarity.
- **Counter Usage**: `Counter` simplifies frequency comparisons for anagrams.
- **Pattern Practice**: Master sliding window for other Grind 108 problems like **Longest Substring Without Repeating Characters** and **3Sum**.

## Related Problems
- **49. Group Anagrams** (Week 1, Grind 108): Uses frequency maps to group anagrams, similar to comparing `window_count` and `p_count`.
- **8. Longest Substring Without Repeating Characters** (Week 1, Grind 108): Uses a variable-size sliding window to track distinct characters.
- **13. Longest Repeating Character Replacement** (Week 1, Grind 108): Uses a variable-size sliding window to maximize substring length with `k` replacements.
- **567. Permutation in String** (not in Grind 108): Similar sliding window for permutation check.
- **76. Minimum Window Substring** (not in Grind 108): Harder variable-size sliding window problem.