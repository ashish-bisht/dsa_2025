
**Key Points in `sol.md`**:
- **Beginner-Friendly**: Uses simple language, avoids jargon, and explains every step.
- **Deep Logic Dive**: Emphasizes the sorted key as the main crux, with a detailed explanation of why it works.
- **Pointers**: Discusses iteration and sorting in pointer-like terms, even though Python abstracts them.
- **Structure**: Follows the required sections, with clear examples and connections to other problems.
- **Trade-offs**: Mentions the character-count alternative for completeness.

---

### 3. `quick.md`
This file provides a concise summary (100–200 words) for quick recall, highlighting the key idea and related problems.

```markdown
# Group Anagrams Quick Reference

**Key Idea**: Group strings that are anagrams by using a sorted string as a hash map key. Anagrams sort to the same string (e.g., "eat" and "tea" both sort to "aet"). Iterate through the input, sort each string, and group originals by this key in a `defaultdict(list)`. Return the hash map values.

**Framework**:
1. Initialize `defaultdict(list)` for anagram groups.
2. For each string, sort its characters to get a key.
3. Append the original string to the key’s list.
4. Return the dictionary values as a list.

**Main Crux**: Sorting normalizes anagrams into a unique key, enabling efficient grouping.

**Complexity**:
- Time: O(N * K * log K), where N is the number of strings, K is the max string length.
- Space: O(N * K) for the hash map.

**Similar Problems**:
- Find All Anagrams in a String (Week 1): Uses character frequency for anagrams.
- Longest Substring Without Repeating Characters (Week 1): Involves character counting.
- Word Break (Week 4): String manipulation with dynamic programming.

**Pattern**: Hash map grouping by a normalized key.