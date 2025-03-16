class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_index=0
        n=len(nums)
        for i in range(n):
            if(i>max_index):
                return False
            max_index=max(max_index, i+nums[i])
            if(max_index>=n):
                return True
        return True


            
        