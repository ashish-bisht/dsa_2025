def min_rotated_sorted_array(nums):
    left = 0
    right = len(nums)-1

    while left < right:
        mid = (left+right)//2

      
        if nums[mid] > nums[right]:
            left = mid+1

        else:
            right = mid

    return nums[left]



print(min_rotated_sorted_array([3,4,5,1,2]))
print(min_rotated_sorted_array([4,5,6,7,0,1,2]))
print(min_rotated_sorted_array([11,13,15,17]))