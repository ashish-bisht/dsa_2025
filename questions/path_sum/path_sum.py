from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # Initialize result list to store all valid paths
        result = []
        
        def dfs(current_node: Optional[TreeNode], current_sum: int, current_path: List[int]) -> None:
            # Step 1: Main Hoon (Who Am I?)
            # - current_node: Current node in the tree (or None if past a leaf)
            # - current_sum: Sum of node values from root to current node
            # - current_path: List of node values in the current path
            # - Subproblem: Find all paths from current_node to a leaf where total sum equals targetSum
            
            # Step 2: Kya Karoon (Check and Do?)
            # Base Case 1: If node is None, no path to explore, return
            if not current_node:
                return
            
            # Update current_sum and current_path with current node's value
            current_sum += current_node.val
            current_path.append(current_node.val)
            
            # Base Case 2: If at a leaf node and sum equals targetSum
            if not current_node.left and not current_node.right and current_sum == targetSum:
                # Append a copy of current_path to avoid mutation
                result.append(current_path[:])  # No return needed; None children handle termination
            
            # Step 3: Bacho Jao (Send Kids!)
            # Recursively explore left and right children, passing a copy of current_path
            dfs(current_node.left, current_sum, current_path[:])
            dfs(current_node.right, current_sum, current_path[:])
            
            # Step 4: Kya Laya (What Did Kids Bring?)
            # - Kids modify result list directly when they find valid paths
            # - No need to combine results here, as base case handles appending
            
            # Step 5: Ye Lo (Here's the Answer!)
            # - No return value needed; result is built in place
            # - Backtracking is implicit via path copies
            
        # Initial call: Start from root with sum 0 and empty path
        dfs(root, 0, [])
        
        # Return the collected paths
        return result