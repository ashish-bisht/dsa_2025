from collections import deque

def binary_tree_zig_zag(root):
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

        if count % 2 == 0:
            res.append(cur_level)
        else:
            res.append(cur_level[::-1])

    return res
            
