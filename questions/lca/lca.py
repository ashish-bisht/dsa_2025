# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(current_node: 'TreeNode', target_p: 'TreeNode', target_q: 'TreeNode') -> 'TreeNode':
            # Step 1: Main Hoon (Who Am I?)
            # I am at current_node, tasked with finding the LCA of target_p and target_q.
            # My subproblem: Determine if current_node is the LCA or find the LCA in my subtrees.
            # Return: A TreeNode (LCA, target_p, target_q, or None if neither found).

            # Step 2: Kya Karoon (Check and Do?)
            # Base Case 1: If current_node is None, no LCA or targets here, return None.
            if not current_node:
                return None

            # Base Case 2: If current_node is target_p or target_q, return current_node.
            # This handles cases where we find one of the target nodes.
            if current_node.val == target_p.val or current_node.val == target_q.val:
                return current_node

            # Step 3: Bacho Jao (Send Kids!)
            # Recursively search left and right subtrees for target_p, target_q, or LCA.
            left_result = dfs(current_node.left, target_p, target_q)
            right_result = dfs(current_node.right, target_p, target_q)

            # Step 4: Kya Laya (What Did Kids Bring?)
            # Combine results from left and right subtrees:
            # - If both left_result and right_result are non-None, we found target_p in one subtree
            #   and target_q in the other, so current_node is the LCA.
            if left_result and right_result:
                return current_node

            # - If only one is non-None, return that result (could be target_p, target_q, or an LCA).
            # - If both are None, return None (neither target was found).
            return left_result if left_result else right_result

            # Step 5: Ye Lo (Here’s the Answer!)
            # The return statement above handles this. No memoization needed, as the tree has
            # no overlapping subproblems.

        # Initiate recursion from the root and return the LCA.
        return dfs(root, p, q)