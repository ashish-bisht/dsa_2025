import heapq

def kth_largest(nums, k):
    
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap,num)

        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return nums[0]



print(kth_largest([3,2,1,5,6,4], k = 2))