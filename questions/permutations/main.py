from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    # Handle empty input
    if not nums:
        return []
    
    # Initialize result to store all permutations
    result = []
    
    def backtrack(cur_path: List[int], cur_nums: List[int]) -> None:
        # Step 1: Main Hoon (Who Am I?)
        # I'm building a permutation in cur_path, with cur_nums available to choose from.
        
        # Step 2: Kya Karoon (Check and Do?)
        # Base Case: If no numbers remain, permutation is complete
        if not cur_nums:
            result.append(cur_path[:])  # Append a copy
            return
        
        # Step 3: Bacho Jao (Send Kids!)
        # Try each remaining number
        for idx in range(len(cur_nums)):
            num = cur_nums[idx]
            # Remove num from cur_nums and add to cur_path
            next_nums = cur_nums[:idx] + cur_nums[idx+1:]
            cur_path.append(num)
            backtrack(cur_path, next_nums)  # Recurse
            cur_path.pop()  # Backtrack: undo choice
        
        # Step 4: Kya Laya (What Did Kids Bring?)
        # Kids append valid permutations to result in base case; nothing to combine.
        
        # Step 5: Ye Lo (Here's the Answer!)
        # All permutations are in result after recursion completes.
    
    # Start backtracking with empty path and all numbers
    backtrack([], nums)
    return result

# Test the function
if __name__ == "__main__":
    print(permute([1, 2, 3]))  # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]