from typing import List
import math

def longestIncreasingSubsequence(nums: List[int]) -> int:
    memo = {}
    
    def findLongestSubsequence(current_index: int, prev_value: float) -> int:
        # Step 1: Main Hoon (Who Am I?)
        # Subproblem: longest increasing subsequence from current_index with prev_value
        
        # Step 2: Kya Karoon (Check and Do?)
        # Base Case: No elements left
        if current_index >= len(nums):
            print(f"State (index={current_index}, prev_value={prev_value}): 0")
            return 0
        # Limits: Check memoization
        state = (current_index, prev_value)
        if state in memo:
            print(f"State (index={current_index}, prev_value={prev_value}): {memo[state]} (memoized)")
            return memo[state]
        
        # Step 3: Bacho Jao (Send Kids!)
        # Lun Na Lun Approach
        # Lun: Take current element (if possible)
        take_element = 0
        if nums[current_index] > prev_value:
            take_element = 1 + findLongestSubsequence(current_index + 1, nums[current_index])
        # Na Lun: Skip current element
        skip_element = findLongestSubsequence(current_index + 1, prev_value)
        
        # Step 4: Kya Laya (What Did Kids Bring?)
        # Maximum of take or skip
        max_length = max(take_element, skip_element)
        
        # Step 5: Ye Lo (Here’s the Answer!)
        # Memorize and return
        memo[state] = max_length
        print(f"State (index={current_index}, prev_value={prev_value}): {max_length}")
        return max_length
    
    # Start from index 0 with no previous value
    return findLongestSubsequence(0, float('-inf'))