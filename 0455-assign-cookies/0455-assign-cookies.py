class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i=j=0
        n=len(s)
        m=len(g)
        
        while i<n and j < m:
            if s[i]>=g[j]:
                j+=1
            i+=1
        return j