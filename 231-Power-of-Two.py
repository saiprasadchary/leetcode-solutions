class Solution(object):
    def isPowerOfTwo(self, n):
        \\\
        :type n: int
        :rtype: bool
        \\\
        return n > 0 and (n & (n - 1)) == 0
        # p2=1;
        # if n==1:
        #     return True;
        # for i in range(n//2+1):
        #     if n==p2:
        #         return True;
        #     p2*=2
        # return False        