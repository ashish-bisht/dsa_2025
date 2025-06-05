# main.py
# Problem: LeetCode 377 - Combination Sum IV
# Description: Given an array of distinct integers nums and a target integer target,
# return the number of possible permutations that sum to target, where order matters
# and numbers can be used unlimited times.
# Approach: Recursive with memoization, using a for-loop to try all numbers for each remaining sum.

from typing import List

def combinationSum4(nums: List[int], target: int) -> int:
    # Input validation: handle empty array
    if not nums:
        return 0
    
    # Memoization dictionary: stores remaining_sum -> number of permutations
    memo = {}
    
    def dp(remaining_sum: int) -> int:
        # Main Hoon: Define the subproblem
        # dp(remaining_sum) = number of permutations summing to remaining_sum using nums
        
        # Kya Karoon: Check base cases and memoization
        if remaining_sum == 0:
            # Base Case (Success): Found a valid permutation
            print(f"State (remaining_sum={remaining_sum}): 1")
            return 1
        if remaining_sum < 0:
            # Base Case (Failure): Overshot the target
            print(f"State (remaining_sum={remaining_sum}): 0")
            return 0
        if remaining_sum in memo:
            # Memoization: Return cached result
            print(f"State (remaining_sum={remaining_sum}): {memo[remaining_sum]} (memoized)")
            return memo[remaining_sum]
        
        # Bacho Jao: Generate subproblems
        # Try each number in nums to reduce remaining_sum
        total_permutations = 0
        for num in nums:
            if remaining_sum - num >= 0:
                total_permutations += dp(remaining_sum - num)
        
        # Kya Laya: Combine subproblem results
        # Sum of permutations from all valid subproblems
        
        # Ye Lo: Memoize and print state
        memo[remaining_sum] = total_permutations
        print(f"State (remaining_sum={remaining_sum}): {total_permutations}")
        return total_permutations
    
    # Start recursion with the full target
    result = dp(target)
    return result

# Test case
nums = [1, 2, 3]
target = 4
print(f"Input: nums={nums}, target={target}")
result = combinationSum4(nums, target)
print(f"Output: {result}")
print("Explanation:")
print("The possible combination ways are:")
combinations = [
    "(1, 1, 1, 1)",
    "(1, 1, 2)",
    "(1, 2, 1)",
    "(1, 3)",
    "(2, 1, 1)",
    "(2, 2)",
    "(3, 1)"
]
for combo in combinations:
    print(combo)