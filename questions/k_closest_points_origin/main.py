import heapq

def k_closest(points, k):
    heap = []

    for point in points:
        x,y = point

        heapq.heappush(heap, ((x*x + y*y), point))

    
    return  [heapq.heappop(heap)[1] for _ in range(k)]


print(k_closest([[1,3],[-2,2]],1))
print(k_closest([[3,3],[5,-1],[-2,4]],2))