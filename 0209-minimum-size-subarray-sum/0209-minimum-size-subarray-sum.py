class Solution(object):
    def minSubArrayLen(self, target, nums):
        n=len(nums)
        r=0
        l=0
        res=float('inf')
        sum1=0
        while r<n:
            sum1+=nums[r]
            while sum1>=target:
                res=min(res,r-l+1)
                sum1=sum1-nums[l]
                l+=1
            else:
                r+=1
        print(res)       
        if res!=float('inf'):
            return res
        else:
            return 0

        # res=float('inf')

        # for i in range(n):

        #     tempSum=0
        #     for j in range(i,n):
        #         tempSum+=nums[j]
        #         if tempSum>=target:
        #             res=min(res, j-i+1)
                    
        # if res!=float('inf'):
        #     return res
        # else:
        #     return 0
        