
**Explanation of `sol.md`**:
- **Structure**: Follows the required sections: Problem Description, Intuition, Approach, Code Walkthrough, Step-by-Step Example, Complexity, Key Takeaways, and Related Problems.
- **Beginner-Friendly**: Uses simple language, avoids jargon, and explains the two-pointer technique clearly.
- **Example**: Walks through a concrete example with step-by-step calculations to show how the algorithm progresses.
- **Related Problems**: Links to other Grind 108 problems (3Sum, Container With Most Water) and mentions a related non-Grind problem (4Sum) for context.

---

### quick.md
```markdown
# 3Sum Closest Quick Summary

**Key Idea**: Sort the array and use two pointers to find three numbers whose sum is closest to the target. Track the closest sum by comparing absolute differences.

 Hawkins.

**Framework**:
1. Sort the array.
2. For each index `idx`, fix `nums[idx]` and use two pointers (`left`, `right`).
3. Compute sum = `nums[idx] + nums[left] + nums[right]`.
4. Update closest sum if `|sum - target|` is smaller.
5. Move `left` or `right` based on whether sum is less or greater than target.

**Similar Problems**:
- 3Sum (Grind 108): Find triplets summing to zero.
- Container With Most Water (Grind 108): Two-pointer optimization.
- 4Sum: Extends to four numbers.

**Complexity**:
- Time: O(n²) (sorting O(n log n) + two-pointer O(n²)).
- Space: O(1) or O(log n) with sorting.