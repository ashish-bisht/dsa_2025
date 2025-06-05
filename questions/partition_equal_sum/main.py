# main.py
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Calculate total sum of the array
        total_sum = sum(nums)
        
        # If total sum is odd, equal partition is impossible
        if total_sum % 2 != 0:
            return False
        
        # Target sum for each subset
        target_sum = total_sum // 2
        
        # Memoization dictionary to store computed states
        memo = {}
        
        def can_partition(current_index: int, remaining_sum: int) -> bool:
            """
            Recursive function to determine if a subset summing to remaining_sum
            can be formed using nums[current_index:].
            
            Args:
                current_index: Current position in nums
                remaining_sum: Remaining sum to achieve
            
            Returns:
                bool: True if such a subset exists, False otherwise
            """
            # Main Hoon: Define the subproblem state
            state = (current_index, remaining_sum)
            
            # Kya Karoon: Base cases
            if remaining_sum == 0:
                print(f"State (index={current_index}, sum={remaining_sum}): True (Base case: sum reached)")
                return True
            if current_index == len(nums):
                print(f"State (index={current_index}, sum={remaining_sum}): False (Base case: out of numbers)")
                return False
            if remaining_sum < 0:
                print(f"State (index={current_index}, sum={remaining_sum}): False (Base case: negative sum)")
                return False
            
            # Check memoization
            if state in memo:
                print(f"State (index={current_index}, sum={remaining_sum}): {memo[state]} (Memoized)")
                return memo[state]
            
            # Bacho Jao: Lun Na Lun (Take or Don't Take)
            include = False
            if nums[current_index] <= remaining_sum:
                # Lun: Take current number
                include = can_partition(current_index + 1, remaining_sum - nums[current_index])
            
            # Na Lun: Skip current number
            exclude = can_partition(current_index + 1, remaining_sum)
            
            # Kya Laya: Combine results
            result = include or exclude
            
            # Ye Lo: Memoize and print state
            memo[state] = result
            print(f"State (index={current_index}, sum={remaining_sum}): {result}")
            
            return result
        
        # Start recursion from index 0 with target sum
        return can_partition(0, target_sum)

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 5, 11, 5]
    result = solution.canPartition(nums)
    print(f"Can partition {nums} into equal subsets: {result}")