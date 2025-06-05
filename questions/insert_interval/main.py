def insert_inerval(intervals, newInterval):
    if not intervals:
        return newInterval
    
    for interval in intervals:
        if interval[1] >= newInterval[0]:
            interval[1] = max(interval[1], newInterval[0])
            break

    
    # now we merge intervals .

    res = [intervals[0]]

    for interval in intervals:
        last_interval = res[-1]

        if interval[1] <= last_interval[1]:
            last_interval[1] = max(last_interval[1], interval[1])

        else:
            res.append(interval)


    return res


print(insert_inerval(intervals = [[1,3],[6,9]], newInterval = [2,5]))
print(insert_inerval(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))