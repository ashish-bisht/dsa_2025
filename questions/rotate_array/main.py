# Problem: Rotate Array
# Difficulty: Medium
# LeetCode: https://leetcode.com/problems/rotate-array
# Description:
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# Example: nums = [1,2,3,4,5,6,7], k = 3 -> [5,6,7,1,2,3,4]
# Constraints:
# - 1 <= nums.length <= 10^5
# - -2^31 <= nums[i] <= 2^31 - 1
# - 0 <= k <= 10^5

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Rotates the array nums to the right by k steps in-place.
        Do not return anything, modify nums in-place instead.
        """
        # Handle edge cases
        if not nums or k == 0:
            return
        
        n = len(nums)
        # Normalize k to avoid unnecessary rotations (k > n)
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

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    print(f"Original: {nums1}, k={k1}")
    solution.rotate(nums1, k1)
    print(f"Rotated: {nums1}")  # Expected: [5, 6, 7, 1, 2, 3, 4]
    
    # Test case 2
    nums2 = [-1, -100, 3, 99]
    k2 = 2
    print(f"Original: {nums2}, k={k2}")
    solution.rotate(nums2, k2)
    print(f"Rotated: {nums2}")  # Expected: [3, 99, -1, -100]
    
    # Test case 3
    nums3 = [1]
    k3 = 0
    print(f"Original: {nums3}, k={k3}")
    solution.rotate(nums3, k3)
    print(f"Rotated: {nums3}")  # Expected: [1]