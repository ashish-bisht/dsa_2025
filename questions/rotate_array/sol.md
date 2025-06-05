# Rotate Array

## Problem Description

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative. The rotation must be done **in-place**, meaning you should modify the original array without using extra space proportional to the array size.

**Example 1:**

- Input: `nums = [1,2,3,4,5,6,7]`, `k = 3`
- Output: `[5,6,7,1,2,3,4]`
- Explanation: Rotate `[1,2,3,4,5,6,7]` right by 3 steps:
  - After 1 step: `[7,1,2,3,4,5,6]`
  - After 2 steps: `[6,7,1,2,3,4,5]`
  - After 3 steps: `[5,6,7,1,2,3,4]`

**Example 2:**

- Input: `nums = [-1,-100,3,99]`, `k = 2`
- Output: `[3,99,-1,-100]`

**Constraints:**

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

**LeetCode Link**: [Rotate Array](https://leetcode.com/problems/rotate-array)

## Intuition

Rotating an array to the right by `k` steps means moving the last `k` elements to the front and shifting the rest toward the end. A naive approach might involve shifting elements one step at a time, but this would be inefficient for large `k`. Instead, we can use a clever **reverse-based approach** to achieve the rotation in-place with minimal extra space.

The key insight is that reversing the entire array and then reversing two specific portions can achieve the desired rotation. For example, for `[1,2,3,4,5,6,7]` with `k=3`:

- Reverse the whole array: `[7,6,5,4,3,2,1]`
- Reverse the first `k` elements: `[5,6,7,4,3,2,1]`
- Reverse the remaining `n-k` elements: `[5,6,7,1,2,3,4]`

This gives us the correct rotation in a simple and efficient way.

## Approach

1. **Handle Edge Cases**:
   - If the array is empty or `k=0`, no rotation is needed.
   - If `k` is larger than the array length `n`, normalize `k` using `k = k % n` to avoid redundant rotations.

2. **Reverse-Based Algorithm**:
   - Write a helper function `reverse(start, end)` to reverse elements in the array from index `start` to `end`.
   - Step 1: Reverse the entire array (`0` to `n-1`).
   - Step 2: Reverse the first `k` elements (`0` to `k-1`).
   - Step 3: Reverse the remaining `n-k` elements (`k` to `n-1`).

3. **In-Place Modification**:
   - Use the helper function to swap elements in-place, ensuring O(1) extra space.

## Code Walkthrough

Let’s break down the Python code:

```python
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        # Handle edge cases
        if not nums or k == 0:
            return
        
        n = len(nums)
        # Normalize k to avoid unnecessary rotations
        k = k % n
        
        # Helper function to reverse a portion of the array
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # Step 1: Reverse the entire array
        reverse(0, n - 1)
        # Step 2: Reverse the first k elements
        reverse(0, k - 1)
        # Step 3: Reverse the remaining n-k elements
        reverse(k, n - 1)
