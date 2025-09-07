class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res=[]
        if not digits:
            return res
        digitsToChar={
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs_helper(ind, subset):
            if len(subset)==len(digits):
                res.append("".join(subset))
                return

            for ch in digitsToChar[digits[ind]]:
                subset.append(ch)
                dfs_helper(ind+1, subset)
                subset.pop()

        subset=[]
        dfs_helper(0, subset)
        return res

        




