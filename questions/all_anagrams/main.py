# 438. Find All Anagrams in a String
# Difficulty: Medium
# LeetCode Link: https://leetcode.com/problems/find-all-anagrams-in-a-string
# Description:
# Given two strings s and p, find all the start indices of p's anagrams in s.
# An anagram is a word or phrase formed by rearranging the letters of another.
# The strings consist of lowercase English letters only, and the length of both
# strings s and p will not be larger than 20,100.
# Example:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0, 6]
# Explanation: The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Initialize result list to store starting indices of anagrams
        result = []
        
        # If p is longer than s, no anagrams are possible
        if len(p) > len(s):
            return result
        
        # Create frequency maps for characters in p and the first window in s
        p_count = Counter(p)
        window_count = Counter(s[:len(p)])
        
        # Check if the first window is an anagram
        if window_count == p_count:
            result.append(0)
        
        # Slide the window over s, starting from index 1
        for idx in range(1, len(s) - len(p) + 1):
            # Remove the character at the start of the previous window
            char_to_remove = s[idx - 1]
            window_count[char_to_remove] -= 1
            if window_count[char_to_remove] == 0:
                del window_count[char_to_remove]
            
            # Add the new character at the end of the current window
            char_to_add = s[idx + len(p) - 1]
            window_count[char_to_add] += 1
            
            # Check if the current window is an anagram
            if window_count == p_count:
                result.append(idx)
        
        return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Standard case with two anagrams
    s1, p1 = "cbaebabacd", "abc"
    print(f"Test 1: s={s1}, p={p1}")
    print(f"Output: {solution.findAnagrams(s1, p1)}")  # Expected: [0, 6]
    
    # Test case 2: Overlapping anagrams
    s2, p2 = "abab", "ab"
    print(f"Test 2: s={s2}, p={p2}")
    print(f"Output: {solution.findAnagrams(s2, p2)}")  # Expected: [0, 1, 2]
    
    # Test case 3: Single large anagram
    s3, p3 = "aaaaaaaaaa", "aaaaaaaaaa"
    print(f"Test 3: s={s3}, p={p3}")
    print(f"Output: {solution.findAnagrams(s3, p3)}")  # Expected: [0]
    
    # Test case 4: No anagrams possible
    s4, p4 = "abc", "abcd"
    print(f"Test 4: s={s4}, p={p4}")
    print(f"Output: {solution.findAnagrams(s4, p4)}")  # Expected: []