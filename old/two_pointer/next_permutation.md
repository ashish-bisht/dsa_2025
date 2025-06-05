# Next Permutation: A Comprehensive Guide

## Introduction

The "Next Permutation" algorithm finds the lexicographically next greater permutation of a given sequence of numbers. In simpler terms, it rearranges the numbers to create the next greater sequence. If the sequence is already the largest possible (in descending order), it wraps around to the smallest sequence (ascending order).

This algorithm is useful in many contexts, including:
- Generating all permutations of a sequence
- Solving combinatorial problems
- Implementing permutation-related functionality in programming languages

## Problem Statement

Given an array of integers, rearrange the numbers into the lexicographically next greater permutation. If such an arrangement is not possible, rearrange it to the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

## Understanding Permutation Order

Before diving into the algorithm, let's understand what "lexicographically next" means with a simple example:

```
Permutation order for [1,2,3]:

[1,2,3] → [1,3,2] → [2,1,3] → [2,3,1] → [3,1,2] → [3,2,1] → [1,2,3] (wraps around)
 ↑           ↑                                                           
current     next
```

Consider the sequence [1, 2, 3]:
- All possible permutations in lexicographical order are:
  [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]
  
- If our current permutation is [1, 2, 3], the next permutation is [1, 3, 2]
- If our current permutation is [2, 3, 1], the next permutation is [3, 1, 2]
- If our current permutation is [3, 2, 1] (largest possible), the next permutation wraps around to [1, 2, 3] (smallest possible)

## The Algorithm

The key insight is to find the first pair of adjacent elements (from right to left) where the left element is smaller than the right element. This identifies the position where we can make a change to get the next bigger permutation.

### Step-by-Step Algorithm:

1. Find the largest index `pivot` such that array[pivot] < array[pivot + 1]
   - If no such index exists, the permutation is the last permutation (sorted in descending order)
   - In this case, reverse the whole array to get the first permutation (sorted in ascending order)
   
2. Find the largest index `successor` such that array[successor] > array[pivot]
   - The `successor` is the element that will replace our pivot
   - We need the **rightmost** element greater than the pivot (not the smallest greater element)
   - This ensures we get the next permutation, not one that's further ahead in the sequence
   
3. Swap the values at indices `pivot` and `successor`
   
4. Reverse the subarray starting at position `pivot + 1` to the end

Let's walk through this with examples.

### Understanding the Successor

The `successor` is critical to finding the next permutation:

```
Array: [1, 3, 5, 4, 2]
         ↑
       pivot (value 3)
```

After identifying the pivot (3), we need to find its successor:
- We look at all elements to the right of pivot: [5, 4, 2]
- We need to find the rightmost element greater than 3
- Both 5 and 4 are greater than 3
- 4 is the rightmost among these, so it becomes the successor

```
Array: [1, 3, 5, 4, 2]
         ↑     ↑
       pivot  successor (value 4)
```

Why the rightmost element? Because we want the next permutation, not just any larger permutation. By choosing the rightmost element that's greater than the pivot, we ensure we're making the smallest possible increase.

## Example 1: [1, 2, 3]

Let's trace through each step:

1. Find the pivot:
   - Starting from the right, we check: Is 3 < something? No, we're at the end
   - Is 2 < 3? Yes, so pivot = 1 (index of 2)
   
   Current state: [1, 2, 3], pivot = 1
   
   ```
   Find pivot (first element from right that is smaller than its right neighbor):
   
   [1, 2, 3]
       ↑
     pivot
   ```

2. Find the successor:
   - We need to find the rightmost element that is greater than the pivot value
   - Pivot value is 2, so we need to find the rightmost element > 2
   - The only element to the right of pivot is 3, and 3 > 2
   - So successor = 2 (index of 3)
   
   Current state: [1, 2, 3], pivot = 1, successor = 2
   
   ```
   Find successor (rightmost element larger than pivot):
   
   [1, 2, 3]
       ↑  ↑
    pivot  successor
     (2)  (3)
   
   Note: We're looking for the rightmost element greater than 2
   ```

