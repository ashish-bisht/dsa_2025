from collections import defaultdict

def find_course_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    """
    Returns the order in which courses should be taken to satisfy all prerequisites.
    Uses DFS to perform topological sort and detect cycles in a directed graph.
    
    Args:
        num_courses: Number of courses (0 to num_courses-1).
        prerequisites: List of [course, prerequisite] pairs.
    
    Returns:
        list[int]: A valid order of courses, or [] if a cycle exists.
    """
    # Build adjacency list: graph[prereq] -> list of courses requiring prereq
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    # Track fully processed courses
    visited = set()
    # Track courses in current DFS path for cycle detection
    current_path = set()
    # Store topological order
    course_order = []
    
    def dfs(current_course: int) -> bool:
        """
        Recursive DFS to check if a course can be included in the topological order.
        
        Args:
            current_course: The course being processed (integer, 0 to num_courses-1).
        
        Returns:
            bool: True if no cycle is detected, False if a cycle exists.
        """
        # Step 1: Main Hoon (Who Am I?)
        # Current subproblem: Check if current_course can be added without a cycle
        print(f"Processing course: {current_course}")
        
        # Step 2: Kya Karoon (Check and Do?)
        # Base Case 1: If course is already visited, skip (already in order)
        if current_course in visited:
            print(f"  Base case: Course {current_course} already visited, returning True")
            return True
        # Base Case 2: If course is in current path, cycle detected
        if current_course in current_path:
            print(f"  Base case: Cycle detected at course {current_course}, returning False")
            return False
        # Preprocessing: Add course to current path for cycle detection
        print(f"  Adding course {current_course} to current_path")
        current_path.add(current_course)
        
        # Step 3: Bacho Jao (Send Kids!)
        # Explore all dependent courses
        print(f"  Exploring dependents of course {current_course}: {graph[current_course]}")
        for next_course in graph[current_course]:
            # Recursively check if next_course can be added
            if not dfs(next_course):
                print(f"  Cycle found in subtree of course {next_course}, returning False")
                return False
        
        # Step 4: Kya Laya (What Did Kids Bring?)
        # If we reach here, no cycle was found in any subtree
        print(f"  No cycles found for course {current_course}")
        
        # Step 5: Ye Lo (Here’s the Answer!)
        # Mark course as visited AFTER recursion to confirm subtree is cycle-free
        # Reason: In topological sort, a course is only fully processed after
        # all its dependencies are processed and added to the order.
        print(f"  Marking course {current_course} as visited")
        visited.add(current_course)
        # Remove course from current path (backtrack)
        print(f"  Removing course {current_course} from current_path")
        current_path.remove(current_course)
        # Add course to topological order (post-order)
        print(f"  Adding course {current_course} to course_order")
        course_order.append(current_course)
        
        return True
    
    # Check all courses to handle disconnected components
    print(f"Starting DFS for {num_courses} courses")
    for course in range(num_courses):
        print(f"Checking course {course}")
        if not dfs(course):
            print("Cycle detected, returning []")
            return []
    
    # Reverse the order to ensure prerequisites come before dependent courses
    print(f"Final course order (before reverse): {course_order}")
    return course_order[::-1]