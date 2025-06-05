# 01 Matrix
# Difficulty: Medium
# Link: https://leetcode.com/problems/01-matrix/
# Description:
# Given an m x n binary matrix mat of 0s and 1s, return a matrix of the same size
# where each cell contains the distance to the nearest 0 in the original matrix.
# Distance is measured as the number of steps (up, down, left, right) to reach a 0.
#
# Example:
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]

from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Get matrix dimensions
        rows = len(mat)
        cols = len(mat[0])
        
        # Initialize result matrix with large values (infinity-like)
        # This will store the distance to the nearest 0 for each cell
        dist = [[float('inf')] * cols for _ in range(rows)]
        
        # Initialize queue for BFS
        # Start with all cells containing 0
        queue = deque()
        
        # Step 1: Add all 0 cells to queue and set their distance to 0
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    dist[row][col] = 0
                    queue.append((row, col))
        
        # Step 2: BFS to find shortest distance to 0 for each cell
        # Define four directions: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        while queue:
            # Get current cell's coordinates
            curr_row, curr_col = queue.popleft()
            
            # Check all four neighboring cells
            for delta_row, delta_col in directions:
                new_row = curr_row + delta_row
                new_col = curr_col + delta_col
                
                # Check if the new position is within bounds
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    # If we can reach this neighbor in a shorter distance
                    # (current cell's distance + 1), update it
                    if dist[new_row][new_col] > dist[curr_row][curr_col] + 1:
                        dist[new_row][new_col] = dist[curr_row][curr_col] + 1
                        queue.append((new_row, new_col))
        
        return dist


# Test cases for local verification
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    mat1 = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    result1 = solution.updateMatrix(mat1)
    print("Test case 1:")
    for row in result1:
        print(row)
    # Expected output: [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
    
    # Test case 2
    mat2 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    result2 = solution.updateMatrix(mat2)
    print("\nTest case 2:")
    for row in result2:
        print(row)
    # Expected output: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]