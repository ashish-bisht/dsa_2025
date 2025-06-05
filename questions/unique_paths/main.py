def unique_paths(m,n):

    memo = {}

    def dfs(row, col):

        if row < 0 or row >= m or col < 0 or col >= n:
            return 0
        
        if row == m-1 and col == n-1:
            return 1
        
        state = (row,col)

        if state in memo:
            return memo[state]
        

        down = dfs(row+1,col)
        right = dfs(row, col+1)


        result = down + right 

        memo[state] = result

        return result
    
    return dfs(0,0)


print(unique_paths(3,7))

