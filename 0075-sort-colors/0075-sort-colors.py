class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        for i in range(len(nums)):
            count[nums[i]] = count[nums[i]] + 1
        
        i = 0
        for color in range(len(count)):
            for _ in range(count[color]):
                nums[i] = color
                i += 1