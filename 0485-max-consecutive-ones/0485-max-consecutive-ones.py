class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=r=0
        zeros=0
        maxLen=0
        n=len(nums)
        while r<n:
            if(nums[r]==0):
                zeros+=1
            
            if zeros>=1:
                if(nums[l]==0):
                    zeros-=1
                l+=1
            if(zeros==0):
                maxLen=max(maxLen, r-l+1)
            r+=1
        return maxLen
        