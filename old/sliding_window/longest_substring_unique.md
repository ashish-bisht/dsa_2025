# Longest Substring With Unique Characters

## Problem Statement

Given a string, find the length of the longest substring that contains only unique characters (no repeating characters).

**Example:**
- Input: "abcabcbb"
- Output: 3
- Explanation: The longest substring with unique characters is "abc", which has a length of 3.

## Understanding the Problem

Let's break down what we're looking for:
- A **substring** is a contiguous sequence of characters within a string
- We want the **longest** substring where **all characters are unique**
- We need to return the **length** of this substring

## Visual Representation

Let's visualize this with our example "abcabcbb":

```
String:  a  b  c  a  b  c  b  b
Index:   0  1  2  3  4  5  6  7
```

Possible substrings with unique characters:
- "a" (length 1)
- "ab" (length 2)
- "abc" (length 3)
- "bca" (length 3)
- "cab" (length 3)
- "cb" (length 2)
- "b" (length 1)

The longest ones are "abc", "bca", and "cab", all with length 3.

## Algorithm: Sliding Window Approach

The most efficient approach to solve this problem is using the **sliding window** technique with a hash map to track characters.

### How the Sliding Window Works:

1. Maintain two pointers: `window_start` and `window_end`
2. Expand the window by moving `window_end` to the right
3. If we encounter a duplicate character, shrink the window from the left by moving `window_start`
4. Keep track of the maximum window size we've seen

### Algorithm Steps:

1. Initialize an empty hash map `char_index` to store characters and their most recent positions
2. Initialize `window_start = 0`, `max_length = 0`
3. Iterate through the string with `window_end` from 0 to length-1:
   - If the current character is in the hash map AND its index is >= `window_start`:
     - Update `window_start` to the position after the last occurrence of this character
   - Update the character's position in the hash map
   - Calculate current window length: `window_end - window_start + 1`
   - Update `max_length` if current window is longer
4. Return `max_length`

## Step-by-Step Implementation

Let's implement this algorithm in Python and trace through the execution for "abcabcbb":

```python
def longest_substring_with_unique_chars(input_string):
    # Dictionary to store the last position of each character
    char_index = {}
    
    window_start = 0
    max_length = 0
    
    # Iterate through each character in the string
    for window_end in range(len(input_string)):
        current_char = input_string[window_end]
        
        # If we've seen this character before and it's within our current window
        if current_char in char_index and char_index[current_char] >= window_start:
            # Move window_start to the position after the last occurrence of the character
            window_start = char_index[current_char] + 1
        
        # Update the last position of this character
        char_index[current_char] = window_end
        
        # Calculate current window length
        current_length = window_end - window_start + 1
        
        # Update max_length if current_length is greater
        max_length = max(max_length, current_length)
        
        # Print the state for visualization
        print(f"Step {window_end+1}: Examining '{current_char}'")
        print(f"  window_start = {window_start}, window_end = {window_end}")
        print(f"  Current window: '{input_string[window_start:window_end+1]}' (length: {current_length})")
        print(f"  char_index = {char_index}")
        print(f"  max_length = {max_length}")
        print()
    
    return max_length
```

## Execution Walkthrough

Let's trace through the algorithm with the example string "abcabcbb":

### Step 1: Examining 'a'
- `window_start = 0, window_end = 0`
- Current window: 'a' (length: 1)
- `char_index = {'a': 0}`
- `max_length = 1`

### Step 2: Examining 'b'
- `window_start = 0, window_end = 1`
- Current window: 'ab' (length: 2)
- `char_index = {'a': 0, 'b': 1}`
- `max_length = 2`

### Step 3: Examining 'c'
- `window_start = 0, window_end = 2`
- Current window: 'abc' (length: 3)
- `char_index = {'a': 0, 'b': 1, 'c': 2}`
- `max_length = 3`

### Step 4: Examining 'a'
- We've seen 'a' before at index 0
- Move `window_start` to 0 + 1 = 1
- `window_start = 1, window_end = 3`
- Current window: 'bca' (length: 3)
- `char_index = {'a': 3, 'b': 1, 'c': 2}`
- `max_length = 3`

