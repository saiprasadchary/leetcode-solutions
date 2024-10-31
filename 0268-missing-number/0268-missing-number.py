class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # maxi=max(nums);
        # for i in range(maxi):
        #     print(i)
        #     if i not in nums:
        #         return i;
        # return maxi+1;
        seen={}
        for i in range(len(nums)):
            seen[nums[i]]=1;
        
        for i in range(len(nums)):
            if i not in seen:
                return i
        return i+1