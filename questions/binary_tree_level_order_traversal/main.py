# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        que = deque([root])

        res = []
        count = 0
        while que:
            cur_level_length = len(que)

            cur_level = []

            for _ in range(cur_level_length):
                cur_node = que.popleft()
                cur_level.append(cur_node.val)

                if cur_node.left:
                    que.append(cur_node.left)

                if cur_node.right:
                    que.append(cur_node.right)
            res.append(cur_level[-1])

        return res
                