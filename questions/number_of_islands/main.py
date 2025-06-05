# main.py
from typing import List

def number_of_islands(grid: List[List[str]]) -> int:
    """
    Counts the number of islands in a 2D grid, where an island is a group of '1's
    connected vertically or horizontally. Uses DFS to mark and explore each island.

    Args:
        grid: List[List[str]], a 2D grid of '1' (land) and '0' (water).

    Returns:
        int: The number of islands.
    """
    # Handle empty grid edge case
    if not grid or not grid[0]:
        return 0
    
    # Initialize variables
    island_count = 0
    row_count = len(grid)
    col_count = len(grid[0])
    
    def explore_island(row: int, col: int) -> None:
        """
        DFS to explore and mark all cells of an island starting at (row, col).
        Follows the recursive framework: Main Hoon, Kya Karoon, Bacho Jao, Kya Laya, Ye Lo!
        """
        # Step 1: Main Hoon (Who Am I?)
        # Current subproblem: Explore the cell at (row, col) and its connected land cells.
        # State: (row, col) coordinates and the grid.
        
        # Step 2: Kya Karoon (Check and Do?)
        # Base Case (Failure): Stop if out of bounds or not a land cell.
        if (row < 0 or row >= row_count or
            col < 0 or col >= col_count or
            grid[row][col] != "1"):
            return
        
        # Preprocessing: Mark current cell as visited by setting it to '0'.
        grid[row][col] = "0"
        
        # Step 3: Bacho Jao (Send Kids!)
        # Explore all four adjacent cells (up, right, down, left).
        explore_island(row - 1, col)  # Up
        explore_island(row, col + 1)  # Right
        explore_island(row + 1, col)  # Down
        explore_island(row, col - 1)  # Left
        
        # Step 4: Kya Laya (What Did Kids Bring?)
        # No results to combine, as DFS modifies the grid in-place.
        
        # Step 5: Ye Lo (Here’s the Answer!)
        # The island is fully explored; no return value needed.
    
    # Iterate over each cell in the grid
    for row in range(row_count):
        for col in range(col_count):
            if grid[row][col] == "1":
                # Found a new island; increment count and explore it
                island_count += 1
                explore_island(row, col)
    
    return island_count

# Test the function
if __name__ == "__main__":
    test_grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    result = number_of_islands(test_grid)
    print(f"Number of islands: {result}")  # Expected output: 3