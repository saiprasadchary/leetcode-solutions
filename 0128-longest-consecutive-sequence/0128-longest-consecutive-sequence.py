class Solution(object):
    def longestConsecutive(self, nums):
        #bruteforce

        n=len(nums)
        maxlen=1
        cnt=1
        if not nums:
            return 0
        if n==1:
            return 1
        nums=list(set(nums))
        nums.sort()
        for i in range(1, len(nums)):
            if(nums[i-1]+1==nums[i]):
                cnt+=1
                print(nums[i-1], nums[i])
                maxlen=max(cnt, maxlen)
            else:
                cnt=1
        return maxlen

        