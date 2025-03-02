class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        
        return self.BSS(nums,goal)- self.BSS(nums, goal-1)

    def BSS(self, nums,goal):
        l=r=0
        n=len(nums)
        cnt=0
        sum1=0
        if goal<0:
            return 0
        while r<n:
            sum1+=nums[r]
            while sum1>goal:
                sum1-=nums[l]
                l+=1
            if sum1<=goal:
                cnt+=r-l+1
            r+=1
        return cnt

        # this solution could solve for all the values irrespective of just 0's and 1's and also +ve and -ve's too
        # cnt=0
        # freq={0:1}
        # n=len(nums)
        # pref_sum=0
        # for i in range(n):
        #     pref_sum+=nums[i]
        #     if pref_sum-goal in freq:
        #         cnt+=freq[pref_sum-goal]
        #     freq[pref_sum]=freq.get(pref_sum,0)+1
        # return cnt;

            






        # The below is a brute force approach that considers every possible subarray to get the sum 
        # and keeps a count to track the matching sum:

        # n=len(nums)
        # count=0

        # for i in range(n):
        #     sum1=0
        #     for j in range(i,n):
        #         sum1+=nums[j]
        #         if sum1==goal:
        #             count+=1
        #         # elif sum1>goal:
        #         #     break
        # return count