3. Swap elements at pivot and successor:
   - Swap elements at indices 1 and 2: 2 and 3
   
   Current state: [1, 3, 2]
   
   ```
   Swap pivot and successor:
   
   [1, 2, 3]  →  [1, 3, 2]
       ↑  ↑          ↑  ↑
    pivot  successor    (swapped)
   ```

4. Reverse the subarray from pivot + 1 to end:
   - Reverse the subarray from index 2 to the end
   - This is just the single element [2], so nothing changes
   
   Final state: [1, 3, 2]
   
   ```
   Reverse the subarray after pivot:
   
   [1, 3, 2]  →  [1, 3, 2]
        ↑           ↑
    pivot+1      (nothing changes since
                  it's a single element)
   ```

So the next permutation of [1, 2, 3] is [1, 3, 2].

## Example 2: [3, 2, 1]

1. Find the pivot:
   - Is 1 < something? No
   - Is 2 < 1? No
   - Is 3 < 2? No
   - We can't find a pivot, so this is the last permutation
   
   Current state: [3, 2, 1], no pivot found
   
   ```
   Find pivot:
   
   [3, 2, 1]
   
   Checking from right to left:
   1 < next? No (there's no next element)
   2 < 1? No (2 > 1)
   3 < 2? No (3 > 2)
   
   No pivot found - this is already the last permutation
   ```

   Since no pivot is found, we reverse the entire array:
   
   ```
   Reverse the entire array:
   
   [3, 2, 1] → [1, 2, 3]
   
   This is the wrap-around case - from the last permutation
   back to the first permutation
   ```
   
   Final state: [1, 2, 3]

So the next permutation of [3, 2, 1] is [1, 2, 3].

## Example 3: [1, 3, 5, 4, 2]

Let's trace through in detail:

1. Find the pivot:
   - Is 2 < something? No
   - Is 4 < 2? No
   - Is 5 < 4? No
   - Is 3 < 5? Yes, so pivot = 1 (index of 3)
   
   Current state: [1, 3, 5, 4, 2], pivot = 1
   
   ```
   Find pivot:
   
   [1, 3, 5, 4, 2]
       ↑
     pivot
   ```

2. Find the successor:
   - We need to find the rightmost element greater than the pivot value
   - Pivot value is 3, so we need the rightmost element > 3
   - Elements to the right of pivot: [5, 4, 2]
   - Both 5 and 4 are greater than 3
   - Since we want the rightmost one, successor = 3 (index of 4)
   
   Current state: [1, 3, 5, 4, 2], pivot = 1, successor = 3
   
   ```
   Find successor:
   
   [1, 3, 5, 4, 2]  ← Scanning from right to left
       ↑     ↑
    pivot  successor
     (3)    (4)
   
   Why not choose 5? Because 4 is the rightmost element > 3,
   which gives us the lexicographically next permutation
   ```

3. Swap elements at pivot and successor:
   - Swap elements at indices 1 and 3: 3 and 4
   
   Current state: [1, 4, 5, 3, 2]
   
   ```
   Swap pivot and successor:
   
   [1, 3, 5, 4, 2]  →  [1, 4, 5, 3, 2]
       ↑     ↑            ↑     ↑
    pivot  successor   (swapped)
   ```

4. Reverse the subarray from pivot + 1 to end:
   - Reverse the subarray from index 2 to the end: [5, 3, 2]
   - After reversing: [2, 3, 5]
   
   Final state: [1, 4, 2, 3, 5]
   
   ```
   Reverse subarray after pivot:
   
   [1, 4, 5, 3, 2]  →  [1, 4, 2, 3, 5]
          ↑                 ↑
      pivot+1           (reversed)
   ```

So the next permutation of [1, 3, 5, 4, 2] is [1, 4, 2, 3, 5].

## Implementation in Python

Here's a clear Python implementation with detailed comments:

