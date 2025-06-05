# Problem: Longest Palindromic Substring
# Difficulty: Medium
# LeetCode: https://leetcode.com/problems/longest-palindromic-substring
# Description:
# Given a string s, return the longest palindromic substring in s.
# A string is palindromic if it reads the same forward and backward.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Handle empty string case
        if not s:
            return ""
        
        # Initialize variables to track the longest palindrome
        start = 0  # Starting index of the longest palindrome
        max_length = 1  # Length of the longest palindrome (single char is a palindrome)
        
        # Helper function to expand around a center
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
        
        # Iterate through each index as a potential palindrome center
        for idx in range(len(s)):
            # Case 1: Odd-length palindrome centered at idx
            # Example: "racecar" centered at 'e'
            odd_len, odd_start = expand_around_center(idx, idx)
            
            # Case 2: Even-length palindrome centered between idx and idx+1
            # Example: "abba" centered between the two 'b's
            even_len, even_start = expand_around_center(idx, idx + 1)
            
            # Update if odd-length palindrome is longer
            if odd_len > max_length:
                max_length = odd_len
                start = odd_start
            
            # Update if even-length palindrome is longer
            if even_len > max_length:
                max_length = even_len
                start = even_start
        
        # Return the substring from start to start + max_length
        return s[start:start + max_length]

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Normal case with odd-length palindrome
    assert solution.longestPalindrome("babad") in ["bab", "aba"]  # Both are valid
    
    # Test case 2: Normal case with even-length palindrome
    assert solution.longestPalindrome("cbbd") == "bb"
    
    # Test case 3: Single character
    assert solution.longestPalindrome("a") == "a"
    
    # Test case 4: Empty string
    assert solution.longestPalindrome("") == ""
    
    # Test case 5: All same characters
    assert solution.longestPalindrome("aaaa") == "aaaa"
    
    print("All test cases passed!")