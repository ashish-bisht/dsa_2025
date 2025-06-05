def can_jump(nums):
    max_reach = 0

    for index in range(len(nums)):
        if index > max_reach:
            return False
        
        max_reach = max(max_reach, index + nums[index])

        if max_reach >= len(nums)-1:
            return True
    return True


print(can_jump([2,3,1,1,4]))