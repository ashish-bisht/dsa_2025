# Sort Colors
# Difficulty: Medium
# LeetCode Link: https://leetcode.com/problems/sort-colors
# Description:
# Given an array nums with n objects colored red, white, or blue, sort them in-place
# so that objects of the same color are adjacent, with the colors in the order red,
# white, and blue. We will use the integers 0, 1, and 2 to represent the color red,
# white, and blue, respectively. You must solve this problem without using the
# library's sort function.

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Sorts an array of 0s, 1s, and 2s in-place using the Dutch National Flag algorithm.
        Args:
            nums: List of integers representing colors (0 = red, 1 = white, 2 = blue).
        Returns:
            None: Modifies nums in-place.
        """
        # Initialize three pointers:
        # left: everything before left is 0 (red)
        # cur: scans the array, processing each element
        # right: everything after right is 2 (blue)
        left = 0
        cur = 0
        right = len(nums) - 1

        # Continue until cur pointer crosses right pointer
        while cur <= right:
            if nums[cur] == 0:
                # Swap with left to place 0 in red section
                nums[left], nums[cur] = nums[cur], nums[left]
                left += 1
                cur += 1
            elif nums[cur] == 2:
                # Swap with right to place 2 in blue section
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1
                # Do not increment cur, as swapped element needs checking
            else:  # nums[cur] == 1
                # 1 is in correct section, move cur forward
                cur += 1

# Test cases for local verification
if __name__ == "__main__":
    # Test case 1: Mixed colors
    nums1 = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums1)
    print(f"Test 1: {nums1}")  # Expected: [0, 0, 1, 1, 1, 2]

    # Test case 2: Small mixed array
    nums2 = [2, 0, 1]
    Solution().sortColors(nums2)
    print(f"Test 2: {nums2}")  # Expected: [0, 1, 2]

    # Test case 3: All same color
    nums3 = [1, 1, 1]
    Solution().sortColors(nums3)
    print(f"Test 3: {nums3}")  # Expected: [1, 1, 1]

    # Test case 4: Single element
    nums4 = [2]
    Solution().sortColors(nums4)
    print(f"Test 4: {nums4}")  # Expected: [2]