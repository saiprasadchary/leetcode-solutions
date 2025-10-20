
from collections import deque
class Solution(object):

    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS=len(grid)
        COLS=len(grid[0])
        fresh_orange_cnt=0
        que=deque()

        for row in range(ROWS):
            for cols in range(COLS):
                if(grid[row][cols]==1):
                    fresh_orange_cnt+=1
                if(grid[row][cols]==2):
                    que.append((row, cols))
        #print(que, fresh_orange_cnt)

        dimensions=[(-1, 0), (0,1), (1,0), (0, -1)]

        size_level=len(que)
        time=0
    
        while que and fresh_orange_cnt:
            for _ in range(len(que)):   # here the len(que) becomes fixed for the first instance of elements in the que, even though the values are append after, it doesn't get affected.
                r, c = que.popleft()
                for ro, co in dimensions:
                    if 0 <= r + ro < ROWS and 0 <= c + co < COLS and grid[r + ro][c + co] == 1:
                        que.append((r + ro, c + co))
                        grid[r + ro][c + co] = 2
                        fresh_orange_cnt -= 1
            time += 1  # after one full layer (minute)
        
        if(fresh_orange_cnt==0):
            return time
        else:
            return -1
