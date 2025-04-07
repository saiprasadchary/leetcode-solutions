class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        uniq=[]
        res=[]
        n=len(arr)
        
        nums=set(arr)
        uniq=sorted(nums)

        freq={}
        for ind, val in enumerate(uniq):
            freq[val]=ind+1
        
        for k in range(n):
            res.append(freq[arr[k]])
        return res



        