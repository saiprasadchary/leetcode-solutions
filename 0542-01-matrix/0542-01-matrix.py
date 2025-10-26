class Solution(object):
    from collections import deque
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        ROWS=len(mat)
        COLS=len(mat[0])
        visited=[]
        res=[]

        for _ in range(ROWS):
            visited.append([0]*COLS)
            res.append([0]*COLS)

        que=deque()
        level=0

        # traversing to find what is needed to be nearest i.e 0, and dumping into que
        for row in range(ROWS):
            for col in range(COLS):
                if mat[row][col]==0:
                    que.append((row, col, level))
                    visited[row][col]=1
        dimensions=[(0,1), (1,0), (-1,0), (0, -1)]
        while que:
            r, c, level = que.popleft()
            for ro, co in dimensions:
                nrow=ro+r
                ncol=co+c
                if 0<=nrow<ROWS and 0<=ncol<COLS and visited[nrow][ncol]==0:
                    visited[nrow][ncol]=1
                    res[nrow][ncol]=level+1
                    que.append((nrow, ncol, level+1))
        return res
                


                