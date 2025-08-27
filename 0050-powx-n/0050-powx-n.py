class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def helper(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            
            res=helper(x, n//2)
            res=res*res
            return res if n%2==0 else x*res

        res=helper(x, abs(n))
        return res if n>0 else 1/res




        # the common solution that comes is:
        # if x==0:
        #     return 0
        # if n==0:
        #     return 1
        # return x**n