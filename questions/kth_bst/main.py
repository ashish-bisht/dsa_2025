# main.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Shared state to track progress
        count = 0  # Number of nodes processed in inorder traversal
        result = 0  # Value of the kth smallest node

        def dfs(current_node: Optional[TreeNode]) -> None:
            nonlocal count, result  # Access shared state
            
            # Step 1: Main Hoon (Who Am I?)
            # Subproblem: Process the subtree rooted at current_node to find the kth smallest element
            # State: current_node (current subtree), count (nodes processed), result (kth value)
            
            # Step 2: Kya Karoon (Check and Do?)
            # Base Case: If current_node is None, return (empty subtree)
            if not current_node:
                return
            
            # Limits: If result is already set, skip further processing
            if result != 0:
                return
            
            # Process left subtree (smaller values first)
            # Step 3: Bacho Jao (Send Kids!)
            dfs(current_node.left)
            
            # Process current node (inorder: left, root, right)
            # Increment count and check if this is the kth node
            count += 1
            if count == k:
                result = current_node.val
                return  # Early termination: kth node found
            
            # Process right subtree (larger values)
            dfs(current_node.right)
            
            # Step 4: Kya Laya (What Did Kids Bring?)
            # Left subtree processed smaller nodes, current node incremented count,
            # right subtree processes larger nodes if needed.
            
            # Step 5: Ye Lo (Here's the Answer!)
            # Result is updated when count == k; no return value needed for dfs
        
        # Initiate recursion
        dfs(root)
        
        # Return the kth smallest value
        return result