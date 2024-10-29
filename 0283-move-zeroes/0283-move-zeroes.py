class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0  # Pointer for placing non-zero elements
        j = 1  # Pointer for scanning the array

        # Special handling for length 2 is removed for generality and simplicity
        while j < len(nums):
            if nums[i] == 0 and nums[j] != 0:
                # Perform swap if current is zero and jth is non-zero
                nums[i], nums[j] = nums[j], nums[i]
                i += 1  # Move i to the next index for the next potential non-zero placement
            elif nums[i] != 0:
                i += 1  # If nums[i] is non-zero, just move i to catch up with j if needed
            j += 1 