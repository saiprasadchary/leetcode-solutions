class Solution(object):
    def longestConsecutive(self, nums):
        
        #bruteforce approach
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        maxlen=1
        cnt=1
        nums=list(set(nums))
        nums.sort()
        for i in range(1, len(nums)):
            if(nums[i-1]+1==nums[i]):
                cnt+=1
                maxlen=max(cnt, maxlen)
            else:
                cnt=1
        return maxlen

        