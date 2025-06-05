class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Handle empty array: if nums is empty, no sequences exist, return 0
        if not nums:
            return 0
        
        # Convert nums to a set for O(1) lookups and to remove duplicates
        # Duplicates don't affect sequence length (e.g., [1,1,2] is same as [1,2])
        # Time: O(n) to create the set, where n is length of nums
        nums_set = set(nums)
        
        # Initialize max_streak to track the longest consecutive sequence
        # Start with 0, as we update it only when we find valid sequences
        max_streak = 0
        
        # Iterate over nums_set (not nums) to process each unique number exactly once
        # This avoids redundant checks for duplicates, preventing TLE
        # Time: O(m) where m is number of unique numbers (m <= n)
        for num in nums_set:
            # Check if num is the start of a sequence (i.e., num-1 is not in set)
            # This ensures we only process the smallest number of each sequence
            # Time: O(1) for set lookup
            if num - 1 not in nums_set:
                # Initialize current number and streak length
                # cur_num tracks the next number in the sequence
                # cur_streak counts the length of the current sequence
                cur_num = num
                cur_streak = 1
                
                # Extend the sequence as long as cur_num + 1 exists in the set
                # Each number is checked at most once across all sequences
                # Time: O(1) per lookup, total O(m) for all while loop iterations
                while cur_num + 1 in nums_set:
                    cur_num += 1
                    cur_streak += 1
                
                # Update max_streak if the current sequence is longer
                # Time: O(1)
                max_streak = max(max_streak, cur_streak)
        
        # Return the length of the longest consecutive sequence
        # If no sequences were found (e.g., all numbers are non-consecutive), max_streak remains 0
        return max_streak