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

        while i<(len(s)) and j < len(g):
            print(i,j)

            if s[i]>=g[j]:
                j+=1

            i+=1
        return j