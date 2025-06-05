def contiguous_array(nums):
    sum_index_dict = {0:-1}

    max_length = 0


    cur_sum = 0


    for index, num in enumerate(nums):
        cur_sum += 1 if num ==1 else -1

        if cur_sum in sum_index_dict:
            max_length = max(max_length, index - sum_index_dict[cur_sum])
        else:
            sum_index_dict[cur_sum] = index


    return max_length



  


print(contiguous_array( [0,1,1,1,1,1,0,0,0]))