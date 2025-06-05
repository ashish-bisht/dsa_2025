class Node:
    def __init__(self, name):
        self.left = None
        self.right = None
        self.name = name



# create tree

root = Node("A")

root.left = Node("B")
root.left.left = Node("D")
root.left.right = Node("E")
root.left.left.left = Node("H")
root.left.left.right = Node("I")

root.right = Node("C")
root.right.left = Node("F")
root.right.right = Node("G")


def get_lowest_common_manager(top_manager, report_one, report_two):

    if not top_manager:
        return 
    
    if top_manager.name == report_one or top_manager.name == report_two:
        return top_manager
    
    left = get_lowest_common_manager(top_manager.left, report_one, report_two)
    right = get_lowest_common_manager(top_manager.right, report_one, report_two)

    if not left:
        return right
    
    if not right: 
        return left
    
    print(top_manager.name)
    return top_manager


print(get_lowest_common_manager(root, "E", "I"))