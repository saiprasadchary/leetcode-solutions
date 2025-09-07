class Solution(object):

    def IsPalindrome(self, partitions):
        n=len(partitions)
        for i in range(n//2):
            if(partitions[i]!=partitions[n-i-1]):
                return False
        return True

    def dfs_helper(self, ind, s, substr, res):

        if(ind==len(s)):
            res.append(substr[:])
            return

        for i in range(ind, len(s)):
            partitions=s[ind:i+1]

            if self.IsPalindrome(partitions):
                substr.append(partitions)
                self.dfs_helper(i+1, s, substr, res)
                substr.pop()
        
        
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res=[]
        substr=[]
        self.dfs_helper(0, s, substr, res)
        return res

        