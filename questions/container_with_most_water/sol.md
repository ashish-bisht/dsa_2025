# Container With Most Water Solution

## Problem Description

Given an array of non-negative integers `height`, where each element represents the height of a vertical line at index `i`, find two lines that, together with the x-axis, form a container that holds the maximum amount of water. The area of water is calculated as the minimum height of the two lines multiplied by the distance between them. Return the maximum possible area.

**Example**:

- Input: `height = [1,8,6,2,5,4,8,3,7]`
- Output: `49`
- Explanation: The lines at indices 1 (height 8) and 8 (height 7) form a container with area `min(8, 7) * (8 - 1) = 7 * 7 = 49`.

**Constraints**:

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

## Intuition

The problem asks for the maximum area formed by two vertical lines and the x-axis. The area depends on:

1. **Width**: The distance between the two lines (indices `j - i`).
2. **Height**: The minimum height of the two lines, as water cannot exceed the shorter line.

A brute-force approach would check every pair of lines, calculating the area for each pair, but this takes `O(n^2)` time, which is too slow given the constraints (`n` up to `10^5`). Instead, we can use a two-pointer technique to optimize the solution to `O(n)`.

The key insight is to start with the maximum possible width (one pointer at the start, one at the end) and iteratively reduce the width while trying to increase the height. Since the area is limited by the shorter line, we should move the pointer at the shorter line inward, hoping to find a taller line that could increase the area.

## Approach

1. Initialize two pointers: `left` at index `0` and `right` at index `len(height) - 1`.
2. Initialize a variable `max_area` to store the maximum area found.
3. While `left < right`:
   - Calculate the current area as `min(height[left], height[right]) * (right - left)`.
   - Update `max_area` if the current area is larger.
   - If `height[left] < height[right]`, increment `left` to try a taller line on the left.
   - Otherwise, decrement `right` to try a taller line on the right.
4. Return `max_area`.

## Code Walkthrough

```python
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
