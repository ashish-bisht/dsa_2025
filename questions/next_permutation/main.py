

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modifies nums in-place to produce the next lexicographically greater permutation.
        If no such permutation exists, reverses nums to the smallest permutation.
        """
        # Step 1: Find the first element from the right that is smaller than the next element
        # This identifies the point where the sequence stops being non-increasing
        break_point = len(nums) - 1
        while break_point > 0 and nums[break_point - 1] >= nums[break_point]:
            break_point -= 1

        # Step 2: If a break point is found, swap the element before it with the smallest
        # element to its right that is larger, to create a slightly larger prefix
        if break_point > 0:
            next_larger_index = len(nums) - 1
            while next_larger_index >= break_point and nums[next_larger_index] <= nums[break_point - 1]:
                next_larger_index -= 1
            nums[break_point - 1], nums[next_larger_index] = nums[next_larger_index], nums[break_point - 1]

        # Step 3: Reverse the subarray after the break point to get the smallest possible suffix
        # This ensures the overall permutation is the smallest possible next permutation
        left = break_point
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1