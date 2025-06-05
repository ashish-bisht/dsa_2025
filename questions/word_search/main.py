# main.py

from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    # Handle edge cases for empty inputs
    if not word:
        return True
    if not board or not board[0]:
        return False
    
    def dfs(i: int, j: int, cur_index: int) -> bool:
        # Step 1: Main Hoon (Who Am I?)
        # I am at position (i, j) on the board, trying to match word[cur_index].
        # My subproblem is to check if word[cur_index:] can be formed from this position.
        
        # Step 2: Kya Karoon (Check and Do?)
        # Base Case (Success): If cur_index == len(word), all characters are matched.
        if cur_index == len(word):
            return True
        
        # Base Case (Failure): Check if current position is invalid.
        # - Out of bounds
        # - Cell is marked as visited ('#')
        # - Current cell doesn't match word[cur_index]
        if (
            i < 0 or i >= len(board) or
            j < 0 or j >= len(board[0]) or
            board[i][j] == '#' or
            board[i][j] != word[cur_index]
        ):
            return False
        
        # Preprocessing: Mark current cell as visited to avoid reuse
        tmp = board[i][j]
        board[i][j] = '#'
        
        # Step 3: Bacho Jao (Send Kids!)
        # Explore all four directions (up, down, left, right) for the next character.
        res = (
            dfs(i - 1, j, cur_index + 1) or  # Up
            dfs(i + 1, j, cur_index + 1) or  # Down
            dfs(i, j - 1, cur_index + 1) or  # Left
            dfs(i, j + 1, cur_index + 1)     # Right
        )
        
        # Step 4: Kya Laya (What Did Kids Bring?)
        # If any direction leads to a valid path, res will be True.
        
        # Step 5: Ye Lo (Here's the Answer!)
        # Restore the cell and return the result.
        board[i][j] = tmp
        return res
    
    # Iterate over each cell to start DFS if it matches word[0]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                if dfs(i, j, 0):
                    return True
    
    return False