class Solution(object):


    def dfs_helper(self, candidates, i, subset, target, res):

        #base case
        if i==len(candidates):
            if target==0:
                res.append(subset[:])
            return
        
        # if target<0 or i==len(candidates):
        #     return
        if target>=candidates[i]:
            subset.append(candidates[i])
            self.dfs_helper(candidates, i, subset, target-candidates[i], res)
            subset.pop()


        self.dfs_helper(candidates, i+1, subset, target, res)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        subset=[]
        self.dfs_helper(candidates, 0, subset, target, res)
        return res
        