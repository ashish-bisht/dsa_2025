
**Constraints**:
- `1 <= nums.length <= 300`
- `nums[i]` is either `0`, `1`, or `2`.

## Intuition
The problem involves sorting an array with only three distinct values (`0`, `1`, `2`) in-place. A naive approach like counting sort requires extra space, which we want to avoid. The **Dutch National Flag algorithm** is perfect, as it uses three pointers to partition the array into three sections:
- All `0`s (red) at the start.
- All `1`s (white) in the middle.
- All `2`s (blue) at the end.

We use three pointers named `left`, `cur`, and `right`:
- `left`: Everything before `left` is `0`.
- `cur`: Scans the array, deciding where each element belongs.
- `right`: Everything after `right` is `2`.

By swapping elements based on the value at `cur`, we sort the array in one pass.

## Approach
1. Initialize pointers:
   - `left = 0`: Next position for a `0`.
   - `cur = 0`: Current element being checked.
   - `right = len(nums) - 1`: Next position for a `2`.
2. While `cur <= right`:
   - If `nums[cur] == 0`:
     - Swap `nums[cur]` with `nums[left]` to place the `0` in the red section.
     - Increment `left` and `cur`.
   - If `nums[cur] == 2`:
     - Swap `nums[cur]` with `nums[right]` to place the `2` in the blue section.
     - Decrement `right` (don’t increment `cur` to check the swapped element).
   - If `nums[cur] == 1`:
     - Increment `cur` (no swap needed, as `1` belongs in the middle).
3. Stop when `cur > right`, at which point the array is sorted.

### Alternative Implementation
The user-provided code included additional checks:
- After swapping a `0`, increment `cur` only if `cur == left`.
- After swapping a `2`, increment `cur` only if `cur == right`.
These checks aim to skip redundant processing when `cur` is at a boundary but are unnecessary. The standard approach (used in `main.py`) always increments `cur` after a `0` swap and never after a `2` swap, simplifying the logic without affecting correctness.

### Deep Dive into Pointers
Pointers are the **crux** of this solution. Let’s analyze their roles and why we manipulate them:

- **`left` Pointer**:
  - **Purpose**: Ensures all elements before `left` are `0`s (red section).
  - **Movement**: Increments after swapping a `0` to `nums[left]`, expanding the red section.
  - **Why?**: The swapped `0` is correctly placed, and `left` moves to the next position for a future `0`. The element swapped to `cur` is either a `1` or a processed `0`, so incrementing `cur` is safe.

- **`cur` Pointer**:
  - **Purpose**: Scans the array, examining each element to decide its placement.
  - **Movement**:
    - Increments after `nums[cur] == 1` (correct position).
    - Increments after `nums[cur] == 0` (after swap, as the new element at `cur` is processed).
    - Stays put after `nums[cur] == 2` (to check the element swapped from `right`).
  - **Why not increment after `2`?**: The element swapped from `right` could be a `0`, `1`, or `2`, so we must recheck it. This is the **main crux**—ensuring swapped elements are processed correctly.
  - **Alternative Code’s Conditions**:
    - The `if cur == left` check increments `cur` when swapping with itself, avoiding rechecking a known `0`. However, incrementing `cur` always is safe, as the swapped element is processed.
    - The `if cur == right` check increments `cur` after placing a `2`, but keeping `cur` static is better to check the swapped element.
    - These conditions add complexity without significant benefit, as the standard logic handles edge cases naturally.

- **`right` Pointer**:
  - **Purpose**: Ensures all elements after `right` are `2`s (blue section).
  - **Movement**: Decrements after swapping a `2` to `nums[right]`, shrinking the blue section.
  - **Why?**: The swapped `2` is correctly placed, and `right` moves to the next position for a future `2`.

- **Main Crux**:
  - The algorithm’s efficiency comes from partitioning the array in one pass with in-place swaps.
  - The critical decision is not incrementing `cur` after a `2` swap, ensuring the swapped element is checked. This prevents misplacing elements like a `0` swapped from `right`.
  - The `left`, `cur`, `right` names intuitively reflect the partitioning: `left` anchors the start, `right` the end, and `cur` navigates the middle.

## Code Walkthrough
```python
left = 0
cur = 0
right = len(nums) - 1