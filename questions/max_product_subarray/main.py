def max_product_subarray(nums):
    if not nums:
        return 0
    min_so_far = nums[0]
    max_so_far = nums[0]
    max_of_max = nums[0]


    for index in range(1, len(nums)):
        cur_num = nums[index]
        temp_max = max_so_far
        max_so_far = max(cur_num, max(temp_max * cur_num, cur_num * min_so_far))
        min_so_far = min(cur_num, min(min_so_far * cur_num, temp_max * cur_num))

        max_of_max = max(max_of_max, max_so_far)

    return max_of_max


print(max_product_subarray( [2,3,-2,4]))
    
