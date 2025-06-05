def merge_interval(intervals):
    if not intervals or len(intervals) <= 1:
        return intervals
    
    intervals.sort(key= lambda x:x[0])

    res = [intervals[0]]

    for index in range(1, len(intervals)):
        last_merged_interval = res[-1]
        cur_interval = intervals[index]
        if last_merged_interval[1] >= cur_interval[0]:
            last_merged_interval[1] = max(last_merged_interval[1], cur_interval[1])

        else:
            res.append(cur_interval)


    return res

    



print(merge_interval(intervals = [[1,3],[2,6],[8,10],[15,18]]))