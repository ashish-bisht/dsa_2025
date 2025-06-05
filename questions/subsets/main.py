# main.py

from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    """
    Generates all possible subsets (power set) of the given array of unique integers.
    
    Args:
        nums: List of distinct integers.
    
    Returns:
        List of lists containing all possible subsets.
    
    Example:
        Input: nums = [1, 2, 3]
        Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    """
    # Handle empty input
    if not nums:
        return [[]]
    
    result = []  # Stores all subsets
    
    def backtrack(current_index: int, current_combination: List[int]) -> None:
        """
        Recursively generates subsets using backtracking.
        
        Args:
            current_index: Current index in nums to process.
            current_combination: Current subset being built.
        """
        # Step 1: Main Hoon (Who Am I?)
        # We are at current_index, building current_combination.
        
        # Step 2: Kya Karoon (Check and Do?)
        # Add current_combination to result (valid subset at this point)
        result.append(current_combination[:])  # Copy to avoid mutation
        
        # Step 3: Bacho Jao (Send Kids!)
        # Try including each element from current_index onward
        for index in range(current_index, len(nums)):
            # Include nums[index] and recurse
            backtrack(index + 1, current_combination + [nums[index]])
        
        # Step 4: Kya Laya (What Did Kids Bring?)
        # Kids update result globally; no need to combine results here.
        
        # Step 5: Ye Lo (Here's the Answer!)
        # Result is updated; no return needed for this helper.
    
    # Start backtracking from index 0 with empty combination
    backtrack(0, [])
    
    return result

# Test the function
if __name__ == "__main__":
    test_nums = [1, 2, 3]
    print(subsets(test_nums))