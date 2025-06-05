# Longest Palindromic Substring

## Problem Description
Given a string `s`, return the **longest palindromic substring** in `s`. A palindromic string reads the same forward and backward. If multiple valid answers exist, return any one.

**Example**:
- Input: `s = "babad"`
- Output: `"bab"` or `"aba"` (both are valid)
- Input: `s = "cbbd"`
- Output: `"bb"`

**Constraints**:
- `1 <= s.length <= 1000`
- `s` consists of lowercase or uppercase letters.

**LeetCode Link**: [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring)

## Intuition
A palindrome is a sequence that is the same when reversed, like `"racecar"` (odd length) or `"deked"` (even length). To find the longest palindromic substring, we can:
1. Treat each character (or pair of characters) as the potential center of a palindrome.
2. Use two pointers (`left` and `right`) to expand outward from the center, checking if characters match.
3. Track the longest palindrome found across all centers.

This "expand around center" approach handles both odd-length palindromes (centered at one character) and even-length palindromes (centered between two characters). The pointers are critical: they define the boundaries of the palindrome and help calculate its length and starting position.

## Approach
1. **Handle edge case**: If the string is empty, return an empty string.
2. **Initialize variables**:
   - `start`: Starting index of the longest palindrome.
   - `max_length`: Length of the longest palindrome (default to 1, as a single character is a palindrome).
3. **Define a helper function** `expand_around_center(left, right)`:
   - Uses `left` and `right` pointers to expand outward while characters match and indices are within bounds.
   - When expansion stops, `left` is one position before the palindrome's start, and `right` is one position after its end.
   - Returns the palindrome's length and starting index.
4. **Iterate through each index**:
   - Check for an odd-length palindrome centered at index `i` (e.g., `"aba"`).
   - Check for an even-length palindrome centered between `i` and `i+1` (e.g., `"bb"`).
   - Update `start` and `max_length` if a longer palindrome is found.
5. **Return the substring** using `start` and `max_length`.

## Code Walkthrough
```python
def longestPalindrome(self, s: str) -> str:
    if not s:
        return ""
    
    start = 0
    max_length = 1
    
    def expand_around_center(left: int, right: int) -> tuple[int, int]:
        # Expand while within bounds and characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1  # Move left pointer outward (to the left)
            right += 1  # Move right pointer outward (to the right)
        
        # When the while loop ends:
        # - left is one position BEFORE the start of palindrome
        # - right is one position AFTER the end of palindrome
        # Example with "racecar" centered at 'e':
        # When loop ends: left=-1, right=7
        # Palindrome starts at index 0 (left+1) and ends at index 6 (right-1)
        
        # Calculate length: (right-1) - (left+1) + 1 = right - left - 1
        length_of_palindrome = right - left - 1
        
        # Calculate start: left + 1 (left has overshot by 1)
        palindrome_start = left + 1
        return length_of_palindrome, palindrome_start
    
    for idx in range(len(s)):
        # Case 1: Odd-length palindrome centered at idx
        # Example: "racecar" centered at 'e'
        odd_len, odd_start = expand_around_center(idx, idx)
        # Case 2: Even-length palindrome centered between idx and idx+1
        # Example: "abba" centered between the two 'b's
        even_len, even_start = expand_around_center(idx, idx + 1)
        
        if odd_len > max_length:
            max_length = odd_len
            start = odd_start
        if even_len > max_length:
            max_length = even_len
            start = even_start
    
    return s[start:start + max_length]