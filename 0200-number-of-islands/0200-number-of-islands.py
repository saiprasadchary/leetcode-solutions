class Solution(object):
    def bfs(self, row, col, grid, ROWS, COLS, visited):        
        dimensions=[(0,1), (1,0), (-1,0), (0,-1)]
        que=deque()
        que.append((row, col))
        while que:
            r,c=que.popleft()
            for ro, co in dimensions:
                nrow=r+ro
                ncol=c+co
                if(0<=nrow<ROWS and 0<=ncol<COLS and grid[nrow][ncol]=="1" and visited[nrow][ncol]==0):
                    visited[nrow][ncol]=1
                    que.append((nrow, ncol))

    def numIslands(self, grid):
        ROWS=len(grid)
        COLS=len(grid[0])
        visited=[]
        for i in range(ROWS):
            visited.append([0 for j in range(COLS)])
        cnt=0
        que=deque()
        for row in range(ROWS):
            for col in range(COLS):
                if(grid[row][col]=="1" and visited[row][col]==0):
                    cnt+=1
                    visited[row][col] = 1  
                    self.bfs(row, col, grid, ROWS, COLS, visited)

        return cnt
