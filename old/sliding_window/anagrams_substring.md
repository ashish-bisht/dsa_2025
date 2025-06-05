# Visual Anagram Finder: Step-by-Step States with Code

## The Problem
Find how many substrings in `s` are anagrams of `t`.

**Example:**
- `s = "caabab"`
- `t = "aba"`

## Visual Explanation with All States

### First, we count letters in our target string `t`:
```
t = "aba"

STATE OF t_counts:
{
  'a': 2,  (two 'a' letters)
  'b': 1   (one 'b' letter)
}
```

### Next, we prepare our sliding window:
```
s = "caabab"
    ↑↑↑      (window of size 3, same as length of t)
```

### Initial window state (window = "caa"):
```
STATE OF window_counts:
{
  'c': 1,  (one 'c' letter)
  'a': 2   (two 'a' letters)
}

COMPARISON:
window_counts = {'c': 1, 'a': 2}
t_counts =     {'a': 2, 'b': 1}

Are they equal? NO (window has 'c' instead of 'b')
COUNT = 0
```

### Slide window right (window = "aab"):
```
s = "caabab"
     ↑↑↑     (window moved one position right)
```

```
PREVIOUS STATE:
window_counts = {'c': 1, 'a': 2}

OPERATIONS:
1. Add new character: 'b'
   window_counts = {'c': 1, 'a': 2, 'b': 1}

2. Remove old character: 'c'
   window_counts['c'] -= 1 → {'c': 0, 'a': 2, 'b': 1}
   Since 'c' count is 0, remove it → {'a': 2, 'b': 1}

CURRENT STATE:
window_counts = {'a': 2, 'b': 1}

COMPARISON:
window_counts = {'a': 2, 'b': 1}
t_counts =     {'a': 2, 'b': 1}

Are they equal? YES!
COUNT = 1
```

### Slide window right again (window = "aba"):
```
s = "caabab"
      ↑↑↑    (window moved one position right)
```

```
PREVIOUS STATE:
window_counts = {'a': 2, 'b': 1}

OPERATIONS:
1. Add new character: 'a'
   window_counts = {'a': 3, 'b': 1}

2. Remove old character: 'a'
   window_counts['a'] -= 1 → {'a': 2, 'b': 1}

CURRENT STATE:
window_counts = {'a': 2, 'b': 1}

COMPARISON:
window_counts = {'a': 2, 'b': 1}
t_counts =     {'a': 2, 'b': 1}

Are they equal? YES!
COUNT = 2
```

### Slide window right final time (window = "bab"):
```
s = "caabab"
       ↑↑↑   (window moved one position right)
```

```
PREVIOUS STATE:
window_counts = {'a': 2, 'b': 1}

OPERATIONS:
1. Add new character: 'b'
   window_counts = {'a': 2, 'b': 2}

2. Remove old character: 'a'
   window_counts['a'] -= 1 → {'a': 1, 'b': 2}

CURRENT STATE:
window_counts = {'a': 1, 'b': 2}

COMPARISON:
window_counts = {'a': 1, 'b': 2}
t_counts =     {'a': 2, 'b': 1}

Are they equal? NO (counts don't match)
COUNT = 2 (unchanged)
```

### Final answer: 2 anagram substrings

## Summary as a Table

| Step | Window | Operation | window_counts | Equal to t_counts? | Count |
|------|--------|-----------|---------------|-------------------|-------|
| Init | "caa" | Initial count | {'c': 1, 'a': 2} | NO | 0 |
| 1 | "aab" | Add 'b', Remove 'c' | {'a': 2, 'b': 1} | YES | 1 |
| 2 | "aba" | Add 'a', Remove 'a' | {'a': 2, 'b': 1} | YES | 2 |
| 3 | "bab" | Add 'b', Remove 'a' | {'a': 1, 'b': 2} | NO | 2 |

## Memory Diagram

