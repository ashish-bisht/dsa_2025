# Maximum Subarray (LeetCode #53)

## Problem Description
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

### Examples
- **Input**: `nums = [-2,1,-3,4,-1,2,1,-5,4]`  
  **Output**: `6`  
  **Explanation**: The subarray `[4,-1,2,1]` has the largest sum `6`.
- **Input**: `nums = [1]`  
  **Output**: `1`
- **Input**: `nums = [-1]`  
  **Output**: `-1`

### Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Solution
We use **Kadane’s Algorithm**, a dynamic programming approach that runs in **O(n)** time and uses **O(1)** space.

### Approach
- Initialize `current_sum` and `max_sum` with the first element.
- For each element `nums[i]`:
  - Update `current_sum` as the maximum of `nums[i]` (start new subarray) or `current_sum + nums[i]` (extend existing subarray).
  - Update `max_sum` if `current_sum` is larger.
- Return `max_sum`.

### Code
```python
def max_subarray(nums):
    max_sum = nums[0]
    cur_sum = nums[0]
    
    for idx in range(1, len(nums)):
        cur_sum = max(nums[idx], cur_sum+nums[idx])
        max_sum = max(cur_sum, max_sum)

    return max_sum