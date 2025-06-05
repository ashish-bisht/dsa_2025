# Problem: 3Sum Closest
# Difficulty: Medium
# LeetCode: https://leetcode.com/problems/3sum-closest
# Description:
# Given an integer array nums of length n and an integer target, find three integers
# in nums such that their sum is closest to target. Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # Sort the array to make two-pointer technique easier
        nums.sort()
        length_array = len(nums)
        # Initialize closest_sum to a large value
        closest_sum = float('inf')
        
        # Iterate through each element as the first number
        for idx in range(length_array - 2):
            # Use two pointers: left starts after idx, right at the end
            left = idx + 1
            right = length_array - 1
            
            while left < right:
                # Calculate the current sum of three numbers
                current_sum = nums[idx] + nums[left] + nums[right]
                
                # If current_sum equals target, return it immediately
                if current_sum == target:
                    return current_sum
                
                # Update closest_sum if current_sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on comparison with target
                if current_sum < target:
                    left += 1  # Need a larger sum, move left pointer right
                else:
                    right -= 1  # Need a smaller sum, move right pointer left
        
        return closest_sum

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: nums = [-1,2,1,-4], target = 1
    assert solution.threeSumClosest([-1, 2, 1, -4], 1) == 2  # [-1, 1, 2] sums to 2
    
    # Test case 2: nums = [0,0,0], target = 1
    assert solution.threeSumClosest([0, 0, 0], 1) == 0  # [0, 0, 0] sums to 0
    
    # Test case 3: nums = [1,1,1,0], target = -100
    assert solution.threeSumClosest([1, 1, 1, 0], -100) == 3  # [1, 1, 1] sums to 3
    
    print("All test cases passed!")