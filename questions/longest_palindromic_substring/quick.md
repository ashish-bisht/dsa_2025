
### 3. quick.md
*Updated to briefly mention the pointer-based expansion while keeping it concise (100–200 words).*

```markdown
# Longest Palindromic Substring - Quick Reference

**Key Idea**: Use two pointers (`left` and `right`) to expand around each index as a potential palindrome center, checking for odd and even-length palindromes.

**Framework**:
1. For each index `i`:
   - Odd palindrome: Set `left=i`, `right=i`, expand outward.
   - Even palindrome: Set `left=i`, `right=i+1`, expand outward.
2. Expand while `s[left] == s[right]` and indices are valid.
3. When expansion stops, `left` is before the start, `right` is after the end.
4. Calculate length (`right - left - 1`) and start (`left + 1`).
5. Track the longest palindrome's start and length.
6. Return the substring.

**Complexity**:
- Time: O(n²) – iterate `n` indices, expand up to `n/2` steps.
- Space: O(1) – only use variables.

**Similar Problems**:
- Longest Substring Without Repeating Characters (Week 1)
- Word Break (Week 4)
- Regular Expression Matching (Week 5)