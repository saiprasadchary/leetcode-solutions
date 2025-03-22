class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.SDI(nums, k)- self.SDI(nums, k-1)

    def SDI(self, nums, k):
        l=r=0
        n=len(nums)
        freq={}
        cnt=0
        if(k==0):
            return 0
        while r<n:
            freq[nums[r]]=freq.get(nums[r],0)+1
            while len(freq)>k:
                freq[nums[l]]-=1
                if(freq[nums[l]]==0):
                    del freq[nums[l]]
                l+=1
            if(len(freq)<=k):
                cnt+=r-l+1
            r+=1
        return cnt

        