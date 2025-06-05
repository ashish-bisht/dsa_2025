# main.py
from typing import List

def letter_combinations(digits: str) -> List[str]:
    # Handle empty input
    if not digits:
        return []
    
    # Initialize result to store all combinations
    result = []
    
    # Mapping of digits to letters
    digits_word_dict = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }
    
    def backtrack(cur_index: int, current_combination: List[str]) -> None:
        # Step 1: Main Hoon (Who Am I?)
        # I'm processing the digit at cur_index, building current_combination.
        
        # Step 2: Kya Karoon (Check and Do?)
        # Base Case: If all digits are processed, add combination to result
        if cur_index == len(digits):
            result.append("".join(current_combination))
            return
        
        # Preprocessing: Get letters for the current digit
        letters = digits_word_dict[digits[cur_index]]
        
        # Step 3: Bacho Jao (Send Kids!)
        # For each letter, add it to the combination and recurse
        for letter in letters:
            current_combination.append(letter)  # Make choice
            backtrack(cur_index + 1, current_combination)  # Recurse
            current_combination.pop()  # Backtrack by undoing choice
        
        # Step 4: Kya Laya (What Did Kids Bring?)
        # Kids append to result in base case; nothing to combine here.
        
        # Step 5: Ye Lo (Here's the Answer!)
        # All combinations are in result after recursion completes.
    
    # Start recursion with index 0 and empty combination
    backtrack(0, [])
    return result

# Test the function
if __name__ == "__main__":
    print(letter_combinations("23"))  # Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']