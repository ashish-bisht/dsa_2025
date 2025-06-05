
**Explanation**:

- The `sol.md` file is comprehensive, beginner-friendly, and follows the specified structure.
- It explains the problem, intuition, approach, and code in simple language.
- The step-by-step example uses the input from Example 1 to clarify the process.
- Complexity analysis is clear, and related problems are linked to Grind 108.

---

### File 3: `quick.md`

```markdown
# 3Sum Quick Reference

**Key Idea**: Sort the array and fix one number, then use two pointers to find two numbers summing to the negative of the fixed number. Skip duplicates to avoid duplicate triplets.

**Framework**:
1. Sort the array.
2. For each index `i`, fix `nums[i]` and solve 2Sum for `-nums[i]` using two pointers (`left = i + 1`, `right = n - 1`).
3. If sum == 0, add triplet and skip duplicates for `left` and `right`.
4. If sum < 0, move `left` right; if sum > 0, move `right` left.

**Complexity**:
- Time: O(n²) (sorting O(n log n) + two-pointer O(n²)).
- Space: O(1) or O(n) (depending on sorting).

**Similar Problems** (Grind 108):
- 3Sum Closest (Week 1)
- Subarray Sum Equals K (Week 1)
- Container With Most Water (Week 1)
