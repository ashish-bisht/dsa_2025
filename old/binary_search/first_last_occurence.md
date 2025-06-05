# Finding First and Last Occurrences of a Number in a Sorted Array

## Problem Statement

Given a sorted array of integers and a target value, find the first and last position of the target in the array. If the target is not found, return `[-1, -1]`.

**Example:**
```
Input: numbers = [5, 7, 7, 8, 8, 8, 10], target = 8
Output: [3, 5]
Explanation: The first occurrence of 8 is at index 3, and the last occurrence is at index 5.

Input: numbers = [5, 7, 7, 8, 8, 10], target = 6
Output: [-1, -1]
Explanation: 6 is not present in the array.
```

## Understanding the Problem

This problem asks us to find the boundary positions (first and last) of a target element in a sorted array. Since the array is sorted, we can use binary search to efficiently find these positions.

The key insight is that we need to find:
1. The leftmost occurrence of the target (first position)
2. The rightmost occurrence of the target (last position)

## The Key Difference: Finding First vs Last Occurrence

The most important concept to understand is how binary search can be modified to find either the first or last occurrence of an element.

### Standard Binary Search Logic
In a standard binary search, when we find a match (`middle_value == target`), we immediately return that index. But this doesn't work for finding boundaries because we need to find the extreme positions.

### Modified Binary Search for Boundaries
We need to modify the binary search in two different ways:

1. **For First Occurrence**: When we find a match, we store the position but continue searching in the left half.
2. **For Last Occurrence**: When we find a match, we store the position but continue searching in the right half.

This subtle but critical difference is what allows us to find the boundaries.

## Visual Comparison of the Two Approaches

Let's see the difference visually with array `[5, 7, 7, 8, 8, 8, 10]` and target `8`:

```
Array:  [5, 7, 7, 8, 8, 8, 10]
Index:   0  1  2  3  4  5  6
```

### Finding First Occurrence:
When we find our first match at index 3, we mark it as a potential answer but continue searching in the LEFT half to see if there are earlier occurrences.

### Finding Last Occurrence:
When we find our first match at index 3, we mark it as a potential answer but continue searching in the RIGHT half to see if there are later occurrences.

## Step-by-Step Implementation

Let's implement the solution with clear, meaningful variable names and detailed comments:

```python
def find_first_and_last_position(numbers, target):
    # Edge case: empty array
    if not numbers:
        return [-1, -1]
    
    # Find the first occurrence
    first_position = find_first_position(numbers, target)
    
    # If target is not found, return [-1, -1]
    if first_position == -1:
        return [-1, -1]
    
    # Find the last occurrence
    last_position = find_last_position(numbers, target)
    
    return [first_position, last_position]

def find_first_position(numbers, target):
    left_pointer = 0
    right_pointer = len(numbers) - 1
    potential_first_position = -1
    
    while left_pointer <= right_pointer:
        middle_pointer = left_pointer + (right_pointer - left_pointer) // 2
        middle_value = numbers[middle_pointer]
        
        if middle_value == target:
            # Found a match, but it might not be the FIRST occurrence
            # Update potential position and continue searching in the LEFT half
            potential_first_position = middle_pointer
            right_pointer = middle_pointer - 1  # Key line: Move LEFT
        elif middle_value < target:
            # Target must be in the right half
            left_pointer = middle_pointer + 1
        else:  # middle_value > target
            # Target must be in the left half
            right_pointer = middle_pointer - 1
    
    return potential_first_position

def find_last_position(numbers, target):
    left_pointer = 0
    right_pointer = len(numbers) - 1
    potential_last_position = -1
    
    while left_pointer <= right_pointer:
        middle_pointer = left_pointer + (right_pointer - left_pointer) // 2
        middle_value = numbers[middle_pointer]
        
        if middle_value == target:
            # Found a match, but it might not be the LAST occurrence
            # Update potential position and continue searching in the RIGHT half
            potential_last_position = middle_pointer
            left_pointer = middle_pointer + 1  # Key line: Move RIGHT
        elif middle_value < target:
            # Target must be in the right half
            left_pointer = middle_pointer + 1
        else:  # middle_value > target
            # Target must be in the left half
            right_pointer = middle_pointer - 1
    
    return potential_last_position
```

## Detailed Walkthrough: The Critical Difference

Let's trace through the algorithm with our example to highlight the key difference between finding the first and last occurrence.

**Input**: `numbers = [5, 7, 7, 8, 8, 8, 10], target = 8`

### Execution of `find_first_position()`:

**Initial state**:
- `numbers = [5, 7, 7, 8, 8, 8, 10]` (values)
- `indices =  [0, 1, 2, 3, 4, 5, 6]`
- `target = 8`
- `left_pointer = 0`
- `right_pointer = 6`
- `potential_first_position = -1`

#### Iteration 1:
```
numbers = [5, 7, 7, 8, 8, 8, 10]
           L        M        R
indices =  [0, 1, 2, 3, 4, 5, 6]
```
- `middle_pointer = (0 + 6) // 2 = 3`
- `middle_value = numbers[3] = 8`
- `middle_value == target`, so:
  - `potential_first_position = 3`
  - `right_pointer = 3 - 1 = 2` (move LEFT)

#### Iteration 2:
```
numbers = [5, 7, 7, 8, 8, 8, 10]
           L     R
              M
indices =  [0, 1, 2, 3, 4, 5, 6]
```
- `middle_pointer = (0 + 2) // 2 = 1`
- `middle_value = numbers[1] = 7`
- `middle_value < target`, so:
  - `left_pointer = 1 + 1 = 2`

#### Iteration 3:
```
numbers = [5, 7, 7, 8, 8, 8, 10]
                 LR
                 M
indices =  [0, 1, 2, 3, 4, 5, 6]
```
- `middle_pointer = (2 + 2) // 2 = 2`
- `middle_value = numbers[2] = 7`
- `middle_value < target`, so:
  - `left_pointer = 2 + 1 = 3`

