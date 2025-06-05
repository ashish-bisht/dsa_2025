# 3. Longest Substring Without Repeating Characters
# Difficulty: Medium
# LeetCode Link: https://leetcode.com/problems/longest-substring-without-repeating-characters
# Description:
# Given a string s, find the length of the longest substring without repeating characters.
# Example:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with length 3.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Map characters to their latest index
        character_index = {}
        # Track longest substring length
        max_length = 0
        # Left pointer of sliding window
        left = 0
        
        # Iterate with right pointer
        for right in range(len(s)):
            cur_character = s[right]
            # Check if cur_character is a duplicate in the window
            #sara game ismein window ka hai, right chalti rahege, left ko khichna hai, left mein bas ye sochna haio ke , agar left alreadty aage aagaye hai to agar koi duplcaite window se peche hai to pehce kane ke jkaurate ni

            if cur_character in character_index and character_index[cur_character] >= left:
                # Move left past the duplicate
                left = character_index[cur_character] + 1
            # Update max_length with current window size
            max_length = max(max_length, right - left + 1)
            # Store current index of cur_character
            character_index[cur_character] = right
        
        return max_length

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Standard case
    s1 = "abcabcbb"
    print(f"Test 1: s={s1}")
    print(f"Output: {solution.lengthOfLongestSubstring(s1)}")  # Expected: 3
    
    # Test case 2: All identical characters
    s2 = "bbbbb"
    print(f"Test 2: s={s2}")
    print(f"Output: {solution.lengthOfLongestSubstring(s2)}")  # Expected: 1
    
    # Test case 3: Unique characters
    s3 = "pwwkew"
    print(f"Test 3: s={s3}")
    print(f"Output: {solution.lengthOfLongestSubstring(s3)}")  # Expected: 3
    
    # Test case 4: Empty string
    s4 = ""
    print(f"Test 4: s={s4}")
    print(f"Output: {solution.lengthOfLongestSubstring(s4)}")  # Expected: 0
    
    # Test case 5: Single character
    s5 = "a"
    print(f"Test 5: s={s5}")
    print(f"Output: {solution.lengthOfLongestSubstring(s5)}")  # Expected: 1