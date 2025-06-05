# Problem: 3Sum
# Difficulty: Medium
# LeetCode: https://leetcode.com/problems/3sum
# Description:
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
# i != j, i != k, j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Initialize result list to store valid triplets
        result = []
        # Sort the array to make it easier to avoid duplicates and use two-pointer technique
        nums.sort()
        n = len(nums)
        
        # Iterate through the array, fixing the first number
        for i in range(n - 2):
            # Skip duplicates for the first number to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Use two pointers for the remaining numbers
            left = i + 1
            right = n - 1
            
            while left < right:
                # Calculate the sum of the triplet
                curr_sum = nums[i] + nums[left] + nums[right]
                
                if curr_sum == 0:
                    # Found a valid triplet, add to result
                    result.append([nums[i], nums[left], nums[right]])
                    # Move left pointer and skip duplicates
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Move right pointer and skip duplicates
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif curr_sum < 0:
                    # Sum is too small, move left pointer to increase sum
                    left += 1
                else:
                    # Sum is too large, move right pointer to decrease sum
                    right -= 1
        
        return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    print("Test 1:", solution.threeSum(nums1))  # Expected: [[-1,-1,2], [-1,0,1]]
    
    # Test case 2
    nums2 = [0, 1, 1]
    print("Test 2:", solution.threeSum(nums2))  # Expected: []
    
    # Test case 3
    nums3 = [0, 0, 0]
    print("Test 3:", solution.threeSum(nums3))  # Expected: [[0,0,0]]
    
    # Test case 4
    nums4 = [-2, 0, 1, 1, 2]
    print("Test 4:", solution.threeSum(nums4))  # Expected: [[-2,0,2], [-2,1,1]]