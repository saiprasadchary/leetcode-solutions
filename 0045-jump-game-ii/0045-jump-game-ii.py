class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # recursion solution:

        # DP

        # Greedy approach(optimal)

        l,r=0,0
        jump=0
        n=len(nums)

        while r<n-1:
            farthest=0

            for i in range(l,r+1):
                farthest=max(farthest, i+nums[i])

            jump+=1
            l=r+1
            r=farthest
            if l>r:
                return -1
            
        return jump
        