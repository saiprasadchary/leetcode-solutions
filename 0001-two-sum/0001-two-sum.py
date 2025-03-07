class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        freq={}
        for ind, val in enumerate(nums):
            key=target-val
            if key in freq:
                return [ind, freq[key]]
            freq[val]=ind
        return [-1,-1]