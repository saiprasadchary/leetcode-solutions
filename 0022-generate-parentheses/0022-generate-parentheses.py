class Solution(object):

    def helper(self,n, opened, closed, curr, res):
        if opened ==0 and closed==0:
            res.append(curr)
        
        if opened:          
            self.helper(n, opened-1, closed, curr+"(", res)
        
        if curr and curr[-1]==")" and opened==closed:
            pass

        elif curr and curr[-1]==")" and opened<closed:
            self.helper(n, opened, closed-1, curr+")", res)

        elif curr and closed:
            self.helper(n, opened, closed-1, curr+")", res)


    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        opened=n
        closed=n
        curr=""
        res=[]
        self.helper(n, opened, closed, curr, res)
        return res

         
        