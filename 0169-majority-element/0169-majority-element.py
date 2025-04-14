class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cand=0
        cnt=0
        n=len(nums)
        for i in range(n):
            if cnt==0:
                cand=nums[i]
            if(cand==nums[i]):
                cnt+=1
            else:
                cnt-=1
        return cand
