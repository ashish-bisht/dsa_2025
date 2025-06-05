# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(current_node: 'Node') -> 'Node':
    # Initialize hash map to store original node -> cloned node mappings
    visited = {}
    
    def clone_dfs(current_node: 'Node') -> 'Node':
        # Step 1: Main Hoon (Who Am I?)
        # Current subproblem: Clone current_node and its neighbors
        # State: current_node (Node or None), visited (hash map)
        print(f"Processing node: {current_node.val if current_node else 'None'}")
        
        # Step 2: Kya Karoon (Check and Do?)
        # Base Case 1: If node is None, return None
        if not current_node:
            print("  Base case: Null node, returning None")
            return None
        
        # Base Case 2: If node already cloned, return its clone
        if current_node in visited:
            print(f"  Base case: Node {current_node.val} already cloned, returning clone")
            return visited[current_node]
        
        # Preprocessing: Create new node with same value, empty neighbors
        cloned_node = Node(current_node.val)
        print(f"  Created new node with val {cloned_node.val}")
        
        # Store in visited to mark as cloned
        visited[current_node] = cloned_node
        print(f"  Added node {current_node.val} to visited")
        
        # Step 3: Bacho Jao (Send Kids!)
        # For each neighbor, recursively clone it
        print(f"  Processing neighbors of node {current_node.val}: {[n.val for n in current_node.neighbors]}")
        for neighbor in current_node.neighbors:
            # Step 4: Kya Laya (What Did Kids Bring?)
            # Get cloned neighbor from recursive call
            cloned_neighbor = clone_dfs(neighbor)
            # Append cloned neighbor to cloned_node's neighbors
            cloned_node.neighbors.append(cloned_neighbor)
            print(f"    Added cloned neighbor {cloned_neighbor.val} to node {cloned_node.val}'s neighbors")
        
        # Step 5: Ye Lo (Here’s the Answer!)
        # Return the cloned node
        print(f"  Returning cloned node {cloned_node.val}")
        return cloned_node
    
    # Start recursion with the input node
    return clone_dfs(current_node)