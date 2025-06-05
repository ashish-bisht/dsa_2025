# Mastering Binary Search: Common Patterns and Applications

Binary search is a powerful algorithm that goes far beyond just searching for elements in a sorted array. This guide will help you identify common patterns where binary search can be applied and provide concrete examples so you can recognize these patterns during interviews.

## Table of Contents
1. [Core Binary Search Concept](#core-binary-search-concept)
2. [Pattern 1: Classic Sorted Array Search](#pattern-1-classic-sorted-array-search)
3. [Pattern 2: Finding Boundary Points](#pattern-2-finding-boundary-points)
4. [Pattern 3: Search in Rotated/Modified Sorted Arrays](#pattern-3-search-in-rotatedmodified-sorted-arrays)
5. [Pattern 4: Optimization Problems with Monotonic Functions](#pattern-4-optimization-problems-with-monotonic-functions)
6. [Pattern 5: Search in 2D Sorted Matrices](#pattern-5-search-in-2d-sorted-matrices)
7. [Pattern 6: Finding Peak Elements](#pattern-6-finding-peak-elements)
8. [Pattern 7: Capacity Allocation Problems](#pattern-7-capacity-allocation-problems)
9. [Pattern 8: Square Root and Nth Root Problems](#pattern-8-square-root-and-nth-root-problems)
10. [Common Pitfalls and Mistakes](#common-pitfalls-and-mistakes)
11. [Recognizing Binary Search Opportunities](#recognizing-binary-search-opportunities)

## Core Binary Search Concept

Binary search is fundamentally about efficiently eliminating half of the search space at each step. Its time complexity is O(log n), making it extremely efficient for large datasets.

**Prerequisites for using binary search:**
1. The search space can be represented as a range (often an array or a numerical range)
2. There is a way to determine if a mid-point is too high, too low, or just right
3. After checking a mid-point, you can eliminate a portion of the search space

## Pattern 1: Classic Sorted Array Search

**Description:** Find a target element in a sorted array.

**Example Problem:** Find if element K exists in sorted array A.

```python
def binary_search(array, target):
    left, right = 0, len(array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if array[mid] == target:
            return mid  # Found the target
        elif array[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
            
    return -1  # Target not found
```

**How to Recognize:**
- You're asked to find a specific value in a sorted collection
- The problem constraints mention large array sizes (suggesting O(log n) is needed)
- The problem explicitly mentions a sorted array

## Pattern 2: Finding Boundary Points

**Description:** Find the boundary between elements that satisfy a condition and elements that don't.

**Example Problem:** Find the first or last occurrence of an element in a sorted array with duplicates.

```python
def find_first_occurrence(array, target):
    left, right = 0, len(array) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if array[mid] == target:
            result = mid  # Found a match, but continue searching left
            right = mid - 1
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return result
```

**How to Recognize:**
- You need to find the first/last element that satisfies a condition
- The elements in the search space have a clear ordering
- The problem involves finding a threshold or boundary

## Pattern 3: Search in Rotated/Modified Sorted Arrays

**Description:** Search in arrays that are mostly sorted but with some modification, like rotation.

**Example Problem:** Find a target in a sorted and rotated array.

```python
def search_rotated(array, target):
    left, right = 0, len(array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if array[mid] == target:
            return mid
            
        # Check which half is normally ordered
        if array[left] <= array[mid]:  # Left half is ordered
            if array[left] <= target < array[mid]:
                right = mid - 1  # Target is in the left half
            else:
                left = mid + 1   # Target is in the right half
        else:  # Right half is ordered
            if array[mid] < target <= array[right]:
                left = mid + 1   # Target is in the right half
            else:
                right = mid - 1  # Target is in the left half
                
    return -1
```

**How to Recognize:**
- Array is "almost" sorted but with some twist (rotated, has a pattern)
- Problem involves finding an element in such an array
- The array still maintains some ordered property we can leverage

## Pattern 4: Optimization Problems with Monotonic Functions

**Description:** Find the optimal value that satisfies a condition, where the function is monotonic.

**Example Problem:** The "Cutting Wood" problem we just solved.

```python
def find_optimal_cutter_height(tree_heights, required_wood):
    left_height = 0
    right_height = max(tree_heights)
    optimal_height = 0
    
    while left_height <= right_height:
        mid_height = (left_height + right_height) // 2
        wood_cut = calculate_wood_cut(tree_heights, mid_height)
        
        if wood_cut >= required_wood:
            optimal_height = mid_height
            left_height = mid_height + 1  # Try higher heights
        else:
            right_height = mid_height - 1  # Try lower heights
    
    return optimal_height
```

**How to Recognize:**
- Problem asks for minimum/maximum value satisfying a condition
- Checking a value tells you about all values on one side (monotonicity)
- Search space is typically a range of possible answers, not an array
- Terms like "minimize the maximum" or "maximize the minimum" appear
- Often seen in resource allocation problems

## Pattern 5: Search in 2D Sorted Matrices

**Description:** Find an element in a matrix where rows and columns are sorted.

**Example Problem:** Search in a matrix where each row is sorted left to right and each column is sorted top to bottom.

```python
def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
        
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1  # Start from top-right corner
    
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1  # Move left
        else:
            row += 1  # Move down
            
    return False
```

**How to Recognize:**
- Problem involves a 2D matrix with sorted rows and/or columns
- You need to find an element or count elements satisfying a condition
- The search space can be reduced based on the sorted property

## Pattern 6: Finding Peak Elements

**Description:** Find a peak element (an element greater than or equal to its neighbors) in an array.

**Example Problem:** Find any peak element in an unsorted array where adjacent elements are different.

```python
def find_peak_element(array):
    left, right = 0, len(array) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if array[mid] > array[mid + 1]:
            # Peak is in the left half (including mid)
            right = mid
        else:
            # Peak is in the right half
            left = mid + 1
            
    return left  # This will be a peak
```

**How to Recognize:**
- Problem asks for a "peak," "local maximum," or "local minimum"
- The array isn't necessarily sorted
- The condition checks the relationship between adjacent elements

## Pattern 7: Capacity Allocation Problems

**Description:** Find the minimum capacity needed to complete a task under constraints.

**Example Problem:** Allocate minimum capacity to complete N tasks in D days (like leetcode's "Capacity to Ship Packages").

```python
def min_capacity(weights, days):
    def can_ship(capacity):
        days_needed = 1
        current_weight = 0
        
        for weight in weights:
            if current_weight + weight > capacity:
                days_needed += 1
                current_weight = weight
            else:
                current_weight += weight
                
        return days_needed <= days
    
    left = max(weights)  # Minimum capacity needed
    right = sum(weights)  # Maximum capacity needed
    
    while left < right:
        mid = (left + right) // 2
        
        if can_ship(mid):
            right = mid  # Try smaller capacity
        else:
            left = mid + 1  # Need larger capacity
            
    return left
```

**How to Recognize:**
- Problem involves allocating resources or capacity
- You need to minimize or maximize some value
- There's a clear feasibility check for a given value
- The function is monotonic (if capacity X works, any larger capacity also works)

## Pattern 8: Square Root and Nth Root Problems

**Description:** Find the square root or nth root of a number without using built-in functions.

**Example Problem:** Find the integer square root of a number.

```python
def int_sqrt(x):
    if x <= 1:
        return x
        
    left, right = 1, x // 2
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
            
    return right  # Return the floor of the square root
```

**How to Recognize:**
- Problem asks for computing root without using built-in functions
- Requires high precision or dealing with very large numbers
- Involves finding a value where a monotonic function crosses a threshold

## Common Pitfalls and Mistakes

1. **Getting stuck in infinite loops**: Always ensure your termination condition is correct and that you're properly narrowing the search space.

2. **Off-by-one errors**: Be careful with your boundaries, especially when deciding whether to use `mid`, `mid+1`, or `mid-1`.

3. **Integer overflow**: When calculating mid, use `mid = left + (right - left) // 2` instead of `(left + right) // 2` to prevent potential overflow in some languages.

4. **Not handling edge cases**: Remember to handle empty arrays, single-element arrays, and other special cases.

5. **Using the wrong search condition**: Make sure your condition correctly divides the search space based on the problem requirements.

## Recognizing Binary Search Opportunities

Look for these clues to identify binary search opportunities:

1. **The search space is ordered or can be ordered**: Either fully sorted, partially sorted, or following some pattern.

2. **Monotonicity exists**: If a condition is true for X, it's true for all values greater/less than X.

3. **You need an O(log n) solution**: The problem constraints hint at needing something faster than O(n).

4. **The problem involves finding a specific value or threshold**: You're looking for an exact match or the first/last element satisfying a condition.

5. **Min-max or max-min optimization**: Problems asking to minimize the maximum or maximize the minimum of something.

6. **Language clues**: Terms like "efficient search," "minimum feasible value," or "find the boundary."

7. **The naive solution is clearly O(n) or worse**: Suggesting a more efficient approach is needed.

## Example 1: Minimum Waiting Time Problem

**Problem:** Given service times for N customers, find the minimum waiting time such that all customers can be served within M minutes.

**Analysis:**
- For any waiting time W, we can check if it's feasible
- As W increases, more customers can be served
- We want the minimum W that satisfies the condition

**Solution using Binary Search:**
```python
def min_waiting_time(service_times, max_minutes):
    def can_serve_all(waiting_time):
        servers_needed = 1
        current_time = 0
        
        for time in service_times:
            if current_time + time > waiting_time:
                servers_needed += 1
                current_time = time
            else:
                current_time += time
                
        return servers_needed <= max_minutes
    
    left = max(service_times)
    right = sum(service_times)
    
    while left < right:
        mid = (left + right) // 2
        
        if can_serve_all(mid):
            right = mid  # Try smaller waiting time
        else:
            left = mid + 1  # Need larger waiting time
            
    return left
```

## Example 2: Koko Eating Bananas

**Problem:** Koko can eat N piles of bananas, where pile[i] has pile[i] bananas. She eats K bananas per hour. Find the minimum K such that she can eat all bananas within H hours.

**Analysis:**
- For any eating speed K, we can calculate the time needed
- As K increases, the time needed decreases (monotonic)
- We want the minimum K that works within H hours

**Solution using Binary Search:**
```python
def min_eating_speed(piles, h):
    def can_finish(speed):
        time_needed = 0
        for pile in piles:
            # Ceiling division
            time_needed += (pile + speed - 1) // speed
        return time_needed <= h
    
    left = 1
    right = max(piles)
    
    while left < right:
        mid = (left + right) // 2
        
        if can_finish(mid):
            right = mid  # Try smaller speed
        else:
            left = mid + 1  # Need larger speed
            
    return left
```

## Conclusion

Binary search is a versatile algorithm that can be applied to a wide range of problems beyond just searching in sorted arrays. By recognizing these common patterns, you'll be better equipped to identify when binary search is the right approach, even when the problem doesn't explicitly mention sorting or searching.

Remember the key insight: binary search works when you can eliminate half of your search space with each comparison, which happens when you have monotonic functions or ordered search spaces.

With practice, you'll develop an intuition for identifying binary search opportunities and be able to solve complex problems efficiently.