```
t = "aba"
s = "caabab"

TARGET DICTIONARY:
t_counts = {
  'a': 2,
  'b': 1
}

WINDOW EVOLUTION:
Window 1: "caa" → {'c': 1, 'a': 2}
  ↓ 
Window 2: "aab" → {'a': 2, 'b': 1} ✓ (MATCH!)
  ↓
Window 3: "aba" → {'a': 2, 'b': 1} ✓ (MATCH!)
  ↓
Window 4: "bab" → {'a': 1, 'b': 2}
```

## Key Insight Visualization

Instead of recounting all letters in each window (inefficient):
```
Window 1: "caa" → Count from scratch: {'c': 1, 'a': 2}
Window 2: "aab" → Count from scratch: {'a': 2, 'b': 1}
Window 3: "aba" → Count from scratch: {'a': 2, 'b': 1}
Window 4: "bab" → Count from scratch: {'a': 1, 'b': 2}
```

We use the sliding window technique (efficient):
```
Window 1: "caa" → Count once: {'c': 1, 'a': 2}
Window 2: "aab" → Update: +b, -c → {'a': 2, 'b': 1}
Window 3: "aba" → Update: +a, -a → {'a': 2, 'b': 1}
Window 4: "bab" → Update: +b, -a → {'a': 1, 'b': 2}
```

This reduces our operations from O(n×m) to O(n).

## Complete Python Implementation

```python
def count_anagram_substrings(s, t):
    """
    Counts the number of substrings in s that are anagrams of t
    
    Args:
        s: The string to search within
        t: The string to find anagrams of
        
    Returns:
        The count of anagram substrings
    """
    # Edge cases
    if len(s) < len(t) or not s or not t:
        return 0
    
    # Create a dictionary to count letters in t
    t_counts = {}
    for char in t:
        if char in t_counts:
            t_counts[char] += 1
        else:
            t_counts[char] = 1
    
    # Create a dictionary for our sliding window
    window_counts = {}
    
    # Initialize the first window
    for i in range(len(t)):
        char = s[i]
        if char in window_counts:
            window_counts[char] += 1
        else:
            window_counts[char] = 1
    
    # Count of anagrams found
    count = 0
    
    # Check if first window is an anagram
    if window_counts == t_counts:
        count += 1
    
    # Slide the window through string s
    for i in range(len(t), len(s)):
        # Add new character to window
        new_char = s[i]
        if new_char in window_counts:
            window_counts[new_char] += 1
        else:
            window_counts[new_char] = 1
        
        # Remove character that's no longer in window
        old_char = s[i - len(t)]
        window_counts[old_char] -= 1
        
        # If count becomes 0, remove the character from dictionary
        if window_counts[old_char] == 0:
            del window_counts[old_char]
        
        # Check if current window is an anagram
        if window_counts == t_counts:
            count += 1
    
    return count

# Example usage
s = "caabab"
t = "aba"
result = count_anagram_substrings(s, t)
print(f"Number of anagram substrings: {result}")  # Output: 2
```

## Walk-through with Our Example

Let's trace through the algorithm one more time:

1. We set up `t_counts = {'a': 2, 'b': 1}` for our target `t = "aba"`
2. We initialize our first window "caa" with `window_counts = {'c': 1, 'a': 2}`
3. Compare: Not equal, so `count = 0`
4. Slide window to "aab":
   - Add 'b' → {'c': 1, 'a': 2, 'b': 1}
   - Remove 'c' → {'a': 2, 'b': 1}
   - Compare: Equal! `count = 1`
5. Slide window to "aba":
   - Add 'a' → {'a': 3, 'b': 1}
   - Remove 'a' → {'a': 2, 'b': 1}
   - Compare: Equal! `count = 2`
6. Slide window to "bab":
   - Add 'b' → {'a': 2, 'b': 2}
   - Remove 'a' → {'a': 1, 'b': 2}
   - Compare: Not equal, so `count = 2`
7. Return `count = 2`