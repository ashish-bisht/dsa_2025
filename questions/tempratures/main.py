# Problem: Daily Temperatures
# Difficulty: Medium
# LeetCode: https://leetcode.com/problems/daily-temperatures
# Description:
# Given an array of integers temperatures representing daily temperatures,
# return an array answer such that answer[i] is the number of days you have to
# wait after the ith day to get a warmer day. If there is no future day for
# which this is possible, keep answer[i] == 0 instead.

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # Initialize result array with zeros (default: no warmer day)
        length_array = len(temperatures)
        answer = [0] * length_array
        # Stack to store indices of days with increasing temperatures
        stack = []
        
        # Iterate through each day (index) in temperatures
        for current_idx in range(length_array):
            # While stack is not empty and current temperature is warmer than
            # the temperature at the index at the top of the stack
            while stack and temperatures[current_idx] > temperatures[stack[-1]]:
                # Pop the previous day's index from stack
                prev_idx = stack.pop()
                # Calculate days to wait: current_idx - prev_idx
                answer[prev_idx] = current_idx - prev_idx
            # Push current day's index onto stack
            stack.append(current_idx)
        
        return answer

# Test cases for local verification
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Example from problem
    test1 = [73, 74, 75, 71, 69, 72, 76, 73]
    expected1 = [1, 1, 4, 2, 1, 1, 0, 0]
    result1 = solution.dailyTemperatures(test1)
    print(f"Test 1: {result1} | Expected: {expected1} | Pass: {result1 == expected1}")
    
    # Test case 2: Monotonically decreasing temperatures
    test2 = [80, 79, 78, 77]
    expected2 = [0, 0, 0, 0]
    result2 = solution.dailyTemperatures(test2)
    print(f"Test 2: {result2} | Expected: {expected2} | Pass: {result2 == expected2}")
    
    # Test case 3: Single temperature
    test3 = [50]
    expected3 = [0]
    result3 = solution.dailyTemperatures(test3)
    print(f"Test 3: {result3} | Expected: {expected3} | Pass: {result3 == expected3}")