# Container With Most Water
# Difficulty: Medium
# LeetCode Link: https://leetcode.com/problems/container-with-most-water
# Description: Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
# Two vertical lines are drawn at points (i, ai) and (j, aj). Find two lines that together with the x-axis form
# a container, such that the container contains the most water. Return the maximum area of water the container can store.
# Note: You may not slant the container.

class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Initialize two pointers: left at start, right at end
        left = 0
        right = len(height) - 1
        max_area = 0

        # Continue until pointers meet
        while left < right:
            # Calculate area: min height * width
            current_area = min(height[left], height[right]) * (right - left)
            # Update max_area if current_area is larger
            max_area = max(max_area, current_area)

            # Move the pointer at the shorter height to find a potentially larger area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Example from LeetCode
    assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49, "Test case 1 failed"
    
    # Test case 2: Two bars
    assert solution.maxArea([1, 1]) == 1, "Test case 2 failed"
    
    # Test case 3: Increasing heights
    assert solution.maxArea([1, 2, 3, 4, 5]) == 6, "Test case 3 failed"
    
    # Test case 4: Same heights
    assert solution.maxArea([2, 2, 2, 2]) == 6, "Test case 4 failed"
    
    print("All test cases passed!")