class Solution(object):

    def dfs_helper(self, element, arr, subset, res, total, k):
        if len(subset)==k:
            if total==0:
                res.append(subset[:])
            else:
                return

        
        for ele in range(element, len(arr)+1):

            if ele<=total:
                subset.append(ele)
                self.dfs_helper(ele+1, arr, subset, res, total-ele, k)
                subset.pop()


    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res=[]
        subset=[]
        arr=[1,2,3,4,5,6,7,8,9]
        self.dfs_helper(1, arr, subset, res, n, k)
        return res
        