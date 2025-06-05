grid = [[2,1,1],[1,1,0],[0,1,1]]

from collections import deque

def rotten_oranges(grid):
    
    que = deque()
    fresh_oranges = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):

            if grid[row][col] == 1:
                fresh_oranges +=1

            if grid[row][col] == 2:
                que.append((row,col))

    if fresh_oranges == 0:
        return 0
    


    minutes = 0
    directions = ((-1,0), (1,0), (0,-1), (0,1))
    while que and fresh_oranges > 0:
       
       

    
        # check all directions
        #up, down, left, right
        for _ in range(len(que)):
            cur_row , cur_col = que.popleft()


            for dr_row, dr_col in directions:
                new_row, new_col = cur_row+dr_row, cur_col+dr_col

                if( 0 <= new_row <len(grid) and 
                    0 <= new_col <len(grid[0]) and 
                    grid[new_row][new_col] == 1) :
                    grid[new_row][new_col] = 2
                    fresh_oranges -=1
                    que.append((new_row,new_col))
                
        minutes +=1

    
    return minutes if fresh_oranges == 0 else -1
    

print(rotten_oranges([[2,1,1],[1,1,0],[0,1,1]]))
print(rotten_oranges( [[2,1,1],[0,1,1],[1,0,1]]))

