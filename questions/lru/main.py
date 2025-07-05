class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.leaf = Node()

        self.head.next = self.leaf
        self.leaf.prev = self.head


    def add_node(self, node):
        self.node.prev = 
