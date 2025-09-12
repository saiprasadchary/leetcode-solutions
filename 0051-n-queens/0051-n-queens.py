class Solution(object):

    def isSafe(self, row, col, board, n):
        dupRow=row
        dupCol=col
        while row>= 0 and col >= 0:
            if board[row][col]=='Q':
                return False
            row-=1
            col-=1
        
        col=dupCol
        row=dupRow
        while col>=0:
            if board[row][col]=="Q":
                return False
            col-=1

        col=dupCol
        row=dupRow  
        while row < n and col >= 0:
            if board[row][col]=="Q":
                return False
            row+=1
            col-=1     
        return True

    def dfs(self, col, board, n, res):
        #base case
        if col ==n:
            res.append([''.join(row) for row in board])
            return
        
        for row in range(n):
            if self.isSafe(row, col, board, n):
                board[row][col]= "Q"
                self.dfs(col+1, board, n, res)

                #backtracking
                board[row][col]="."

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res=[]
        sublist=[]
        board=[]

        for i in range(n):
            temp=[]
            for j in range(n):
                temp.append(".")
            board.append(temp)
        
        self.dfs(0, board, n, res)
        return res
        