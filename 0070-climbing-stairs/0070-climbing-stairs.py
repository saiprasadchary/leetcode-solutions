class Solution(object):

    def __init__(self):
            self.mem={1:1,2:2};    

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n not in self.mem:
            self.mem[n]=self.climbStairs(n-1)+self.climbStairs(n-2);
        return self.mem[n]

                