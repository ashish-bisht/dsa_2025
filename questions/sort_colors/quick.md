
**Explanation of sol.md**:
- **Variable Names**: Uses `left`, `cur`, `right` to match your preference, emphasizing their intuitive roles.
- **Alternative Implementation**: Discusses your original code’s `if cur == left` and `if cur == right` conditions, explaining why they’re redundant.
- **Pointer Deep Dive**: Details each pointer’s purpose, movement, and the critical decision not to increment `cur` after a `2` swap.
- **Example**: Walks through the test case `[2,0,2,1,1,0]` to show pointer movements.
- **Takeaways**: Highlights the algorithm’s efficiency and the intuitive naming.

---

### quick.md
Below is the concise summary for quick recall, using `left`, `cur`, and `right`.

```markdown
# Sort Colors Quick Reference

**Key Idea**: Use the Dutch National Flag algorithm to sort an array of 0s, 1s, and 2s in-place with three pointers: `left` (0s before), `cur` (scans middle), and `right` (2s after). Swap elements to partition in one pass, keeping `cur` static after a `2` swap to check the new element.

**Framework**:
1. Initialize `left = 0`, `cur = 0`, `right = len(nums) - 1`.
2. While `cur <= right`:
   - If `nums[cur] = 0`: Swap with `left`, increment `left` and `cur`.
   - If `nums[cur] = 2`: Swap with `right`, decrement `right`.
   - If `nums[cur] = 1`: Increment `cur`.

**Similar Problems** (Grind 108):
- Maximum Subarray (Week 1, #1): Single-pass array processing.
- Rotate Array (Week 1, #3): In-place array manipulation.
- Sort List (Week 2, #7): Sorting with different data structure.

**Complexity**:
- Time: O(n)
- Space: O(1)