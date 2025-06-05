

def max_subarray(nums):
    max_sum = nums[0]
    cur_sum = nums[0]
    
    for idx in range(1, len(nums)):
        cur_sum = max(nums[idx], cur_sum+nums[idx])
        max_sum = max(cur_sum, max_sum)

    return max_sum


def test_max_subarray():
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([1]) == 1
    assert max_subarray([-1]) == -1
    assert max_subarray([-2, -3, -1, -5]) == -1
    assert max_subarray([1, 2, 3, 4]) == 10
    print("All test cases passed!")

if __name__ == "__main__":
    test_max_subarray()



        