```python
def next_permutation(numbers):
    """
    Rearranges numbers in-place to the lexicographically next greater permutation.
    If such arrangement is not possible, it rearranges to the lowest possible order.
    
    Args:
        numbers: List of integers
        
    Returns:
        None (modifies the list in-place)
    """
    # Step 1: Find the pivot (largest index such that numbers[pivot] < numbers[pivot + 1])
    # We scan from right to left to find the first decreasing element
    pivot_index = -1
    for index in range(len(numbers) - 2, -1, -1):
        if numbers[index] < numbers[index + 1]:
            pivot_index = index
            break
    
    # Print the state of variables
    print(f"After finding pivot: numbers={numbers}, pivot_index={pivot_index}")
    
    # If no pivot found, this is the last permutation
    if pivot_index == -1:
        print("No pivot found - this is the last permutation. Reversing the array.")
        numbers.reverse()
        print(f"After reversing: numbers={numbers}")
        return
    
    # Step 2: Find successor (rightmost element greater than pivot)
    # We need the rightmost element that's greater than the pivot to get the next permutation
    pivot_value = numbers[pivot_index]
    successor_index = -1
    
    # Scan from right to left to find the rightmost element > pivot_value
    for index in range(len(numbers) - 1, pivot_index, -1):
        if numbers[index] > pivot_value:
            successor_index = index
            break
    
    print(f"After finding successor: numbers={numbers}, pivot_index={pivot_index}, pivot_value={pivot_value}, successor_index={successor_index}, successor_value={numbers[successor_index]}")
    
    # Step 3: Swap elements at pivot and successor
    numbers[pivot_index], numbers[successor_index] = numbers[successor_index], numbers[pivot_index]
    
    print(f"After swapping: numbers={numbers}")
    
    # Step 4: Reverse the subarray starting at pivot + 1
    # This ensures we get the smallest possible increase
    left = pivot_index + 1
    right = len(numbers) - 1
    
    while left < right:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left += 1
        right -= 1
    
    print(f"Final result after reversing suffix: numbers={numbers}")
```

## Detailed Trace for a Complex Example: [2, 3, 1, 5, 4, 0]

Let's trace through our algorithm step by step with visual diagrams:

1. Find the pivot:
   - Start from the right and find the first pair where left < right
   - Check: Is 0 < something? No (end of array)
   - Check: Is 4 < 0? No
   - Check: Is 5 < 4? No
   - Check: Is 1 < 5? Yes! So pivot = 2 (index of 1)
   
   Current state: [2, 3, 1, 5, 4, 0], pivot = 2
   
   ```
   Find pivot:
   
   [2, 3, 1, 5, 4, 0]
           ↑
         pivot
   ```

2. Find the successor:
   - Looking at elements to the right of pivot (value 1)
   - We need the rightmost element greater than 1
   - Elements to the right: [5, 4, 0]
   - Both 5 and 4 are greater than 1
   - Starting from the right, the first element > 1 is 4
   - So successor = 4 (index of 4)
   
   Current state: [2, 3, 1, 5, 4, 0], pivot = 2, successor = 4
   
   ```
   Find successor (rightmost element > pivot):
   
   [2, 3, 1, 5, 4, 0]  ← Scanning from right to left
           ↑     ↑
        pivot  successor
         (1)    (4)
   
   Visual scan from right to left:
   0 > 1? No
   4 > 1? Yes! This is our successor
   (We don't need to check 5, we already found the rightmost element > 1)
   ```

3. Swap elements at pivot and successor:
   - Swap elements at indices 2 and 4: 1 and 4
   
   Current state: [2, 3, 4, 5, 1, 0]
   
   ```
   Swap pivot and successor:
   
   [2, 3, 1, 5, 4, 0]  →  [2, 3, 4, 5, 1, 0]
           ↑     ↑             ↑     ↑
        pivot  successor    (swapped)
   ```

4. Reverse the subarray from pivot + 1 to end:
   - Reverse the subarray from index 3 to the end: [5, 1, 0]
   - After reversing: [0, 1, 5]
   
   Final state: [2, 3, 4, 0, 1, 5]
   
   ```
   Reverse subarray after pivot:
   
   [2, 3, 4, 5, 1, 0]  →  [2, 3, 4, 0, 1, 5]
              ↑                    ↑
          pivot+1               (reversed)
   ```

So the next permutation of [2, 3, 1, 5, 4, 0] is [2, 3, 4, 0, 1, 5].

## Visual Algorithm Flow Chart

Here's a flowchart summarizing the Next Permutation algorithm:

```
┌─────────────────┐
│  Start          │
└────────┬────────┘
         ▼
┌─────────────────────────────────────────────┐
│ Scan array from right to left to find pivot │
│ (first element smaller than its next one)   │
└────────────────────┬──────────────────────┘
                    ▼
┌─────────────────────────────┐
│ Pivot found?                │─── No ──┐
└────────────┬────────────────┘         │
             │ Yes                      ▼
             ▼                    ┌────────────────────┐
┌─────────────────────────────┐   │ This is the last   │
│ Scan array from right to    │   │ permutation        │
│ left to find successor      │   └──────────┬─────────┘
│ (rightmost element > pivot) │              │
└────────────┬────────────────┘              │
             ▼                               ▼
┌─────────────────────────────┐     ┌────────────────────┐
│ Swap pivot with successor   │     │ Reverse entire     │
└────────────┬────────────────┘     │ array to get the   │
             │                      │ first permutation  │
             ▼                      └──────────┬─────────┘
┌─────────────────────────────┐              │
│ Reverse the subarray after  │              │
│ pivot to ensure we get the  │◄─────────────┘
│ lexicographically next perm │
└────────────┬────────────────┘
             ▼
┌─────────────────┐
│ Done            │
└─────────────────┘
```

### Key Insights About Successor Selection

```
┌───────────────────────────────────────────────────────────┐
│ Why do we choose the rightmost element > pivot?           │
├───────────────────────────────────────────────────────────┤
│                                                           │
│ Example: [1, 5, 8, 4, 7, 6, 5, 3, 1]                      │
│              ↑                                            │
│            pivot (5)                                      │
│                                                           │
│ Valid successors (elements > 5): [8, 7, 6]                │
│                                                           │
│ If we choose 8 (closest next): [1, 8, 5, 4, 7, 6, 5, 3, 1]│
│   After reversing suffix:      [1, 8, 1, 3, 5, 6, 7, 4, 5]│
│                                                           │
│ If we choose 6 (rightmost): [1, 6, 8, 4, 7, 5, 5, 3, 1]   │
│   After reversing suffix:   [1, 6, 1, 3, 5, 5, 7, 4, 8]   │
│                                                           │
│ Choosing 6 (rightmost) gives us the lexicographically     │
│ next permutation, which is what we want.                  │
└───────────────────────────────────────────────────────────┘
```

## Tracing with Variable States in a Table

For the example [1, 3, 5, 4, 2], let's trace the algorithm's execution with a detailed table showing all variable states:

| Step | Action | Array State | pivot_index | pivot_value | successor_index | successor_value | Explanation |
|------|--------|-------------|-------------|-------------|-----------------|-----------------|-------------|
| 0 | Initial state | [1, 3, 5, 4, 2] | - | - | - | - | Starting array |
| 1 | Find pivot | [1, 3, 5, 4, 2] | 1 | 3 | - | - | Found pivot at index 1 (value 3) because 3 < 5 |
| 2 | Find successor | [1, 3, 5, 4, 2] | 1 | 3 | 3 | 4 | Found successor at index 3 (value 4) because it's the rightmost element greater than pivot |
| 3 | Swap pivot & successor | [1, 4, 5, 3, 2] | 1 | 3 | 3 | 4 | Swapped values at indices 1 and 3 |
| 4 | Reverse subarray | [1, 4, 2, 3, 5] | 1 | 3 | 3 | 4 | Reversed the subarray from index 2 to end |

### Detailed Scan for Finding the Successor (Step 2)

For clarity, let's see exactly how we scan for the successor in the above example:

```
Array after finding pivot: [1, 3, 5, 4, 2]
                               ↑
                             pivot (value 3)

Scanning from right to find successor:
→ Check index 4: Is 2 > 3? No (skip)
→ Check index 3: Is 4 > 3? Yes! This is our successor.
  (We don't need to check index 2 with value 5, we already found the rightmost)

Successor found at index 3 with value 4
```

## Time and Space Complexity

- Time Complexity: O(n), where n is the length of the array
  - Finding the pivot: O(n) in worst case
  - Finding the successor: O(n) in worst case
  - Swapping: O(1)
  - Reversing: O(n) in worst case
  
