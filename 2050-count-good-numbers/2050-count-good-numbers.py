class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        def dfs(pos, x):
            if pos==0:
                return 1
            if pos==1:
                return int(x*pos)
            res=dfs(pos//2, x)
            res=(res*res)%MOD
            return res if pos%2==0 else (x*res)%MOD
        

        evenPos=(n+1)//2
        oddPos=n//2
        res=dfs(evenPos, 5)*dfs(oddPos, 4)
        return res%MOD