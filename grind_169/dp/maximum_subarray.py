def max_subarray(nums):
    max_sum = nums[0]
    dp = [0] * len(nums)

    dp[0] = nums[0]

    for index in range(1,len(nums)):
        dp[index] = max(nums[index], nums[index]+dp[index-1])
        max_sum = max(max_sum, dp[index])
    return max_sum

print(max_subarray(nums = [-2,1,-3,4,-1,2,1,-5,4]))
