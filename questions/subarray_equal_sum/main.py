# Subarray Sum Equals K
# Difficulty: Medium
# LeetCode Link: https://leetcode.com/problems/subarray-sum-equals-k
# Description: Given an array of integers `nums` and an integer `k`, return the total number of
# continuous subarrays whose sum equals `k`. A subarray is a contiguous part of the array.
# Example: nums = [1, 1, 1], k = 2 -> Output: 2 (subarrays [1, 1] at indices [0,1] and [1,2])
# Constraints: 
# - Array length is 1 to 2 * 10^4
# - Elements and k can be negative, positive, or zero
# - -10^7 <= nums[i], k <= 10^7

from typing import List  # Import List for type hinting
from collections import defaultdict  # Import defaultdict for hash map with default value 0

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Initialize a hash map to store cumulative sum frequencies
        # Key: cumulative sum up to an index, Value: how many times this sum has occurred
        # Using defaultdict(int) to return 0 for non-existent keys
        sum_freq = defaultdict(int)
        
        # Initialize the frequency of cumulative sum 0 to 1
        # This handles subarrays starting from index 0 that sum to k
        # Example: If cumulative sum at index j is k, we need sum_freq[0] to count it
        sum_freq[0] = 1
        
        # Initialize variable to track the running cumulative sum
        # Starts at 0 and will add each number as we iterate
        current_sum = 0
        
        # Initialize counter for the number of subarrays with sum equal to k
        # This will be our final answer
        count = 0
        
        # Iterate through each number in the input array
        # Index is not needed, so we directly use the number
        for num in nums:
            # Add the current number to the cumulative sum
            # current_sum represents the sum from index 0 to the current index
            current_sum += num
            
            # Check if there exists a previous cumulative sum such that
            # current_sum - previous_sum = k
            # This means the subarray between the previous index and current index sums to k
            # We look for current_sum - k in sum_freq
            if current_sum - k in sum_freq:
                # If found, the frequency of current_sum - k tells us how many subarrays
                # ending at the current index have sum k
                # Add this frequency to our count
                count += sum_freq[current_sum - k]
            
            # Update the hash map with the current cumulative sum
            # Increment the frequency of current_sum by 1
            # This records that we've seen this cumulative sum at the current index
            # Future iterations will use this to find subarrays ending later
            sum_freq[current_sum] += 1
        
        # Return the total number of subarrays with sum k
        return count

# Test cases for local verification
# These verify the solution works for various scenarios
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()
    
    # Test case 1: Basic case with multiple subarrays
    # Input: nums = [1, 1, 1], k = 2
    # Expected: 2 (subarrays [1, 1] at indices [0,1] and [1,2])
    nums1 = [1, 1, 1]
    k1 = 2
    result1 = solution.subarraySum(nums1, k1)
    assert result1 == 2, f"Test case 1 failed: expected 2, got {result1}"
    
    # Test case 2: Array with negative numbers
    # Input: nums = [1, 2, -1, 1, 2], k = 3
    # Expected: 3 (subarrays [1, 2], [1, 2, -1, 1], [1, 2])
    nums2 = [1, 2, -1, 1, 2]
    k2 = 3
    result2 = solution.subarraySum(nums2, k2)
    assert result2 == 3, f"Test case 2 failed: expected 3, got {result2}"
    
    # Test case 3: No subarray sums to k
    # Input: nums = [1, 2, 3], k = 10
    # Expected: 0 (no subarray sums to 10)
    nums3 = [1, 2, 3]
    k3 = 10
    result3 = solution.subarraySum(nums3, k3)
    assert result3 == 0, f"Test case 3 failed: expected 0, got {result3}"
    
    # Test case 4: Single element equal to k
    # Input: nums = [5], k = 5
    # Expected: 1 (subarray [5])
    nums4 = [5]
    k4 = 5
    result4 = solution.subarraySum(nums4, k4)
    assert result4 == 1, f"Test case 4 failed: expected 1, got {result4}"
    
    # Print success message if all tests pass
    print("All test cases passed!")