class Solution(object):
    def dfs(self, row, col, board, visited, ROWS, COLS, dimensions):
        visited[row][col]=2
        for ro, co in dimensions:
            nrow=ro+row
            ncol=co+col
            if 0<=nrow<ROWS and 0<=ncol<COLS and board[nrow][ncol]=="O" and visited[nrow][ncol]==0:
                self.dfs(nrow, ncol, board, visited, ROWS, COLS, dimensions)


    def solve(self, board):
        ROWS=len(board)
        COLS=len(board[0])
        visited=[[0]*COLS for _ in range(ROWS)]
        dimensions=[(0,1), (1,0), (-1,0), (0, -1)]

        for row in range(ROWS):
            for col in range(COLS):
                if (row==0 or row==ROWS-1) or (col==0 or col==COLS-1):
                    if board[row][col]=="O":
                        self.dfs(row, col,board, visited, ROWS, COLS, dimensions)
        for nr in range(ROWS):
            for nc in range(COLS):
                if visited[nr][nc]==2:
                    board[nr][nc]="O"
                else:
                    board[nr][nc]="X"
        # print(visited)
        # print(board)
        





