

def permutation(nums):

    result = []
    # nums_len = len(nums)
    def bactrack(nums, cur_path):

        if not nums:
            result.append(cur_path)
            return

        for index in range(len(nums)):
           bactrack(nums[:index]+ nums[index+1:], cur_path + [nums[index]])

    bactrack(nums, [])
    return result


print(permutation([1,2,3]))

def permutaion2(nums):
    result = []

    nums_len = len(nums)
