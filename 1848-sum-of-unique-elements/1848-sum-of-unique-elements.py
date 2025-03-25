class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        n=len(nums)
        for i in range(n):
            freq[nums[i]]=freq.get(nums[i],0)+1
        sum1=0
        for ele, val in freq.items():
            if(val ==1):
                sum1+=ele
        return sum1

        