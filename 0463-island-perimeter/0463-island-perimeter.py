class Solution(object):
    def dfs(self, r, c, ROW, COL, grid):
        sides=0
        dimensions=[(1,0), (0,1), (-1, 0), (0, -1)]
        for ro, co in dimensions:
            nrow=ro+r
            ncol=co+c
            if nrow < 0 or nrow >= ROW or ncol < 0 or ncol >= COL:
                sides += 1
                print(sides, "hi")
            elif grid[nrow][ncol]==0:
                sides+=1
            
        return sides
            
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS=len(grid)
        COLS=len(grid[0])
        cnt=0
        sides=0

        for row in range(ROWS):
            for col in range(COLS):
                if(grid[row][col]==1):
                    sides+=self.dfs(row, col, ROWS, COLS, grid)
                    
        return sides