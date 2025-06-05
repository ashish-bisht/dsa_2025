# 438. Find All Anagrams in a String (Quick Recall)

**Key Idea**: Use a fixed-size sliding window of size `len(p)` to compare character frequencies in `s` with `p` using `Counter`. Check the first window, then slide by removing the leftmost character and adding the rightmost, collecting anagram start indices.

**Framework**:
1. If `len(p) > len(s)`, return `[]`.
2. Initialize `Counter` for `p` (`p_count`) and first window (`window_count`).
3. Check if first window is an anagram (`window_count == p_count`), append `0` if true.
4. For `idx` in `range(1, len(s) - len(p) + 1)`:
   - Remove `s[idx - 1]` from `window_count`.
   - Add `s[idx + len(p) - 1]` to `window_count`.
   - If `window_count == p_count`, append `idx`.

**Pattern**: Fixed-size sliding window, same anagram check (`window_count == p_count`) for all windows.

**Complexity**:
- Time: O(length_s), single pass with O(1) `Counter` operations.
- Space: O(1), fixed alphabet (26 letters).

**Similar Problems**:
- 49. Group Anagrams (Week 1): Frequency maps for anagrams.
- 8. Longest Substring Without Repeating Characters (Week 1): Variable-size window.
- 13. Longest Repeating Character Replacement (Week 1): Variable-size window.
- 567. Permutation in String: Sliding window for permutations.