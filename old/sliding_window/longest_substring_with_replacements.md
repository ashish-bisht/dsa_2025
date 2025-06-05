# Longest Uniform Substring After Replacements

## Problem Description

Given a string `s` and an integer `k`, find the length of the longest substring that consists of the same character after replacing at most `k` characters.

In other words, find the longest substring where you can change up to `k` characters to make all characters in the substring identical.

## Visual Explanation with Sliding Window

This problem can be efficiently solved using the sliding window technique.

### Approach

1. We'll use a sliding window to examine potential substrings
2. For each character, we'll keep track of its frequency in the current window
3. The key insight: In a valid window, `(window_length - most_frequent_character_count) <= k`
4. As we expand our window, we'll update the maximum valid window length

### Example

Let's consider an example: `s = "AABABBA"` and `k = 1`

We'll trace through the algorithm step by step:

#### Initial State
```
String: A A B A B B A
        ↑
        window_start = 0, window_end = 0
        window = "A"
        frequencies = {'A': 1}
        max_frequency = 1
        max_length = 1
```

#### Step 1: Expand window to "AA"
```
String: A A B A B B A
        ↑ ↑
        window_start = 0, window_end = 1
        window = "AA"
        frequencies = {'A': 2}
        max_frequency = 2
        max_length = 2
```

#### Step 2: Expand window to "AAB"
```
String: A A B A B B A
        ↑ ↑ ↑
        window_start = 0, window_end = 2
        window = "AAB"
        frequencies = {'A': 2, 'B': 1}
        max_frequency = 2
        
        window_length = 3
        most_frequent_char_count = 2
        replacements_needed = 3 - 2 = 1
        
        replacements_needed <= k? Yes (1 <= 1)
        max_length = 3
```

#### Step 3: Expand window to "AABA"
```
String: A A B A B B A
        ↑ ↑ ↑ ↑
        window_start = 0, window_end = 3
        window = "AABA"
        frequencies = {'A': 3, 'B': 1}
        max_frequency = 3
        
        window_length = 4
        most_frequent_char_count = 3
        replacements_needed = 4 - 3 = 1
        
        replacements_needed <= k? Yes (1 <= 1)
        max_length = 4
```

#### Step 4: Expand window to "AABAB"
```
String: A A B A B B A
        ↑ ↑ ↑ ↑ ↑
        window_start = 0, window_end = 4
        window = "AABAB"
        frequencies = {'A': 3, 'B': 2}
        max_frequency = 3
        
        window_length = 5
        most_frequent_char_count = 3
        replacements_needed = 5 - 3 = 2
        
        replacements_needed <= k? No (2 > 1)
        
        We need to shrink the window
```

#### Step 5: Shrink window from the left
```
String: A A B A B B A
          ↑ ↑ ↑ ↑
        window_start = 1, window_end = 4
        window = "ABAB"
        frequencies = {'A': 2, 'B': 2}
        max_frequency = 2
        
        window_length = 4
        most_frequent_char_count = 2
        replacements_needed = 4 - 2 = 2
        
        replacements_needed <= k? No (2 > 1)
        
        We need to shrink the window again
```

#### Step 6: Shrink window from the left again
```
String: A A B A B B A
            ↑ ↑ ↑
        window_start = 2, window_end = 4
        window = "BAB"
        frequencies = {'A': 1, 'B': 2}
        max_frequency = 2
        
        window_length = 3
        most_frequent_char_count = 2
        replacements_needed = 3 - 2 = 1
        
        replacements_needed <= k? Yes (1 <= 1)
```

#### Step 7: Expand window to "BABB"
```
String: A A B A B B A
            ↑ ↑ ↑ ↑
        window_start = 2, window_end = 5
        window = "BABB"
        frequencies = {'A': 1, 'B': 3}
        max_frequency = 3
        
        window_length = 4
        most_frequent_char_count = 3
        replacements_needed = 4 - 3 = 1
        
        replacements_needed <= k? Yes (1 <= 1)
        max_length = 4
```

#### Step 8: Expand window to "BABBA"
```
String: A A B A B B A
            ↑ ↑ ↑ ↑ ↑
        window_start = 2, window_end = 6
        window = "BABBA"
        frequencies = {'A': 2, 'B': 3}
        max_frequency = 3
        
        window_length = 5
        most_frequent_char_count = 3
        replacements_needed = 5 - 3 = 2
        
        replacements_needed <= k? No (2 > 1)
        
        We need to shrink the window
```

