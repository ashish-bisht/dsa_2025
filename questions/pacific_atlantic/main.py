from typing import List, Tuple, Set

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Get matrix dimensions
        rows, cols = len(heights), len(heights[0])
        # Sets to store cells reachable from each ocean
        pacific_reachable: Set[Tuple[int, int]] = set()
        atlantic_reachable: Set[Tuple[int, int]] = set()

        def dfs(row: int, col: int, prev_height: int, visited: Set[Tuple[int, int]]) -> None:
            """
            Recursive DFS to mark cells reachable from the current ocean.
            Args:
                row: Current row index
                col: Current column index
                prev_height: Height of the previous cell (for reverse flow)
                visited: Set of cells reachable from the current ocean
            """
            # Main Hoon: Define the subproblem
            current_height = heights[row][col] if 0 <= row < rows and 0 <= col < cols else 'out'
            print(f"DFS at cell ({row}, {col}), prev_height={prev_height}, current_height={current_height}, visited={visited}")

            # Kya Karoon: Base cases and preprocessing
            # Base Case 1: Out of bounds
            if row < 0 or row >= rows or col < 0 or col >= cols:
                print(f"  -> Out of bounds, returning")
                return
            # Base Case 2: Already visited
            if (row, col) in visited:
                print(f"  -> Already visited, returning")
                return
            # Base Case 3: Height constraint (reverse flow: current height >= prev_height)
            if heights[row][col] < prev_height:
                print(f"  -> Height {heights[row][col]} < prev_height {prev_height}, returning")
                return

            # Preprocessing: Mark current cell as reachable
            visited.add((row, col))
            print(f"  -> Added ({row}, {col}) to visited")

            # Bacho Jao: Explore adjacent cells in order: up, right, down, left
            print(f"  -> Exploring up: ({row-1}, {col})")
            dfs(row - 1, col, heights[row][col], visited)  # Up
            print(f"  -> Exploring right: ({row}, {col+1})")
            dfs(row, col + 1, heights[row][col], visited)  # Right
            print(f"  -> Exploring down: ({row+1}, {col})")
            dfs(row + 1, col, heights[row][col], visited)  # Down
            print(f"  -> Exploring left: ({row}, {col-1})")
            dfs(row, col - 1, heights[row][col], visited)  # Left

            # Kya Laya: No return value (void), result is in visited set
            # Ye Lo: No memoization needed (visited set prevents reprocessing)

        # Start DFS from Pacific boundaries (top edge: row=0, left edge: col=0)
        print("Starting DFS for Pacific Ocean")
        for col in range(cols):
            print(f"\nStarting from top edge: (0, {col})")
            dfs(0, col, float('-inf'), pacific_reachable)  # Top edge
        for row in range(rows):
            print(f"\nStarting from left edge: ({row}, 0)")
            dfs(row, 0, float('-inf'), pacific_reachable)  # Left edge

        # Start DFS from Atlantic boundaries (bottom edge: row=rows-1, right edge: col=cols-1)
        print("\nStarting DFS for Atlantic Ocean")
        for col in range(cols):
            print(f"\nStarting from bottom edge: ({rows-1}, {col})")
            dfs(rows - 1, col, float('-inf'), atlantic_reachable)  # Bottom edge
        for row in range(rows):
            print(f"\nStarting from right edge: ({row}, {cols-1})")
            dfs(row, cols - 1, float('-inf'), atlantic_reachable)  # Right edge

        # Find cells reachable from both oceans (intersection of sets)
        result = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific_reachable and (row, col) in atlantic_reachable:
                    result.append([row, col])

        print(f"\nFinal result: {result}")
        return result