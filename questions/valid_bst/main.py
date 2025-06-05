# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(current_node: TreeNode, min_val: float, max_val: float) -> bool:
            # Main Hoon: I am the current node, ensuring my subtree is a valid BST
            # with values strictly between min_val and max_val.
            
            # Kya Karoon: Base Case - if node is None, it’s a valid BST.
            if not current_node:
                return True
            
            # Preprocessing: Check if current node's value is within (min_val, max_val).
            if current_node.val <= min_val or current_node.val >= max_val:
                return False
            
            # Limits: No additional pruning needed beyond range check.
            
            # Bacho Jao: Validate left subtree with upper bound as current value,
            # and right subtree-que with lower bound as current value.
            left_is_valid = validate(current_node.left, min_val, current_node.val)
            right_is_valid = validate(current_node.right, current_node.val, max_val)
            
            # Kya Laya: Subtree is valid only if both left and right subtrees are valid.
            is_valid = left_is_valid and right_is_valid
            
            # Ye Lo: Return whether this subtree is a valid BST.
            return is_valid
        
        # Start validation with infinite bounds to handle all integer values
        return validate(root, float('-inf'), float('inf'))