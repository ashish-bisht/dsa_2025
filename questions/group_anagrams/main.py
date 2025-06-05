# Group Anagrams
# Difficulty: Medium
# LeetCode Link: https://leetcode.com/problems/group-anagrams
# Description:
# Given an array of strings, group the anagrams together. An anagram is a word formed by rearranging the letters
# of another, such as "cinema" and "iceman". The output should be a list of lists, where each sublist contains
# strings that are anagrams of each other. The order of the output does not matter.
# Example:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
# Constraints:
# - 1 <= strs.length <= 10^4
# - 0 <= strs[i].length <= 100
# - strs[i] consists of lowercase English letters.

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a defaultdict to store groups of anagrams
        # Key: sorted string (or character count), Value: list of original strings
        anagram_groups = defaultdict(list)
        
        # Iterate through each string in the input list
        for current_str in strs:
            # Sort the characters of the string to create a key
            # Sorting ensures anagrams have the same key (e.g., "eat" and "tea" both become "aet")
            sorted_key = ''.join(sorted(current_str))
            
            # Add the original string to the list associated with this key
            anagram_groups[sorted_key].append(current_str)
        
        # Convert the dictionary values to a list to match the required output format
        return list(anagram_groups.values())


# Test cases for local verification
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Standard case with multiple anagram groups
    input1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output1 = solution.groupAnagrams(input1)
    print("Test 1:", output1)  # Expected: [["eat","tea","ate"],["tan","nat"],["bat"]]
    
    # Test case 2: Empty string
    input2 = [""]
    output2 = solution.groupAnagrams(input2)
    print("Test 2:", output2)  # Expected: [[""]]
    
    # Test case 3: Single string
    input3 = ["a"]
    output3 = solution.groupAnagrams(input3)
    print("Test 3:", output3)  # Expected: [["a"]]
    
    # Test case 4: All anagrams
    input4 = ["cat", "act", "tac"]
    output4 = solution.groupAnagrams(input4)
    print("Test 4:", output4)  # Expected: [["cat","act","tac"]]