class Solution(object):

    def dfs(self, s, wordDict, ind, memo):
        if(ind==len(s)):
            return True
        if ind in memo:
            return memo[ind]
        
        for i in range(ind, len(s)):
            if(s[ind:i+1] in wordDict):
                #print(s[ind:i+1])
                if self.dfs(s, wordDict, i+1, memo):
                    memo[ind]=1
                    return True
        memo[ind]=0
        return False


    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        #using the memoization for optimal approach
        return self.dfs(s, wordDict, 0, {})

        