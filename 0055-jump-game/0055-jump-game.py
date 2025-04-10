class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        n=len(nums)
        if n==1:
            return True

        maxind=0
        for i in range(n):
            if(i>maxind):
                return False
            maxind=max(maxind, i+nums[i])
        return True






        # max_index=0
        # n=len(nums)
        # for i in range(n):
        #     if(i>max_index):
        #         return False
        #     max_index=max(max_index, i+nums[i])
        #     if(max_index>=n):
        #         return True
        # return True


            
        