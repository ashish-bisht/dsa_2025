### 3. quick.md

This file provides a concise summary for quick recall.

```markdown
# Product of Array Except Self (Quick Summary)

**Key Idea**: Compute the product of all elements except `nums[i]` without division by calculating products of elements to the left and right of each index in O(n) time.

**Framework**:
1. Initialize `answer` array with 1s.
2. Forward pass: Compute left products (`answer[i] = product of nums[0..i-1]`).
3. Backward pass: Multiply `answer[i]` by right products (`product of nums[i+1..n-1]`).

**Complexity**:
- Time: O(n) (two passes over array).
- Space: O(1) (excluding output array, if optimized).

**Similar Problems**:
- Maximum Subarray (Week 1): Tracks max sum instead of product.
- Subarray Sum Equals K (Week 1): Uses prefix sums, similar to prefix products.
- Maximum Product Subarray (Week 2): Handles products over subarrays.

**Hint**: Think of each index as needing everything “before” and “after” it. Use two passes to collect these products efficiently.
