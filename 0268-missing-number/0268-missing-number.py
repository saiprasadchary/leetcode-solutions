class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=max(nums);
        for i in range(maxi):
            print(i)
            if i not in nums:
                return i;
        return maxi+1;
        