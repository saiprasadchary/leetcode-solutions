class Solution(object):

    def dfs(self, row, col, grid, visited, ROWS, COLS, dimensions):
        visited[row][col]=2
        for r, c in dimensions:
            ro=row+r
            co=col+c
            if 0<=ro<ROWS and 0<=co<COLS and grid[ro][co]==1 and visited[ro][co]==0:
                self.dfs(ro, co, grid, visited, ROWS, COLS, dimensions)
        

    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS=len(grid)
        COLS=len(grid[0])
        visited=[[0]*COLS for _ in range(ROWS)]
        dimensions=[(0,1),(1,0),(-1,0),(0,-1)]

        #boundary traversal to identify the affected one's
        for row in range(ROWS):
            for col in range(COLS):
                if(row==0 or row==ROWS-1 or col==0 or col==COLS-1) and grid[row][col]==1:
                    self.dfs(row, col, grid, visited, ROWS, COLS, dimensions)
        
        cnt=0
        for nr in range(ROWS):
            for nc in range(COLS):
                if grid[nr][nc]==1 and visited[nr][nc]==0:
                    cnt+=1
        return cnt