class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n=len(num)
        even=odd=0
        for i in range(n):
            if i%2==0:
                even+=int(num[i])
            else:
                odd+=int(num[i])
        
        return even==odd
        