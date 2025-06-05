# main.py
from collections import defaultdict

def can_finish_courses(num_courses: int, prerequisites: list[list[int]]) -> bool:
    """
    Determines if it's possible to finish all courses given prerequisites.
    Uses DFS to detect cycles in a directed graph.
    
    Args:
        num_courses: Number of courses (0 to num_courses-1).
        prerequisites: List of [course, prerequisite] pairs.
    
    Returns:
        bool: True if all courses can be completed, False if there's a cycle.
    """
    # Handle edge case: no prerequisites means all courses can be taken
    if not prerequisites:
        return True
    
    # Build adjacency list: graph[prereq] -> list of courses requiring prereq
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    # Track fully processed courses
    visited = set()
    # Track courses in current DFS path for cycle detection
    current_path = set()
    
    def dfs(current_course: int) -> bool:
        """
        Recursive DFS to check if a course can be completed without cycles.
        
        Args:
            current_course: The course being processed.
        
        Returns:
            bool: True if no cycle is detected, False otherwise.
        """
        # Main Hoon: Define the current subproblem
        # We're checking if current_course can be completed without a cycle
        
        # Kya Karoon: Base cases and preprocessing
        # Base Case 1: If course is already visited, no cycle in its subtree
        if current_course in visited:
            return True
        # Base Case 2: If course is in current path, cycle detected
        if current_course in current_path:
            return False
        # Preprocessing: Add course to current path
        current_path.add(current_course)
        
        # Bacho Jao: Explore all dependent courses (children)
        for next_course in graph[current_course]:
            # Recursively check if next_course can be completed
            # If any recursive call returns False, a cycle exists
            if not dfs(next_course):
                return False
        
        # Kya Laya: Combine results from children
        # If we reach here, no cycle was found in any subtree
        
        # Ye Lo: Finalize answer, clean up, and return
        # Mark course as fully processed
        visited.add(current_course)
        # Remove course from current path (backtrack)
        current_path.remove(current_course)
        return True
    
    # Check all courses to handle disconnected components
    for course in range(num_courses):
        if not dfs(course):
            return False
    
    return True

# Test the function
if __name__ == "__main__":
    # Example: 5 courses, prerequisites mean course 1 requires 0, etc.
    test_num_courses = 5
    test_prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3]]
    result = can_finish_courses(test_num_courses, test_prerequisites)
    print(f"Can finish all courses: {result}")  # Should print True