class Solution(object):
    def check(self, nums):
        count=0
        n=len(nums)
        for i in range(len(nums)):
            if nums[i]>nums[(i+1)%n]:
                count=count+1
        if count>1:
            return False
        else:
            return True