class Solution(object):

    def dfs_helper(self, board, r, c, word, wi):
        #base case: VALID
        if wi==len(word):
            return True
        m_rows=len(board)
        n_cols=len(board[0])

        # INVALID-1 #edge cases if the pointed char has no where to go at the edge cases:
        if(r==m_rows or r<0 or c==n_cols or c<0):
            return False
        
        # INVALID-2 # if the visited value is seen, and the pointeed value != word char
        if(board[r][c]==" " or board[r][c]!=word[wi]):
            return False
        
        #main case
        ch=board[r][c]
        board[r][c]=" "

        found=(self.dfs_helper(board, r+1, c, word, wi+1) or self.dfs_helper(board, r-1, c, word, wi+1) or self.dfs_helper(board, r, c+1, word, wi+1) or self.dfs_helper(board, r, c-1, word, wi+1))
        #backtracking
        board[r][c]=ch
        return found

    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m_rows=len(board)
        n_cols=len(board[0])
        #picking each and every value of the board in a brute force way 
        #to check if the word sequence exists
        for r in range(m_rows):
            for c in range(n_cols):
                if self.dfs_helper(board, r, c, word, 0)== True:
                    return True
        return False