Now `left_pointer > right_pointer`, so the loop ends.
Result: `potential_first_position = 3`

### Execution of `find_last_position()`:

**Initial state**:
- `numbers = [5, 7, 7, 8, 8, 8, 10]` (values)
- `indices =  [0, 1, 2, 3, 4, 5, 6]`
- `target = 8`
- `left_pointer = 0`
- `right_pointer = 6`
- `potential_last_position = -1`

#### Iteration 1:
```
numbers = [5, 7, 7, 8, 8, 8, 10]
           L        M        R
indices =  [0, 1, 2, 3, 4, 5, 6]
```
- `middle_pointer = (0 + 6) // 2 = 3`
- `middle_value = numbers[3] = 8`
- `middle_value == target`, so:
  - `potential_last_position = 3`
  - `left_pointer = 3 + 1 = 4` (move RIGHT)

#### Iteration 2:
```
numbers = [5, 7, 7, 8, 8, 8, 10]
                       L     R
                          M
indices =  [0, 1, 2, 3, 4, 5, 6]
```
- `middle_pointer = (4 + 6) // 2 = 5`
- `middle_value = numbers[5] = 8`
- `middle_value == target`, so:
  - `potential_last_position = 5`
  - `left_pointer = 5 + 1 = 6` (move RIGHT)

#### Iteration 3:
```
numbers = [5, 7, 7, 8, 8, 8, 10]
                             LR
                             M
indices =  [0, 1, 2, 3, 4, 5, 6]
```
- `middle_pointer = (6 + 6) // 2 = 6`
- `middle_value = numbers[6] = 10`
- `middle_value > target`, so:
  - `right_pointer = 6 - 1 = 5`

Now `left_pointer > right_pointer`, so the loop ends.
Result: `potential_last_position = 5`

## Visualizing the Difference

The key difference is in how we handle finding a match:

In `find_first_position()`:
- When we find a match at index 3, we save it and move LEFT
- This allows us to find earlier occurrences if they exist
- We keep looking left until we can't go any further

In `find_last_position()`:
- When we find a match at index 3, we save it and move RIGHT
- This allows us to find later occurrences if they exist
- We keep looking right until we can't go any further

## Visual Example: Finding First and Last Occurrences When Target is Not Present

Let's trace through another example where the target is not present in the array.

**Input**: `numbers = [5, 7, 7, 8, 8, 8, 10], target = 6`

### Execution of `find_first_position()`:

**Initial state**:
- `numbers = [5, 7, 7, 8, 8, 8, 10]` (values)
- `indices =  [0, 1, 2, 3, 4, 5, 6]`
- `target = 6`
- `left_pointer = 0`
- `right_pointer = 6`
- `potential_first_position = -1`

#### Iteration 1:
```
numbers = [5, 7, 7, 8, 8, 8, 10]
           L        M        R
indices =  [0, 1, 2, 3, 4, 5, 6]
```
- `middle_pointer = (0 + 6) // 2 = 3`
- `middle_value = numbers[3] = 8`
- `middle_value > target`, so:
  - `right_pointer = 3 - 1 = 2`

#### Iteration 2:
```
numbers = [5, 7, 7, 8, 8, 8, 10]
           L     R
              M
indices =  [0, 1, 2, 3, 4, 5, 6]
```
- `middle_pointer = (0 + 2) // 2 = 1`
- `middle_value = numbers[1] = 7`
- `middle_value > target`, so:
  - `right_pointer = 1 - 1 = 0`

#### Iteration 3:
```
numbers = [5, 7, 7, 8, 8, 8, 10]
           LR
           M
indices =  [0, 1, 2, 3, 4, 5, 6]
```
- `middle_pointer = (0 + 0) // 2 = 0`
- `middle_value = numbers[0] = 5`
- `middle_value < target`, so:
  - `left_pointer = 0 + 1 = 1`

Now `left_pointer > right_pointer`, so the loop ends.
Result: `potential_first_position = -1` (target not found)

Since the first position is -1, we know the target isn't in the array, so we return `[-1, -1]` without running `find_last_position()`.

## Time and Space Complexity Analysis

### Time Complexity:
- We perform at most two binary searches, each taking O(log n) time, where n is the length of the array.
- Overall time complexity: O(log n)

### Space Complexity:
- We only use a constant amount of extra space regardless of the input size.
- Overall space complexity: O(1)

## Common Mistakes to Avoid

1. **Not Understanding the Key Difference**: The critical difference is how we continue searching after finding a match - left for first occurrence, right for last occurrence.

2. **Returning Too Early**: In standard binary search, we return as soon as we find a match. Here, we need to keep searching after finding a match.

3. **Forgetting to Update Potential Position**: Always update the potential position before continuing the search.

4. **Incorrect Boundary Updates**: Make sure you're updating the correct boundary (left or right) when you find a match.

## Key Insights and Learnings

1. **Modified Binary Search**: By tweaking how we handle matches, we can use binary search to find boundary positions.

2. **Storing Potential Answers**: In boundary-finding algorithms, we often need to store potential answers and keep searching.

3. **Problem-Specific Logic**: The same algorithm (binary search) can be adapted to solve different problems by changing how we handle matches.

4. **Importance of Termination Conditions**: Pay careful attention to when and how the search loop terminates.

## Code Template for Similar Boundary Problems

This pattern of modifying binary search to find boundaries can be applied to many other problems:
- Finding the insertion point for a new element in a sorted array
- Finding the first element greater than or equal to a target
- Finding the last element less than or equal to a target

The key is to understand when to move left or right after finding a match, based on what boundary you're trying to locate.