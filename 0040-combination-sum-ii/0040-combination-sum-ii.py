class Solution(object):


    def dfs_helper(self, candidates, i, sublist, res, target):
        if target==0:
            res.append(sublist[:])
            return
        
        for ind in range(i, len(candidates)):
            if i<ind and candidates[ind]==candidates[ind-1]:
                continue
            
            if candidates[ind]>target:
                break

            sublist.append(candidates[ind])

            self.dfs_helper(candidates, ind+1, sublist, res, target-candidates[ind])

            sublist.pop()

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        sublist=[]
        candidates.sort()

        self.dfs_helper(candidates, 0, sublist, res, target)
        return res
        