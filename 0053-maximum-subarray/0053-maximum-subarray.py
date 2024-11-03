class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum=float('-inf');
        sum1=0
        for i in nums:
            sum1+=i;
            
            if sum1>maxSum:
                maxSum=sum1;
            if sum1<0:
                sum1=0;
        return maxSum


        # BruteForce
        # if len(nums)==1:
        #     return nums[0]
        # maxSum=float('-inf')
        # for  i in range(len(nums)):
        #     sum1=0
        #     for j in range(i, len(nums)):
        #         sum1+=nums[j]
        #         if sum1>maxSum:
        #             maxSum=sum1;
        # return maxSum;
                
                
        