```
Time Complexity Visualization:

Finding pivot:    [X][X][X][X][X]  → O(n)
Finding successor:[X][X][X][X][X]  → O(n)
Swapping:         [O]              → O(1)
Reversing:        [X][X][X][X][X]  → O(n)
                  -----------------
Total:                               O(n)
```
  
- Space Complexity: O(1)
  - The algorithm works in-place, only using a constant amount of extra space

## When to Use Next Permutation

1. **Generating all permutations**: By repeatedly applying the next permutation algorithm, you can generate all possible permutations of a sequence.

2. **Combinatorial optimization**: Some optimization problems require evaluating different permutations to find an optimal solution.

3. **Competitive programming**: This algorithm is commonly used in competitive programming to solve permutation-related problems efficiently.

## Common Variations and Extensions

1. **Previous Permutation**: Finding the lexicographically previous permutation is very similar - just reverse the comparison operators in the algorithm.

2. **Kth Permutation**: Finding the kth permutation directly without generating all preceding permutations requires a different approach using factorial number systems.

3. **Permutation Rank**: Finding the rank (position) of a given permutation in the lexicographical ordering of all permutations.

## Why This Algorithm Works: Intuitive Explanation

To understand why this algorithm works, let's think about what makes a permutation "next" in lexicographical order:

1. **To get the next permutation**, we need to increase the sequence by the smallest amount possible.

2. **Key insight**: To minimize the increase, we should modify the rightmost elements possible.

   ```
   If we change [1,2,3,4,5] at the 1st position: BIG change
   If we change [1,2,3,4,5] at the 5th position: SMALL change
   ```

3. **Finding the pivot**: When we scan from right to left and find the first decreasing element (the pivot), we've found the position we need to change.

   ```
   In [1,5,8,4,7,6,5,3,1], scanning from right:
   1,3,5,6,7,4,8,5,1
           ↑
        First decrease
   ```

4. **Choosing the successor**: We pick the rightmost element greater than the pivot to ensure the smallest possible increase.

5. **Reversing the suffix**: After swapping pivot and successor, the suffix is still in descending order. To get the lexicographically smallest arrangement, we reverse it to ascending order.

This process ensures we find precisely the next permutation - not one further ahead in the sequence.

## Conclusion

The Next Permutation algorithm provides an elegant, efficient solution for finding the next lexicographically greater arrangement of elements. Its constant space complexity makes it particularly valuable for applications where memory usage is a concern.

Understanding this algorithm thoroughly helps build intuition for other permutation-related problems and combinatorial mathematics in general.

## Key Takeaways

- The successor is the rightmost element greater than the pivot, not just any greater element
- Reversing the suffix after swapping is crucial for getting the lexicographically next permutation
- The algorithm has O(n) time complexity and O(1) space complexity
- When no pivot exists, the permutation is the last one in sequence

## Practice Problems

To strengthen your understanding, try applying this algorithm to solve these problems:

1. Generate all permutations of [1, 2, 3, 4]
2. Find the 10th permutation of [0, 1, 2, 3, 4] without generating all permutations
3. Given a permutation, find its rank in the lexicographical ordering of all permutations

## Visual Comparison of Key Permutation Examples

```
┌───────────────────┬────────────────────┬─────────────────────┐
│ Initial State     │ Next Permutation   │ Description         │
├───────────────────┼────────────────────┼─────────────────────┤
│ [1,2,3]           │ [1,3,2]            │ Simple case         │
├───────────────────┼────────────────────┼─────────────────────┤
│ [3,2,1]           │ [1,2,3]            │ Last permutation    │
│                   │                    │ wraps to first      │
├───────────────────┼────────────────────┼─────────────────────┤
│ [1,3,5,4,2]       │ [1,4,2,3,5]        │ Complex case with   │
│                   │                    │ multiple elements   │
├───────────────────┼────────────────────┼─────────────────────┤
│ [2,3,1,5,4,0]     │ [2,3,4,0,1,5]      │ Another complex     │
│                   │                    │ case                │
└───────────────────┴────────────────────┴─────────────────────┘
```