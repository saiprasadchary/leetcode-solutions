class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        cnt=0
        freq={0:1}
        n=len(nums)
        pref_sum=0
        for i in range(n):
            pref_sum+=nums[i]
            if pref_sum-goal in freq:
                cnt+=freq[pref_sum-goal]
            freq[pref_sum]=freq.get(pref_sum,0)+1
        return cnt;

            






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