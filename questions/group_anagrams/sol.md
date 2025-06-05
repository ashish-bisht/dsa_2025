# Group Anagrams Solution

## Problem Description
Given an array of strings `strs`, group all strings that are anagrams of each other. An anagram is a word formed by rearranging the letters of another (e.g., "eat" and "tea"). Return a list of lists, where each sublist contains strings that are anagrams. The order of the output doesn’t matter.

**Example**:
- Input: `strs = ["eat","tea","tan","ate","nat","bat"]`
- Output: `[["eat","tea","ate"],["tan","nat"],["bat"]]`

**Constraints**:
- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## Intuition
To group anagrams, we need a way to identify strings that have the same letters (in any order). If two strings are anagrams, they have the same characters with the same frequencies. For example, "eat" and "tea" both have one 'e', one 'a', and one 't'.

A natural approach is to create a "key" for each string that represents its character composition. Two strings with the same key are anagrams. We can:
1. Sort the characters of each string to get a key (e.g., "eat" and "tea" both sort to "aet").
2. Use a hash map to group strings by this key.
3. Return the grouped strings as a list of lists.

This approach is intuitive because sorting normalizes the string, making anagrams map to the same key.

## Approach
We’ll use a hash map to group anagrams, with the sorted string as the key and a list of original strings as the value. Here’s the step-by-step plan:
1. Initialize a `defaultdict(list)` to store anagram groups.
2. For each string in `strs`:
   - Sort its characters to create a key.
   - Add the original string to the list associated with this key in the hash map.
3. Return the values of the hash map as a list.

### Why Use Sorting?
Sorting the characters ensures that anagrams produce identical keys. For example, "eat", "tea", and "ate" all sort to "aet". This is the **main crux** of the solution: the sorted string acts as a unique identifier for anagrams.

### Alternative: Character Count Key
Instead of sorting, we could create a key by counting the frequency of each character (e.g., "eat" becomes a tuple like `[1,0,0,...,1,0,...,1]` for 'e', 'a', 't'). This is faster for long strings but more complex to implement. Sorting is simpler and works well for the given constraints (string length ≤ 100).

## Code Walkthrough
Let’s break down the Python code:

```python
from typing import List
from collections import defaultdict