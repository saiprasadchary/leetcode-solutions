class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x==0:
            return 0
        elif x!=0 and n==0:
            return 1
        return x**n