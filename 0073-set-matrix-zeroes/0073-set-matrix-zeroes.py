class Solution(object):

    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        col0 = 1  # Indicates whether the first column needs to be zeroed

        # Mark the rows and columns to be zeroed
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark the ith row
                    if j == 0:
                        col0 = 0  # Special handling for the first column
                    else:
                        matrix[0][j] = 0  # Mark the jth column
        
        # Zero out cells based on marks in the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Zero out the first row if necessary
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        
        # Zero out the first column if necessary
        if col0 == 0:
            for i in range(m):
                matrix[i][0] = 0

        return matrix


      


       
