class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=r=0
        n=len(nums)
        zeros=0
        maxlen=0
        while r<n:
            if nums[r]==0:
                zeros+=1
            # here the twist comes until we find the zeros condition to be true we keep the windsize to shrink by one through the if statement and simplify doesnt considers the maxlen until zeros condition is satisfied.
            if zeros > k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            if zeros <=k:
                windlen=r-l+1
                maxlen=max(windlen, maxlen)
            r+=1
        return maxlen




        
        # this is the better solution actually as while loop for the l pointer, until it finds the another zero is shouldbe eliminated in the optimal one which is shown above:
        # n=len(nums)
        # r=0
        # l=0
        # zeros=0
        # maxlen=0
        # while r<n:
        #     if nums[r]==0:
        #         zeros+=1;
        #     if zeros<=k:
        #         len1=r-l+1
        #         maxlen=max(len1, maxlen)
        #     if zeros>k:
        #         while zeros>k:
        #             if nums[l]==0:
        #                 zeros-=1
        #             l+=1
        #     r+=1
        # return maxlen


        # maxlen=0
        # n=len(nums)
        # for i in range(n):
        #     zeros=0
        #     for j in range(i,n):
        #         if nums[j]==0:
        #             zeros+=1
        #         if zeros<=k:
        #             len1=j-i+1
        #             maxlen=max(len1, maxlen)
        #         else:
        #             break
        # return maxlen


