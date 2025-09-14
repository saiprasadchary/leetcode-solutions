class Solution(object):

    # def isSafe(self, row, col, board, n):
    #     dupRow=row
    #     dupCol=col
    #     #upper diagonal left check
    #     while row>= 0 and col >= 0:
    #         if board[row][col]=='Q':
    #             return False
    #         row-=1
    #         col-=1
    #     #left check
    #     col=dupCol
    #     row=dupRow
    #     while col>=0:
    #         if board[row][col]=="Q":
    #             return False
    #         col-=1
    #     #lower diagonal left check
    #     col=dupCol
    #     row=dupRow  
    #     while row < n and col >= 0:
    #         if board[row][col]=="Q":
    #             return False
    #         row+=1
    #         col-=1     
    #     return True

    def dfs(self, col, board, n, res, leftRow, upperDiagonal, lowerDiagonal):
        #base case
        if col ==n:
            res.append([''.join(row) for row in board])
            return
        
        for row in range(n):
            if leftRow[row]==0 and lowerDiagonal[row+col]==0 and upperDiagonal[n-1 + col-row]==0:
                board[row][col]= "Q"
                leftRow[row]=1
                lowerDiagonal[row+col]=1
                upperDiagonal[n-1 + col - row]=1
                self.dfs(col+1, board, n, res, leftRow, upperDiagonal, lowerDiagonal)

                #backtracking
                board[row][col]="."
                leftRow[row]=0
                lowerDiagonal[row+col]=0
                upperDiagonal[n-1 + col - row]=0


    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res=[]
        sublist=[]
        board=[]

        for i in range(n):
            board.append(["."]*n)
        
        leftRow=[0]*n
        lowerDiagonal = [0] * (2 * n - 1)
        upperDiagonal = [0] * (2 * n - 1)

        self.dfs(0, board, n, res, leftRow, upperDiagonal, lowerDiagonal)
        return res
        