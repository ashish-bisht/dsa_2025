from collections import deque

def binary_tree_level_order(root):
    que = deque([root])
    res = []

    while que:
        cur_level_length = len(que)

        cur_level_res = []

        for _ in range(len(cur_level_length)):
            cur_node = que.popleft()
            cur_level_res.append(cur_node.val)

            if cur_node.left:
                que.append(cur_node.left)

            if cur_node.right:
                que.append(cur_node.right)

        res.append(cur_level_res[-1])
            

        
        
