# 3. Longest Substring Without Repeating Characters (Quick Recall)

**Key Idea**: Variable-size sliding window to find longest substring without duplicates. Expand with `right`, shrink `left` on window duplicates, track max length.

**Framework**:
1. Initialize `max_length = 0`, `character_index = {}`, `left = 0`.
2. For `right` in `range(len(s))`:
   - If `s[right] in character_index` and `character_index[s[right]] >= left`, duplicate in window, set `left = character_index[s[right]] + 1`.
   - Update `max_length = max(max_length, right - left + 1)`.
   - Set `character_index[s[right]] = right`.
3. Return `max_length`.

**Pattern**: Variable-size window, unlike **Find All Anagrams in a String**’s fixed-size.

**Complexity**:
- Time: O(length_s).
- Space: O(min(length_s, m)), `m` is character set size.

**Similar Problems**:
- 438. Find All Anagrams in a String (Week 1).
- 13. Longest Repeating Character Replacement (Week 1).
- 76. Minimum Window Substring.