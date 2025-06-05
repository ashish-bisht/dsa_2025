# Product of Array Except Self

## Problem Description

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all elements of `nums` except `nums[i]`. The algorithm must run in O(n) time and cannot use division. The product of any prefix or suffix is guaranteed to fit in a 32-bit integer.

**Example 1**:

- Input: `nums = [1, 2, 3, 4]`
- Output: `[24, 12, 8, 6]`
- Explanation:
  - `answer[0] = 2 * 3 * 4 = 24`
  - `answer[1] = 1 * 3 * 4 =>; 12`
  - `answer[2] = 1 * 2 * 4 = 8`
  - `answer[3] = 1 * 2 * 3 = 6`

**Example 2**:

- Input: `nums = [-1, 1, 0, -3, 3]`
- Output: `[0, 0, 9, 0, 0]`

**Constraints**:

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`

## Intuition

The challenge is to compute the product of all elements except the current index without using division and in O(n) time. A naive approach might compute the total product and divide by `nums[i]`, but division is forbidden, and zeros complicate it.

Instead, we compute the product of all elements to the **left** and **right** of each index and multiply them. For `nums = [1, 2, 3, 4]` at index 1:

- Left product = `1`
- Right product = `3 * 4 = 12`
- Answer = `1 * 12 = 12`

We can calculate left products in a forward pass and right products in a backward pass, storing intermediate results in the output array to save space.

## Approach

1. Initialize the `answer` array with 1s (size `n`).
2. **Forward pass**: Compute the product of all elements to the left of each index.
   - For index `i`, store the product of `nums[0]` to `nums[i-1]` in `answer[i]`.
   - Use a variable `left_product` to track the running product.
3. **Backward pass**: Multiply each `answer[i]` by the product of all elements to the right.
   - Use a variable `right_product` to track the running product of `nums[i+1]` to `nums[n-1]`.
4. Return the `answer` array.

### Optimization

This approach uses only the `answer` array for intermediate storage, achieving O(1) extra space (excluding the output array). The forward pass stores left products, and the backward pass multiplies by right products directly.

## Code Walkthrough

```python
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n  # Stores final result and intermediate products

        # Forward pass: answer[i] stores product of all elements to the left of i
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        # Backward pass: Multiply answer[i] by product of all elements to the right of i
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer
```

- **Line 3-4**: Initialize `answer` with 1s to store left products and final results.
- **Line 7-9**: Forward pass fills `answer` with left products. For `i=0`, `answer[0] = 1` (no elements to the left). Update `left_product` with `nums[i]`.
- **Line 12-14**: Backward pass multiplies `answer[i]` by `right_product` to include right products. Update `right_product` with `nums[i]`.

## Step-by-Step Example

For `nums = [1, 2, 3, 4]`:

1. Initialize:
   - `answer = [1, 1, 1, 1]`
   - `left_product = 1`, `right_product = 1`
2. Forward pass:
   - `i=0`: `answer[0] = 1`, `left_product = 1 * 1 = 1`
   - `i=1`: `answer[1] = 1`, `left_product = 1 * 2 = 2`
   - `i=2`: `answer[2] = 2`, `left_product = 2 * 3 = 6`
   - `i=3`: `answer[3] = 6`, `left_product = 6 * 4 = 24`
   - After: `answer = [1, 1, 2, 6]`
3. Backward pass:
   - `i=3`: `answer[3] = 6 * 1 = 6`, `right_product = 1 * 4 = 4`
   - `i=2`: `answer[2] = 2 * 4 = 8`, `right_product = 4 * 3 = 12`
   - `i=1`: `answer[1] = 1 * 12 = 12`, `right_product = 12 * 2 = 24`
   - `i=0`: `answer[0] = 1 * 24 = 24`, `right_product = 24 * 1 = 24`
   - After: `answer = [24, 12, 8, 6]`
4. Return: `[24, 12, 8, 6]`

## Time and Space Complexity

- **Time Complexity**: O(n)
  - Forward pass: O(n) to compute left products.
  - Backward pass: O(n) to compute right products and final answer.
  - Total: O(n).
- **Space Complexity**: O(1) (excluding output array)
  - Only uses `answer` array and two variables (`left_product`, `right_product`).
  - No additional arrays are needed.

## Key Takeaways

- Computing left and right products is a powerful technique for array problems.
- Reusing the output array for intermediate results optimizes space to O(1).
- The two-pass approach avoids division and handles edge cases (e.g., zeros) seamlessly.
- This pattern is useful for problems involving prefix/suffix computations.

## Related Problems

- **Maximum Subarray** (Week 1): Tracks max sum instead of product across array.
- **Subarray Sum Equals K** (Week 1): Uses prefix sums, similar to prefix products.
- **Maximum Product Subarray** (Week 2): Computes max product over subarrays.
