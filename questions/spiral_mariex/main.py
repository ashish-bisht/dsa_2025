# Spiral Matrix
# Difficulty: Medium
# LeetCode Link: https://leetcode.com/problems/spiral-matrix
# Description:
# Given an m x n matrix, return all elements of the matrix in spiral order (clockwise).
# Example:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Handle empty matrix case
        if not matrix or not matrix[0]:
            return []
        
        # Initialize result list to store spiral order
        result = []
        
        # Get dimensions of the matrix
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Define boundaries for traversal
        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1
        
        # Traverse matrix in spiral order until boundaries cross
        while top <= bottom and left <= right:
            # Traverse right (top row, from left to right)
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1  # Move top boundary down
            
            # Traverse down (right column, from top to bottom)
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1  # Move right boundary left
            
            # Check if there are more rows to process
            if top <= bottom:
                # Traverse left (bottom row, from right to left)
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1  # Move bottom boundary up
            
            # Check if there are more columns to process
            if left <= right:
                # Traverse up (left column, from bottom to top)
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1  # Move left boundary right
        
        return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: 3x3 matrix
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Test case 1:", solution.spiralOrder(matrix1))  # Expected: [1, 2, 3, 6, 9, 8, 7, 4, 5]
    
    # Test case 2: 3x4 matrix
    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print("Test case 2:", solution.spiralOrder(matrix2))  # Expected: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    
    # Test case 3: Empty matrix
    matrix3 = []
    print("Test case 3:", solution.spiralOrder(matrix3))  # Expected: []
    
    # Test case 4: 1x1 matrix
    matrix4 = [[7]]
    print("Test case 4:", solution.spiralOrder(matrix4))  # Expected: [7]