### Step 5: Examining 'b'
- We've seen 'b' before at index 1
- Move `window_start` to 1 + 1 = 2
- `window_start = 2, window_end = 4`
- Current window: 'cab' (length: 3)
- `char_index = {'a': 3, 'b': 4, 'c': 2}`
- `max_length = 3`

### Step 6: Examining 'c'
- We've seen 'c' before at index 2
- Move `window_start` to 2 + 1 = 3
- `window_start = 3, window_end = 5`
- Current window: 'abc' (length: 3)
- `char_index = {'a': 3, 'b': 4, 'c': 5}`
- `max_length = 3`

### Step 7: Examining 'b'
- We've seen 'b' before at index 4
- Move `window_start` to 4 + 1 = 5
- `window_start = 5, window_end = 6`
- Current window: 'cb' (length: 2)
- `char_index = {'a': 3, 'b': 6, 'c': 5}`
- `max_length = 3`

### Step 8: Examining 'b'
- We've seen 'b' before at index 6
- Move `window_start` to 6 + 1 = 7
- `window_start = 7, window_end = 7`
- Current window: 'b' (length: 1)
- `char_index = {'a': 3, 'b': 7, 'c': 5}`
- `max_length = 3`

Final result: `max_length = 3`

## Visual Window Movement

Let's visualize how our window moves through the string:

```
String:  a  b  c  a  b  c  b  b
         ↑           
         window_start & window_end
         
String:  a  b  c  a  b  c  b  b
         ↑  ↑        
         |  window_end
         window_start
         
String:  a  b  c  a  b  c  b  b
         ↑     ↑     
         |     window_end
         window_start
         
String:  a  b  c  a  b  c  b  b
            ↑     ↑  
            |     window_end
            window_start
            
String:  a  b  c  a  b  c  b  b
               ↑     ↑
               |     window_end
               window_start
               
String:  a  b  c  a  b  c  b  b
                  ↑     ↑
                  |     window_end
                  window_start
                  
String:  a  b  c  a  b  c  b  b
                     ↑     ↑
                     |     window_end
                     window_start
                     
String:  a  b  c  a  b  c  b  b
                           ↑  ↑
                           |  window_end
                           window_start
```

## Time and Space Complexity Analysis

- **Time Complexity**: O(n), where n is the length of the string. We traverse the string once.
- **Space Complexity**: O(min(m, n)), where m is the size of the character set and n is the length of the string. In the worst case, we might need to store all unique characters in the hash map.

## Variations and Follow-up Questions

1. **What if we need to return the actual substring instead of just its length?**
   - Keep track of the start and end indices of the maximum window.

2. **What if we need to find the longest substring with at most K distinct characters?**
   - Modify the algorithm to allow up to K distinct characters in the window.

3. **What if the input string is very large and cannot fit into memory?**
   - Process the string in chunks, maintaining state between chunks.

## Optimizations

- For ASCII characters (128 or 256 characters), we could use a fixed-size array instead of a hash map for slightly better performance.
- We could potentially optimize further by skipping characters when we encounter a duplicate.

## Common Mistakes and Pitfalls

1. **Forgetting to update the character index**: Always update the index of the current character in the hash map.
2. **Incorrect window adjustment**: Make sure to move `window_start` to the position *after* the last occurrence of the duplicate character.
3. **Off-by-one errors**: Be careful with the calculation of the window length.

## Practice Problems

Here are similar problems to practice:
1. Longest Substring with At Most K Distinct Characters
2. Minimum Window Substring
3. Substring with Concatenation of All Words
4. Longest Repeating Character Replacement

## Conclusion

The "Longest Substring With Unique Characters" problem is a classic example of the sliding window technique. By using a hash map to track the most recent positions of characters, we can efficiently find the longest substring with all unique characters in O(n) time.

Remember the key insights:
- Use a sliding window approach
- Track character positions with a hash map
- Adjust the window when duplicates are found
- Keep track of the maximum window size

With practice, this pattern can be applied to many similar string processing problems.