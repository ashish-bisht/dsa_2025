# 3Sum Closest Solution

## Problem Description
Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that their sum is closest to `target`. Return the sum of the three integers. You may assume that each input has exactly one solution.

**Example 1**:
- Input: `nums = [-1,2,1,-4], target = 1`
- Output: `2` (The sum of `[-1,1,2]` is 2, which is closest to 1)

**Example 2**:
- Input: `nums = [0,0,0], target = 1`
- Output: `0` (The sum of `[0,0,0]` is 0, closest to 1)

**Constraints**:
- `3 <= nums.length <= 500`
- `-1000 <= nums[i] <= 1000`
- `-10^4 <= target <= 10^4`

## Intuition
The brute-force approach would check every possible triplet, but this takes O(n³) time, which is too slow for arrays up to 500 elements. Instead, we can optimize by sorting the array and using a two-pointer technique, similar to the **3Sum** problem. Sorting allows us to efficiently search for pairs that, when added to a fixed number, give a sum close to the target. By tracking the closest sum found, we can update it whenever we find a better candidate.

## Approach
1. **Sort the array**: This enables the two-pointer technique and ensures we can avoid duplicate triplets if needed.
2. **Iterate over the first number**: For each index `idx`, fix `nums[idx]` as the first number of the triplet.
3. **Use two pointers**:
   - Set `left = idx + 1` and `right = len(nums) - 1`.
   - Compute the sum: `current_sum = nums[idx] + nums[left] + nums[right]`.
   - If `current_sum == target`, return it immediately (exact match).
   - Update `closest_sum` if the absolute difference `|current_sum - target|` is smaller than the current best.
   - If `current_sum < target`, increment `left` to increase the sum.
   - If `current_sum > target`, decrement `right` to decrease the sum.
4. **Return the closest sum**: After checking all triplets, return the sum closest to the target.

## Code Walkthrough
Let’s walk through the code for clarity:
```python
nums.sort()  # Sort to enable two-pointer technique
length_array = len(nums)
closest_sum = float('inf')  # Track closest sum to target

for idx in range(length_array - 2):  # Leave space for left and right pointers
    left = idx + 1
    right = length_array - 1
    while left < right:
        current_sum = nums[idx] + nums[left] + nums[right]
        if current_sum == target:  # Exact match
            return current_sum
        if abs(current_sum - target) < abs(closest_sum - target):  # Update if closer
            closest_sum = current_sum
        if current_sum < target:  # Need larger sum
            left += 1
        else:  # Need smaller sum
            right -= 1
return closest_sum