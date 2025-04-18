class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=r=0
        n=len(nums)
        wind_sum=0
        left=0
        maxSum=0
        freq={}

        while r<n:

            freq[nums[r]]=freq.get(nums[r], 0)+1
 
            wind_sum+=nums[r]
            
            while freq[nums[r]]>1:
                freq[nums[left]]-=1
                wind_sum-=nums[left]
                if(freq[nums[left]]==0):
                    del freq[nums[left]]
                left+=1
            if(r-left+1==len(freq)):
                maxSum=max(maxSum, wind_sum)
            r+=1

        return maxSum

