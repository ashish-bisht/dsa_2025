from typing import List

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    # Handle empty input
    if not candidates:
        return []
    
    # Initialize results to store all valid combinations
    combinations = []
    
    def backtrack(index: int, current_sum: int, current_combination: List[int]) -> None:
        # Step 1: Main Hoon (Who Am I?)
        # I'm at candidates[index], building a combination with current_sum.
        
        # Step 2: Kya Karoon (Check and Do?)
        # Base Case (Success): If current_sum equals target, add combination
        if current_sum == target:
            combinations.append(current_combination[:])  # Append a copy
            return
        
        # Base Case (Failure): If current_sum exceeds target, stop
        if current_sum > target:
            return
        
        # Step 3: Bacho Jao (Send Kids!)
        # Try each candidate from index onward, allowing reuse
        for i in range(index, len(candidates)):
            candidate = candidates[i]
            current_combination.append(candidate)  # Make choice
            # Recurse with same index (allow reuse) and updated sum
            backtrack(i, current_sum + candidate, current_combination)
            current_combination.pop()  # Backtrack by undoing choice
        
        # Step 4: Kya Laya (What Did Kids Bring?)
        # Kids append valid combinations to results in base case; nothing to combine here.
        
        # Step 5: Ye Lo (Here's the Answer!)
        # All valid combinations are in combinations after recursion completes.
    
    # Start recursion with index 0, sum 0, and empty combination
    backtrack(0, 0, [])
    return combinations

# Test the function
if __name__ == "__main__":
    print(combination_sum([2, 3, 6, 7], 7))  # Output: [[2, 2, 3], [7]]