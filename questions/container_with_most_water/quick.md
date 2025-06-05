
```markdown
# Container With Most Water Quick Reference

**Key Idea**: Use two pointers to maximize the area formed by two lines and the x-axis. Start with pointers at both ends (max width) and move the pointer at the shorter height inward to potentially increase the area.

**Framework**:
1. Set `left = 0`, `right = len(height) - 1`, `max_area = 0`.
2. While `left < right`:
   - Compute area: `min(height[left], height[right]) * (right - left)`.
   - Update `max_area`.
   - Move pointer at shorter height (`left += 1` if `height[left] < height[right]`, else `right -= 1`).
3. Return `max_area`.

**Similar Problems**:
- Trapping Rain Water (Hard, Week 5)
- 3Sum (Medium, Week 1)
- Maximum Subarray (Medium, Week 1)

**Complexity**:
- Time: `O(n)`
- Space: `O(1)`