#### Step 9: Shrink window from the left
```
String: A A B A B B A
              ↑ ↑ ↑ ↑
        window_start = 3, window_end = 6
        window = "ABBA"
        frequencies = {'A': 2, 'B': 2}
        max_frequency = 2
        
        window_length = 4
        most_frequent_char_count = 2
        replacements_needed = 4 - 2 = 2
        
        replacements_needed <= k? No (2 > 1)
```

We continue this process until we've processed the entire string. The maximum valid window length we found was 4.

### State Tracking Summary

| Step | Window | Character Frequencies | Max Frequency | Replacements Needed | Valid? | Max Length |
|------|--------|------------------------|---------------|---------------------|--------|------------|
| 1 | "A" | {'A': 1} | 1 | 0 | Yes | 1 |
| 2 | "AA" | {'A': 2} | 2 | 0 | Yes | 2 |
| 3 | "AAB" | {'A': 2, 'B': 1} | 2 | 1 | Yes | 3 |
| 4 | "AABA" | {'A': 3, 'B': 1} | 3 | 1 | Yes | 4 |
| 5 | "AABAB" | {'A': 3, 'B': 2} | 3 | 2 | No | 4 |
| 6 | "ABAB" | {'A': 2, 'B': 2} | 2 | 2 | No | 4 |
| 7 | "BAB" | {'A': 1, 'B': 2} | 2 | 1 | Yes | 4 |
| 8 | "BABB" | {'A': 1, 'B': 3} | 3 | 1 | Yes | 4 |
| 9 | "BABBA" | {'A': 2, 'B': 3} | 3 | 2 | No | 4 |
| 10 | "ABBA" | {'A': 2, 'B': 2} | 2 | 2 | No | 4 |
| ... | ... | ... | ... | ... | ... | ... |

### Result
The longest uniform substring after at most 1 replacement is of length 4.

## Complete Python Implementation

```python
def longest_uniform_substring(s, k):
    """
    Find the length of the longest substring that consists of the same character
    after replacing at most k characters.
    
    Args:
        s: Input string
        k: Maximum number of characters that can be replaced
        
    Returns:
        Length of the longest uniform substring possible
    """
    if not s:
        return 0
    
    n = len(s)
    
    # Edge case: if k is larger than or equal to the string length,
    # we can replace all characters to make them the same
    if k >= n:
        return n
    
    # Initialize variables
    max_length = 0
    max_frequency = 0
    window_start = 0
    char_frequency = {}
    
    # Expand the window
    for window_end in range(n):
        # Update frequency of the current character
        current_char = s[window_end]
        char_frequency[current_char] = char_frequency.get(current_char, 0) + 1
        
        # Update the maximum frequency
        max_frequency = max(max_frequency, char_frequency[current_char])
        
        # Calculate how many replacements are needed in the current window
        # (window length - count of the most frequent character)
        replacements_needed = (window_end - window_start + 1) - max_frequency
        
        # If we need more replacements than allowed, shrink the window
        while replacements_needed > k:
            # Remove the leftmost character from the window
            leftmost_char = s[window_start]
            char_frequency[leftmost_char] -= 1
            window_start += 1
            
            # Recalculate max_frequency (this can be optimized further)
            max_frequency = max(char_frequency.values())
            
            # Update replacements needed
            replacements_needed = (window_end - window_start + 1) - max_frequency
        
        # Update the maximum length
        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length

# Example usage
s = "AABABBA"
k = 1
result = longest_uniform_substring(s, k)
print(f"Length of longest uniform substring after {k} replacements: {result}")  # Output: 4
```

## Optimization Note

In the solution above, we recalculate the maximum frequency after shrinking the window. This can be optimized further:

1. We only need to recalculate max_frequency if the removed character was the most frequent character
2. We can use binary search to find the optimal window size

However, the current solution is already efficient with O(n) time complexity, where n is the length of the string.

## Complexity Analysis

- **Time Complexity**: O(n) where n is the length of the string
  - We process each character at most twice (once when adding to the window, once when removing)
  
- **Space Complexity**: O(min(n, m)) where m is the size of the character set
  - We store frequencies of characters in the window

## Key Insights

1. The problem is a perfect fit for the sliding window technique
2. The key insight is the relationship between window length, most frequent character count, and k
3. For a valid window: (window_length - most_frequent_character_count) ≤ k
4. We can create a uniform substring by replacing all non-most-frequent characters with the most frequent character