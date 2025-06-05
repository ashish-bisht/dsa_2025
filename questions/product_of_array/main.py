# Problem: Product of Array Except Self
# Difficulty: Medium
# LeetCode: https://leetcode.com/problems/product-of-array-except-self
# Description:
# Given an integer array nums, return an array answer such that answer[i] is equal to the product
# of all the elements of nums except nums[i]. The product of any prefix or suffix of nums is
# guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and
# without using the division operation.

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        # Initialize answer array to store final result and intermediate products
        answer = [1] * n

        # Forward pass: answer[i] stores product of all elements to the left of i
        left_product = 1
        for i in range(n):
            answer[i] = left_product  # Store product of elements before i
            left_product *= nums[i]  # Update product for next index

        # Backward pass: Multiply answer[i] by product of all elements to the right of i
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product  # Multiply by right product
            right_product *= nums[i]  # Update product for next index

        return answer

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3, 4]
    print(f"Input: {nums1}")
    print(f"Output: {solution.productExceptSelf(nums1)}")  # Expected: [24, 12, 8, 6]
    
    # Test case 2
    nums2 = [-1, 1, 0, -3, 3]
    print(f"Input: {nums2}")
    print(f"Output: {solution.productExceptSelf(nums2)}")  # Expected: [0, 0, 9, 0, 0]
    
    # Test case 3
    nums3 = [2, 3, 4, 5]
    print(f"Input: {nums3}")
    print(f"Output: {solution.productExceptSelf(nums3)}")  # Expected: [60, 40, 30, 24]